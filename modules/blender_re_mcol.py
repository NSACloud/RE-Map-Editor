import os
import bpy

import numpy as np

from .blender_utils import showMessageBox
from .gen_functions import textColors,raiseWarning
from .file_re_mcol import readMCOL,writeMCOL,MCOLFile,Vertex,Face,BoundingBox
from math import radians
def findHeaderObj():
	if bpy.data.collections.get("MCOLData",None) != None:
		objList = bpy.data.collections["MCOLData"].all_objects
		headerList = [obj for obj in objList if obj.get("~TYPE",None) == "RE_MCOL_ROOT"]
		if len(headerList) >= 1:
			return headerList[0]
		else:
			return None

def calcBoundingBox(vertexList):
    x,y,z = zip(*vertexList)
    return (min(x),min(y),min(z),max(x),max(y),max(z))

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

def setMCOLMaterialColor(materialType,material):
	matColorDict = {
		"mBacteria":([0.416273832321167, 0.7544741630554199, 0.8000000715255737, 1.0],0.4838709831237793,0.032258063554763794,0.44301074743270874,"OPAQUE"),
		"mBone":([0.8000000715255737, 0.7151283621788025, 0.7238350510597229, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mBranch":([0.21651943027973175, 0.11146067827939987, 0.023909471929073334, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mCarcass":([0.4411577880382538, 0.03557462990283966, 0.04162605106830597, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mCarpet":([1.0, 0.0, 0.0, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mCloth":([1.0, 0.8415196537971497, 0.5463077425956726, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mDeadLeaf":([0.09457795321941376, 0.2215341329574585, 0.006330573000013828, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mDesert":([1.0, 0.8781372308731079, 0.47666579484939575, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mGrassIvy":([0.0, 0.5287831425666809, 0.1134696677327156, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mGrassLong":([0.0, 0.22661957144737244, 0.05191297084093094, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mGrassShort":([0.0, 1.0, 0.2066877782344818, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mGravel":([0.5479327440261841, 0.5717013478279114, 0.5373721122741699, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mIceThin":([0.5196467638015747, 1.0, 0.9654799699783325, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mIceWall":([0.5196467638015747, 1.0, 0.9654799699783325, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mIronGrille":([0.9778991937637329, 0.8884511590003967, 1.0, 1.0],0.5,1.0,0.5,"OPAQUE"),
		"mIvy":([0.0, 0.5287831425666809, 0.1134696677327156, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mLava":([1.0, 0.5225215554237366, 0.0, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mMagma":([0.02771833725273609, 0.016613703221082687, 0.0, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mMarbleRich":([1.0, 1.0, 1.0, 1.0],0.5,0.0,0.02631578966975212,"OPAQUE"),
		"mMetal":([0.9778991937637329, 0.8884511590003967, 1.0, 1.0],0.5,1.0,0.5,"OPAQUE"),
		"mMud":([0.19243527948856354, 0.08655200153589249, 0.02742246352136135, 1.0],0.5,0.0,0.25,"OPAQUE"),
		"mMushroom":([1.0, 0.9167267680168152, 0.7460368871688843, 1.0],0.5,0.0,0.25,"OPAQUE"),
		"mNest":([1.0, 0.9167267680168152, 0.7460368871688843, 1.0],0.5,0.0,0.25,"OPAQUE"),
		"mNone":([1.0, 0.0, 0.0, 0.5],0.5,0.0,0.5,"BLEND"),
		"mNormalIce":([0.5196467638015747, 1.0, 0.9654799699783325, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mNormalMarble":([1.0, 1.0, 1.0, 1.0],0.5,0.0,0.02631578966975212,"OPAQUE"),
		"mNormalRock":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mNormalSnow":([1.0, 1.0, 1.0, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mNormalWater":([0.12663723528385162, 0.5982999205589294, 1.0, 0.7758619785308838],0.5,0.0,1.0,"BLEND"),
		"mNormalWood":([1.0, 0.673946738243103, 0.3818436563014984, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mRockWall":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mRope":([1.0, 0.673946738243103, 0.3818436563014984, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mSand":([1.0, 0.8781372308731079, 0.47666579484939575, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mSap":([0.0, 0.5287831425666809, 0.1134696677327156, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mSlopeNormalWater":([0.12663723528385162, 0.5982999205589294, 1.0, 0.7758619785308838],0.5,0.0,1.0,"BLEND"),
		"mSlopeSap":([0.0, 0.5287831425666809, 0.1134696677327156, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"mSlopeWaterShallow":([0.13534127175807953, 0.876750648021698, 1.0, 0.3850572407245636],0.5,0.0,1.0,"BLEND"),
		"mSnowRock":([0.3657931685447693, 0.5625621676445007, 0.6258003115653992, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mSoil":([0.45640337467193604, 0.2813066840171814, 0.10336671769618988, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mStone":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mStraw":([1.0, 0.9374356865882874, 0.0, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mWaterDeep":([0.13534127175807953, 0.876750648021698, 1.0, 0.550572407245636],0.5,0.0,1.0,"BLEND"),
		"mWaterShallow":([0.13534127175807953, 0.876750648021698, 1.0, 0.3850572407245636],0.5,0.0,1.0,"BLEND"),
		"mWetGrass":([0.0, 0.22661957144737244, 0.05191297084093094, 1.0],0.5,0.0,0.0,"OPAQUE"),
		"mWetGravel":([0.5479327440261841, 0.5717013478279114, 0.5373721122741699, 1.0],0.5,0.0,0.0,"OPAQUE"),
		"mWetRock":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,0.0,"OPAQUE"),
		"mWetSand":([1.0, 0.8781372308731079, 0.47666579484939575, 1.0],0.5,0.0,0.0,"OPAQUE"),
		"mWood":([1.0, 0.4829767644405365, 0.1718321591615677, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mWoodCreak":([0.4641399383544922, 0.22813959419727325, 0.0841190442442894, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"mWoodWater":([0.4641399383544922, 0.3392921984195709, 0.28379711508750916, 1.0],0.5,0.0,1.0,"OPAQUE"),
		
		#RE4
		"Ceramic":([1.0, 1.0, 1.0, 1.0],0.5,0.0,0.02631578966975212,"OPAQUE"),
		"Cloth_OnStone":([0.5196467638015747, 1.0, 0.9654799699783325, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Cloth_OnWood":([1.0, 0.8415196537971497, 0.5463077425956726, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Cloth_Padding":([1.0, 0.8415196537971497, 0.5463077425956726, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Concrete_Smooth":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Glass":([1.0, 1.0, 1.0, 0.3],0.5,0.0,0.5,"BLEND"),
		"Gravel":([0.5479327440261841, 0.5717013478279114, 0.5373721122741699, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Meat":([0.4411577880382538, 0.03557462990283966, 0.04162605106830597, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Metal_Thick":([0.9778991937637329, 0.8884511590003967, 1.0, 1.0],0.5,1.0,0.5,"OPAQUE"),
		"Metal_Thin":([0.9778991937637329, 0.8884511590003967, 1.0, 1.0],0.5,1.0,0.5,"OPAQUE"),
		"Muddy":([0.19243527948856354, 0.08655200153589249, 0.02742246352136135, 1.0],0.5,0.0,0.25,"OPAQUE"),
		"Paper_OnStone":([1.0, 0.9374356865882874, 0.0, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Plants":([0.0, 0.5287831425666809, 0.1134696677327156, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Plants_Dead":([0.09457795321941376, 0.2215341329574585, 0.006330573000013828, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Plastic_Container":([1.0, 1.0, 1.0, 1.0],0.5,0.0,0.02631578966975212,"OPAQUE"),
		"Plastic_OnWood":([1.0, 0.673946738243103, 0.3818436563014984, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Puddle_SoftSurface":([1.0, 0.673946738243103, 0.3818436563014984, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Rubber":([0.09457795321941376, 0.2215341329574585, 0.006330573000013828, 1.0],0.5,0.0,0.5,"OPAQUE"),
		"Soil":([0.45640337467193604, 0.2813066840171814, 0.10336671769618988, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Stone_Rough":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Stone_Rubble":([0.27600690722465515, 0.26472023129463196, 0.2812042534351349, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Stone_Tile":([1.0, 1.0, 1.0, 1.0],0.5,0.0,0.02631578966975212,"OPAQUE"),
		"Swampy":([0.5479327440261841, 0.5717013478279114, 0.5373721122741699, 1.0],0.5,0.0,0.0,"OPAQUE"),
		"Wood_Rotten":([0.4641399383544922, 0.22813959419727325, 0.0841190442442894, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Wood_Rotten__BPass":([0.4641399383544922, 0.22813959419727325, 0.0841190442442894, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Wood_Rough":([1.0, 0.673946738243103, 0.3818436563014984, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Wood_Smooth":([1.0, 0.4829767644405365, 0.1718321591615677, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"_VHit":([0.12663723528385162, 0.5982999205589294, 1.0, 0.7758619785308838],0.5,0.0,1.0,"BLEND"),
		#CPT
		"Default":([0.220258, 0.220258, 0.220258, 1.0],0.5,0.0,1.0,"OPAQUE"),
		"Ascend":([0.12663723528385162, 0.5982999205589294, 1.0, 0.7758619785308838],0.5,0.0,1.0,"BLEND"),
	}
	matColor = matColorDict.get(materialType,([1.0, 0.0, 0.0, 0.20000000298023224],0.5,0.0,0.5,"BLEND"))
	material.diffuse_color = matColor[0]
	material.specular_intensity = matColor[1]
	material.metallic = matColor[2]
	material.roughness = matColor[3]
	material.blend_method = matColor[4]
#MCOL IMPORT

def importMCOLFile(filePath,importOptions = {"clearScene":False,"loadBoundingBoxes":False,"loadBoundingBoxTree":False,"mergeDuplicateMaterials":False}):
	mcolFile = readMCOL(filePath)
	if importOptions["clearScene"]:
		for collection in bpy.data.collections:
			for obj in collection.objects:
				collection.objects.unlink(obj)
			bpy.data.collections.remove(collection)
		for bpy_data_iter in (bpy.data.objects,bpy.data.meshes,bpy.data.lights,bpy.data.cameras):
			for id_data in bpy_data_iter:
				bpy_data_iter.remove(id_data)
		for material in bpy.data.materials:
			bpy.data.materials.remove(material)
		for amt in bpy.data.armatures:
			bpy.data.armatures.remove(amt)
		for obj in bpy.data.objects:
			bpy.data.objects.remove(obj)
			obj.user_clear()
	#mcolRoot = createEmpty("RE_MCOL_ROOT ("+os.path.split(filePath)[1]+")",[("~TYPE","RE_MCOL_ROOT"),("MCOLVersion",os.path.splitext(filePath)[1].split(".")[1])],None,"MCOLData")
	#mcolRoot.rotation_euler = (radians(90.0),0.0,0.0)
	meshVertexList = []
	meshFaceList = []
	materialDict = {}
	for vertex in mcolFile.vertexList:
		meshVertexList.append(vertex.pos)
	
	for faceIndex, face in enumerate(mcolFile.faceList):
		#print(str((face.vertIndex0,face.vertIndex1,face.vertIndex2)))
		meshFaceList.append((face.vertIndex0,face.vertIndex1,face.vertIndex2))
		if materialDict.get(face.stringIndex,None) == None:
			#Build dict of used string indices to be used to make materials
			materialDict[face.stringIndex] = {"faceList":set([faceIndex]),"matName":mcolFile.stringTable1.stringList1[face.stringIndex*2]}
		else:
			materialDict[face.stringIndex]["faceList"].add(faceIndex)
	meshName = "MCOL_Mesh "  + os.path.splitext(os.path.split(filePath)[1])[0]
	
	meshData = bpy.data.meshes.new(meshName)
	meshData.from_pydata(meshVertexList, [], meshFaceList)
	meshData.update()	
	meshObj = bpy.data.objects.new(meshName, meshData)
	for matIndex, materialEntry in enumerate(materialDict.values()):
		name = "MCOL_MAT_"+str(matIndex).zfill(3)+ " (" + materialEntry["matName"]+")"
		if len(name) > 63:#Max blender name size
			name = "MCOL_MAT_"+str(matIndex).zfill(3)+ " (" + materialEntry["matName"][0:45]+"...)"
		newMat = bpy.data.materials.new(name)
		newMat["materialString"] = materialEntry["matName"]
		if "cpe_" in materialEntry["matName"]:
			setMCOLMaterialColor(newMat["materialString"].split("cpe_")[1], newMat)
		elif "CPT_" in materialEntry["matName"]:
			setMCOLMaterialColor(newMat["materialString"].split("CPT_")[1], newMat)
		else:
			setMCOLMaterialColor(newMat["materialString"].split("__")[0], newMat)
		meshObj.data.materials.append(newMat)
		for faceIndex in materialEntry["faceList"]:
			meshObj.data.polygons[faceIndex].material_index = matIndex
	
	
	if bpy.data.collections.get("MCOLData",None) == None:#Create collection if the name given doesn't exist
		newCollection = bpy.data.collections.new("MCOLData")
		bpy.context.scene.collection.children.link(newCollection)
	
	layer_collection = bpy.data.collections["MCOLData"]
	layer_collection.objects.link(meshObj) #link it with collection
	meshObj["~TYPE"] = "MCOL_MESH"
	#meshObj.parent = mcolRoot
	meshObj.rotation_euler = (radians(90.0),0.0,0.0)	
	
	if importOptions["loadBoundingBoxes"]:
		bboxVertList = []
		bboxEdgeList = []
		for index,boundingBox in enumerate(mcolFile.boundingBoxList):
			currentStartIndex = index*8
			bboxVertList.extend([
			(boundingBox.x1,boundingBox.y1,boundingBox.z1),
			(boundingBox.x2,boundingBox.y1,boundingBox.z1),
			(boundingBox.x1,boundingBox.y2,boundingBox.z1),
			(boundingBox.x1,boundingBox.y1,boundingBox.z2),
			(boundingBox.x2,boundingBox.y2,boundingBox.z2),
			(boundingBox.x1,boundingBox.y2,boundingBox.z2),
			(boundingBox.x2,boundingBox.y1,boundingBox.z2),
			(boundingBox.x2,boundingBox.y2,boundingBox.z1),
			
			])
			bboxEdgeList.extend([
			(currentStartIndex+0,currentStartIndex+1),
			(currentStartIndex+0,currentStartIndex+2),
			(currentStartIndex+0,currentStartIndex+3),
			(currentStartIndex+1,currentStartIndex+7),
			(currentStartIndex+1,currentStartIndex+6),
			(currentStartIndex+6,currentStartIndex+4),
			(currentStartIndex+6,currentStartIndex+3),
			(currentStartIndex+3,currentStartIndex+5),
			(currentStartIndex+5,currentStartIndex+2),
			(currentStartIndex+5,currentStartIndex+4),
			(currentStartIndex+7,currentStartIndex+4),
			(currentStartIndex+7,currentStartIndex+2),
			])
		bboxName = "MCOL_BBoxes"
		
		bboxData = bpy.data.meshes.new(bboxName)
		bboxData.from_pydata(bboxVertList, bboxEdgeList, [])
		bboxData.update()
		
		bboxObj = bpy.data.objects.new(bboxName, bboxData)
		layer_collection.objects.link(bboxObj)
		#bboxObj.parent = mcolRoot
		bboxObj.show_bounds = True
		
	if importOptions["loadBoundingBoxTree"]:
		bboxVertList = []
		bboxEdgeList = []
		bboxObjList = []
		parentDict = {}
		prevBox = None
		lastIndex = len(mcolFile.boundingBoxList)+1
		for index,boundingBox in enumerate(mcolFile.boundingBoxList):
			currentStartIndex = index*8
			bboxVertList = [
			(boundingBox.x1,boundingBox.y1,boundingBox.z1),
			(boundingBox.x2,boundingBox.y2,boundingBox.z2),
			
			]
			bboxName = "BBOX_" + str(index).zfill(4)
			if boundingBox.flag != 0: bboxName += "_FACE"
			bboxData = bpy.data.meshes.new(bboxName)
			bboxData.from_pydata(bboxVertList, [], [])
			bboxData.update()
			
			bboxObj = bpy.data.objects.new(bboxName, bboxData)
			bpy.data.collections["MCOLData"].objects.link(bboxObj)
			#bboxObj.parent = mcolRoot
			bboxObj.show_bounds = True
			bboxObjList.append(bboxObj)
			
			if boundingBox.flag == 0:
				parentDict[boundingBox.index] = prevBox
			if parentDict.get(index,None) != lastIndex and parentDict.get(index,None) != None:
				bboxObj.parent = parentDict[index]
			prevBox = bboxObj
	return meshObj


#MCOL EXPORT

def MCOLErrorCheck():
	print("\nChecking for problems with MDF structure...")
	
	#Check that there is mdf data collection
	#Check that there is only one header
	#Check that all materials have only one flag, property list and texture binding objects
	#Check that all materials are parented to the header
	#Check that parenting structure is valid
	#Check for duplicate material names
	errorList = []
	warningList = []
	materialNameSet = set()
	noesisMeshMaterialSet = set()
	if bpy.data.collections.get("MCOLData",None) != None:
		objList = bpy.data.collections["MCOLData"].all_objects
	else:
		errorList.append("MCOL objects must be in a collection named \"MCOLData\".")
		objList = []
	headerCount = 0
	meshCount = 0
	for obj in objList:
		
		if obj.get("~TYPE",None) == "RE_MCOL_ROOT":
			headerCount += 1
			if obj.parent != None:
				errorList.append("MCOL root cannot be a child of another object.")
			for child in obj.children:
				if child.type == "MESH":
					meshCount+=1
				
	if headerCount == 0:
		errorList.append("No MCOL root object in scene.")
		
	elif headerCount > 1:
		errorList.append("Cannot export with more than one MDF header in a scene.")
	
	if meshCount == 0:
		errorList.append("No mesh is parented to the MCOL root.")
		
	elif meshCount > 1:
		errorList.append("There can only be one mesh parented to an MCOL root, join all meshes.")
		
		for warning in warningList:
			raiseWarning(warning)
			
	if errorList == []:
		print("No errors found.")
		#print(noesisMeshMaterialSet)
		if warningList != []:
			showMessageBox("Warnings occured during export. Check Window > Toggle System Console for details.",title = "Export Warning", icon = "ERROR")
		return True
	else:
		errorString = ""
		for error in errorList:
			errorString += textColors.FAIL +"ERROR: " + error + textColors.ENDC +"\n"
		showMessageBox("MCOL structure contains errors and cannot export. Check Window > Toggle System Console for details.",title = "Export Error", icon = "ERROR")
		print(errorString)
		print(textColors.FAIL + "__________________________________\nMCOL export failed."+textColors.ENDC)
		return False
def exportMCOLFile(filepath):
	valid = MCOLErrorCheck()
	if valid:
		print(textColors.OKCYAN + "__________________________________\nMCOL export started."+textColors.ENDC)
		newMCOLFile = MCOLFile()
		mcolRoot = findHeaderObj()
		vertexCount = 0
		faceCount = 0
		for mesh in mcolRoot.children:
			if mesh.type == "MESH":
				edgeDict = {}
				for material in mesh.data.materials:
					newMCOLFile.stringTable1.stringList1.append(material["materialString"])
				newMCOLFile.stringTable1.stringList2 = newMCOLFile.stringTable1.stringList1
				newMCOLFile.stringTable2.stringList1 = newMCOLFile.stringTable1.stringList1
				newMCOLFile.stringTable2.stringList2 = newMCOLFile.stringTable1.stringList1
				for vertex in mesh.data.vertices:
					newVertex = Vertex()
					newVertex.pos = vertex.co
					newMCOLFile.vertexList.append(newVertex)
				for faceIndex,face in enumerate(mesh.data.polygons):
					#Gather all edges of faces
					for edge_key in face.edge_keys:
						if str(edge_key) not in edgeDict:
							edgeDict[str(edge_key)]=[faceIndex]
						else:
							edgeDict[str(edge_key)].append(faceIndex)
				for faceIndex,face in enumerate(mesh.data.polygons):
					newFace = Face()
					newFace.stringIndex = face.material_index
					newFace.vertIndex0 = face.vertices[0]
					newFace.vertIndex1 = face.vertices[1]
					newFace.vertIndex2 = face.vertices[2]
					adjFaceList  = [-1,-1,-1]
					currentAdjFaceIndex = 0
					for edge_key in face.edge_keys:
						print(edgeDict[str(edge_key)])
						for face in edgeDict[str(edge_key)]:
							if face != faceIndex:
								adjFaceList[currentAdjFaceIndex] = face
								currentAdjFaceIndex += 1
								break
					newFace.adjFaceIndex0 = adjFaceList[0]
					newFace.adjFaceIndex1 = adjFaceList[1]
					newFace.adjFaceIndex2 = adjFaceList[2]
					newMCOLFile.faceList.append(newFace)
			vertexCount += len(mesh.data.vertices)
			faceCount += len(mesh.data.polygons)
		
		keyBoundingBox = calcBoundingBox((v.pos for v in newMCOLFile.vertexList))
		newMCOLFile.bvhmHeader.boxMinX = keyBoundingBox[0]
		newMCOLFile.bvhmHeader.boxMinY = keyBoundingBox[1]
		newMCOLFile.bvhmHeader.boxMinZ = keyBoundingBox[2]
		newMCOLFile.bvhmHeader.boxMaxX = keyBoundingBox[3]
		newMCOLFile.bvhmHeader.boxMaxY = keyBoundingBox[4]
		newMCOLFile.bvhmHeader.boxMaxZ = keyBoundingBox[5]
		
		currentBBoxIndex = 1
		for faceIndex,face in enumerate(newMCOLFile.faceList):
			adjFaceBBox0Entry = None
			adjFaceBBox1Entry = None
			adjFaceBBox2Entry = None
			newBBoxList = []
			if face.adjFaceIndex0 != -1:
				currentBBoxIndex +=1
				adjFaceBBox0Entry = BoundingBox()
				adjFace0BBox = calcBoundingBox(
					[newMCOLFile.vertexList[face.vertIndex0].pos,
					newMCOLFile.vertexList[face.vertIndex1].pos,
					newMCOLFile.vertexList[face.vertIndex2].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex0].vertIndex0].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex0].vertIndex1].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex0].vertIndex2].pos])
				adjFaceBBox0Entry.x1 = adjFace0BBox[0]
				adjFaceBBox0Entry.y1 = adjFace0BBox[1]
				adjFaceBBox0Entry.z1 = adjFace0BBox[2]
				adjFaceBBox0Entry.x2 = adjFace0BBox[3]
				adjFaceBBox0Entry.y2 = adjFace0BBox[4]
				adjFaceBBox0Entry.z2 = adjFace0BBox[5]
				
			
			if face.adjFaceIndex1 != -1:
				currentBBoxIndex +=1
				adjFaceBBox1Entry = BoundingBox()
				adjFace1BBox = calcBoundingBox(
					[newMCOLFile.vertexList[face.vertIndex0].pos,
					newMCOLFile.vertexList[face.vertIndex1].pos,
					newMCOLFile.vertexList[face.vertIndex2].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex1].vertIndex0].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex1].vertIndex1].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex1].vertIndex2].pos])
				adjFaceBBox1Entry.x1 = adjFace1BBox[0]
				adjFaceBBox1Entry.y1 = adjFace1BBox[1]
				adjFaceBBox1Entry.z1 = adjFace1BBox[2]
				adjFaceBBox1Entry.x2 = adjFace1BBox[3]
				adjFaceBBox1Entry.y2 = adjFace1BBox[4]
				adjFaceBBox1Entry.z2 = adjFace1BBox[5]
			if face.adjFaceIndex2 != -1:
				currentBBoxIndex +=1
				adjFaceBBox2Entry = BoundingBox()
				adjFace2BBox = calcBoundingBox(
					[newMCOLFile.vertexList[face.vertIndex0].pos,
					newMCOLFile.vertexList[face.vertIndex1].pos,
					newMCOLFile.vertexList[face.vertIndex2].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex2].vertIndex0].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex2].vertIndex1].pos,
					newMCOLFile.vertexList[newMCOLFile.faceList[face.adjFaceIndex2].vertIndex2].pos])
				adjFaceBBox2Entry.x1 = adjFace2BBox[0]
				adjFaceBBox2Entry.y1 = adjFace2BBox[1]
				adjFaceBBox2Entry.z1 = adjFace2BBox[2]
				adjFaceBBox2Entry.x2 = adjFace2BBox[3]
				adjFaceBBox2Entry.y2 = adjFace2BBox[4]
				adjFaceBBox2Entry.z2 = adjFace2BBox[5]
			currentBBoxIndex += 1
			faceBBoxEntry = BoundingBox()
			faceBBoxEntry.flag = 128
			faceBBoxEntry.index = faceIndex
			faceBBox = calcBoundingBox(
				[newMCOLFile.vertexList[face.vertIndex0].pos,
				newMCOLFile.vertexList[face.vertIndex1].pos,
				newMCOLFile.vertexList[face.vertIndex2].pos])
			faceBBoxEntry.x1 = faceBBox[0]
			faceBBoxEntry.y1 = faceBBox[1]
			faceBBoxEntry.z1 = faceBBox[2]
			faceBBoxEntry.x2 = faceBBox[3]
			faceBBoxEntry.y2 = faceBBox[4]
			faceBBoxEntry.z2 = faceBBox[5]
			
			if adjFaceBBox0Entry != None:
				adjFaceBBox0Entry.index = currentBBoxIndex
				newMCOLFile.boundingBoxList.append(adjFaceBBox0Entry)
			
			if adjFaceBBox1Entry != None:
				adjFaceBBox1Entry.index = currentBBoxIndex
				newMCOLFile.boundingBoxList.append(adjFaceBBox1Entry)
			if adjFaceBBox2Entry != None:
				adjFaceBBox2Entry.index = currentBBoxIndex
				newMCOLFile.boundingBoxList.append(adjFaceBBox2Entry)
			newMCOLFile.boundingBoxList.append(faceBBoxEntry)
			
			
		#DEBUG
		bboxVertList = []
		bboxEdgeList = []
		parentDict = {}
		for index,boundingBox in enumerate(newMCOLFile.boundingBoxList):
			currentStartIndex = index*8
			bboxVertList.extend([
			(boundingBox.x1,boundingBox.y1,boundingBox.z1),
			(boundingBox.x2,boundingBox.y1,boundingBox.z1),
			(boundingBox.x1,boundingBox.y2,boundingBox.z1),
			(boundingBox.x1,boundingBox.y1,boundingBox.z2),
			(boundingBox.x2,boundingBox.y2,boundingBox.z2),
			(boundingBox.x1,boundingBox.y2,boundingBox.z2),
			(boundingBox.x2,boundingBox.y1,boundingBox.z2),
			(boundingBox.x2,boundingBox.y2,boundingBox.z1),
			
			])
			bboxEdgeList.extend([
			(currentStartIndex+0,currentStartIndex+1),
			(currentStartIndex+0,currentStartIndex+2),
			(currentStartIndex+0,currentStartIndex+3),
			(currentStartIndex+1,currentStartIndex+7),
			(currentStartIndex+1,currentStartIndex+6),
			(currentStartIndex+6,currentStartIndex+4),
			(currentStartIndex+6,currentStartIndex+3),
			(currentStartIndex+3,currentStartIndex+5),
			(currentStartIndex+5,currentStartIndex+2),
			(currentStartIndex+5,currentStartIndex+4),
			(currentStartIndex+7,currentStartIndex+4),
			(currentStartIndex+7,currentStartIndex+2),
			])
		bboxName = "TEST_EXPORT_MCOL_BBoxes"
		
		bboxData = bpy.data.meshes.new(bboxName)
		bboxData.from_pydata(bboxVertList, bboxEdgeList, [])
		bboxData.update()
		
		bboxObj = bpy.data.objects.new(bboxName, bboxData)
		bpy.data.collections["MCOLData"].objects.link(bboxObj)
		bboxObj.parent = mcolRoot
		bboxObj.show_bounds = True
		
		
		#END DEBUG
		writeMCOL(newMCOLFile,filepath)
		return True