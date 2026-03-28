#Author: NSA Cloud
import json
import os
import re
import bpy
import uuid
from datetime import datetime

from .gen_functions import textColors,raiseWarning
from .blender_utils import showErrorMessageBox

from .blender_re_scn import getRSZTreeRecursive,createEmpty,applyInstanceFields,getNewUUID,addRSZPointer
from .re_rsz_lookup_main import stringToHash,getRSZInstance


def getNewUUID():
	return str(uuid.uuid4().int)

def findHeaderObj():
	if bpy.data.collections.get("chainData",None) != None:
		objList = bpy.data.collections["chainData"].all_objects
		headerList = [obj for obj in objList if obj.get("TYPE",None) == "RE_CHAIN_HEADER"]
		if len(headerList) >= 1:
			return headerList[0]
		else:
			return None
PRESET_VERSION = 1#To be changed when there are changes to rsz preset parsing
RSZ_ROOTS = set(["RSZ_SCN_ROOT","RSZ_USR_ROOT","RSZ_PFB_ROOT"])
#Special keys that have different behaviors depending on which one it is
reservedKeys = set(["!ParentObj!","!Collection!","!RSZIndex!"])


def saveAsPreset(activeObj,presetName,game):
	instanceCache = {}
	#TODO
	#
	if activeObj != None:
		jsonDict = {"Info":{},"Objects":{},"RSZPointers":[],"gameObjectReferences":{}}
		startingRSZIndex = 9000
		chainObjType = activeObj.get("TYPE",None)
		if not re.search(r'^[\w,\s-]+\.[A-Za-z]{3}$',presetName) and not ".." in presetName:#Check that the preset name contains no invalid characters for a file name
			currentObj = activeObj
			while currentObj.parent != None and currentObj.parent.get("~TYPE") not in RSZ_ROOTS:
				currentObj = currentObj.parent
		
			if currentObj.parent.get("~TYPE") in RSZ_ROOTS:
				jsonDict["Info"]["Source RSZ"] = os.path.split(currentObj.parent["Export Path"])[1]
			jsonDict["Info"]["Source Object"] = activeObj.name
			jsonDict["Info"]["Timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")#Used to judge if a preset is out of date
			jsonDict["Info"]["Preset Version"] = PRESET_VERSION
			jsonDict["Info"]["Tags"] = set()
			hierarchyList = sorted(getRSZTreeRecursive(activeObj),key=lambda k: k.name)
		
			#file.write(hierarchyList)
		
			nameSet = set()
			objNameDict = {}
			isRoot = True
			
			for obj in hierarchyList:
				if obj.get("~TYPE",None) == "RSZ_INSTANCE" or obj.get("~TYPE",None) == "RSZ_EXTERNAL_USERDATA":
					
					currentNameIndex = 0
					newStructName = obj["~instanceType"]
					newStructName = newStructName.replace(".","_")
					newStructName = newStructName.replace("`","")
					newStructName = newStructName.replace("<","")
					newStructName = newStructName.replace(">","")
					newStructName = newStructName.replace(",","")
					newStructName = newStructName.replace("[","")
					newStructName = newStructName.replace("]","")
					newStructName = newStructName.replace("!","")
					newStructName = newStructName.replace(",","")
					newStructName = newStructName.replace(",","")
					newStructName = newStructName.replace("|","")
					newStructName = newStructName.replace(" ","_")
					newStructName = newStructName.replace("=","")
					newStructName = re.sub('@"[^\w\.@-]<>`"',"", newStructName)
					
					name = newStructName + str(currentNameIndex)
					while name in nameSet:
						name = newStructName + str(currentNameIndex)
						currentNameIndex += 1
					nameSet.add(name)
					objNameDict[obj] = name
			objCount = len(hierarchyList)
			for index,obj in enumerate(reversed(hierarchyList)):
				jsonDict["Objects"][objNameDict[obj]]={}
				if obj["~TYPE"] == "RSZ_EXTERNAL_USERDATA":
					jsonDict["Objects"][objNameDict[obj]]["UserData Path"] = obj["UserData Path"]
				else:
					if instanceCache.get(obj["~instanceType"],None) == None:
						instanceHash = stringToHash(obj["~instanceType"],game)
						instance = getRSZInstance(instanceHash,game)()
					else:
						instance = instanceCache[obj["~instanceType"]]
					
					instance.setFields(obj)
					#print(instance.getFields())
					#jsonDict["Objects"][objNameDict[obj]] = instance.getFields()
					if obj["~instanceType"] == "via.GameObject":
						jsonDict["Objects"][objNameDict[obj]]["GUID"] = obj["GUID"]
						jsonDict["Objects"][objNameDict[obj]]["~virtualPrefabPath"] = obj["~virtualPrefabPath"]
						jsonDict["gameObjectReferences"][obj["GUID"]]=objNameDict[obj]
					elif obj["~instanceType"] == "chainsaw.GimmickCore":
						jsonDict["Info"]["Tags"].add("PRESET_GIMMICK")
					elif obj["~instanceType"] == "chainsaw.DropItem":
						jsonDict["Info"]["Tags"].add("PRESET_DROPITEM")
					for field in instance.fields.values():
						jsonDict["Objects"][objNameDict[obj]][field.name]=field.value
						#print(type(field.value))
					
					
				"""
				
				for key,value in obj.items():
					if key !="re_rsz_object":
						if key == "GUID":
							jsonDict["Objects"][objNameDict[obj]][key]=value
							jsonDict["gameObjectReferences"][value]=objNameDict[obj]
						else:
							if isinstance(value,str):
								jsonDict["Objects"][objNameDict[obj]][str(key)]=str(value)
								
							elif value.__class__.__name__ == "IDPropertyArray":
								if value.to_list() != []:
									if value[0].__class__.__name__ == "IDPropertyArray":
										print("found")
									newList = []
									for subvalue in value.to_list():
										newList.append(subvalue)
									
									print(newList)
									jsonDict["Objects"][objNameDict[obj]][str(key)]=newList
								else:
									jsonDict["Objects"][objNameDict[obj]][str(key)]=value.to_list()
							else:
								jsonDict["Objects"][objNameDict[obj]][str(key)]=value
				"""
				jsonDict["Objects"][objNameDict[obj]]["~instanceType"]=obj["~instanceType"]
				if obj.get("~isObject",None) != None:
					jsonDict["Objects"][objNameDict[obj]]["~isObject"]=obj["~isObject"]
				
				if obj.get("~TYPE",None) != None:
					jsonDict["Objects"][objNameDict[obj]]["~TYPE"]=obj["~TYPE"]
				
				if obj == activeObj:
					jsonDict["Objects"][objNameDict[obj]]["!ParentObj!"]="!ROOT_OBJECT!"
				else:
					jsonDict["Objects"][objNameDict[obj]]["!ParentObj!"]=objNameDict[obj.parent]
				jsonDict["Objects"][objNameDict[obj]]["!Collection!"]="RSZData"
				jsonDict["Objects"][objNameDict[obj]]["!RSZIndex!"]=startingRSZIndex + objCount-1-index
				for item in obj.re_rsz_object.rszObjectPointers:
						if item.targetObject != None:
							jsonDict["RSZPointers"].append({"sourceObject":objNameDict[obj],"fieldName":item.fieldName,"targetObject":objNameDict[item.targetObject]})
			
			jsonDict["Info"]["Tags"] = list(jsonDict["Info"]["Tags"])#Convert set to list so it can be converted to json
			jsonPath = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),"Presets",game,presetName+".json")
			#print(jsonDict)#debug
			try:
				os.makedirs(os.path.split(jsonPath)[0])
			except:
				pass
			with open(jsonPath, 'w', encoding='utf-8') as f:
				json.dump(jsonDict, f, ensure_ascii=False, indent=4)
				print(textColors.OKGREEN+"Saved preset to " + str(jsonPath) + textColors.ENDC)
				return True
		else:
			showErrorMessageBox("Invalid preset file name. ")
	else:
		showErrorMessageBox("A chain object must be selected when saving a preset.")
		

