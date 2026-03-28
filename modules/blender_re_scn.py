#Author: NSA Cloud
import bpy
import os
import uuid

from math import radians
from mathutils import Vector,Matrix

from .gen_functions import textColors,raiseWarning,raiseError
from .file_re_scn import readRE_SCN,writeRE_SCN,SCNFile,GameObjectInfo,FolderInfo,UserDataInfo,ResourceInfo,PrefabInfo
from .file_re_user import readRE_User,writeRE_User,UserFile
from .file_re_pfb import readRE_PFB,writeRE_PFB,PFBFile,GameObjectInfoPFB
#from .file_re_mesh_noesis_internal import importREMeshFileNoesis
from .re_rsz_lookup_main import hashToString,stringToHash,hashToCRC,getRSZInstance
from .mesh.blender_re_mesh_map_editor import importREMeshFile
from .blender_re_mcol import importMCOLFile
from .re4_items import getRE4ItemInfo

from json import dumps

from .file_re_rsz import InstanceInfo, RSZUserDataInfo
global MESH_VERSION
global MDF_VERSION
global SCN_VERSION
global MCOL_VERSION
FBX_IMPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"FBXCache","import")#RE-Mesh-Noesis-Wrapper\TempFBX\import
ADDON_NAME = os.path.basename(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Gets name of addon folder, which is used to get addon preferences

global importedSCNSet 
importedSCNSet = set()#Keep a list of imported scn paths so that an infinite loop cannot occur in case of a circular reference
#Clear the list when first scn is done

#Blender ints are always signed, so uints have to be converted to ints (and back when exporting)

def getCollection(collectionName,parentCollection = None,makeNew = False):
	if makeNew or not bpy.data.collections.get(collectionName):
		collection = bpy.data.collections.new(collectionName)
		collectionName = collection.name
		if parentCollection != None:
			parentCollection.children.link(collection)
		else:
			bpy.context.scene.collection.children.link(collection)
	return bpy.data.collections[collectionName]

def setupEEVEE(sunObject = None,fogObject = None):
	#bpy.context.scene.eevee.use_bloom = True#Enable bloom
	#bpy.context.scene.eevee.use_ssr = True#Enable screen space reflections
	#bpy.context.scene.eevee.use_gtao = True#Enable ambient occlusion
	#bpy.context.scene.eevee.shadow_cube_size = "1024"#Increase shadow resolution
	#bpy.context.scene.eevee.shadow_cascade_size = "2048"#Increase shadow resolution
	#bpy.context.scene.view_settings.view_transform = "Standard"#Set color mode
	bpy.context.scene.eevee.shadow_resolution_scale = .4
	bpy.context.scene.eevee.use_raytracing = True
	nodeTree = bpy.data.worlds["World"].node_tree
	SkyTextureNode = nodeTree.nodes.get("Sky Texture",None)
	volumeScatterNode = nodeTree.nodes.get("Volume Scatter",None)
	if SkyTextureNode == None:
		SkyTextureNode = nodeTree.nodes.new('ShaderNodeTexSky')
	SkyTextureNode.sky_type = "PREETHAM"
	if sunObject != None:
		sunEulerRot = sunObject.matrix_world.to_euler("XYZ")
		SkyTextureNode.sun_direction = sunEulerRot
	BackgroundNode = nodeTree.nodes.get("Background")
	BackgroundNode.inputs[1].default_value = 0.03#Strength
	nodeTree.links.new(SkyTextureNode.outputs[0],BackgroundNode.inputs[0])
	worldOutputNode = nodeTree.nodes.get("World Output",None)
	if fogObject != None:
		if volumeScatterNode == None:
			volumeScatterNode = nodeTree.nodes.new('ShaderNodeVolumeScatter')
		if worldOutputNode != None:
			nodeTree.links.new(volumeScatterNode.outputs["Volume"],worldOutputNode.inputs["Volume"])
			volumeScatterNode.inputs["Density"].default_value = fogObject.get("Density",0.0)/2.0#Halve the fog values since they seem a little high for blender
def unsignedToSigned(uintValue):
	intValue = uintValue & ((1 << 32) - 1)
	intValue = (intValue & ((1 << 31) - 1)) - (intValue & (1 << 31))
	return intValue
def signedToUnsigned(intValue):
	return intValue & 0xffffffff

arrayDataTypes = set(["int2","uint2","int3","uint3","float2","float3","vec2","vec3","vec4","mat4","obb","aabb"])
multiDimensionalDataTypes = set(["mat4","obb","aabb"])
#Blender doesn't let you have lists inside lists as custom properties for whatever reason so lists containing lists are converted to strings

def applyInstanceFields(instance,obj):#Assigns fields as custom properties on objects
	#keys,fields = instance.getFields().items()
	obj["~isObject"] = instance.instanceInfo.isObject
	obj["~instanceType"] = instance.instanceInfo.name
	for field in instance.fields.values():
		if "REMAP_Object" in field.tagSet or "REMAP_UserData" in field.tagSet:#Add constraint to use as a pointer since using pointer properties for every single rsz type isn't feasible
			#if obj.re_rsz_objectpointers.rszObjectPointers#TODO Check for duplicates
			if field.isList:
				for index, value in enumerate(field.value):
					newPropGroup = obj.re_rsz_object.rszObjectPointers.add()#Add constraints for tracking indices, the target is set once all objects are imported
					newPropGroup.fieldName = field.name+"["+str(index)+"]"
			else:
				newPropGroup = obj.re_rsz_object.rszObjectPointers.add()#Add constraints for tracking indices, the target is set once all objects are imported
				newPropGroup.fieldName = field.name
		
		try:
			if (field.isList or field.dataType in multiDimensionalDataTypes) and field.dataType in arrayDataTypes:
				obj[field.name] = dumps(field.value)#Convert python list into json string to store in custom property
			else:
				obj[field.name] = field.value
		except OverflowError:
			if field.dataType == "uint":
				if field.isList:
					newList = []
					for entry in field.value:
						newList.append(unsignedToSigned(entry))
					obj[field.name] = newList
				else:
					obj[field.name] = unsignedToSigned(field.value)
			else:
				raise

def checkNameUsage(baseName,checkSubString = True):
	if checkSubString:
		return any(baseName in name for name in [obj.name for obj in bpy.data.objects])
	else:
		return baseName in [obj.name for obj in bpy.data.objects]

def createEmpty(name,propertyList,parent = None,collectionName = None):
	obj = bpy.data.objects.new( name, None )
	bpy.context.scene.collection.objects.link(obj)
	obj.empty_display_size = .10
	obj.empty_display_type = 'PLAIN_AXES'
	obj.parent = parent
	for property in propertyList:#Reverse list so items get added in correct order
 
		obj[property[0]] = property[1]
	if collectionName != None:    
		master_collection = bpy.context.scene.collection
		
		if bpy.data.collections.get(collectionName,None) == None:#Create collection if the name given doesn't exist
			newCollection = bpy.data.collections.new(collectionName)
			bpy.context.scene.collection.children.link(newCollection)
		
		layer_collection = bpy.data.collections[collectionName]
		layer_collection.objects.link(obj) #link it with collection
		master_collection.objects.unlink(obj) #unlink it from master collection
		
	return obj

def createLight(name,propertyList,lightType = "POINT",parent = None,collectionName = None):
	# Create light datablock
	light_data = bpy.data.lights.new(name=name, type=lightType)
	light_data.energy = 10
	
	# Create new object, pass the light data 
	lightObj = bpy.data.objects.new(name=name, object_data=light_data)
	
	for property in propertyList:#Reverse list so items get added in correct order
		lightObj[property[0]] = property[1]
		
	lightObj.parent = parent	
	if collectionName != None:    
		if bpy.data.collections.get(collectionName,None) == None:#Create collection if the name given doesn't exist
			newCollection = bpy.data.collections.new(collectionName)
			bpy.context.scene.collection.children.link(newCollection)
		
		layer_collection = bpy.data.collections[collectionName]
		layer_collection.objects.link(lightObj) #link it with collection
		
	return lightObj

def addRSZPointer(obj,linkFieldName,targetObj):
	newPropGroup = obj.re_rsz_object.rszObjectPointers.add()
	newPropGroup.fieldName = linkFieldName
	newPropGroup.targetObject = targetObj

def getNewUUID():
	return str(uuid.uuid4().int)
	
def setLightDisplayObjectProperties(instanceObj,lightObj):
	lightType = lightObj.data.type
	if lightType == "POINT":
		lightObj.data.re_rsz_pointlight.lightObject = lightObj
		for key, value in instanceObj.items():
			if key in lightObj.data.re_rsz_pointlight.__annotations__.keys():
				try:
					setattr(lightObj.data.re_rsz_pointlight,key,instanceObj[key])
				except Exception as err:
					print("Failed to set " + str(key) + " to " +str(value) +"\n" + str(err)) 
	elif lightType == "SPOT":
		lightObj.data.re_rsz_spotlight.lightObject = lightObj
		for key, value in instanceObj.items():
			if key in lightObj.data.re_rsz_spotlight.__annotations__.keys():
				try:
					if key == "Cone":
						#print(value)
						setattr(lightObj.data.re_rsz_spotlight,key,instanceObj[key])
					else:
						setattr(lightObj.data.re_rsz_spotlight,key,instanceObj[key])
				except Exception as err:
					print("Failed to set " + str(key) + " to " +str(value) +"\n" + str(err)) 
	elif lightType == "SUN":
		#print("Setting " + str(key))#debug
		#print("To " + str(value))#debug
		lightObj.data.re_rsz_directionallight.lightObject = lightObj
		for key, value in instanceObj.items():
			if key in lightObj.data.re_rsz_directionallight.__annotations__.keys():
				try:
					setattr(lightObj.data.re_rsz_directionallight,key,instanceObj[key])
				except Exception as err:
					print("Failed to set " + str(key) + " to " +str(value) +"\n" + str(err)) 
def joinSubMeshes(objList):
	if bpy.app.version < (3,2,0):
		ctx = bpy.context.copy()
	
		# one of the objects to join
		ctx['active_object'] = objList[0]
		ctx['selected_editable_objects'] = objList
		bpy.ops.object.join(ctx)
		return ctx["active_object"]
	else:
		with bpy.context.temp_override(active_object=objList[0], selected_editable_objects=objList):
			   bpy.ops.object.join()
			   return bpy.context.active_object
meshCache = {}#Fast cache for creating copies of already imported meshes
def clearBlenderMeshCache():
	meshCache.clear()
def loadMesh(meshPath,mdfPath,parentObj = None,optimizedImport = False,isCompositeMesh = False,loadMaterials = False,loadUnusedTextures = False,loadUnusedProps = False,useBackfaceCulling = False,reloadCachedTextures = False,currentChunkPath = None,collectionName = "RSZData",lodTarget = 0):
	meshImportOptions = {"clearScene":False,"createCollections":False,"loadMaterials":loadMaterials,"loadUnusedTextures":loadUnusedTextures,"loadUnusedProps":loadUnusedProps,"useBackfaceCulling":useBackfaceCulling,"reloadCachedTextures":False,"mdfPath":"","importAllLODs":False,"importBlendShapes":False,"rotate90":False,"mergeArmature":"","importArmatureOnly":False,"mergeGroups":True,"importShadowMeshes":False,"importOcclusionMeshes":False,"importBoundingBoxes":False}
	meshName = "DISPLAY_"+os.path.basename(meshPath)
	#print(bpy.context.preferences.addons[ADDON_NAME].preferences.noesisPath)
	stringIndex = meshPath.find("natives")
	if stringIndex != -1:
		#nativesRoot = meshPath[stringIndex:stringIndex+12]#Get natives\stm or natives\x64
		newMeshPath = meshPath[stringIndex::]+MESH_VERSION
	else:
		#nativesRoot = os.path.join("natives","STM")
		newMeshPath = os.path.join("natives","STM",meshPath+MESH_VERSION)

	newObj = None	
	#nativesPath = os.path.relpath(meshPath, "ROOTMESHDIR")
	#print(nativesPath)
	cachedMesh = meshCache.get(newMeshPath,None)
	if cachedMesh != None:#Create duplicate of existing mesh
		#print("Creating duplicate of "+cachedMesh.name)
		newObj = cachedMesh.copy()
		newObj.data = cachedMesh.data#.copy()
		newObj.animation_data_clear()
		newObj.parent = parentObj
		newObj.matrix_world = parentObj.matrix_world
		bpy.data.collections[collectionName].objects.link(newObj)
		newObj.constraints.clear()
		constraint = newObj.constraints.new(type = "COPY_TRANSFORMS")
		if isCompositeMesh:
			constraint.target = parentObj
			constraint.name = "Move the transform controller instead"
		#else:
			#constraint.target = parentObj.parent
			#constraint.name = "Move the game object instead"
	else:
		meshFilePath = ""
		if not os.path.isfile(meshFilePath):
				meshFilePath = None
				
		if meshFilePath == None:#If it can't be found at either game or chunk path, check based off imported scn chunk
			meshFilePath = os.path.join(currentChunkPath,newMeshPath)
			if not os.path.isfile(meshFilePath):
				meshFilePath = None
		if meshFilePath != None:
			if loadMaterials:
				if "natives" not in mdfPath:
					newMDFPath = os.path.join("ROOTMESHDIR","natives","STM",mdfPath)
					
				mdfNativesPath = os.path.relpath(newMDFPath, "ROOTMESHDIR")
				newMDFPath = ""#TODO Fix
				#newMDFPath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.gamePath,mdfNativesPath+MDF_VERSION)
				#print(mdfPath)
				#if not os.path.isfile(newMDFPath):
				#	newMDFPath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.chunkPath,mdfNativesPath+MDF_VERSION)
					#print(mdfPath)
				if not os.path.isfile(newMDFPath):
					newMDFPath = os.path.join(currentChunkPath,"natives","STM",mdfPath).replace("/","\\")+MDF_VERSION
					#print("TEST MDF PATH "+newMDFPath )
				if os.path.isfile(newMDFPath):
					meshImportOptions["mdfPath"] = newMDFPath
				else:
					meshImportOptions["mdfPath"]=""
					#print("VALID MDF PATH")
			armatureObj, newObjList = importREMeshFile(meshFilePath,meshImportOptions,lodTarget)
			
			#bpy.ops.import_scene.fbx(filepath = FBXPath,bake_space_transform=True,use_manual_orientation=True,axis_forward = "Y",axis_up ="Z")

			
			if armatureObj != None:#If there's an armature, only change the parent object of the armature
				armatureObj.parent = parentObj	
			if newObjList != None:
				for obj in newObjList:
					obj.name = meshName
					obj["~TYPE"] = "RSZ_DISPLAY_MESH"  
					
					master_collection = bpy.context.scene.collection
					if bpy.data.collections.get(collectionName,None) == None:#Create collection if the name given doesn't exist
						newCollection = bpy.data.collections.new(collectionName)
						bpy.context.scene.collection.children.link(newCollection)
						
					layer_collection = bpy.data.collections[collectionName]
					layer_collection.objects.link(obj) #link it with collection
					master_collection.objects.unlink(obj) #unlink it from master collection
	
				newObj = joinSubMeshes(newObjList)
				newObj.name = meshName
				newObj.parent = parentObj
				newObj["~TYPE"] = "RSZ_DISPLAY_MESH"
				if optimizedImport:
					newObj.name = os.path.split(meshPath)[1]
				else:
					
					if isCompositeMesh:
						constraint = newObj.constraints.new(type = "COPY_TRANSFORMS")
						constraint.target = parentObj
						constraint.name = "Move the transform controller instead"
					#else:
						#constraint.target = parentObj.parent
						#constraint.name = "Move the game object instead"
					if bpy.data.collections.get(collectionName,None) == None:#Create collection if the name given doesn't exist
						newCollection = bpy.data.collections.new(collectionName)
						bpy.context.scene.collection.children.link(newCollection)
					
				layer_collection = bpy.data.collections[collectionName]
				for collection in newObj.users_collection:
					collection.objects.unlink(newObj) #unlink it from all collections
				layer_collection.objects.link(newObj) #link it with collection
				
			if loadMaterials:
				pass#TODO
			else:
				newObj.data.materials.clear()
			meshCache.update({newMeshPath:newObj})
	return newObj
"""
		noesisPath = bpy.context.preferences.addons[ADDON_NAME].preferences.noesisPath
		FBXPath = None
		if os.path.isfile(os.path.join(FBX_IMPORT_DIR,newMeshPath.split(".mesh")[0]+".fbx")):#If fbx is already cached, import it
			FBXPath = os.path.join(FBX_IMPORT_DIR,newMeshPath.split(".mesh")[0]+".fbx")
		else:
			
			meshFilePath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.gamePath,newMeshPath)
			print("Checking for cached fbx at: "+os.path.join(FBX_IMPORT_DIR,newMeshPath.split(".mesh")[0]+".fbx"))
			if not os.path.isfile(meshFilePath):#Check game natives for mesh first
				meshFilePath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.chunkPath,newMeshPath)
			if not os.path.isfile(meshFilePath):
					meshFilePath = None
					
			if meshFilePath == None:#If it can't be found at either game or chunk path, check based off imported scn chunk
				meshFilePath = os.path.join(currentChunkPath,newMeshPath)
				if not os.path.isfile(meshFilePath):
					meshFilePath = None
			if meshFilePath != None:
				if loadMaterials:
					if "natives" not in mdfPath:
						newMDFPath = os.path.join("ROOTMESHDIR","natives","STM",mdfPath)
						
					mdfNativesPath = os.path.relpath(newMDFPath, "ROOTMESHDIR")
					newMDFPath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.gamePath,mdfNativesPath+MDF_VERSION)
					#print(mdfPath)
					if not os.path.isfile(newMDFPath):
						newMDFPath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.chunkPath,mdfNativesPath+MDF_VERSION)
						#print(mdfPath)
					if not os.path.isfile(newMDFPath):
						newMDFPath = os.path.join(currentChunkPath,"natives","STM",mdfPath).replace("/","\\")+MDF_VERSION
						#print("TEST MDF PATH "+newMDFPath )
					if os.path.isfile(newMDFPath):
						meshImportOptions["mdfPath"] = newMDFPath
					else:
						meshImportOptions["mdfPath"]=""
						#print("VALID MDF PATH")
				#FBXPath = importREMeshFileNoesis(meshFilePath,noesisPath,options = {"clearScene":False,"useBetterFBX":False})
				FBXPath = importREMeshFile(meshFilePath,meshImportOptions,lodTarget)
				
			else:
				raiseWarning("Could not import "+ newMeshPath+", path not found in game natives or chunk natives.")
				
		if FBXPath != None:
			sceneObjSet = set(bpy.context.scene.objects)
			bpy.ops.import_scene.fbx(filepath = FBXPath,bake_space_transform=True,use_manual_orientation=True,axis_forward = "Y",axis_up ="Z")
			newSceneObjSet = set(bpy.context.scene.objects)
			newObjectList = list(newSceneObjSet.difference(sceneObjSet))


			if loadMaterials:
				if "natives" not in mdfPath:
					newMDFPath = os.path.join("ROOTMESHDIR","natives","STM",mdfPath)
					
				mdfNativesPath = os.path.relpath(newMDFPath, "ROOTMESHDIR")
				newMDFPath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.gamePath,mdfNativesPath+MDF_VERSION)
				#print(mdfPath)
				if not os.path.isfile(newMDFPath):
					newMDFPath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.chunkPath,mdfNativesPath+MDF_VERSION)
					#print(mdfPath)
				if not os.path.isfile(newMDFPath):
					newMDFPath = os.path.join(currentChunkPath,"natives","STM",mdfPath).replace("/","\\")+MDF_VERSION
					#print("TEST MDF PATH "+newMDFPath )
				if os.path.isfile(newMDFPath):
					pass
					#print("VALID MDF PATH")
					
					#importMDF(newMDFPath,newObjectList,noesisPath,loadMaterialLevel,reloadCachedTextures,chunkPath=bpy.context.preferences.addons[ADDON_NAME].preferences.chunkPath)
			
"""

			

def loadMCOL(mcolPath,parentObj = None,currentChunkPath = ""):
	#print(bpy.context.preferences.addons[ADDON_NAME].preferences.noesisPath)
	MCOLRoot = None
	cachedMesh = meshCache.get(mcolPath,None)
	if cachedMesh != None:#Create duplicate of existing mesh
		#print("Creating duplicate of "+cachedMesh.name)
		MCOLRoot = cachedMesh.copy()
		MCOLRoot.data = cachedMesh.data.copy()
		MCOLRoot.animation_data_clear()
		MCOLRoot.parent = parentObj
		MCOLRoot.matrix_basis = Matrix()
		MCOLRoot.location = (0.0,0.0,0.0)
		MCOLRoot.rotation_euler = (0.0,0.0,0.0)
		MCOLRoot.scale = (1.0,1.0,1.0)
		bpy.data.collections["MCOLData"].objects.link(MCOLRoot)
		MCOLRoot.constraints.clear()
	else:
		stringIndex = mcolPath.find("natives")
		if stringIndex != -1:
			#nativesRoot = meshPath[stringIndex:stringIndex+12]#Get natives\stm or natives\x64
			newMCOLPath = os.path.normpath(mcolPath[stringIndex::]+MCOL_VERSION)
		else:
			#nativesRoot = os.path.join("natives","STM")
			newMCOLPath = os.path.normpath(os.path.join("natives","STM",mcolPath+MCOL_VERSION))
	
			
		#mcolFilePath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.gamePath,newMCOLPath)
		mcolFilePath = ""#TODO Fix
		#if not os.path.isfile(mcolFilePath):#Check game natives for mesh first
			#mcolFilePath = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.chunkPath,newMCOLPath)
		if not os.path.isfile(mcolFilePath):
				mcolFilePath = None
		if mcolFilePath == None:#If it can't be found at either game or chunk path, check based off imported scn chunk
			mcolFilePath = os.path.join(currentChunkPath,newMCOLPath)
			if not os.path.isfile(mcolFilePath):
				mcolFilePath = None
		if mcolFilePath != None:
			try:
				MCOLRoot = importMCOLFile(mcolFilePath)
				MCOLRoot.rotation_euler = (0.0,0.0,0.0)
				MCOLRoot.parent = parentObj
				meshCache[mcolPath] = MCOLRoot
			except Exception as err:
				raiseWarning("Failed to import "+ mcolFilePath)
				print(err)
		else:
			raiseWarning("Could not import "+ newMCOLPath +", path not found in game natives or chunk natives.")
	return MCOLRoot
def addIndexConstraints(instanceObjectDict):
	#print(instanceObjectDict)
	for obj in instanceObjectDict.values():
		for group in obj.re_rsz_object.rszObjectPointers.values():
			isList = False
			if group.fieldName.endswith("]"):#List field names always have brackets
				fieldName = group.fieldName.split("[")[0]
				fieldIndex = int(group.fieldName.split("[")[1].split("]")[0])
				isList = True
			else:
				fieldName = group.fieldName
			if not isList:
				if fieldName in obj.keys():
					targetIndex = obj[fieldName]
					if targetIndex == 0:
						group.targetObject = None
					else:
						group.targetObject = instanceObjectDict[targetIndex]
			else:
				targetIndex = obj[fieldName][fieldIndex]
				if targetIndex == 0:
					group.targetObject = None
				else:
					group.targetObject = instanceObjectDict[targetIndex]
#MESH INSTANCING - for use with optimized import option. Credit to scatter object plugin for instancing code
def make_duplicator(target_collection, source_object, matrices):
    triangle_scale = 0.1

    duplicator = triangle_object_from_matrices(source_object.name + " Duplicator", matrices, triangle_scale)
    duplicator.instance_type = 'FACES'
    duplicator.use_instance_faces_scale = True
    duplicator.show_instancer_for_viewport = False
    duplicator.show_instancer_for_render = False
    duplicator.instance_faces_scale = 1 / triangle_scale
    source_object.parent = duplicator

    target_collection.objects.link(duplicator)

def triangle_object_from_matrices(name, matrices, triangle_scale):
    mesh = triangle_mesh_from_matrices(name, matrices, triangle_scale)
    return bpy.data.objects.new(name, mesh)

def triangle_mesh_from_matrices(name, matrices, triangle_scale):
    mesh = bpy.data.meshes.new(name)
    vertices, polygons = mesh_data_from_matrices(matrices, triangle_scale)
    mesh.from_pydata(vertices, [], polygons)
    mesh.update()
    mesh.validate()
    return mesh

unit_triangle_vertices = (
    Vector((-3**-0.25, -3**-0.75, 0)),
    Vector((3**-0.25, -3**-0.75, 0)),
    Vector((0, 2/3**0.75, 0)))

def mesh_data_from_matrices(matrices, triangle_scale):
    vertices = []
    polygons = []
    triangle_vertices = [triangle_scale * v for v in unit_triangle_vertices]

    for i, matrix in enumerate(matrices):
        vertices.extend((matrix @ v for v in triangle_vertices))
        polygons.append((i * 3 + 0, i * 3 + 1, i * 3 + 2))

    return vertices, polygons

OPTIMIZED_IMPORT_INSTANCE_SET = set(["via.render.Mesh","via.Transform","via.render.CompositeMesh","via.render.CompositeMeshInstanceGroup","via.render.CompositeMeshTransformController","via.render.PointLight","via.render.SpotLight","via.render.DirectionalLight","via.physics.MeshShape","via.physics.Colliders"])				
optimizedMeshImportDict = {}#Dict containing mesh paths to be imported all at once as instanced meshes
optimizedMCOLImportDict = {}
optimizedObjectDeleteList = []
def clearOptimizedMeshImportCache():
	optimizedMeshImportDict.clear()
	optimizedMCOLImportDict.clear()
	for obj in optimizedObjectDeleteList:
		#pass
		bpy.data.objects.remove(obj, do_unlink=True)
def importRSZFile(filepath,fileType = "SCN",importOptions = {"game":"MHRise","loadLinkedScenes":True,"loadMeshes":True,"loadMaterials":True,"materialLoadLevel":"1","loadLights":True,"fixClippingDistance":True,"optimizeEEVEESettings":True,"checkChunkFirst":True,"optimizedImport":False},firstFile = True,parentCollection = None):
	
	game = importOptions["game"]
	
	meshLODTarget = importOptions["lodTarget"]
	global MESH_VERSION
	global MDF_VERSION
	global SCN_VERSION
	global MCOL_VERSION
	global importedSCNSet
	if firstFile:
		clearBlenderMeshCache()#Remove dict references to blender objects, otherwise it will cause issues when things are deleted
		importedSCNSet = set()
	importedSCNSet.add(filepath.replace("\\","/").split("natives/STM/")[-1])
	
	if fileType == "SCN":
		rszFile = readRE_SCN(filepath,game = game)
	elif fileType == "USR":
		rszFile = readRE_User(filepath,game = game)
	elif fileType == "PFB":
		rszFile = readRE_PFB(filepath,game = game)
	else:
		raiseWarning("Unknown file type:" + fileType)
		return False
	
	if game == "RE4":
		SCN_VERSION = ".20"
		MESH_VERSION = ".221108797"
		MDF_VERSION = ".32"
		MCOL_VERSION = ".20021"
	elif game == "DR":
		SCN_VERSION = ".21"
		MESH_VERSION = ".240424828"
		MDF_VERSION = ".40"
		MCOL_VERSION = ".24021"
	elif game == "MHRise":
		SCN_VERSION = ".20"
		MESH_VERSION = ".2109148288"
		MDF_VERSION = ".23"
		MCOL_VERSION = ".13020"
	elif game == "RE2RT":
		SCN_VERSION = ".20"
		MESH_VERSION = ".2109108288"
		MDF_VERSION = ".21"
		MCOL_VERSION = ".13020"
	
	nativesRoot = None
	stringIndex = filepath.find("natives")
	if stringIndex != -1:
		nativesRoot = filepath[stringIndex:stringIndex+12]#Get natives\stm or natives\x64
		currentChunkPath = filepath[:stringIndex]#Get root path
		currentFilePath = filepath[stringIndex::]#Get path without chunk
	else:
		currentFilePath = ""
	sunObject = None#For setting up EEVEE
	fogObject = None
	if importOptions["fixClippingDistance"]:
		for area in bpy.context.screen.areas:
			if area.type == "VIEW_3D":
				area.spaces.active.clip_start = 0.1
				area.spaces.active.clip_end = 10000.0
	if parentCollection == None:
		parentCollection = getCollection("RSZData")		
	
	RootCollection = getCollection(os.path.split(filepath)[1],parentCollection=parentCollection,makeNew = True)
	RootCollection.color_tag = "COLOR_07"
	RSZRoot = createEmpty(fileType+"_ROOT ("+os.path.split(filepath)[1]+")",[("~TYPE","RSZ_"+fileType+"_ROOT"),("Game",game),("Export Path",""),("Export With Export All","True")],None,RootCollection.name)
	RSZRoot.rotation_euler = (radians(90.0),0.0,0.0)
	RSZRoot.scale = (1,1,1)
	
	#if currentFilePath != "":
		#RSZRoot["Export Path"] = os.path.join(bpy.context.preferences.addons[ADDON_NAME].preferences.gamePath,currentFilePath)
	
	externalUserDataIndexSet = set()
	for externalUserData in rszFile.rsz.RSZUserDataInfoList:#For determining gaps in components
		externalUserDataIndexSet.add(externalUserData.instanceIndex)
		
	importedInstanceIndexSet = set()
	parentObjectDict = {-1:RSZRoot,0:None}#Store object table index pointing to blender object
	instanceObjectDict = {}
	if fileType == "SCN":
		for folderInfo in rszFile.FolderInfoList:
			folderInstanceIndex = rszFile.rsz.ObjectTable[folderInfo.objectTableIndex]
			importedInstanceIndexSet.add(folderInstanceIndex)
			folderInstance =  rszFile.rsz.InstanceList[folderInstanceIndex]
			subName = folderInstance.fields["folderName"].value+" "
			name = str(folderInstanceIndex).zfill(3)+"-"+subName+"("+folderInstance.instanceInfo.name+")"
			folderObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObjectDict[folderInfo.objectTableParentIndex],RootCollection.name)	
			applyInstanceFields(folderInstance, folderObj)
			folderObj.re_rsz_object.rszIndex = folderInstanceIndex
			parentObjectDict.update({folderInfo.objectTableIndex:folderObj})
			instanceObjectDict.update({folderInstanceIndex:folderObj})
			if folderInstance.fields["scnPath"].value != "" and folderInstance.fields["scnPath"].value != "NULL_STR" and importOptions["loadLinkedScenes"]:
				if nativesRoot != None:
					scnPath = os.path.join(currentChunkPath,nativesRoot,folderInstance.fields["scnPath"].value+SCN_VERSION).replace('/',os.sep)
					if os.path.isfile(scnPath):
						try:
							if folderInstance.fields["scnPath"] not in importedSCNSet:
								importedSCNSet.add(folderInstance.fields["scnPath"])
								importRSZFile(scnPath,"SCN",importOptions,firstFile=False,parentCollection=RootCollection)
							else:
								print("Skipped importing " + scnPath + " since it has already been imported")
						except Exception as err:
							raiseWarning("Error occured during importing linked SCN " + scnPath)
							print(err)
					else:
						raiseWarning("Could not find "+ scnPath + ", skipping.")
				else:
					raiseWarning("Cannot import linked scn since current scn path is not in a natives folder.")
	if fileType == "SCN":
		
		#OPTIMIZED IMPORT
		if importOptions["optimizedImport"]:
			optimizedObjectDeleteList.append(RSZRoot)
			for gameObjectInfo in rszFile.GameObjectInfoList:
				gameObjectInstanceIndex = rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex]
				importedInstanceIndexSet.add(gameObjectInstanceIndex)
				#Parse components backwards so that instances can be parented to their parent object properly
				
				gameObjectInstance =  rszFile.rsz.InstanceList[gameObjectInstanceIndex]
				
				
				subName = gameObjectInstance.fields["gameObjectName"].value+" "
				name = str(gameObjectInstanceIndex).zfill(3)+"-"+subName+"("+gameObjectInstance.instanceInfo.name+")"
				
						
				gameObjectObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObjectDict[gameObjectInfo.objectTableParentIndex],RootCollection.name)
				
				applyInstanceFields(gameObjectInstance, gameObjectObj)
				gameObjectObj.show_name = True
				gameObjectObj.show_in_front = True
				#gameObjectObj.matrix_parent_inverse = parentObjectDict[gameObjectInfo.objectTableParentIndex].matrix_world.inverted()
				parentObjectDict.update({gameObjectInfo.objectTableIndex:gameObjectObj})
				instanceObjectDict.update({gameObjectInstanceIndex:gameObjectObj})
				previousObjectInstance = None
				for componentIndex in reversed(range(gameObjectInstanceIndex+1,rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex+gameObjectInfo.componentCount]+1)):
					#print(componentIndex)
					if componentIndex not in externalUserDataIndexSet:
						importedInstanceIndexSet.add(componentIndex)
						instance = rszFile.rsz.InstanceList[componentIndex]
						if instance.instanceInfo.name in OPTIMIZED_IMPORT_INSTANCE_SET:
							if instance.instanceInfo.isObject:
								parentObject = gameObjectObj
							else:
								parentObject = previousObjectInstance
							name = str(componentIndex).zfill(3)+"-("+instance.instanceInfo.name+")"
							componentObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObject,RootCollection.name)
							applyInstanceFields(instance, componentObj)
							if instance.instanceInfo.isObject:
								previousObjectInstance = componentObj
							componentObj.re_rsz_object.rszIndex = componentIndex
							componentObj.empty_display_size = 0
							if instance.instanceInfo.name == "via.Transform":
								gameObjectObj.location = instance.fields["v00"].value[0:3]
								gameObjectObj.rotation_mode = "QUATERNION"
								gameObjectObj.rotation_quaternion = (instance.fields["v01"].value[3],instance.fields["v01"].value[0],instance.fields["v01"].value[1],instance.fields["v01"].value[2])#Blender quaternions are wxyz, not xyzw
								gameObjectObj.scale = instance.fields["v02"].value[0:3]
								
								
							elif instance.instanceInfo.name == "via.render.CompositeMeshTransformController":
								componentObj.location = instance.fields["v2"].value[0:3]
								componentObj.rotation_mode = "QUATERNION"
								componentObj.rotation_quaternion = (instance.fields["v3"].value[3],instance.fields["v3"].value[0],instance.fields["v3"].value[1],instance.fields["v3"].value[2])#Blender quaternions are wxyz, not xyzw
								componentObj.scale = instance.fields["v4"].value[0:3]
							instanceObjectDict.update({componentIndex:componentObj})
			bpy.context.view_layer.update()
			for obj in instanceObjectDict.values():
				instanceType = obj.get("~instanceType")
				if instanceType == "via.render.CompositeMeshInstanceGroup":
					if obj["v0"] != "NULL_STR":
						for index in obj["v2"]:
							meshInstanceObj = instanceObjectDict[index]
							meshEntry = optimizedMeshImportDict.get(obj["v0"])
							if meshEntry == None:
								meshEntry = {"mdfPath":obj["v1"],"matrixList":[meshInstanceObj.matrix_world]}
								optimizedMeshImportDict[obj["v0"]] = meshEntry
							else:
								meshEntry["matrixList"].append(meshInstanceObj.matrix_world)
				elif instanceType == "via.render.Mesh" and obj["meshPath"] != "NULL_STR":
					meshEntry = optimizedMeshImportDict.get(obj["meshPath"])
					if meshEntry == None:
						meshEntry = {"mdfPath":obj["mdfPath"],"matrixList":[obj.matrix_world]}
						optimizedMeshImportDict[obj["meshPath"]] = meshEntry
					else:
						meshEntry["matrixList"].append(obj.matrix_world)
				elif instanceType == "via.physics.MeshShape":
					if obj["v01"] != "NULL_STR":
						meshEntry = optimizedMCOLImportDict.get(obj["v01"])
						if meshEntry == None:
							optimizedMCOLImportDict[obj["v01"]] = [obj.matrix_world]
						else:
							optimizedMCOLImportDict[obj["v01"]].append(obj.matrix_world)
				elif importOptions["loadLights"]:
					if instanceType == "via.render.PointLight":
						newLight = createLight("DISPLAY_PointLight",[("~TYPE","RSZ_DISPLAY_POINTLIGHT")],lightType = "POINT",parent = obj,collectionName="RSZ Lights")
						setLightDisplayObjectProperties(obj,newLight)
						newLight.parent = None
						newLight.matrix_world = obj.matrix_world
					elif instanceType == "via.render.SpotLight":
						newLight = createLight("DISPLAY_SpotLight",[("~TYPE","RSZ_DISPLAY_SPOTLIGHT")],lightType = "SPOT",parent = obj,collectionName="RSZ Lights")
						setLightDisplayObjectProperties(obj,newLight)
						newLight.parent = None
						newLight.matrix_world = obj.matrix_world
					#"via.render.DirectionalLight"
				optimizedObjectDeleteList.append(obj)
		else:
			
		#NON OPTIMIZED IMPORT
			compositeMeshLoadList = []
			for gameObjectInfo in rszFile.GameObjectInfoList:
				gameObjectInstanceIndex = rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex]
				importedInstanceIndexSet.add(gameObjectInstanceIndex)
				#Parse components backwards so that instances can be parented to their parent object properly
				
				gameObjectInstance =  rszFile.rsz.InstanceList[gameObjectInstanceIndex]
				
				
				subName = gameObjectInstance.fields["gameObjectName"].value+" "
				name = str(gameObjectInstanceIndex).zfill(3)+"-"+subName+"("+gameObjectInstance.instanceInfo.name+")"
				#Find if game object contains a via.render.mesh component and use that mesh, if it doesn't have one, use an empty
				gameObjectObj = None
				for componentIndex in range(gameObjectInstanceIndex+1,rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex+gameObjectInfo.componentCount]+1):
					instance = rszFile.rsz.InstanceList[componentIndex]
					if importOptions["loadMeshes"] and instance.instanceInfo.name == "via.render.Mesh" and instance.fields["meshPath"] != "NULL_STR":
						gameObjectObj = loadMesh(instance.fields["meshPath"].value.replace("/","\\"),instance.fields["mdfPath"].value,parentObjectDict[gameObjectInfo.objectTableParentIndex],loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath,lodTarget = meshLODTarget,collectionName=RootCollection.name)
						if gameObjectObj != None:
							gameObjectObj.name = name
							gameObjectObj["~TYPE"] = "RSZ_INSTANCE"
					if instance.instanceInfo.name == "via.GameObject":
						break
				if gameObjectObj == None:
					gameObjectObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObjectDict[gameObjectInfo.objectTableParentIndex],RootCollection.name)
				applyInstanceFields(gameObjectInstance, gameObjectObj)
				gameObjectObj.re_rsz_object.rszIndex = gameObjectInstanceIndex
				gameObjectObj["GUID"] = gameObjectInfo.uuid
				
				#Set virtual prefab path, may or may not lead to a real prefab file. Probably used for instancing game objects
				if gameObjectInfo.prefabID != -1:
					gameObjectObj["~virtualPrefabPath"] = rszFile.PrefabInfoList[gameObjectInfo.prefabID].string
				else:
					gameObjectObj["~virtualPrefabPath"] = ""
				gameObjectObj.show_name = True
				if gameObjectObj.type == "EMPTY":
					gameObjectObj.show_in_front = True
				#gameObjectObj.matrix_parent_inverse = parentObjectDict[gameObjectInfo.objectTableParentIndex].matrix_world.inverted()
				parentObjectDict.update({gameObjectInfo.objectTableIndex:gameObjectObj})
				instanceObjectDict.update({gameObjectInstanceIndex:gameObjectObj})
				previousObjectInstance = None
				for componentIndex in reversed(range(gameObjectInstanceIndex+1,rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex+gameObjectInfo.componentCount]+1)):
					#print(componentIndex)
					if componentIndex not in externalUserDataIndexSet:
						importedInstanceIndexSet.add(componentIndex)
						instance = rszFile.rsz.InstanceList[componentIndex]
						if instance.instanceInfo.isObject:
							parentObject = gameObjectObj
						else:
							parentObject = previousObjectInstance
						name = str(componentIndex).zfill(3)+"-("+instance.instanceInfo.name+")"
						componentObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObject,RootCollection.name)
						applyInstanceFields(instance, componentObj)
						if instance.instanceInfo.isObject:
							previousObjectInstance = componentObj
						componentObj.re_rsz_object.rszIndex = componentIndex
						componentObj.empty_display_size = 0
						if instance.instanceInfo.name == "via.Transform":
							gameObjectObj.location = instance.fields["v00"].value[0:3]
							gameObjectObj.rotation_mode = "QUATERNION"
							gameObjectObj.rotation_quaternion = (instance.fields["v01"].value[3],instance.fields["v01"].value[0],instance.fields["v01"].value[1],instance.fields["v01"].value[2])#Blender quaternions are wxyz, not xyzw
							gameObjectObj.scale = instance.fields["v02"].value[0:3]
						
						
						#elif instance.instanceInfo.name == "via.render.Mesh":
						#	if importOptions["loadMeshes"]:
						#		try:
						#			if instance.fields["meshPath"].value != "NULL_STR":
						#				loadMesh(instance.fields["meshPath"].value.replace("/","\\"),instance.fields["mdfPath"].value,componentObj,loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath,lodTarget = meshLODTarget)
						#		except Exception as err:
						#			raiseWarning("Failed to load mesh on "+componentObj.name + " " + str(err))
						
						#RE4 Composite Mesh Group
						elif instance.instanceInfo.name == "via.render.CompositeMeshInstanceGroup":
							
							if importOptions["loadMeshes"]:
								compositeMeshLoadList.append(componentObj)#Since components are parsed in reverse order, the meshes have to be loaded later
						#RE4 Composite Mesh Instance		
						elif instance.instanceInfo.name == "via.render.CompositeMeshTransformController":
							componentObj.location = instance.fields["v2"].value[0:3]
							componentObj.rotation_mode = "QUATERNION"
							componentObj.rotation_quaternion = (instance.fields["v3"].value[3],instance.fields["v3"].value[0],instance.fields["v3"].value[1],instance.fields["v3"].value[2])#Blender quaternions are wxyz, not xyzw
							componentObj.scale = instance.fields["v4"].value[0:3]
						
						elif instance.instanceInfo.name == "via.physics.MeshShape":
							if importOptions["loadCollisions"]:
								if instance.fields["v01"].value != "NULL_STR":
									loadMCOL(instance.fields["v01"].value.replace("/","\\"),componentObj,currentChunkPath)
						elif instance.instanceInfo.name == "via.render.PointLight":
							if importOptions["loadLights"]:
								newLight = createLight("DISPLAY_PointLight",[("~TYPE","RSZ_DISPLAY_POINTLIGHT")],lightType = "POINT",parent = componentObj,collectionName=RootCollection.name)
								setLightDisplayObjectProperties(componentObj,newLight)
						elif instance.instanceInfo.name == "via.render.SpotLight":
							if importOptions["loadLights"]:
								newLight = createLight("DISPLAY_SpotLight",[("~TYPE","RSZ_DISPLAY_SPOTLIGHT")],lightType = "SPOT",parent = componentObj,collectionName=RootCollection.name)
								setLightDisplayObjectProperties(componentObj,newLight)
						elif instance.instanceInfo.name == "via.render.DirectionalLight":
							if importOptions["loadLights"]:
								componentObj.rotation_mode = "XYZ"
								componentObj.rotation_euler = (componentObj["Direction"][0],componentObj["Direction"][1],componentObj["Direction"][2])
								newLight = createLight("DISPLAY_DirectionalLight",[("~TYPE","RSZ_DISPLAY_DIRECTIONALLIGHT")],lightType = "SUN",parent = componentObj,collectionName=RootCollection.name)
								sunObject = newLight
								setLightDisplayObjectProperties(componentObj,newLight)
						
						elif instance.instanceInfo.name == "via.render.VolumetricFog":
							if fogObject == None:#
										fogObject = componentObj
							elif fogObject.get("Density",100.0) > componentObj.get("Density",101.0):#Get volumetric fog with the lowest density
								fogObject = componentObj
						#RE4		
						elif instance.instanceInfo.name == "chainsaw.DropItem":
							if componentObj.parent != None:
								componentObj.parent.empty_display_type = "SPHERE"
								
						elif instance.instanceInfo.name == "chainsaw.DropItemContext.SaveData":
							if importOptions["loadMeshes"]:
								itemInfo = getRE4ItemInfo(instance.fields["ItemID"].value)
								try:
									if itemInfo != None:
										
										loadMesh(itemInfo["Mesh Path"].replace("/","\\"),itemInfo["MDF Path"],componentObj,loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath)
								except Exception as err:
									raiseWarning("Failed to load mesh on "+componentObj.name + " " + str(err))
						instanceObjectDict.update({componentIndex:componentObj})
					
					else:
						importedInstanceIndexSet.add(componentIndex)
						
						instanceType = ""
						path = ""
						for entry in rszFile.rsz.RSZUserDataInfoList:
							if entry.instanceIndex == componentIndex:
								instanceType = hashToString(entry.hash,game)
								path = entry.string
						name = str(componentIndex).zfill(3)+"-( EXTERNAL "+instanceType+")"
						externalUserDataObj = createEmpty(name, [("~TYPE","RSZ_EXTERNAL_USERDATA"),("~instanceType",instanceType),("UserData Path",path)],previousObjectInstance,RootCollection.name)
						externalUserDataObj.re_rsz_object.rszIndex = componentIndex
						instanceObjectDict.update({componentIndex:externalUserDataObj})
			"""
			for index,prefabInfo in enumerate(rszFile.PrefabInfoList):
				name = "Prefab-"+str(index).zfill(3)+" ("+os.path.split(prefabInfo.string)[1]+")"
				createEmpty(name, [("~TYPE","RSZ_PREFAB"),("Prefab Path",prefabInfo.string)],parentObjectDict[prefabInfo.objectTableParentIndex],RootCollection.name)
			"""
			#RE4 composite mesh loading
			for meshInstanceGroup in compositeMeshLoadList:
				for index in meshInstanceGroup["v2"]:
					meshInstanceObj = instanceObjectDict[index]
					try:
						if meshInstanceGroup["v0"] != "NULL_STR":
							loadMesh(meshInstanceGroup["v0"].replace("/","\\"),meshInstanceGroup["v1"],meshInstanceObj,isCompositeMesh=True,loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath,lodTarget = meshLODTarget,collectionName=RootCollection.name)
					except Exception as err:
						raiseWarning("Failed to load mesh on "+componentObj.name + " " + str(err))
	
	elif fileType == "USR":
		prevObjectIndex = 0
		for objectIndex in rszFile.rsz.ObjectTable:#There can't be more than one object in a userdata afaik, but just in case there is more, account for it
			for instanceIndex in reversed(range(prevObjectIndex+1,objectIndex+1)):#Import in reverse so that the child objects can be parented properly
				instance = rszFile.rsz.InstanceList[instanceIndex]
				print(instanceIndex)
				print(instance)
				if instance.instanceInfo.isObject:
					parentObject = RSZRoot
				else:
					parentObject = previousObjectInstance
				name = str(instanceIndex).zfill(3)+"-("+instance.instanceInfo.name+")"
				componentObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObject,RootCollection.name)
				applyInstanceFields(instance, componentObj)
				if instance.instanceInfo.isObject:
					previousObjectInstance = componentObj
				componentObj.re_rsz_object.rszIndex = instanceIndex
				componentObj.empty_display_size = 0
				instanceObjectDict.update({instanceIndex:componentObj})
				importedInstanceIndexSet.add(instanceIndex)
	
	elif fileType == "PFB":
		#debug
		"""
		for info in rszFile.GameObjectInfoList:
			print(info)
		
		for info in rszFile.UserDataInfoList:
			print(info)
		
		for instance in rszFile.rsz.InstanceList:
			print(instance)
		"""
		for gameObjectInfo in rszFile.GameObjectInfoList:
			gameObjectInstanceIndex = rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex]
			importedInstanceIndexSet.add(gameObjectInstanceIndex)
			#Parse components backwards so that instances can be parented to their parent object properly
			
			gameObjectInstance =  rszFile.rsz.InstanceList[gameObjectInstanceIndex]
			
			
			subName = gameObjectInstance.fields["gameObjectName"].value+" "
			name = str(gameObjectInstanceIndex).zfill(3)+"-"+subName+"("+gameObjectInstance.instanceInfo.name+")"
			gameObjectObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObjectDict[gameObjectInfo.objectTableParentIndex],RootCollection.name)
			applyInstanceFields(gameObjectInstance, gameObjectObj)
			gameObjectObj.re_rsz_object.rszIndex = gameObjectInstanceIndex
			gameObjectObj["GUID"] = gameObjectInfo.uuid
			gameObjectObj["~virtualPrefabPath"] = ""
			gameObjectObj.show_name = True
			gameObjectObj.show_in_front = True
			#gameObjectObj.matrix_parent_inverse = parentObjectDict[gameObjectInfo.objectTableParentIndex].matrix_world.inverted()
			parentObjectDict.update({gameObjectInfo.objectTableIndex:gameObjectObj})
			instanceObjectDict.update({gameObjectInstanceIndex:gameObjectObj})
			previousObjectInstance = None
			for componentIndex in reversed(range(gameObjectInstanceIndex+1,rszFile.rsz.ObjectTable[gameObjectInfo.objectTableIndex+gameObjectInfo.componentCount]+1)):
				#print(componentIndex)
				if componentIndex not in externalUserDataIndexSet:
					importedInstanceIndexSet.add(componentIndex)
					instance = rszFile.rsz.InstanceList[componentIndex]
					if instance.instanceInfo.isObject:
						parentObject = gameObjectObj
					else:
						parentObject = previousObjectInstance
					name = str(componentIndex).zfill(3)+"-("+instance.instanceInfo.name+")"
					componentObj = createEmpty(name, [("~TYPE","RSZ_INSTANCE")],parentObject,RootCollection.name)
					applyInstanceFields(instance, componentObj)
					if instance.instanceInfo.isObject:
						previousObjectInstance = componentObj
					componentObj.re_rsz_object.rszIndex = componentIndex
					componentObj.empty_display_size = 0
					if instance.instanceInfo.name == "via.Transform":
						gameObjectObj.location = instance.fields["v00"].value[0:3]
						gameObjectObj.rotation_mode = "QUATERNION"
						gameObjectObj.rotation_quaternion = (instance.fields["v01"].value[3],instance.fields["v01"].value[0],instance.fields["v01"].value[1],instance.fields["v01"].value[2])#Blender quaternions are wxyz, not xyzw
						gameObjectObj.scale = instance.fields["v02"].value[0:3]
						
					elif instance.instanceInfo.name == "via.render.Mesh":
						if importOptions["loadMeshes"]:
							try:
								if instance.fields["meshPath"].value != "NULL_STR":
									loadMesh(instance.fields["meshPath"].value.replace("/","\\"),instance.fields["mdfPath"].value,componentObj,loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath,lodTarget = meshLODTarget,collectionName=RootCollection.name)
							except Exception as err:
								raiseWarning("Failed to load mesh on "+componentObj.name + " " + str(err))
					
					#RE4 Composite Mesh Group
					elif instance.instanceInfo.name == "via.render.CompositeMeshInstanceGroup":
						
						if importOptions["loadMeshes"]:
							compositeMeshLoadList.append(componentObj)#Since components are parsed in reverse order, the meshes have to be loaded later
					#RE4 Composite Mesh Instance		
					elif instance.instanceInfo.name == "via.render.CompositeMeshTransformController":
						componentObj.location = instance.fields["v2"].value[0:3]
						componentObj.rotation_mode = "QUATERNION"
						componentObj.rotation_quaternion = (instance.fields["v3"].value[3],instance.fields["v3"].value[0],instance.fields["v3"].value[1],instance.fields["v3"].value[2])#Blender quaternions are wxyz, not xyzw
						componentObj.scale = instance.fields["v4"].value[0:3]
					
					elif instance.instanceInfo.name == "via.physics.MeshShape":
						if importOptions["loadCollisions"]:
							if instance.fields["v01"].value != "NULL_STR":
								loadMCOL(instance.fields["v01"].value.replace("/","\\"),componentObj,currentChunkPath)		
					elif instance.instanceInfo.name == "via.render.PointLight":
						if importOptions["loadLights"]:
							newLight = createLight("DISPLAY_PointLight",[("~TYPE","RSZ_DISPLAY_POINTLIGHT")],lightType = "POINT",parent = componentObj,collectionName=RootCollection.name)
							setLightDisplayObjectProperties(componentObj,newLight)
					elif instance.instanceInfo.name == "via.render.SpotLight":
						if importOptions["loadLights"]:
							newLight = createLight("DISPLAY_SpotLight",[("~TYPE","RSZ_DISPLAY_SPOTLIGHT")],lightType = "SPOT",parent = componentObj,collectionName=RootCollection.name)
							setLightDisplayObjectProperties(componentObj,newLight)
					elif instance.instanceInfo.name == "via.render.DirectionalLight":
						if importOptions["loadLights"]:
							componentObj.rotation_mode = "XYZ"
							componentObj.rotation_euler = (componentObj["Direction"][0],componentObj["Direction"][1],componentObj["Direction"][2])
							newLight = createLight("DISPLAY_DirectionalLight",[("~TYPE","RSZ_DISPLAY_DIRECTIONALLIGHT")],lightType = "SUN",parent = componentObj,collectionName=RootCollection.name)
							sunObject = newLight
							setLightDisplayObjectProperties(componentObj,newLight)
					
					elif instance.instanceInfo.name == "via.render.VolumetricFog":
						if fogObject == None:#
							fogObject = componentObj
						elif fogObject.get("Density",100.0) > componentObj.get("Density",101.0):#Get volumetric fog with the lowest density
							fogObject = componentObj
					#RE4		
					elif instance.instanceInfo.name == "chainsaw.DropItem":
						if componentObj.parent != None:
							componentObj.parent.empty_display_type = "SPHERE"
							
					elif instance.instanceInfo.name == "chainsaw.DropItemContext.SaveData":
						if importOptions["loadMeshes"]:
							itemInfo = getRE4ItemInfo(instance.fields["ItemID"].value)
							try:
								if itemInfo != None:
									
									loadMesh(itemInfo["Mesh Path"].replace("/","\\"),itemInfo["MDF Path"],componentObj,loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath,lodTarget = meshLODTarget,collectionName=RootCollection.name)
							except Exception as err:
								raiseWarning("Failed to load mesh on "+componentObj.name + " " + str(err))
					instanceObjectDict.update({componentIndex:componentObj})
				
				else:
					importedInstanceIndexSet.add(componentIndex)
					
					instanceType = ""
					path = ""
					for entry in rszFile.rsz.RSZUserDataInfoList:
						if entry.instanceIndex == componentIndex:
							instanceType = hashToString(entry.hash,game)
							path = entry.string
					name = str(componentIndex).zfill(3)+"-( EXTERNAL "+instanceType+")"
					externalUserDataObj = createEmpty(name, [("~TYPE","RSZ_EXTERNAL_USERDATA"),("~instanceType",instanceType),("UserData Path",path)],previousObjectInstance,RootCollection.name)
					externalUserDataObj.re_rsz_object.rszIndex = componentIndex
					instanceObjectDict.update({componentIndex:externalUserDataObj})
	if not importOptions["optimizedImport"]:
		addIndexConstraints(instanceObjectDict)
	#print(parentObjectDict)
	if firstFile:#Clear cache once the first scn has been fully imported (after all recursion has been done)
		if importOptions["optimizedImport"]:
			if importOptions["loadMeshes"]:
				#print(optimizedMeshImportDict)
				meshInstanceCollection = bpy.data.collections.get("RSZ Mesh Instances",None)#Create collection if the name given doesn't exist
				if meshInstanceCollection == None:
				    meshInstanceCollection = bpy.data.collections.new("RSZ Mesh Instances")
				    bpy.context.scene.collection.children.link(meshInstanceCollection)
	
				meshRootCollection = bpy.data.collections.get("RSZ Mesh Roots",None)#Create collection if the name given doesn't exist
				if meshRootCollection == None:
				    meshRootCollection = bpy.data.collections.new("RSZ Mesh Roots")
				    bpy.context.scene.collection.children.link(meshRootCollection)
				optimizedMeshLoadCount = len(optimizedMeshImportDict)
				for index, (meshPath, meshEntry) in enumerate(optimizedMeshImportDict.items()):
					try:
						rootMesh = loadMesh(meshPath.replace("/","\\"),meshEntry["mdfPath"],None,optimizedImport=True,loadMaterials=importOptions["loadMaterials"],loadUnusedTextures = importOptions["loadUnusedTextures"],loadUnusedProps = importOptions["loadUnusedProps"],useBackfaceCulling = importOptions["useBackfaceCulling"],currentChunkPath = currentChunkPath,collectionName="RSZ Mesh Roots",lodTarget = meshLODTarget)
						rootMesh.scale = (1.0,1.0,1.0)
						make_duplicator(meshInstanceCollection,rootMesh,meshEntry["matrixList"])
						if index % 10 == 0:
							print(f"Optimized Mesh Import {str(index)} / {str(optimizedMeshLoadCount)}")
					except Exception as err:
						raiseWarning("Failed to import mesh " + meshPath +" "+ str(err))
				
				#bpy.data.collections['RSZ Mesh Roots'].hide_viewport = True
			if importOptions["loadCollisions"]:
				mcolInstanceCollection = bpy.data.collections.get("MCOL Instances",None)#Create collection if the name given doesn't exist
				if mcolInstanceCollection == None:
				    mcolInstanceCollection = bpy.data.collections.new("MCOL Instances")
				    bpy.context.scene.collection.children.link(mcolInstanceCollection)
	
				for mcolPath, matrixList in optimizedMCOLImportDict.items():
					try:
						rootMesh = loadMCOL(mcolPath.replace("/","\\"),None,currentChunkPath)
						if rootMesh != None:
							rootMesh.scale = (1.0,1.0,1.0)
							make_duplicator(mcolInstanceCollection,rootMesh,matrixList)
					except Exception as err:
						raiseWarning("Failed to load " + mcolPath + " " + str(err))
		clearOptimizedMeshImportCache()
		optimizedObjectDeleteList.clear()
		clearBlenderMeshCache()#Remove dict references to blender objects, otherwise it will cause issues when things are deleted
		importedSCNSet = set()
		
	if importOptions["optimizeEEVEESettings"]:
		setupEEVEE(sunObject,fogObject)
	print("Finished importing " + filepath)
	return True
	"""
	for index, instance in enumerate(rszFile.rsz.InstanceList):
		index += 1
		if instance.instanceInfo.name == "via.GameObject":
			subName = instance.v0.value+" "
		else:
			subName=""
		name = str(index).zfill(3)+"-"+subName+"("+instance.instanceInfo.name+")"
		createEmpty(name, [("~TYPE","RSZ_INSTANCE")],RSZRoot,RootCollection.name)
	"""
	
