#Author: NSA Cloud

#Stripped down import only version of RE Mesh Editor

import bpy
import bmesh
import os
from math import radians,floor,sqrt
from mathutils import Vector,Matrix
from itertools import chain, repeat, islice
from .file_re_mesh import readREMesh,Sphere,AABB,Matrix4x4,meshFileVersionToGameNameDict
from .re_mesh_parse import ParsedREMesh,VisconGroup,LODLevel,SubMesh,ParsedBone,Skeleton
from ..mdf.file_re_mdf import readMDF
from ..mdf.blender_re_mesh_mdf import findMDFPathFromMeshPath,importMDF
from ..gen_functions import splitNativesPath,raiseWarning
from ..blender_utils import showErrorMessageBox
import time
import numpy as np																																																																												
timeFormat = "%d"
rotateNeg90Matrix = Matrix.Rotation(radians(-90.0), 4, 'X')
rotate90Matrix = Matrix.Rotation(radians(90.0), 4, 'X')
def triangulateMesh(mesh):
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bmesh.ops.triangulate(bm, faces = bm.faces[:])
    bm.to_mesh(mesh)

def pad_infinite(iterable, padding=None):
	return chain(iterable, repeat(padding))

def pad(iterable, size, padding=None):
	return islice(pad_infinite(iterable, padding), size)
def normalize(lst):
	s = sum(lst)
	if s != 0.0:
		return list(map(lambda x: float(x)/s, lst))
	else: 
		return lst
def normalizeVec(vec):
    return Vector(vec).normalized()
def dist(a, b) -> float:
    return  ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)**0.5
def bounding_sphere_ritter(points):
    # Initial guess, same as before
    x = points[0]    #any arbitrary point in the point cloud works
    y = max(points,key= lambda p: dist(p,x) )    #choose point y furthest away from x
    z = max(points,key= lambda p: dist(p,y) )    #choose point z furthest away from y
    center, radius = (((y[0]+z[0])/2,(y[1]+z[1])/2,(y[2]+z[2])/2), dist(y,z)/2)    #initial bounding sphere
    
    # Note this doesn't use the radius^2 optimization that Ritter uses
    for p in points:
        d = dist(p, center)
        if d < radius:
            continue
        radius = .5 * (radius + d)
        old_to_new = d - radius
        new_center_x = (center[0] * radius + old_to_new * p[0]) / d
        new_center_y = (center[1] * radius + old_to_new * p[1]) / d
        new_center_z = (center[2] * radius + old_to_new * p[2]) / d
        center = (new_center_x, new_center_y, new_center_z)
    return center, radius
    
def vertexPosToGlobal(local_coords, world_matrix):

    # Reshape coords to Nx3 matrix
    local_coords.shape = (-1, 3)

    # Add an extra 1.0s column (for matrix dot product)
    local_coords = np.c_[local_coords, np.ones(local_coords.shape[0])]

    # Then:
    # Dot product matrix with the coords transpose
    # Keep the first 3 rows (x,y,z)
    # Transpose result to Nx3
    # Flatten
    global_coords = np.dot(world_matrix, local_coords.T)[0:3].T.reshape((-1))
    return np.reshape(global_coords,(-1,3))

def joinObjects(objList):
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
	
def createMaterialDict(materialNameList):
	materialDict = {}
	for materialName in materialNameList:
		material = bpy.data.materials.new(materialName)
		material.use_nodes = True;
		materialDict[materialName] = material
	return materialDict

def getCollection(collectionName,parentCollection = None,makeNew = False):
	if makeNew or not bpy.data.collections.get(collectionName):
		collection = bpy.data.collections.new(collectionName)
		collectionName = collection.name
		if parentCollection != None:
			parentCollection.children.link(collection)
		else:
			bpy.context.scene.collection.children.link(collection)
	return bpy.data.collections[collectionName]

def findArmatureObjFromData(armatureData):
	armatureObj = None
	for obj in bpy.context.scene.objects:
		if obj.type == "ARMATURE" and obj.data == armatureData:
			armatureObj = obj
			break
	return armatureObj
