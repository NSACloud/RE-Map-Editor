#Author: NSA Cloud
import bpy
import os
import uuid

from bpy.types import Operator
from bpy.types import Mesh
from .blender_utils import showMessageBox
from .re_rsz_propertyGroups import RSZ_PointLightPropertyGroup
from .blender_re_scn import exportRSZFile,reindexTree,addRSZPointer,getNewUUID

from .re_rsz_presets import saveAsPreset,readPresetJSON

from .re4_items import RE4ItemEnumList, getRE4ItemInfo

RSZ_ROOT_SET = set(["RSZ_SCN_ROOT","RSZ_USR_ROOT","RSZ_PFB_ROOT"])

TRUE_STRINGS_SET = set(["t","true","y","yes"])

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

class WM_OT_AddRSZObject(Operator):
	
	bl_label = "Add RSZ Instance"
	bl_idname = "re_rsz.add_object"
	bl_description = "Creates an RSZ Instance"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}
	
class WM_OT_AddMeshObject(Operator):
	
	bl_label = "Add Mesh"
	bl_idname = "re_rsz.add_mesh"
	bl_description = "Creates a new mesh game object"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}
	
class WM_OT_AddPointLightObject(Operator):
	
	bl_label = "Add Point Light"
	bl_idname = "re_rsz.add_point_light"
	bl_description = "Creates a new point light game object"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}
class WM_OT_AddSpotLightObject(Operator):
	
	bl_label = "Add Spot Light"
	bl_idname = "re_rsz.add_spot_light"
	bl_description = "Creates a new spot light game object"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}
class WM_OT_AddDirectionalLightObject(Operator):

	bl_label = "Add Sun Light"
	bl_idname = "re_rsz.add_directional_light"
	bl_description = "Creates a new directional light object"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}

class WM_OT_AddEPVObject(Operator):
	
	bl_label = "Add Stage EPV"
	bl_idname = "re_rsz.add_epv"
	bl_description = "Creates a new epv game object"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}

class WM_OT_ReloadMeshes(Operator):
	
	bl_label = "Reload All Meshes"
	bl_idname = "re_rsz.reload_meshes"
	bl_description = "Reload all display meshes"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}
class WM_OT_ReindexTree(Operator):
	
	bl_label = "Reindex Tree"
	bl_idname = "re_rsz.reindex_tree"
	bl_description = "Makes rsz indices sequential, this is done automatically on export if needed"
	def execute(self, context):
		if bpy.context.active_object != None and bpy.context.active_object.get("~TYPE",None) in RSZ_ROOT_SET:
			reindexTree(bpy.context.active_object)
			self.report({"INFO"},"Reindexed RSZ Tree.")
		else:
			showMessageBox("Must select an RSZ Root object.")
		return {'FINISHED'}

class WM_OT_IncreaseRSZIndex(Operator):
	
	bl_label = "Increment RSZ Index"
	bl_idname = "re_rsz.increment_rsz_index"
	bl_description = "Increases RSZ index of selected objects by amount set in the UI"
	def execute(self, context):
		for obj in bpy.context.selected_objects:
			if obj.get("~TYPE",None)== "RSZ_INSTANCE" or obj.get("~TYPE",None) == "RSZ_EXTERNAL_USERDATA":
				obj.re_rsz_object.rszIndex += bpy.context.scene.re_rsz_toolpanel.indexAmount
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}

class WM_OT_ExportAllRSZ(Operator):
	
	bl_label = "Export All RSZ"
	bl_idname = "re_rsz.export_all"
	bl_description = "Exports all RSZ files at the path set on their root custom property"
	
	def execute(self, context):
		RSZCollection = bpy.data.collections.get("RSZData",None)
		if RSZCollection != None:
			for obj in RSZCollection.all_objects:
				if obj.get("~TYPE",None) == "RSZ_SCN_ROOT" and obj.get("Export With Export All","False").lower() in TRUE_STRINGS_SET:
					bpy.context.view_layer.objects.active = obj
					print("Exporting " + obj.name +"\n"+obj["Export Path"])
					exportRSZFile(obj,obj["Export Path"],"SCN",obj["Game"])
				elif obj.get("~TYPE",None) == "RSZ_USR_ROOT" and obj.get("Export With Export All","False").lower() in TRUE_STRINGS_SET:
					bpy.context.view_layer.objects.active = obj
					print("Exporting " + obj.name +"\n"+obj["Export Path"])
					exportRSZFile(obj,obj["Export Path"],"USR",obj["Game"])
		showMessageBox("Exported all RSZ files.","Export Complete")
		self.report({"INFO"},"Exported all RSZ files in scene.")
		return {'FINISHED'}
	