def getRSZTreeRecursive(ob, levels=32):
    hierarchyList = []
    def recurse(ob, parent, depth,hierarchyList):
        if depth > levels: 
            return
        #file.write("  " * depth, ob.name)
        instanceType = ob.get("~instanceType",None)
        
        if instanceType == "via.Folder" or instanceType == "via.GameObject":
            hierarchyList.append(ob)
        for child in sorted(ob.children,key=lambda k: k.re_rsz_object.rszIndex):
            recurse(child, ob,  depth + 1,hierarchyList)
        if instanceType != "via.Folder" and instanceType != "via.GameObject" and (ob.get("~TYPE",None) == "RSZ_INSTANCE" or ob.get("~TYPE",None) == "RSZ_EXTERNAL_USERDATA"):
            hierarchyList.append(ob)
    recurse(ob, ob.parent, 0,hierarchyList)
    return hierarchyList
def reindexTree(rootObj):#TODO
	


    

	
	hierarchyList = getRSZTreeRecursive(rootObj,32)#Get all rsz objects recursively and put them in a list in correct order
	
	
	for index,obj in enumerate(hierarchyList):
	    obj.re_rsz_object.rszIndex = index + 1
	    
	for obj in hierarchyList:
		#Fix index pointers, this will only work on fields that have actually been marked as object indices
		if len(obj.re_rsz_object.rszObjectPointers) != 0:
			for item in obj.re_rsz_object.rszObjectPointers:
				if item.targetObject != None:
					#print(item.targetObject)
					if item.fieldName.endswith("]"):#Is array
						split = item.fieldName.rsplit("[",1)
						realFieldName = split[0]
						arrayIndex = int(split[1].replace("]",""))
						obj[realFieldName][arrayIndex] = item.targetObject.re_rsz_object.rszIndex
						#print("Set array rsz index field " + item.fieldName)
					else:
						#print("Set non array rsz index field " + item.fieldName)
						obj[item.fieldName] = item.targetObject.re_rsz_object.rszIndex