def importSkeleton(parsedSkeleton,armatureName,collection,rotate90,targetArmatureName = None):
	mergedArmature = False
	#Merging with existing armature if specified in import menu
	
	if targetArmatureName != "" and targetArmatureName in bpy.data.armatures:
		armatureObj = findArmatureObjFromData(bpy.data.armatures[targetArmatureName])
		if armatureObj != None:
			armatureData = armatureObj.data
			mergedArmature = True
		else:
			armatureData = bpy.data.armatures.new(armatureName)	
			armatureObj = bpy.data.objects.new(armatureName, armatureData)
			collection.objects.link(armatureObj)
		
	else:
		armatureData = bpy.data.armatures.new(armatureName)	
		armatureObj = bpy.data.objects.new(armatureName, armatureData)
		collection.objects.link(armatureObj)
	armatureObj.hide_viewport = False
	bpy.context.view_layer.objects.active = armatureObj
	bpy.ops.object.mode_set(mode='EDIT')
	
	boneNameIndexDict = {index: bone.boneName for index, bone in enumerate(parsedSkeleton.boneList)}
	
	boneParentList = []#List of tuples containing armature bone and parent bone name string
	for bone in parsedSkeleton.boneList:
		if bone.boneName not in armatureData.bones:
			editBone = armatureData.edit_bones.new(bone.boneName)
			editBone.tail = editBone.head + Vector((.0, .0, .1))
			if bone.parentIndex != -1:
				boneParentList.append((editBone,boneNameIndexDict[bone.parentIndex]))#Set bone parents after all bones have been imported
				#editBone.parent = armatureData.edit_bones[boneNameIndexDict[bone.parentIndex]]
			else:
				bone.head = Vector([.0, .0, .01])
				
			if bone.boundingBox != None:
				editBone.length = sqrt((bone.boundingBox.max.x - bone.boundingBox.min.x)**2 + (bone.boundingBox.max.y - bone.boundingBox.min.y)**2 + (bone.boundingBox.max.z - bone.boundingBox.min.z)**2)*.15
			else:
				editBone.length = .05
			if editBone.length < .01:
				editBone.length = .01
			editBone.matrix = bone.worldMatrix.matrix
			editBone["reMeshWorldMatrix"] = bone.worldMatrix.matrix
			editBone["reMeshLocalMatrix"] = bone.localMatrix.matrix
			editBone["reMeshInverseMatrix"] = bone.inverseMatrix.matrix
			if mergedArmature:
				print(f"[MERGE] Added {bone.boneName} to {armatureObj.name}")
	#Assign bone parents
	for editBone,parentBoneName in boneParentList:
		editBone.parent = armatureData.edit_bones[parentBoneName]
		
	
	bpy.ops.object.mode_set(mode='OBJECT')
	
	if rotate90 and targetArmatureName not in bpy.data.objects:
		prevSelection = bpy.context.selected_objects
		for obj in prevSelection:
			obj.select_set(False)
		
		armatureObj.matrix_world = armatureObj.matrix_world @ rotate90Matrix
		armatureObj.select_set(True)
		#I would prefer not to use bpy.ops but the data.transform on armatures does not function correctly.
		bpy.ops.object.transform_apply(location = False,rotation = True,scale = False)
		armatureObj.select_set(False)
		
		for obj in prevSelection:
			obj.select_set(True)
	return armatureObj