#RE 4
class WM_OT_RE4_AddDropItem(Operator):

	bl_label = "Add Drop Item"
	bl_idname = "re_rsz.re4_add_drop_item"
	bl_description = "Adds a Drop Item game object at the 3D cursor. Requires the associated ItemData user.2 file to imported as well"
	itemID : bpy.props.EnumProperty(name = "Item Name",
									  description = "ID of item",
									  items = RE4ItemEnumList)
	itemCount : bpy.props.IntProperty(name = "Count",
									  description = "Amount of item to receive",
									  default = 1,
									  min = 0)
	mainContextIndex : bpy.props.IntProperty(name = "Main Context ID Index",
									  description = "",
									  default = 10000,
									 )
	relationContextIndex : bpy.props.IntProperty(name = "Relation Context ID Index",
									  description = "",
									  default = 10001,
									 )
	group : bpy.props.IntProperty(name = "Group",
									  description = "",
									  default = 12,
									 )
	
	fixConflicts: bpy.props.BoolProperty(
		name="Fix Conflicts",
		description="Adjust IDs so that they don't overlap",
		default = True,
	)
	loadMesh: bpy.props.BoolProperty(
		name="Load Mesh",
		description="Load mesh associated with item",
		default = False,
	)
	loadMaterials: bpy.props.BoolProperty(
		name="Load Material",
		description="Load material associated with mesh",
		default = False,
	)
	
	def execute(self, context):

		#Add Drop Item
		
		scnRootObj = context.scene.objects[context.scene.re_rsz_toolpanel.re4ItemSCNRoot]
		usrRootObj = context.scene.objects[context.scene.re_rsz_toolpanel.re4ItemUSRRoot]
		
		usrDropItemTableObject = None
		
		for child in usrRootObj.children:
			if child.get("~TYPE",None) == "RSZ_INSTANCE" and child.get("~instanceType",None) == "chainsaw.DropItemSaveDataTable":
				usrDropItemTableObject = child
				print(usrDropItemTableObject)
				break
		itemInfo = getRE4ItemInfo(self.itemID)
		if itemInfo != None:
			newGameObjectName = "DropItem "+itemInfo["Item Name"] + " - " + str(self.itemCount)
		else:
			newGameObjectName = "DropItem "+str(self.itemID) + " - " + str(self.itemCount)
		startingRSZIndex = 9000
		currentItemIndex = self.mainContextIndex
		currentRelationItemIndex = self.relationContextIndex
		if usrDropItemTableObject != None:
			
			if self.fixConflicts:
				indexInUse = False
				relationIndexInUse = False
				for child in usrDropItemTableObject.children:
					if child.get("_Index",None) == currentItemIndex:
						indexInUse = True
					if child.get("_Index",None) == currentRelationItemIndex:
						relationIndexInUse = True
				while(indexInUse):
					indexInUse = False
					currentItemIndex +=  1
					for child in usrDropItemTableObject.children:
						if child.get("_Index",None) == currentItemIndex:
							indexInUse = True
				while(relationIndexInUse):
					relationIndexInUse = False
					currentRelationItemIndex +=  1
					for child in usrDropItemTableObject.children:
						if child.get("_Index",None) == currentRelationItemIndex:
							relationIndexInUse = True
		else:
			self.report({"ERROR"},"Drop Item Table is not imported.")
			return {"CANCELLED"}
		#SCN
		#Add dropItem game object
		dropItemGameObj = createEmpty("via.GameObject",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",1),
			("~instanceType","via.GameObject"),
			("gameObjectName",newGameObjectName),
			("renderProperty","Item|EventStop|GmPause"),
			("v02",1),
			("v03",1),
			("v04",-1),
			("GUID",getNewUUID()),
			("~virtualPrefabPath","_Chainsaw/LevelDesign/Prefab/DropItem.pfb"),
			],scnRootObj,"RSZData")
		
		dropItemGameObj.re_rsz_object.rszIndex = startingRSZIndex
		#Ugly solution for getting parent inverse without rotation
		
		dropItemGameObj.location = bpy.context.scene.cursor.location
		dropItemGameObj.rotation_euler = bpy.context.scene.cursor.rotation_euler
		dropItemGameObj.rotation_mode = "QUATERNION"
		dropItemGameObj.location = (scnRootObj.matrix_world.inverted() @ dropItemGameObj.matrix_basis).to_translation()
		dropItemGameObj.show_name = bpy.context.scene.re_rsz_toolpanel.showGameObjectNames
		dropItemGameObj.empty_display_type = "SPHERE"
		#Add via.transform to dropItem game object
		dropItemTransformObj = createEmpty("via.Transform",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",1),
			("~instanceType","via.Transform"),
			("v00",[0.0, 0.0, 0.0, 0.0]),
			("v01",[0.0, 0.0, 0.0, 1.0]),
			("v02",[1.0, 1.0, 1.0, 0.0]),
			("v03",""),
			("v04",0),
			("v05",0),
			("v06",0),
			("v07",0),
			],dropItemGameObj,"RSZData")
		dropItemTransformObj.re_rsz_object.rszIndex = startingRSZIndex + 1
		#Add chainsaw.DropItem/scnDropItemComponent
		dropItemComponentObj = createEmpty("chainsaw.DropItem",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","chainsaw.DropItem"),
		("v0",1),
		("_ID",710),
		("_Falldown",1),
		("_DamageFalldown",0),
		("CastRayDropdown",-10.0),
		("_ForceLightEffect",0),
		("_WaitFlag",0),
		("_WaitGetItem",0),
		("_WaitGetItemID",-1),
		("_WaitGetItem1st",711),
		("_ItemData",712),
		("_ItemStatic",715),
		],dropItemGameObj,"RSZData")
		dropItemComponentObj.re_rsz_object.rszIndex = startingRSZIndex + 8
		#To drop item, add scnMainContextIDComponent
		scnMainContextIDComponent = createEmpty("chainsaw.ContextID",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.ContextID"),
		("_Category",2),
		("_Kind",0),
		("_Group",self.group),
		("_Index",currentItemIndex),
		],dropItemComponentObj,"RSZData")
		scnMainContextIDComponent.re_rsz_object.rszIndex = startingRSZIndex + 2
		#To drop item, add scnWaitGetItemFirstContextIDComponent
		scnWaitGetItemFirstContextIDComponent = createEmpty("chainsaw.ContextID",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.ContextID"),
		("_Category",-1),
		("_Kind",0),
		("_Group",0),
		("_Index",0),
		],dropItemComponentObj,"RSZData")
		scnWaitGetItemFirstContextIDComponent.re_rsz_object.rszIndex = startingRSZIndex + 3
		#To drop item, add scnItemSaveDataComponent
		scnItemSaveDataComponent = createEmpty("chainsaw.DropItemContext.SaveData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.DropItemContext.SaveData"),
		("ItemID",int(self.itemID)),
		("Count",self.itemCount),
		("AmmoItemID",0),
		("AmmoCount",1000),
		("Durability",0),
		("StageID",40210),
		("Attr",0),
		("StatusEffect",-1),
		("STRUCT_Position__HasValue",0),
		("STRUCT_Position__Value",[0.0, 0.0, 0.0]),
		("STRUCT_DisplayPosition__HasValue",0),
		("STRUCT_DisplayPosition__Value",[0.0, 0.0, 0.0]),
		("STRUCT_DisplayRotation__HasValue",0),
		("STRUCT_DisplayRotation__Value",[0.0, 0.0, 0.0, 0.0]),
		("STRUCT_ColliderScale__HasValue",0),
		("STRUCT_ColliderScale__Value",0.0),
		],dropItemComponentObj,"RSZData")
		scnItemSaveDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 4
		#To drop item, add scnItemRelationContextIDComponent
		scnItemRelationContextIDComponent = createEmpty("chainsaw.ContextID",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.ContextID"),
		("_Category",1),
		("_Kind",0),
		("_Group",self.group),
		("_Index",currentRelationItemIndex),
		],dropItemComponentObj,"RSZData")
		scnItemRelationContextIDComponent.re_rsz_object.rszIndex = startingRSZIndex + 5
		#To drop item, add scnItemRelationDataComponent
		scnItemRelationDataComponent = createEmpty("chainsaw.DropItemContext.RelationData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.DropItemContext.RelationData"),
		("Target",713),
		],dropItemComponentObj,"RSZData")
		scnItemRelationDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 6
		#Link scnItemRelationDataComponent["Target"] to scnItemRelationContextIDComponent
		newPropGroup = scnItemRelationDataComponent.re_rsz_object.rszObjectPointers.add()#Add constraints for tracking indices, the target is set once all objects are imported
		newPropGroup.fieldName = "Target"
		newPropGroup.targetObject = scnItemRelationContextIDComponent
		#To drop item, add scnItemStaticDataComponent
		scnItemStaticDataComponent = createEmpty("chainsaw.DropItemContext.StaticData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.DropItemContext.StaticData"),
		("HasRelation",0),
		("Relation",714),
		("InitPosition",[3.5209341049194336, 0.9442018866539001, -21.02985954284668]),
		("IgnoreTreasureMap",0),
		("MapFloorID",0),
		("IsDLC",0),
		("SubMapStageID",-1),
		("SubMapPosition",[0.0, 0.0, 0.0]),
		],dropItemComponentObj,"RSZData")
		scnItemStaticDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 7
		#Link scnItemStaticDataComponent["Relation"] to scnItemRelationDataComponent
		addRSZPointer(scnItemStaticDataComponent,"Relation",scnItemRelationDataComponent)
		#Link scnDropItemComponent["_ID"] to scnMainContextIDComponent
		addRSZPointer(dropItemComponentObj,"_ID",scnMainContextIDComponent)
		#Link scnDropItemComponent["_WaitGetItem1st"] to scnWaitGetItemFirstContextIDComponent
		addRSZPointer(dropItemComponentObj,"_WaitGetItem1st",scnWaitGetItemFirstContextIDComponent)
		#Link scnDropItemComponent["_ItemData"] to scnItemSaveDataComponent
		addRSZPointer(dropItemComponentObj,"_ItemData",scnItemSaveDataComponent)
		#Link scnDropItemComponent["_ItemStatic"] to scnItemStaticDataComponent
		addRSZPointer(dropItemComponentObj,"_ItemStatic",scnItemStaticDataComponent)
		
		
		#Add chainsaw.InteractHolder
		interactHolder = createEmpty("chainsaw.InteractHolder",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","chainsaw.InteractHolder"),
		("v0",1),
		("_Triggers",[718, 720, 722]),
		("_ForEnemy",0),
		],dropItemGameObj,"RSZData")
		interactHolder.re_rsz_object.rszIndex = startingRSZIndex + 15
		#To interactHolder, add chainsaw.InteractTriggerKey0
		interactTriggerKey0 = createEmpty("chainsaw.InteractTriggerKey",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.InteractTriggerKey"),
		("UniqueName","Pickup"),
		("Succeed",0),
		("WaitTimer",0.0),
		("EnableCheckFlag",""),
		("Targets",255),
		("TargetEnemies",[]),
		("TargetDolls",[]),
		],interactHolder,"RSZData")
		interactTriggerKey0.re_rsz_object.rszIndex = startingRSZIndex + 9
		#To interactHolder, add chainsaw.InteractHolder.TriggerContainer0
		triggerContainer0 = createEmpty("chainsaw.InteractHolder.TriggerContainer",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.InteractHolder.TriggerContainer"),
		("_Trigger",717),
		],interactHolder,"RSZData")
		#Link TriggerContainer0["_Trigger"] to InteractTriggerKey0
		addRSZPointer(triggerContainer0,"_Trigger",interactTriggerKey0)
		triggerContainer0.re_rsz_object.rszIndex = startingRSZIndex + 10
		#To Interact Holder, add chainsaw.InteractTriggerKey1
		interactTriggerKey1 = createEmpty("chainsaw.InteractTriggerKey",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.InteractTriggerKey"),
		("UniqueName","CantPickup"),
		("Succeed",0),
		("WaitTimer",0.0),
		("EnableCheckFlag",""),
		("Targets",255),
		("TargetEnemies",[]),
		("TargetDolls",[]),
		],interactHolder,"RSZData")
		interactTriggerKey1.re_rsz_object.rszIndex = startingRSZIndex + 11
		#To Interact Holder, add chainsaw.InteractHolder.TriggerContainer1
		triggerContainer1 = createEmpty("chainsaw.InteractHolder.TriggerContainer",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.InteractHolder.TriggerContainer"),
		("_Trigger",719),
		],interactHolder,"RSZData")
		triggerContainer1.re_rsz_object.rszIndex = startingRSZIndex + 12
		#Link TriggerContainer1["_Trigger"] to InteractTriggerKey1
		addRSZPointer(triggerContainer1,"_Trigger",interactTriggerKey1)
		#To Interact Holder, add chainsaw.InteractTriggerKey2
		interactTriggerKey2 = createEmpty("chainsaw.InteractTriggerKey",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.InteractTriggerKey"),
		("UniqueName","Craft"),
		("Succeed",0),
		("WaitTimer",0.0),
		("EnableCheckFlag",""),
		("Targets",255),
		("TargetEnemies",[]),
		("TargetDolls",[]),
		],interactHolder,"RSZData")
		interactTriggerKey2.re_rsz_object.rszIndex = startingRSZIndex + 13
		#To Interact Holder, add chainsaw.InteractHolder.TriggerContainer2
		triggerContainer2 = createEmpty("chainsaw.InteractHolder.TriggerContainer",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.InteractHolder.TriggerContainer"),
		("_Trigger",721),
		],interactHolder,"RSZData")
		triggerContainer2.re_rsz_object.rszIndex = startingRSZIndex + 14
		#Link TriggerContainer2["_Trigger"] to InteractTriggerKey2
		addRSZPointer(triggerContainer2,"_Trigger",interactTriggerKey2)
		#Link InteractHolder["_Triggers[0]" to TriggerContainer0
		addRSZPointer(interactHolder,"_Triggers[0]",triggerContainer0)
		#Link InteractHolder["_Triggers[1]"] to TriggerContainer1
		addRSZPointer(interactHolder,"_Triggers[1]",triggerContainer1)
		#Link InteractHolder["_Triggers[2]"] to TriggerContainer2
		addRSZPointer(interactHolder,"_Triggers[2]",triggerContainer2)
	
		
		#Add via.physics.Colliders
		colliders = createEmpty("via.physics.Colliders",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","via.physics.Colliders"),
		("v00",0),
		("v01",1),
		("v02",1),
		("v03",[]),
		("v04",1),
		("v05",[728, 733]),
		],dropItemGameObj,"RSZData")
		colliders.re_rsz_object.rszIndex = startingRSZIndex + 26
		#To Colliders, add CapsuleShape0
		capsuleShape0 = createEmpty("via.physics.CapsuleShape",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.CapsuleShape"),
		("v00",0),
		("v01",[0, 1053609165, 0, 0, 0, -1082130432, 0, 0, 1075139924, 0, 0, 0]),
		],colliders,"RSZData")
		capsuleShape0.re_rsz_object.rszIndex = startingRSZIndex + 16
		#To Colliders, add FilterInfo0
		filterInfo0 = createEmpty("via.physics.FilterInfo",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.FilterInfo"),
		("v00",0),
		("v01",77),
		("v02",0),
		("v03",0),
		("v04",-1),
		],colliders,"RSZData")
		filterInfo0.re_rsz_object.rszIndex = startingRSZIndex + 17
		#To Colliders, add UserData0
		userData0 = createEmpty("via.physics.UserData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.UserData"),
		],colliders,"RSZData")
		userData0.re_rsz_object.rszIndex = startingRSZIndex + 18
		#To Colliders, add GimmickSensorUserData0
		gimmickSensorUserData0 = createEmpty("chainsaw.collision.GimmickSensorUserData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.collision.GimmickSensorUserData"),
		("v0",""),
		("v1",726),
		("_Kind",1),
		("_ID",0),
		],colliders,"RSZData")
		gimmickSensorUserData0.re_rsz_object.rszIndex = startingRSZIndex + 19
		#To Colliders, add Collider0
		collider0 = createEmpty("via.physics.Collider",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.Collider"),
		("v00",1),
		("v01",1),
		("v02",724),
		("v03",725),
		("v04",727),
		("v05","_Chainsaw/Config/Physics/Filter/SensorItem.cfil"),
		("v06","NULL_STR"),
		("v07",""),
		("v08",""),
		],colliders,"RSZData")
		collider0.re_rsz_object.rszIndex = startingRSZIndex + 20
		#Link Collider0["v02"] to CapsuleShape0
		addRSZPointer(collider0,"v02",capsuleShape0)
		#Link Collider0["v03"] to FilterInfo0
		addRSZPointer(collider0,"v03",filterInfo0)
		#Link Collider0["v04"] to GimmickSensorUserData0
		addRSZPointer(collider0,"v04",gimmickSensorUserData0)
		#Link GimmickSensorUserData0["v1"] to UserData0
		addRSZPointer(gimmickSensorUserData0,"v1",userData0)
		#To Colliders, add CapsuleShape1
		capsuleShape1 = createEmpty("via.physics.CapsuleShape",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.CapsuleShape"),
		("v00",0),
		("v01",[0, 1053609165, 0, 0, 0, -1082130432, 0, 0, 1082130432, 0, 0, 0]),
		],colliders,"RSZData")
		capsuleShape1.re_rsz_object.rszIndex = startingRSZIndex + 21
		#To Colliders, add FilterInfo1
		filterInfo1 = createEmpty("via.physics.FilterInfo",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.FilterInfo"),
		("v00",0),
		("v01",77),
		("v02",0),
		("v03",0),
		("v04",-1),
		],colliders,"RSZData")
		filterInfo1.re_rsz_object.rszIndex = startingRSZIndex + 22
		#To Colliders, add UserData1
		userData1 = createEmpty("via.physics.UserData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.UserData"),
		],colliders,"RSZData")
		userData1.re_rsz_object.rszIndex = startingRSZIndex + 23
		#To Colliders, add GimmickSensorUserData1
		gimmickSensorUserData1 = createEmpty("chainsaw.collision.GimmickSensorUserData",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.collision.GimmickSensorUserData"),
		("v0",""),
		("v1",731),
		("_Kind",2),
		("_ID",0),
		],colliders,"RSZData")
		gimmickSensorUserData1.re_rsz_object.rszIndex = startingRSZIndex + 24
		#Link GimmickSensorUserData1["v1"] to UserData1
		addRSZPointer(gimmickSensorUserData1,"v1",userData1)
		#To Colliders, add Collider1
		collider1 = createEmpty("via.physics.Collider",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","via.physics.Collider"),
		("v00",1),
		("v01",1),
		("v02",729),
		("v03",730),
		("v04",732),
		("v05","_Chainsaw/Config/Physics/Filter/SensorItem.cfil"),
		("v06","NULL_STR"),
		("v07",""),
		("v08",""),
		],colliders,"RSZData")
		collider1.re_rsz_object.rszIndex = startingRSZIndex + 25
		#Link Collider1["v02"] to CapsuleShape1
		addRSZPointer(collider1,"v02",capsuleShape1)
		#Link Collider1["v03"] to FilterInfo1
		addRSZPointer(collider1,"v03",filterInfo1)
		#Link Collider1["v04"] to GimmickSensorUserData1
		addRSZPointer(collider1,"v04",gimmickSensorUserData1)
		#Link Colliders["v05"][0] to Collider0
		addRSZPointer(colliders,"v05[0]",collider0)
		#Link Colliders["v05"][1] to Collider1
		addRSZPointer(colliders,"v05[1]",collider1)
		
		#Add chainsaw.PortrayalSettings
		portrayalSettings = createEmpty("chainsaw.PortrayalSettings",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","chainsaw.PortrayalSettings"),
		("v0",1),
		("_Params",737),
		],dropItemGameObj,"RSZData")
		portrayalSettings.re_rsz_object.rszIndex = startingRSZIndex + 30
		#To PortrayalSettings, add PortrayalParam0
		portrayalParam0 = createEmpty("chainsaw.PortrayalSettings.Param",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.PortrayalSettings.Param"),
		("_KeyHash",919028223),
		("_BindTriggerNameHash",-2114883783),
		("CollectChild",1),
		("EndKey",""),
		],portrayalSettings,"RSZData")
		portrayalParam0.re_rsz_object.rszIndex = startingRSZIndex + 27
		#To PortrayalSettings, add PortrayalParam1
		portrayalParam1 = createEmpty("chainsaw.PortrayalSettings.Param",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.PortrayalSettings.Param"),
		("_KeyHash",691592934),
		("_BindTriggerNameHash",-2114883783),
		("CollectChild",1),
		("EndKey",""),
		],portrayalSettings,"RSZData")
		portrayalParam1.re_rsz_object.rszIndex = startingRSZIndex + 28
		#To PortrayalSettings, add PortrayalOptionSettings
		portrayalOptionSettings = createEmpty("chainsaw.OptionSettings`1<chainsaw.PortrayalSettings.Param>",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.OptionSettings`1<chainsaw.PortrayalSettings.Param>"),
		("_Params",[735, 736]),
		],portrayalSettings,"RSZData")
		portrayalOptionSettings.re_rsz_object.rszIndex = startingRSZIndex + 29
		#Link OptionSettings["_Params"][0] to PortrayalParam0
		addRSZPointer(portrayalOptionSettings,"_Params[0]",portrayalParam0)
		#Link OptionSettings["_Params"][1] to PortrayalParam1
		addRSZPointer(portrayalOptionSettings,"_Params[1]",portrayalParam1)
		#Link PortrayalSettings["_Params"] to PortrayalOptionSettings
		addRSZPointer(portrayalSettings,"_Params",portrayalOptionSettings)
		
		#Add chainsaw.CheckFlagSettings
		checkFlagSettings = createEmpty("chainsaw.CheckFlagSettings",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","chainsaw.CheckFlagSettings"),
		("v0",1),
		("_Params",741),
		],dropItemGameObj,"RSZData")
		checkFlagSettings.re_rsz_object.rszIndex = startingRSZIndex + 34
		#To CheckFlagSettings, add FlagCondition
		flagCondition = createEmpty("chainsaw.FlagCondition",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.FlagCondition"),
		("_CheckFlags",[]),
		("_Logic",0),
		],checkFlagSettings,"RSZData")
		flagCondition.re_rsz_object.rszIndex = startingRSZIndex + 31
		#To CheckFlagSettings, add FlagParam
		flagParam = createEmpty("chainsaw.CheckFlagSettings.Param",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.CheckFlagSettings.Param"),
		("_KeyHash",-703533349),
		("_BindTriggerNameHash",-2114883783),
		("_FlagCondition",739),
		],checkFlagSettings,"RSZData")
		flagParam.re_rsz_object.rszIndex = startingRSZIndex + 32
		#Link FlagParam["_FlagCondition"] to FlagCondition
		addRSZPointer(flagParam,"_FlagCondition",flagCondition)
		#To CheckFlagSettings, add CheckFlagOptionSettings
		checkFlagOptionSettings = createEmpty("chainsaw.OptionSettings`1<chainsaw.CheckFlagSettings.Param>",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",0),
		("~instanceType","chainsaw.OptionSettings`1<chainsaw.CheckFlagSettings.Param>"),
		("_Params",[740]),
		],checkFlagSettings,"RSZData")
		checkFlagOptionSettings.re_rsz_object.rszIndex = startingRSZIndex + 33
		#Link CheckFlagOptionSettings["_Params"][0] to FlagParam
		addRSZPointer(checkFlagOptionSettings,"_Params[0]",flagParam)
		#Link CheckFlagSettings["_Params"] to CheckFlagOptionSettings
		addRSZPointer(checkFlagSettings,"_Params",checkFlagOptionSettings)
		
		#Add DisplayPosition gameobject to drop item gameobject
		displayPositionGameObj = createEmpty("via.GameObject",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","via.GameObject"),
		("gameObjectName","DisplayPosition"),
		("renderProperty",""),
		("v02",1),
		("v03",1),
		("v04",-1),
		("GUID",getNewUUID()),
		("~virtualPrefabPath",""),
		],dropItemGameObj,"RSZData")
		displayPositionGameObj.re_rsz_object.rszIndex = startingRSZIndex + 35
		#Add via.transform to DisplayPosition
		displayPositionTransform = createEmpty("via.Transform",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","via.Transform"),
		("v00",[0.0, 0.0, 0.0, 0.0]),
		("v01",[0.0, 0.0, 0.0, 1.0]),
		("v02",[1.0, 1.0, 1.0, 0.0]),
		("v03",""),
		("v04",0),
		("v05",0),
		("v06",0),
		("v07",0),
		],displayPositionGameObj,"RSZData")
		displayPositionTransform.re_rsz_object.rszIndex = startingRSZIndex + 36
		#Add NpcPos gameobject to drop item gameobject
		npcPosGameObj = createEmpty("via.GameObject",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","via.GameObject"),
		("gameObjectName","NpcPos"),
		("renderProperty",""),
		("v02",1),
		("v03",1),
		("v04",-1),
		("GUID",getNewUUID()),
		("~virtualPrefabPath",""),
		],dropItemGameObj,"RSZData")
		npcPosGameObj.re_rsz_object.rszIndex = startingRSZIndex + 37
		#Add via.transform to NpcPos
		npcPosTransform = createEmpty("via.Transform",[
		("~TYPE","RSZ_INSTANCE"),
		("~isObject",1),
		("~instanceType","via.Transform"),
		("v00",[0.0, 0.0, 0.0, 0.0]),
		("v01",[0.0, 0.0, 0.0, 1.0]),
		("v02",[1.0, 1.0, 1.0, 0.0]),
		("v03",""),
		("v04",0),
		("v05",0),
		("v06",0),
		("v07",0),
		],npcPosGameObj,"RSZData")
		npcPosTransform.re_rsz_object.rszIndex = startingRSZIndex + 38
		
		#USR
		
		if usrDropItemTableObject != None:
			#To usrDropItemTableObject, add usrMainContextIDComponent
			usrMainContextIDComponent = createEmpty("chainsaw.ContextID",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",0),
			("~instanceType","chainsaw.ContextID"),
			("_Category",2),
			("_Kind",0),
			("_Group",self.group),
			("_Index",currentItemIndex),
			],usrDropItemTableObject,"RSZData")
			usrMainContextIDComponent.re_rsz_object.rszIndex = startingRSZIndex
			#To usrDropItemTableObject, add usrItemSaveDataComponent
			usrItemSaveDataComponent = createEmpty("chainsaw.DropItemContext.SaveData",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",0),
			("~instanceType","chainsaw.DropItemContext.SaveData"),
			("ItemID",int(self.itemID)),
			("Count",self.itemCount),
			("AmmoItemID",0),
			("AmmoCount",1000),
			("Durability",0),
			("StageID",40210),
			("Attr",0),
			("StatusEffect",-1),
			("STRUCT_Position__HasValue",0),
			("STRUCT_Position__Value",[0.0, 0.0, 0.0]),
			("STRUCT_DisplayPosition__HasValue",0),
			("STRUCT_DisplayPosition__Value",[0.0, 0.0, 0.0]),
			("STRUCT_DisplayRotation__HasValue",0),
			("STRUCT_DisplayRotation__Value",[0.0, 0.0, 0.0, 0.0]),
			("STRUCT_ColliderScale__HasValue",0),
			("STRUCT_ColliderScale__Value",0.0),
			],usrDropItemTableObject,"RSZData")
			usrItemSaveDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 1
			#To usrDropItemTableObject, add usrItemRelationContextIDComponent
			usrItemRelationContextIDComponent = createEmpty("chainsaw.ContextID",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",0),
			("~instanceType","chainsaw.ContextID"),
			("_Category",-1),
			("_Kind",0),
			("_Group",0),
			("_Index",0),
			],usrDropItemTableObject,"RSZData")
			usrItemRelationContextIDComponent.re_rsz_object.rszIndex = startingRSZIndex + 2
			#To usrDropItemTableObject, add usrItemRelationDataComponent
			usrItemRelationDataComponent = createEmpty("chainsaw.DropItemContext.RelationData",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",0),
			("~instanceType","chainsaw.DropItemContext.RelationData"),
			("Target",51),
			],usrDropItemTableObject,"RSZData")
			usrItemRelationDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 3
			#Link usrItemRelationDataComponent["Target"] to usrItemRelationContextIDComponent
			addRSZPointer(usrItemRelationDataComponent,"Target",usrItemRelationContextIDComponent)
			#To usrDropItemTableObject, add usrItemStaticDataComponent
			usrItemStaticDataComponent = createEmpty("chainsaw.DropItemContext.StaticData",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",0),
			("~instanceType","chainsaw.DropItemContext.StaticData"),
			("HasRelation",0),
			("Relation",52),
			("InitPosition",[3.5209341049194336, 0.9442018866539001, -21.02985954284668]),
			("IgnoreTreasureMap",0),
			("MapFloorID",0),
			("IsDLC",0),
			("SubMapStageID",-1),
			("SubMapPosition",[0.0, 0.0, 0.0]),
			],usrDropItemTableObject,"RSZData")
			usrItemStaticDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 4
			#Link usrItemStaticDataComponent["Relation"] to usrItemRelationDataComponent
			addRSZPointer(usrItemStaticDataComponent,"Relation",usrItemRelationDataComponent)
			#To usrDropItemTableObject, add usrDropItemDataComponent
			usrDropItemDataComponent = createEmpty("chainsaw.DropItemSaveDataTable.Data",[
			("~TYPE","RSZ_INSTANCE"),
			("~isObject",0),
			("~instanceType","chainsaw.DropItemSaveDataTable.Data"),
			("ID",49),
			("ItemData",50),
			("ItemStatic",53),
			],usrDropItemTableObject,"RSZData")
			usrItemStaticDataComponent.re_rsz_object.rszIndex = startingRSZIndex + 5
			#Link usrDropItemDataComponent["ID"] to usrMainContextIDComponent
			addRSZPointer(usrDropItemDataComponent,"ID",usrMainContextIDComponent)
			#Link usrDropItemDataComponent["ItemData"] to usrItemSaveDataComponent
			addRSZPointer(usrDropItemDataComponent,"ItemData",usrItemSaveDataComponent)
			#Link usrDropItemDataComponent["ItemStatic"] to usrItemStaticDataComponent
			addRSZPointer(usrDropItemDataComponent,"ItemStatic",usrItemStaticDataComponent)
			#Convert usrDropItemTableObject array to list, add item to it, and set it back
			table = usrDropItemTableObject["Datas"].to_list()
			lastIndex = len(table)
			table.append(9999)#Placeholder, will be fixed by reindexing
			usrDropItemTableObject["Datas"] = table
			#Link usrDropItemTableObject["Datas"][x] to usrDropItemDataComponent
			addRSZPointer(usrDropItemTableObject,"Datas["+str(lastIndex)+"]",usrDropItemDataComponent)
			
			reindexTree(scnRootObj)
			reindexTree(usrRootObj)
			bpy.context.view_layer.objects.active = dropItemGameObj
		self.report({"INFO"},"Added Drop Item.")
		return {'FINISHED'}
	
	def invoke(self,context,event):
		return context.window_manager.invoke_props_dialog(self)