def getChildObjectList(obj,levels = 20):
   objList = []
   def recurse(obj, parent, depth):
	   if depth > levels: 
		   return
	   #print("  " * depth, ob.name)
	   objList.append(obj)

	   for child in obj.children:
		   recurse(child, obj,  depth + 1)
   recurse(obj, obj.parent, 0)
   return objList
#EXPORT FUNCTIONS

def exportRSZFile(targetTree,filepath,fileType = "SCN",game = "RE4"):
	
	if fileType == "SCN":
		rszFile = SCNFile()
	elif fileType == "USR":
		rszFile = UserFile()
	elif fileType == "PFB":
		rszFile = PFBFile()
	else:
		raiseWarning("Unknown file type:" + fileType)
		return False
	
	#reindexTree(targetTree)
	

	obj = bpy.context.active_object
	objList = getChildObjectList(obj)
	currentObjectTableIndex = 0
	
	currentPrefabIndex = 0#Used for game object virtual prefabs and via.Prefab
	objectTableObjIndexDict = {}
	rszFile.rsz.InstanceInfoList.append(InstanceInfo())#Add null entry
	resourceInfoSet = set()
	instanceObjList = sorted([obj for obj in objList if obj.get("~TYPE",None) == "RSZ_INSTANCE" or obj.get("~TYPE",None) == "RSZ_EXTERNAL_USERDATA"],key = lambda obj: obj.re_rsz_object.rszIndex)
	
	prefabObjList = sorted([obj for obj in objList if obj.get("~TYPE",None) == "RSZ_PREFAB"],key = lambda obj: obj.name)
	prefabNameIndexDict = {}
	"""
	for index,prefabObj in enumerate(prefabObjList):
		prefabNameIndexDict[os.path.split(prefabObj["Prefab Path"])[1].split(".pfb")[0]] = index
	print(prefabNameIndexDict)
	"""
	#print(instanceObjList)
	#Fill object table first so that the parent can be gotten if the components come before the game object
	for instanceObj in instanceObjList:
		
		if instanceObj["~TYPE"] == "RSZ_INSTANCE":
			
			if instanceObj["~isObject"]:
				rszFile.rsz.ObjectTable.append(instanceObj.re_rsz_object.rszIndex)
				objectTableObjIndexDict[instanceObj] = currentObjectTableIndex
				currentObjectTableIndex += 1
	
	
	for instanceObj in instanceObjList:
		
		instanceHash = stringToHash(instanceObj["~instanceType"],game)
		if instanceObj["~TYPE"] == "RSZ_INSTANCE":
				
			newInstance = getRSZInstance(instanceHash,game)()
			newInstance.setFields(instanceObj)
			newInstance.instanceInfo.isObject = instanceObj["~isObject"]
			rszFile.rsz.InstanceList.append((newInstance))
			#print(newInstance.fields)
			if instanceObj["~instanceType"] == "via.GameObject":
				componentCount = 0
				for obj in instanceObj.children:
					if obj.get("~TYPE",None) == "RSZ_INSTANCE" and obj.get("~instanceType",None) == "via.Transform":
						obj["v00"] = (instanceObj.location[0],instanceObj.location[1],instanceObj.location[2],0.0)
						obj["v01"] = (instanceObj.rotation_quaternion[1],instanceObj.rotation_quaternion[2],instanceObj.rotation_quaternion[3],instanceObj.rotation_quaternion[0])
						obj["v02"] = (instanceObj.scale[0],instanceObj.scale[1],instanceObj.scale[2],0.0)
					if obj.get("~TYPE",None) == "RSZ_INSTANCE" and obj.get("~instanceType",None) != "via.GameObject" and obj.get("~instanceType",None) != "via.Folder" and obj["~isObject"] == True:
						componentCount += 1
				if fileType == "PFB":
					newGameObjectInfo = GameObjectInfoPFB()
				else:
					newGameObjectInfo = GameObjectInfo()
				newGameObjectInfo.uuid = int.to_bytes((int(instanceObj["GUID"])),length = 16,byteorder= "little",signed = False)
				newGameObjectInfo.objectTableIndex = objectTableObjIndexDict[instanceObj]
				newGameObjectInfo.componentCount = componentCount
				if instanceObj.parent != None and instanceObj.parent.get("~instanceType",None) == "via.GameObject" or instanceObj.parent.get("~instanceType",None) == "via.Folder":
					newGameObjectInfo.objectTableParentIndex = objectTableObjIndexDict[instanceObj.parent]
				else:
					newGameObjectInfo.objectTableParentIndex = -1
					
					
				#If using a virtual prefab path, make prefab info
				
				#Check if virtual prefab path has already been used
				if instanceObj["~virtualPrefabPath"].strip() != "" and prefabNameIndexDict.get(instanceObj["~virtualPrefabPath"],None) == None:
					
					prefabNameIndexDict[instanceObj["~virtualPrefabPath"]] = currentPrefabIndex
					currentPrefabIndex += 1
				
					newPrefabInfo = PrefabInfo()
					newPrefabInfo.string = instanceObj["~virtualPrefabPath"]
					if instanceObj.parent != None and instanceObj.parent.get("~isObject",None) == True:
						newPrefabInfo.objectTableParentIndex = objectTableObjIndexDict[instanceObj.parent]
					else:
						newPrefabInfo.objectTableParentIndex = -1
					rszFile.PrefabInfoList.append(newPrefabInfo)
				
				newGameObjectInfo.prefabID = prefabNameIndexDict.get(instanceObj["~virtualPrefabPath"],-1)
				rszFile.GameObjectInfoList.append(newGameObjectInfo)
			
			
			#Actual prefab paths don't get prefab infos, so prefab infos is only for virtual prefabs
			"""
			elif instanceObj["~instanceType"] == "via.Prefab":#Add prefab info to list
				if instanceObj["v01"] != "" and instanceObj["v01"] != "NULL_STR" and prefabNameIndexDict.get(instanceObj["v01"],None) == None:
					prefabNameIndexDict[instanceObj["v01"]] = currentPrefabIndex
					currentPrefabIndex += 1
					
					newPrefabInfo = PrefabInfo()
					newPrefabInfo.string = instanceObj["v01"]
					if instanceObj.parent != None and instanceObj.parent.get("~isObject",None) == True:
						newPrefabInfo.objectTableParentIndex = objectTableObjIndexDict[instanceObj.parent]
					else:
						newPrefabInfo.objectTableParentIndex = -1
					rszFile.PrefabInfoList.append(newPrefabInfo)
			"""
			if instanceObj["~instanceType"] == "via.Folder":
				newFolderInfo = FolderInfo()
				newFolderInfo.objectTableIndex = objectTableObjIndexDict[instanceObj]
				if instanceObj.parent != None and instanceObj.parent.get("~instanceType",None) == "via.GameObject" or instanceObj.parent.get("~instanceType",None) == "via.Folder":
					newFolderInfo.objectTableParentIndex = objectTableObjIndexDict[instanceObj.parent]
				else:
					newFolderInfo.objectTableParentIndex = -1
				rszFile.FolderInfoList.append(newFolderInfo)
			for field in newInstance.fields.values():
				if "REMAP_Resource" in field.tagSet:
					if field.isList:
						if field.value != []:
							for listValue in field.value:
								if listValue not in resourceInfoSet:
									resourceInfoSet.add(listValue)
									newResourceInfo = ResourceInfo()
									newResourceInfo.string = listValue
									rszFile.ResourceInfoList.append(newResourceInfo)
					elif field.value not in resourceInfoSet:
						if field.value != "" and field.value != "NULL_STR":
							resourceInfoSet.add(field.value)
							newResourceInfo = ResourceInfo()
							newResourceInfo.string = field.value
							rszFile.ResourceInfoList.append(newResourceInfo)
			
		elif instanceObj["~TYPE"] == "RSZ_EXTERNAL_USERDATA":
			newRSZUserDataInfo = RSZUserDataInfo()
			newRSZUserDataInfo.instanceIndex = instanceObj.re_rsz_object.rszIndex
			newRSZUserDataInfo.hash = instanceHash
			if "natives" in instanceObj["UserData Path"]:
				userDataPath = instanceObj["UserData Path"].split(os.path.join("natives,STM"))[1].split(".2")[0]
			else:
				userDataPath = instanceObj["UserData Path"].split(".2")[0]
			newRSZUserDataInfo.string = userDataPath
			rszFile.rsz.RSZUserDataInfoList.append(newRSZUserDataInfo)
			
			newUserDataInfo = UserDataInfo()
			newUserDataInfo.hash = instanceHash
			#newUserDataInfo.CRC = hashToCRC(instanceHash)
			newUserDataInfo.CRC = 0
			newUserDataInfo.string = userDataPath
			rszFile.UserDataInfoList.append(newUserDataInfo)
		newInstanceInfo = InstanceInfo()
		newInstanceInfo.typeIDHash = instanceHash
		newInstanceInfo.CRC = hashToCRC(instanceHash,game)
		rszFile.rsz.InstanceInfoList.append(newInstanceInfo)
		
	
	"""
	for prefabObj in prefabObjList:
		newPrefabInfo = PrefabInfo()
		newPrefabInfo.string = prefabObj["Prefab Path"]
		if prefabObj.parent != None and prefabObj.parent.get("~isObject",None) == True:
			newPrefabInfo.objectTableParentIndex = objectTableObjIndexDict[prefabObj.parent]
		else:
			newPrefabInfo.objectTableParentIndex = -1
		rszFile.PrefabInfoList.append(newPrefabInfo)
	"""
	"""
	for prefabInfo in rszFile.PrefabInfoList:
		print(prefabInfo.string)
	"""
	#print(rszFile.PrefabInfoList)	
	#print(rszFile.ResourceInfoList)
	#print(prefabObjList)
	if fileType == "SCN":
		writeRE_SCN(rszFile, filepath, game)
	elif fileType == "USR":
		writeRE_User(rszFile, filepath, game)	
	elif fileType == "PFB":
		writeRE_PFB(rszFile, filepath, game)	
	else:
		raiseWarning("Unknown file type:" + fileType)
		return False
	return True