def importMesh(meshName = "newMesh",vertexList = [],faceList = [],vertexNormalList = [],vertexColor0List = [],vertexColor1List = [],UV0List = [],UV1List = [],UV2List = [],boneNameList = [],vertexGroupWeightList = [],vertexGroupBoneIndicesList = [],boneNameRemapList = [],material="Material",armature = None,collection = None,rotate90 = True,blendShapeList = []):
	meshData = bpy.data.meshes.new(meshName)
	#Import vertices and faces
	meshData.from_pydata(vertexList, [], faceList)
	
	#Import vertex normals
	if vertexNormalList != []:
		
		
		meshData.update(calc_edges=True)
		meshData.polygons.foreach_set("use_smooth", [True] * len(meshData.polygons))
		meshData.normals_split_custom_set_from_vertices([normalizeVec(v) for v in vertexNormalList])
		if bpy.app.version < (4,0,0):
			meshData.use_auto_smooth = True
			meshData.calc_normals_split()
		"""
		meshData.use_auto_smooth = True
		meshData.polygons.foreach_set("use_smooth", [True] * len(meshData.polygons))
		meshData.normals_split_custom_set_from_vertices(vertexNormalList)
		"""
	#Import UV Layers
	UVLayerList = (UV0List,UV1List,UV2List)
	for layerIndex,layer in enumerate(UVLayerList):
		if layer != []:
			newUVLayer = meshData.uv_layers.new(name = "UVMap"+str(layerIndex))
			for face in meshData.polygons:
				for vertexIndex, loopIndex in zip(face.vertices, face.loop_indices):
					newUVLayer.data[loopIndex].uv = layer[vertexIndex]
	
	
	#Import vertex color layer 0
	if vertexColor0List != []:
		vcol_layer = meshData.vertex_colors.new()
		for l,color in zip(meshData.loops, vcol_layer.data):
			color.color = vertexColor0List[l.vertex_index]
	
	meshObj = bpy.data.objects.new(meshName, meshData)
	
	#Import Weights
	if vertexGroupWeightList != [] and boneNameList != []:
		#Only create vertex groups for bones that get used
		
		if len(boneNameList) > 1:
			#print(boneNameList)
			usedBoneIndices = sorted(list({x for vertex in vertexGroupBoneIndicesList for x in vertex}))#Get all used bone indices in hierarchy order
			for boneIndex in usedBoneIndices:
				meshObj.vertex_groups.new(name = boneNameList[boneIndex])
				
			for vertexIndex, boneIndexList in enumerate(vertexGroupBoneIndicesList):
				#print(vertexIndex)
				#print(boneIndexList)
				for weightIndex, boneIndex in enumerate(boneIndexList):
					if vertexGroupWeightList[vertexIndex][weightIndex] > 0:
						boneName = boneNameList[boneIndex]
						meshObj.vertex_groups[boneName].add([vertexIndex],vertexGroupWeightList[vertexIndex][weightIndex],'ADD')
		else:#No bone remap table edge case
			vg = meshObj.vertex_groups.new(name=boneNameList[0])
			for i in range(len(meshObj.data.vertices)):
				vg.add([i], 1.0, 'REPLACE')
	
	
	
	if armature != None:
		meshObj.parent = armature
		mod = meshObj.modifiers.new(name = 'Armature', type = 'ARMATURE')
		mod.object = armature
		#meshObj.matrix_parent_inverse = armature.matrix_world.inverted()
	if rotate90:
		meshObj.data.transform(rotate90Matrix)
			
		
		#meshObj.matrix_world = meshObj.matrix_world @ rotate90Matrix
	if material != None:
		meshObj.data.materials.append(material)
	if collection != None:
		collection.objects.link(meshObj)
	else:
		bpy.context.scene.collection.objects.link(meshObj)
	
	#Import Blend Shapes
	if blendShapeList != []:
		skB = meshObj.shape_key_add(name = "Basis")
		skB.interpolation = 'KEY_LINEAR'
		print(meshObj.name)
		
		for blendShapeEntry in blendShapeList:
				name = blendShapeEntry.blendShapeName
				print(name)
				#print(blendShapeEntry.deltas)
				deltas = [Vector (val) for val in blendShapeEntry.deltas]
				#print(deltas)
				sk = meshObj.shape_key_add(name = name)
				sk.interpolation = 'KEY_LINEAR'
				print(f"mesh vertices: {len(meshObj.data.vertices)}")
				print(f"delta vertices: {len(deltas)}")
				#if len(deltas) == len(meshObj.data.vertices):
				for i in range(len(meshObj.data.vertices)):
					sk.data[i].co = meshObj.data.vertices[i].co + deltas[i]
	
	return meshObj