class WM_OT_RE4_EditDropItem(Operator):

	bl_label = "Edit Drop Item"
	bl_idname = "re_rsz.re4_edit_drop_item"
	bl_description = "Edit an existing Drop Item component. Requires the associated ItemData user.2 file to imported as well"
	itemID : bpy.props.EnumProperty(name = "Item Name",
									  description = "Amount of item to receive",
									  items = RE4ItemEnumList)
	itemCount : bpy.props.IntProperty(name = "Count",
									  description = "Amount of item to receive",
									  default = 1,
									  min = 0)
	def execute(self, context):

		#Edit Drop Item Test
		
		scnRootObj = context.scene.objects[context.scene.re_rsz_toolpanel.re4ItemSCNRoot]
		usrRootObj = context.scene.objects[context.scene.re_rsz_toolpanel.re4ItemUSRRoot]
		
		activeObj = bpy.context.active_object
		
		scnDropItemComponent = None
		
		if activeObj.get("~TYPE",None) == "RSZ_INSTANCE":
			#Find drop item object
			#Either game object or drop item component can be selected.
			if activeObj.get("~instanceType",None) == "via.GameObject":
				for child in activeObj.children:
					if child.get("~TYPE",None) == "RSZ_INSTANCE" and child.get("~instanceType",None) == "chainsaw.DropItem":
						scnDropItemComponent = child
						break 
			elif activeObj.get("~instanceType",None) == "chainsaw.DropItem":
				scnDropItemComponent = activeObj
				
		if scnDropItemComponent != None:
			scnMainContextIDComponent = None
			scnWaitGetItemFirstContextIDComponent = None
			scnItemSaveDataComponent = None
			scnItemStaticDataComponent = None
			scnItemRelationDataComponent = None
			scnItemRelationContextIDComponent = None
			
			for child in scnDropItemComponent.children:
				if child.re_rsz_object.rszIndex == scnDropItemComponent["_ID"]:
					scnMainContextIDComponent = child
				elif child.re_rsz_object.rszIndex == scnDropItemComponent["_WaitGetItem1st"]:
					scnWaitGetItemFirstContextIDComponent = child
				elif child.re_rsz_object.rszIndex == scnDropItemComponent["_ItemData"]:
					scnItemSaveDataComponent = child
				elif child.re_rsz_object.rszIndex == scnDropItemComponent["_ItemStatic"]:
					scnItemStaticDataComponent = child
			
			if scnItemStaticDataComponent != None:
				for child in scnDropItemComponent.children:
					if child.re_rsz_object.rszIndex == scnItemStaticDataComponent["Relation"]:
						scnItemRelationDataComponent = child
						break
			if scnItemRelationDataComponent != None:
				for child in scnDropItemComponent.children:
					if child.re_rsz_object.rszIndex == scnItemRelationDataComponent["Target"]:
						scnItemRelationContextIDComponent = child
						break
					
			#print(scnDropItemComponent)
			#print(scnMainContextIDComponent)
			#print(scnWaitGetItemFirstContextIDComponent)
			#print(scnItemSaveDataComponent)
			#print(scnItemStaticDataComponent)
			#print(scnItemRelationDataComponent)
			#print(scnItemRelationContextIDComponent)
		
		#Get SaveDataTableObject
		usrDropItemTableObject = None
		
		
		usrMainContextIDComponent = None
		usrItemSaveDataComponent = None
		usrItemRelationContextIDComponent = None
		usrItemRelationDataComponent = None
		usrItemStaticDataComponent = None
		usrDropItemDataComponent = None
		
		#print(usrRootObj.children)
		#print("User")
		for child in usrRootObj.children:
			if child.get("~TYPE",None) == "RSZ_INSTANCE" and child.get("~instanceType",None) == "chainsaw.DropItemSaveDataTable":
				usrDropItemTableObject = child
				print(usrDropItemTableObject)
				break
		
		if usrDropItemTableObject != None:
			for index, child in enumerate(usrDropItemTableObject.children):#Find object that matches the main context id from the scn object
				if child.get("~TYPE",None) == "RSZ_INSTANCE" and child.get("~instanceType",None) == "chainsaw.ContextID" and scnMainContextIDComponent["_Category"] == child["_Category"] and scnMainContextIDComponent["_Group"] == child["_Group"] and scnMainContextIDComponent["_Index"] == child["_Index"]:
					usrMainContextIDComponent = child
					
					usrItemSaveDataComponent = usrDropItemTableObject.children[index+1]
					usrItemRelationContextIDComponent = usrDropItemTableObject.children[index+2]
					usrItemRelationDataComponent = usrDropItemTableObject.children[index+3]
					usrItemStaticDataComponent = usrDropItemTableObject.children[index+4]
					usrDropItemDataComponent = usrDropItemTableObject.children[index+5]
					break
			
			#print(usrMainContextIDComponent)
			#print(usrItemSaveDataComponent)
			#print(usrItemRelationContextIDComponent)
			#print(usrItemRelationDataComponent)
			#print(usrItemStaticDataComponent)
			#print(usrDropItemDataComponent)
			#Verify object indices are correct
			if (usrDropItemDataComponent["ID"] != usrMainContextIDComponent.re_rsz_object.rszIndex or 
			usrDropItemDataComponent["ItemData"] != usrItemSaveDataComponent.re_rsz_object.rszIndex or 
			usrDropItemDataComponent["ItemStatic"] != usrItemStaticDataComponent.re_rsz_object.rszIndex or
			usrItemStaticDataComponent["Relation"] != usrItemRelationDataComponent.re_rsz_object.rszIndex or
			usrItemRelationDataComponent["Target"] != usrItemRelationContextIDComponent.re_rsz_object.rszIndex):
				print("ERROR: Retrieved incorrect indices in user drop table")
		
			
			scnItemSaveDataComponent["Count"] = self.itemCount
			scnItemSaveDataComponent["ItemID"] = int(self.itemID)
			usrItemSaveDataComponent["Count"] = self.itemCount
			usrItemSaveDataComponent["ItemID"] = int(self.itemID)
		self.report({"INFO"},"Edited Drop Item.")
		return {'FINISHED'}
	def invoke(self,context,event):
		return context.window_manager.invoke_props_dialog(self)
