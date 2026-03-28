#Author: NSA Cloud
import bpy
import os

from bpy.types import Operator
from bpy.types import Mesh
from .blender_utils import showMessageBox
from .re_rsz_propertyGroups import RSZ_PointLightPropertyGroup
from .blender_re_scn import exportRSZFile
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
		name = "RSZObject"
		obj = createEmpty(name,[("~TYPE","RE_RSZ_TEST")],None,"RSZData")
		obj: bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
		self.report({"INFO"},"Added RSZ Object.")
		return {'FINISHED'}

class WM_OT_IncreaseRSZIndex(Operator):
	
	bl_label = "Increase RSZ Index"
	bl_idname = "re_rsz.increase_rsz_index"
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
				if obj.get("~TYPE",None) == "RSZ_SCN_ROOT":
					print("Exporting " + obj.name +"\n"+obj["Export Path"])
					exportRSZFile(obj,obj["Export Path"],"SCN")
		self.report({"INFO"},"Exported all RSZ files in scene.")
		return {'FINISHED'}