def importLODGroup(parsedMesh,meshType,meshCollection,materialDict,armatureObj,hiddenCollectionSet,meshOffsetDict,importAllLODs = False,createCollections = True,importShadowMeshes = False,rotate90 = True,mergeGroups = False):
	newObjList = []
	if meshType == "Main Mesh":
		shortName = "Main"
		targetLODList = parsedMesh.mainMeshLODList
	elif meshType == "Shadow Mesh":
		shortName = "Shadow"
		targetLODList = parsedMesh.shadowMeshLODList
	elif meshType == "Occlusion Mesh":
		shortName = "Occlusion"
	firstLOD = True
	
	if parsedMesh.skeleton != None:
		if parsedMesh.skeleton.weightedBones != []:
			boneNameList = parsedMesh.skeleton.weightedBones
		elif len(parsedMesh.skeleton.boneList) != 0:#No bone remap table
			boneNameList = [parsedMesh.skeleton.boneList[0].boneName]
	else:
		boneNameList = []
	
	if not importAllLODs and targetLODList != []:
		targetLODList = [targetLODList[0]]
	
	
	for lodIndex,lod in enumerate(targetLODList):
		shadowLODString = ""
		if importShadowMeshes:
			if lod in parsedMesh.shadowMeshLinkedLODList:
				shadowLODString = f" + Shadow LOD{parsedMesh.shadowMeshLinkedLODList.index(lod)}"
		if createCollections and importAllLODs:
			lodCollection = getCollection(f"{meshType} LOD{str(lodIndex)}{shadowLODString} - {meshCollection.name}",meshCollection,makeNew = True)
			lodCollection["LOD Distance"] = lod.lodDistance
		else:
			lodCollection = meshCollection
		if not firstLOD and createCollections:
			#lodCollection.hide_viewport = True
			hiddenCollectionSet.add(lodCollection.name)
		for visconGroup in lod.visconGroupList:
			objMergeList = []
			for subMesh in visconGroup.subMeshList:
				if subMesh.isReusedMesh:	
					lodCollection.objects.link(meshOffsetDict[subMesh.meshVertexOffset])
				else:
					materialName = parsedMesh.materialNameList[subMesh.materialIndex]
					#print(subMesh.vertexPosList)
					
					if importAllLODs:
						LODNum = f"LOD_{str(lodIndex)}_"
					else:
						LODNum = ""
					meshObj = importMesh(
						#meshName=f"LOD_{str(lodIndex)}_{shortName}_Group_{str(visconGroup.visconGroupNum)}_Sub_{str(subMesh.subMeshIndex)}__{materialName}",
						
						
						
						meshName=f"{LODNum}Group_{str(visconGroup.visconGroupNum)}_Sub_{str(subMesh.subMeshIndex)}__{materialName}",
						vertexList=subMesh.vertexPosList,
						faceList=subMesh.faceList,
						vertexNormalList=subMesh.normalList,
						
						vertexColor0List=subMesh.colorList,
						UV0List=subMesh.uvList,
						UV1List=subMesh.uv2List,
						boneNameList=boneNameList,
						vertexGroupWeightList=subMesh.weightList,
						vertexGroupBoneIndicesList=subMesh.weightIndicesList,
						material = materialDict[materialName],
						armature=armatureObj,
						collection=lodCollection,
						rotate90 = rotate90,
						blendShapeList = subMesh.blendShapeList
						)
					if mergeGroups:
						objMergeList.append(meshObj)
					else:
						newObjList.append(meshObj)
					meshOffsetDict[subMesh.meshVertexOffset] = meshObj
			if mergeGroups:
				if len(objMergeList) > 1:
					newObj = joinObjects(objMergeList)
				else:
					newObj = objMergeList[0] 
				newObjList.append(newObj)
				
		firstLOD = False
		return newObjList


def importBoundingBox(bbox,bboxName,meshCollection,armatureObj = None,boneParent = None,rotate90 = True):
	bboxVertList = [
	(bbox.min.x,bbox.min.y,bbox.min.z),
	(bbox.max.x,bbox.max.y,bbox.max.z),
	
	]
	bboxData = bpy.data.meshes.new(bboxName)
	bboxData.from_pydata(bboxVertList, [], [])
	bboxData.update()
	
	bboxObj = bpy.data.objects.new(bboxName, bboxData)
	meshCollection.objects.link(bboxObj)
	
	if armatureObj != None and boneParent != None:
		constraint = bboxObj.constraints.new(type = "CHILD_OF")
		constraint.target = armatureObj
		constraint.subtarget = boneParent
		constraint.name = "BoneName"
		constraint.inverse_matrix =  Matrix()
		bboxObj["~TYPE"] = "RE_MESH_BONE_BOUNDING_BOX"
	else:
		bboxObj["~TYPE"] = "RE_MESH_BOUNDING_BOX"
		if rotate90:
			bboxObj.matrix_world = bboxObj.matrix_world @ rotate90Matrix
	
	
	bboxObj["MeshExportExclude"] = 1
	
	bboxObj.show_bounds = True
	return bboxObj
def importBoundingSphere(sphere,sphereName,meshCollection,rotate90 = True):
	# Create an empty mesh and the object.
	sphereData = bpy.data.meshes.new(sphereName)
	sphereObj = bpy.data.objects.new(sphereName, sphereData)
	sphereObj.location = (sphere.x,sphere.y,sphere.z)
	sphereObj.display_type = "BOUNDS"
	sphereObj.display_bounds_type ="SPHERE"
	sphereObj["~TYPE"] = "RE_MESH_BOUNDING_SPHERE"
	sphereObj["MeshExportExclude"] = 1
	#sphereData.update()
	
	# Add the object into the scene.
	meshCollection.objects.link(sphereObj)
	

	
	
	# Construct the bmesh sphere and assign it to the blender mesh.
	bm = bmesh.new()
	bmesh.ops.create_uvsphere(bm, u_segments=8, v_segments=8, radius=sphere.r)
	bm.to_mesh(sphereData)
	bm.free()
	bpy.context.view_layer.update()
	if rotate90:
		sphereObj.matrix_world = rotate90Matrix @ sphereObj.matrix_world
	return sphereObj