class WM_OT_RE4_AddNPC(Operator):

	bl_label = "Add NPC"
	bl_idname = "re_rsz.re4_add_npc"
	bl_description = "Adds an NPC game object at the 3D cursor. Requires the associated ItemData user.2 file to imported as well"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added NPC.")
		return {'FINISHED'}

class WM_OT_RE4_EditNPC(Operator):

	bl_label = "Edit NPC"
	bl_idname = "re_rsz.re4_edit_npc"
	bl_description = "Edit an existing NPC game object. Requires the associated ItemData user.2 file to imported as well"
	def execute(self, context):
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Edited NPC.")
		return {'FINISHED'}
	
	
class WM_OT_OpenPresetFolder(Operator):
	bl_label = "Open Preset Folder"
	bl_description = "Opens the preset folder in File Explorer"
	bl_idname = "re_rsz.open_preset_folder"

	def execute(self, context):
		presetsPath = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),"Presets",context.scene.re_rsz_toolpanel.game)
		os.startfile(presetsPath)
		return {'FINISHED'}

class WM_OT_SavePreset(Operator):
	bl_label = "Save Selected As Preset"
	bl_idname = "re_rsz.save_selected_as_preset"
	bl_context = "objectmode"
	bl_description = "Save selected RSZ object as a preset for easy reuse and sharing. All objects that are a child of the selected object will be included. Presets can be accessed using the Open Preset Folder button"
	presetName : bpy.props.StringProperty(name = "Enter Preset Name",default = "newPreset")
	
	@classmethod
	def poll(self,context):
		return context.active_object is not None
	
	def execute(self, context):
		finished = saveAsPreset(context.active_object, self.presetName,context.scene.re_rsz_toolpanel.game)
		if finished:
			self.report({"INFO"},"Saved preset.")
			return {'FINISHED'}
		else:
			return {'CANCELLED'}
	def invoke(self,context,event):
		return context.window_manager.invoke_props_dialog(self)

		return {'FINISHED'}
	
class WM_OT_AddRSZPreset(Operator):
	bl_label = "Add RSZ Preset"
	bl_idname = "re_rsz.add_rsz_preset"
	bl_description = "Add selected RSZ preset to scene"
	bl_options = {'UNDO'}
	def execute(self, context):
		enumValue = bpy.context.scene.re_rsz_toolpanel.rszPresets
		finished = False
		presetsPath = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),"Presets")    
		#activeObj = bpy.context.active_object
		print("Reading Preset: " + enumValue)
		for activeObj in bpy.context.selected_objects:
			finished = readPresetJSON(os.path.join(presetsPath,enumValue),activeObj,bpy.context.scene.re_rsz_toolpanel.game)
		#tag_redraw(bpy.context)
		if finished:
			self.report({"INFO"},"Added RSZ preset.")
			return {'FINISHED'}
		else:
			return {'CANCELLED'}