def readPresetJSON(filepath,activeObj,game):
		try:
			with open(filepath) as jsonFile:
				jsonDict = json.load(jsonFile)
				if jsonDict["Info"]["Preset Version"] > PRESET_VERSION:
					showErrorMessageBox("Preset was created in a newer version and cannot be used. Update to the latest version of the map editor.")
					return False
				
		except Exception as err:
			showErrorMessageBox("Failed to read json file. \n" + str(err))
			return False
		oldGameObjectReferences = {}
		objDict = {}#Store all newly created objects by their names set in the json
		instanceCache = {}#For looking up if any fields have specific tags
		guidRemapDict = {}
		print("Adding preset " + os.path.split(filepath)[1] )
		for objName, objFields in jsonDict["Objects"].items():
			if instanceCache.get(objFields["~instanceType"],None) == None:
				if objFields["~TYPE"] == "RSZ_EXTERNAL_USERDATA":
					#TODO check if userdata is already in scene and redirect all references to that
					#if not checkUserDataUsage(objFields["UserData Path"]):
					currentObj = createEmpty(objName,[("~TYPE",objFields["~TYPE"]),("~instanceType",objFields["~instanceType"]),("UserData Path",objFields["UserData Path"])],parent=None,collectionName=objFields["!Collection!"])
				
				else:
					instanceHash = stringToHash(objFields["~instanceType"],game)
					instance = getRSZInstance(instanceHash,game)()
					
					if objFields.get("~isObject",None) != None:
						instance.isObject = bool(objFields["~isObject"])
					#Apply fields from JSON to instance, this is not done directly to the empty object so that the instance tags can be checked
					#Also makes sure that the way fields are imported stays consistent
					for field in instance.fields.values():
						field.value = objFields[field.name]
						if "REMAP_GameObjectRef" in field.tagSet:#Add game object IDs that need to be fixed later to a list
							if field.isList:
								for index,gameObjectGUID in enumerate(field.value):
									if oldGameObjectReferences.get(gameObjectGUID,None) == None:
										oldGameObjectReferences[gameObjectGUID] = [{"objName":objName,"fieldName":field.name,"index":index}]
									else:
										oldGameObjectReferences[gameObjectGUID].append({"objName":objName,"fieldName":field.name,"index":index})
							else:
								gameObjectGUID = field.value
								if oldGameObjectReferences.get(gameObjectGUID,None) == None:
									oldGameObjectReferences[gameObjectGUID] = [{"objName":objName,"fieldName":field.name,"index":-1}]
								else:
									oldGameObjectReferences[gameObjectGUID].append({"objName":objName,"fieldName":field.name,"index":-1})
				
					currentObj = createEmpty(objName,[("~TYPE",objFields["~TYPE"]),("~instanceType",objFields["~instanceType"])],parent=None,collectionName=objFields["!Collection!"])
					applyInstanceFields(instance, currentObj)
					currentObj.re_rsz_object.rszObjectPointers.clear()#Remove pointers added by apply instance fields, these will be added properly later
				if currentObj["~instanceType"] == "via.GameObject":
					oldGUID = jsonDict["Objects"][objName]["GUID"]
					currentObj["~virtualPrefabPath"] = objFields["~virtualPrefabPath"]
					
					currentObj["GUID"] = getNewUUID()#Remap GUID so that there's no overlap
					guidRemapDict[oldGUID]=currentObj["GUID"]
					
					currentObj.show_name = bpy.context.scene.re_rsz_toolpanel.showGameObjectNames
				else:
					currentObj.empty_display_size = 0
			#Wait until all objects have been created to set their parent objects
			if objFields.get("~isObject",None) != None:
				currentObj["~isObject"] = objFields["~isObject"]
			else:
				if currentObj.get("~isObject",None) != None:
					del currentObj["~isObject"]
			currentObj.re_rsz_object.rszIndex = objFields["!RSZIndex!"]
			objDict[objName] = currentObj
			
		#Set parents
		for objName,obj in objDict.items():
			if jsonDict["Objects"][objName]["!ParentObj!"] != "!ROOT_OBJECT!":
				obj.parent = objDict[jsonDict["Objects"][objName]["!ParentObj!"]]
			else:
				obj.location = bpy.context.scene.cursor.location
				obj.rotation_euler = bpy.context.scene.cursor.rotation_euler
				obj.rotation_mode = "QUATERNION"
				obj.parent = activeObj
				obj.matrix_basis = activeObj.matrix_world.inverted() @ obj.matrix_basis
		#Fix GUID references
		for objRefList in oldGameObjectReferences.values():
			for objRef in objRefList:
				#print(objRef)
				#print(objRef["objName"])
				#print(objDict[objRef["objName"]])
				#print(objDict[objRef["objName"]][objRef["fieldName"]])
				if objRef["index"] == -1:
					#Get game object from old GUID, fix the reference to point to the new GUID
					if objDict[objRef["objName"]][objRef["fieldName"]] != "0":
						objDict[objRef["objName"]][objRef["fieldName"]] = guidRemapDict[objDict[objRef["objName"]][objRef["fieldName"]]]
				else:
					#Same as before but do it for each index of list
					if objDict[objRef["objName"]][objRef["fieldName"]][objRef["index"]] != "0":
						objDict[objRef["objName"]][objRef["fieldName"]][objRef["index"]] = objDict[jsonDict["gameObjectReferences"][objDict[objRef["objName"]][objRef["fieldName"]][objRef["index"]]]]["GUID"]
		#TODO Remap duplicate user data entries
		
		#Set RSZ Pointers
		for ptr in jsonDict["RSZPointers"]:
			addRSZPointer(objDict[ptr["sourceObject"]], ptr["fieldName"], objDict[ptr["targetObject"]])
		
		
		
		return True
def reloadPresets(folderPath):
	presetsPath = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),"Presets")
	presetList = []
	relPathStart = os.path.join(presetsPath,folderPath)
	if os.path.exists(relPathStart):
		for entry in os.scandir(relPathStart):
			if entry.name.endswith(".json") and entry.is_file():
				presetList.append((os.path.relpath(os.path.join(relPathStart,entry),start = presetsPath),os.path.splitext(entry.name)[0],""))
	#print("Loading " + folderPath + " presets...")
	#print("DEBUG:" + str(presetList)+"\n")#debug
	return presetList