def importBoundingBoxes(meshBoundingBox,meshBoundingSphere,meshCollection,armatureObj,parsedSkeleton = None,rotate90 = True):
		meshBBox = importBoundingBox(meshBoundingBox,"Mesh Bounding Box",meshCollection,rotate90 = rotate90)
		meshSphere = importBoundingSphere(meshBoundingSphere,"Mesh Bounding Sphere",meshCollection,rotate90 = rotate90)
		if parsedSkeleton != None:
			for bone in parsedSkeleton.boneList:
				if bone.boundingBox != None:
					importBoundingBox(bone.boundingBox,f"Bone Bounding Box ({bone.boneName})",meshCollection,armatureObj,bone.boneName,rotate90)

meshGameNameConflictDict = set(["RERT"])#Games that use the same mesh version
def resolveMeshGameNameConflict(gameName,filePath):
	rootPath = os.path.split(filePath)[0]
	realGameName = None
	if gameName == "RERT":
		if "RE2" in rootPath:
			realGameName = "RE2RT"
		elif "RE3" in rootPath or "escape" in rootPath.lower():
			realGameName = "RE3RT"
		else:
			realGameName = "RE2RT"
	if realGameName == None:
		realGameName = gameName
	return gameName

#---RE MESH IO FUNCTIONS---#

def importREMeshFile(filePath,options,lodTarget):
	#print(options)
	meshImportStartTime = time.time()
	fileName = os.path.split(filePath)[1].split(".mesh")[0]
	try:
		meshVersion = int(os.path.splitext(filePath)[1].replace(".",""))
	except:
		print("Unable to parse mesh version number in file path.")
		meshVersion = None
	if meshVersion in meshFileVersionToGameNameDict:
		gameName = meshFileVersionToGameNameDict[meshVersion]
		if gameName in meshGameNameConflictDict:
			gameName = resolveMeshGameNameConflict(gameName, filePath)
	else:
		gameName = None
		
	warningList = []
	errorList = []
	
		
	reMesh = readREMesh(filePath,lodTarget)
	meshFileName = os.path.splitext(os.path.split(filePath)[1])[0]
	parsedMesh = ParsedREMesh()
	parsedMesh.ParseREMesh(reMesh)
	armatureObj = None
	meshCollection = bpy.context.scene.collection
	hiddenCollectionSet = set()
	if parsedMesh.skeleton != None:
		armatureObj = importSkeleton(parsedMesh.skeleton,meshFileName.split(".mesh")[0]+" Armature",meshCollection,options["rotate90"],options["mergeArmature"])
	#Create dictionary of material names mapping to material data to avoid assigning the wrong material in case of name duplication
	materialDict = createMaterialDict(parsedMesh.materialNameList)
	meshOffsetDict = dict()

	newObjList = importLODGroup(parsedMesh,"Main Mesh",meshCollection,materialDict,armatureObj,hiddenCollectionSet,meshOffsetDict,False,False,False,options["rotate90"],options["mergeGroups"])
	"""
	if options["importShadowMeshes"] and parsedMesh.shadowMeshLODList != []:
		importLODGroup(parsedMesh,"Shadow Mesh",meshCollection,materialDict,armatureObj,hiddenCollectionSet,meshOffsetDict)
	"""
	
	
	
	meshOffsetDict.clear()
	if options["loadMaterials"] and not options["importArmatureOnly"]:
		#print(filePath.split(".mesh")[1])
		if options["mdfPath"] != "":
			mdfPath = options["mdfPath"]
		else:
			mdfPath = findMDFPathFromMeshPath(filePath)
			#print(mdfPath)
		try:
			if mdfPath != None:
				split = splitNativesPath(mdfPath)
				if split != None:
					chunkPath = split[0]
				else:
					chunkPath = ""
				mdfImportStartTime = time.time()
				mdfFile = readMDF(mdfPath)
				importMDF(mdfFile,materialDict,options["loadUnusedTextures"],options["loadUnusedProps"],options["useBackfaceCulling"],options["reloadCachedTextures"],chunkPath = chunkPath,gameName = gameName)
				
				mdfImportEndTime = time.time()
				mdfImportTime =  mdfImportEndTime - mdfImportStartTime
				print(f"Material importing took {timeFormat%(mdfImportTime * 1000)} ms.")
			else:
				warningList.append("MDF file not found.")
		except Exception as err:
			print(str(err))
			warningList.append("Could not import " + mdfPath +":" + str(err))
	
	meshImportEndTime = time.time()
	meshImportTime =  meshImportEndTime - meshImportStartTime
	print(f"Mesh imported in {timeFormat%(meshImportTime * 1000)} ms.")
	return (armatureObj,newObjList)

	