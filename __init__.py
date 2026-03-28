#Author: NSA Cloud
bl_info = {
	"name": "RE Map Editor",
	"author": "NSA Cloud",
	"version": (0, 1),
	"blender": (3, 1, 2),
	"location": "View3D > Tool Shelf > RE Map Tools",
	"description": "Editor for RE Engine maps.",
	"warning": "",
	"wiki_url": "https://github.com/NSACloud/RE-Map-Editor",
	"tracker_url": "",
	"category": "3D View"}

import bpy
import os

from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty,IntProperty, BoolProperty, EnumProperty, CollectionProperty,PointerProperty
from bpy.types import Operator, OperatorFileListElement,AddonPreferences
from .modules.gen_functions import textColors,raiseWarning,getFolderSize,formatByteSize
from .modules.re_rsz_propertyGroups import( 
	RSZ_PointLightPropertyGroup,
	RSZ_SpotLightPropertyGroup,
	RSZ_DirectionalLightPropertyGroup,
	RSZ_ObjectPointersGroup,
	RSZ_ObjectGroup,
	RE_MapToolPanelPropertyGroup,
)
from .modules.ui_re_rsz_panels import (
	OBJECT_PT_RE_MapTools_Object_Panel,
	OBJECT_PT_RE_MapTools_Visibility_Panel,
	OBJECT_PT_RE_MapTools_Export_Panel,
	LIST_UL_RSZ_Pointers,
	OBJECT_PT_RSZObjectPointersPanel,
	OBJECT_PT_RSZPointLightPanel,
	OBJECT_PT_RSZSpotLightPanel,
	OBJECT_PT_RSZDirectionalLightPanel,
	OBJECT_PT_RE_MapTools_RE4_Panel,
	OBJECT_PT_RSZPresetPanel
)
from .modules.re_rsz_operators import (
	WM_OT_AddRSZObject,
	WM_OT_AddMeshObject,
	WM_OT_AddPointLightObject,
	WM_OT_AddSpotLightObject,
	WM_OT_AddDirectionalLightObject,
	WM_OT_AddEPVObject,
	WM_OT_ReloadMeshes,
	WM_OT_ReindexTree,
	WM_OT_ExportAllRSZ,
	WM_OT_IncreaseRSZIndex,
	WM_OT_RE4_AddDropItem,
	WM_OT_RE4_EditDropItem,
	WM_OT_RE4_AddNPC,
	WM_OT_RE4_EditNPC,
	WM_OT_OpenPresetFolder,
	WM_OT_SavePreset,
	WM_OT_AddRSZPreset,
	   )
from .modules.blender_re_scn import importRSZFile,exportRSZFile

from .modules.blender_re_mcol import importMCOLFile,exportMCOLFile
os.system("color")#Enable console colors
class WM_OT_OpenTextureCacheFolder(Operator):
	bl_label = "Open Texture Cache Folder"
	bl_description = "Opens the texture cache folder in File Explorer"
	bl_idname = "re_map_editor.open_texture_cache_folder"

	def execute(self, context):
		try:
			os.startfile(bpy.context.preferences.addons[__name__].preferences.textureCachePath)
		except:
			pass
		return {'FINISHED'}
class ChunkPathPropertyGroup(bpy.types.PropertyGroup):
    gameName: EnumProperty(
		name="",
		description="Set the game",
		items= [ 
		("DMC5", "Devil May Cry 5", ""),
		("RE2", "Resident Evil 2", ""),
		("RE3", "Resident Evil 3", ""),
		("RE8", "Resident Evil 8", ""),	
		("RE2RT", "Resident Evil 2 Ray Tracing", ""),
		("RE3RT", "Resident Evil 3 Ray Tracing", ""),
		("RE7RT", "Resident Evil 7 Ray Tracing", ""),
		("MHRSB", "Monster Hunter Rise", ""),
		("SF6", "Street Fighter 6", ""),
		("RE4", "Resident Evil 4", ""),
		("DD2", "Dragon's Dogma 2", ""),
		("KG", "Kunitsu-Gami", ""),
		("MHWILDS", "Monster Hunter Wilds", ""),
		]
    )
    path: StringProperty(
        name="Path",
		subtype="DIR_PATH",
		description = "Set the path to the natives\STM folder inside the extracted chunk files\nThis determines where textures will be imported from\n"+r"Example: I:\RE4_EXTRACT\re_chunk_000\natives\STM"
    )


class AddItemOperator(bpy.types.Operator):
	bl_idname = "re_map_editor.chunk_path_list_add_item"
	bl_description = "Add path to the extracted chunk's natives\STM\ folder.\n"+r"Example: I:\RE4_EXTRACT\re_chunk_000\natives\STM"
	bl_label = "Add Path"
	

	def execute(self, context):
		# Add an item to the list
		context.preferences.addons[__name__].preferences.chunkPathList_items.add()
		return {'FINISHED'}

# Operator to remove an item from the list
class RemoveItemOperator(bpy.types.Operator):
	bl_idname = "re_map_editor.chunk_path_list_remove_item"
	bl_description = "Remove chunk path from the list"
	bl_label = "Remove Selected Path"

	index: bpy.props.IntProperty()

	def execute(self, context):
        # Remove the item at the specified index from the list
		context.preferences.addons[__name__].preferences.chunkPathList_items.remove(self.index)
		return {'FINISHED'}

# Operator to reorder items in the list
class ReorderItemOperator(bpy.types.Operator):
	bl_idname = "re_map_editor.chunk_path_list_reorder_item"
	bl_description = "Change the order in which files will be searched"
	bl_label = "Reorder Item"

	direction: bpy.props.EnumProperty(
		items=[('UP', "Up", ""), ('DOWN', "Down", "")],
		default='UP'
	)

	index: bpy.props.IntProperty()

	def execute(self, context):
		# Reorder the item in the list
		if self.direction == 'UP':
			context.preferences.addons[__name__].preferences.chunkPathList_items.move(self.index, self.index - 1)
		elif self.direction == 'DOWN':
			context.preferences.addons[__name__].preferences.chunkPathList_items.move(self.index, self.index + 1)
		return {'FINISHED'}

class MESH_UL_ChunkPathListMapEditor(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		layout.prop(item,"gameName")
		layout.prop(item,"path")
class REMapToolsPreferences(AddonPreferences):
	bl_idname = __name__
 
 
	textureCachePath: StringProperty(
		name="Texture Cache Path",
		subtype='DIR_PATH',
		description = "Location to save converted textures",
		default = os.path.join(os.path.dirname(os.path.realpath(__file__)),"TextureCache")
	)
	useDDS: BoolProperty(
		name="Use DDS Textures (Blender 4.2 or higher)",
		description = "Use DDS textures instead of converting to TIF.\nThis greatly improves mesh import speed but is only usable on Blender 4.2 or higher.\nIf the Blender version is less than 4.2, this option will do nothing",
		default = False if bpy.app.version < (4,2,0) else True
	)
	saveChunkPaths: BoolProperty(
		name="Save Chunk Paths Automatically",
		description = "If a chunk path is detected when a mesh is imported, add it to the chunk path list automatically",
		default = False
	)
	#noesisPath: StringProperty(
	#	name="Noesis.exe Path",
	#	subtype='FILE_PATH',
	#)
	chunkPathList_items: CollectionProperty(type=ChunkPathPropertyGroup)
	chunkPathList_index: IntProperty(name="")
	def draw(self, context):
		layout = self.layout
		layout.prop(self, "textureCachePath")
		layout.label(text=f"Folder Size: {formatByteSize(getFolderSize(self.textureCachePath))}")
		layout.operator("re_map_editor.open_texture_cache_folder")
		#layout.prop(self, "noesisPath")
		layout.label(text = "Chunk Path List")
		layout.template_list("MESH_UL_ChunkPathListMapEditor", "", self, "chunkPathList_items", self, "chunkPathList_index",rows = 3)
		row = layout.row(align=True)
		row.operator("re_map_editor.chunk_path_list_add_item")
		row.operator("re_map_editor.chunk_path_list_remove_item")

        # Reorder buttons
		row = layout.row(align=True)
		row.operator("re_map_editor.chunk_path_list_reorder_item", text="Move Up").direction = 'UP'
		row.operator("re_map_editor.chunk_path_list_reorder_item", text="Move Down").direction = 'DOWN'
class ImportREScene(bpy.types.Operator, ImportHelper):
	'''Import RE Engine RSZ File'''
	bl_idname = "re_scene.importfile"
	bl_label = "Import RE RSZ"
	bl_options = {'PRESET', "REGISTER", "UNDO"}
	files : CollectionProperty(
			name="File Path",
			type=OperatorFileListElement,
			)
	directory : StringProperty(
			subtype='DIR_PATH',
			)
	filename_ext = ".scn.*"
	filter_glob: StringProperty(default="*.scn;*;*.user", options={'HIDDEN'})
	game: EnumProperty(
		name="Game",
		description="Choose which game to import from",
		default = "MHRise",
		items=[ ("MHRise", "Monster Hunter Rise", ""),
				("RE2RT", "Resident Evil 2 RT", ""),
				("RE4", "Resident Evil 4", ""),
				("DR", "Dead Rising", ""),
				("MHWILDS", "Monster Hunter Wilds", ""),
			   ]
		
		)
	clear_scene : BoolProperty(
	   name = "Clear scene before import.",
	   description = "Clears all objects before importing",
	   default = True)
	optimizedImport : BoolProperty(
	   name = "Optimized Import",
	   description = "Load only meshes, lights, and collisions using instancing. Loads much faster and has better performance, but can't be exported back to the game",
	   default = False)
	loadLinkedScenes : BoolProperty(
	   name = "Load Linked Scenes",
	   description = "Load all scn files called by the imported file",
	   default = True)
	loadMeshes : BoolProperty(
	   name = "Load Meshes",
	   description = "Load Meshes (Slow)",
	   default = True)
	lodTarget: EnumProperty(
		name="Mesh LOD Level",
		description="Set the quality of the imported mesh file. Lower quality values increase performance in Blender and decrease loading times.\nIf a mesh file doesn't have that quality level available, the next lowest quality level will be used",
		default = "0",
		items=[ ("0", "Full Quality", "LOD 0"),
				("-1", "-1 Quality Level", "LOD 1"),
				("-2", "-2 Quality Level", "LOD 2"),
				("-3", "-3 Quality Level", "LOD 3"),
				("-4", "-4 Quality Level", "LOD 4"),
				("-5", "-5 Quality Level", "LOD 5"),
				("-6", "-6 Quality Level", "LOD 6"),
				("-7", "-7 Quality Level", "LOD 7"),
				("-8", "-8 Quality Level", "LOD 8"),
			  
			  ]
		
		)
	loadMaterials : BoolProperty(
	   name = "Load Materials (Slow)",
	   description = "Load mesh materials",
	   default = True)
	loadUnusedTextures : BoolProperty(
	   name = "Load Unused Textures",
	   description = "Loads textures that have no function assigned to them in the material shader graph.\nLeaving this disabled will make materials load faster.\nOnly enable this if you plan on editing the material shader graph",
	   default = False)
	loadUnusedProps : BoolProperty(
	   name = "Load Unused Material Properties",
	   description = "Loads material properties that have no function assigned to them in the material shader graph.\nLeaving this disabled will make materials load faster.\nOnly enable this if you plan on editing the material shader graph",
	   default = False)
	useBackfaceCulling : BoolProperty(
	   name = "Use Backface Culling",
	   description = "Enables backface culling on materials. May improve Blender's performance on high poly meshes.\nBackface culling will only be enabled on materials without the two sided flag",
	   default = False)

	reloadCachedTextures : BoolProperty(
	   name = "Reload Cached Textures",
	   description = "Convert all textures again instead of reading from already converted textures. Use this if you make changes to textures and need to reload them",
	   default = False)
	loadLights : BoolProperty(
	   name = "Load Lights",
	   description = "Load supported RSZ light objects as lights",
	   default = True)
	loadCollisions : BoolProperty(
	   name = "Load Collisions",
	   description = "Load Collisions Meshes (MCOL)",
	   default = True)
	fixClippingDistance : BoolProperty(
	   name = "Fix Clipping Distance",
	   description = "Adjusts clipping distance to avoid graphical issues",
	   default = True)
	optimizeEEVEESettings : BoolProperty(
	   name = "Set EEVEE Settings",
	   description = "Adjusts various settings in EEVEE to appear more similar to the game",
	   default = True)
	checkChunkFirst : BoolProperty(
	   name = "Check Chunk First",
	   description = "Try to load any files from the extracted chunk path first, instead of checking the game natives folder",
	   default = True)
	
	def execute(self, context):
		importOptions = {"game":self.game,"loadLinkedScenes":self.loadLinkedScenes,"loadMeshes":self.loadMeshes,"loadMaterials":self.loadMaterials,"loadUnusedTextures":self.loadUnusedTextures,"loadUnusedProps":self.loadUnusedProps,"useBackfaceCulling":self.useBackfaceCulling,"reloadCachedTextures":self.reloadCachedTextures,"loadLights":self.loadLights,"loadCollisions":self.loadCollisions,"fixClippingDistance":self.fixClippingDistance,"optimizeEEVEESettings":self.optimizeEEVEESettings,"checkChunkFirst":self.checkChunkFirst,"optimizedImport":self.optimizedImport,"lodTarget" : int(self.lodTarget)}
		directory = self.directory
		success = False
		for file in self.files:
			filepath = os.path.join(directory, file.name)
			if os.path.isfile(filepath):
				if ".scn" in filepath.lower():
					fileType = "SCN"
				elif ".user" in filepath.lower():
					fileType = "USR"
				elif ".pfb" in filepath.lower():
					fileType = "PFB"
				
				success = importRSZFile(filepath,fileType,importOptions)
		if success:
			return {"FINISHED"}
		else:
			self.report({"INFO"},"Failed to import RE RSZ. See Window > Toggle System Console for details")
			return {"CANCELLED"}
		
class ExportREScene(bpy.types.Operator, ExportHelper):
	'''Export RE Engine RSZ File'''
	bl_idname = "re_scene.exportfile"
	bl_label = "Export RE RSZ"
	bl_options = {'PRESET'}
	filter_glob: StringProperty(default="*.scn;*;*.user", options={'HIDDEN'})
	filename_ext = ".999"
	game: EnumProperty(
		name="Game",
		description="Choose which game to import from",
		default = "RE4",
		items=[ ("MHRise", "Monster Hunter Rise", ""),
				("RE2RT", "Resident Evil 2 RT", ""),
				("RE4", "Resident Evil 4", ""),
				("DR", "Dead Rising", ""),
			   ]
		
		)
	def execute(self, context):
		if context.active_object.get("~TYPE",None) == "RSZ_SCN_ROOT":
			fileType = "SCN"
			if self.game == "MHWILDS":
				filepath = self.filepath.replace(".999",".21")
			else:
				filepath = self.filepath.replace(".999",".20")
		elif context.active_object.get("~TYPE",None) == "RSZ_USR_ROOT":
			fileType = "USR"
			if self.game == "MHWILDS":
				filepath = self.filepath.replace(".999",".3")
			else:
				filepath = self.filepath.replace(".999",".2")
		elif context.active_object.get("~TYPE",None) == "RSZ_PFB_ROOT":
			fileType = "PFB"
			if self.game == "DR" or self.game == "MHWILDS":
				filepath = self.filepath.replace(".999",".18")
			else:
				filepath = self.filepath.replace(".999",".17")
		else:
			fileType = None
		success = exportRSZFile(context.active_object,filepath,fileType,self.game)
		if success:
			self.report({"INFO"},"Exported RE RSZ successfully.")
		return {"FINISHED"}
	
class ImportRE_MCOL(bpy.types.Operator, ImportHelper):
	'''Import RE Engine Map Collision File'''
	bl_idname = "re_mcol.importfile"
	bl_label = "Import RE MCOL (.mcol.13020)"
	bl_options = {'PRESET', "REGISTER", "UNDO"}
	files : CollectionProperty(
			name="File Path",
			type=OperatorFileListElement,
			)
	directory : StringProperty(
			subtype='DIR_PATH',
			)
	filename_ext = ".mcol.*"
	filter_glob: StringProperty(default="*.mcol.*", options={'HIDDEN'})
	
	clear_scene : BoolProperty(
	   name = "Clear scene before import.",
	   description = "Clears all objects before importing",
	   default = True)
	loadBoundingBoxes : BoolProperty(
	   name = "Load Bounding Boxes",
	   description = "Load mcol bounding boxes",
	   default = False)
	loadBoundingBoxTree : BoolProperty(
	   name = "Load Bounding Box Tree",
	   description = "Load Bounding Box Tree (SLOW)",
	   default = False)
	def execute(self, context):
		importOptions = {"clearScene":self.clear_scene,"loadBoundingBoxes":self.loadBoundingBoxes,"loadBoundingBoxTree":self.loadBoundingBoxTree}
		if os.path.isfile(self.filepath):
				
			success = importMCOLFile(self.filepath,importOptions)
			if success:
				return {"FINISHED"}
		self.report({"INFO"},"Failed to import RE MCOL. See Window > Toggle System Console for details")
		return {"CANCELLED"}
class ExportRE_MCOL(bpy.types.Operator, ExportHelper):
	'''Export RE Engine Map Collision File'''
	bl_idname = "re_mcol.exportfile"
	bl_label = "Export RE MCOL (.mcol.13020)"
	bl_options = {'PRESET'}
	filename_ext = ".13020"
	filter_glob: StringProperty(default="*.mcol*", options={'HIDDEN'})

	def execute(self, context):

		success = exportMCOLFile(self.filepath)
		if success:
			self.report({"INFO"},"Exported RE MCOL successfully.")
		return {"FINISHED"}
# Registration
classes = [
	
	ImportREScene,
	ExportREScene,
	ImportRE_MCOL,
	ExportRE_MCOL,
	RE_MapToolPanelPropertyGroup,
	RSZ_PointLightPropertyGroup,
	RSZ_SpotLightPropertyGroup,
	RSZ_DirectionalLightPropertyGroup,
	RSZ_ObjectPointersGroup,
	RSZ_ObjectGroup,
	OBJECT_PT_RE_MapTools_Object_Panel,
	OBJECT_PT_RE_MapTools_Export_Panel,
	OBJECT_PT_RE_MapTools_Visibility_Panel,
	LIST_UL_RSZ_Pointers,	
	OBJECT_PT_RSZObjectPointersPanel,
	OBJECT_PT_RSZPointLightPanel,
	OBJECT_PT_RSZSpotLightPanel,
	OBJECT_PT_RSZDirectionalLightPanel,
	OBJECT_PT_RE_MapTools_RE4_Panel,
	OBJECT_PT_RSZPresetPanel,
	WM_OT_AddRSZObject,
	WM_OT_AddMeshObject,
	WM_OT_AddPointLightObject,
	WM_OT_AddSpotLightObject,
	WM_OT_AddDirectionalLightObject,
	WM_OT_AddEPVObject,
	WM_OT_ReloadMeshes,
	WM_OT_ReindexTree,
	WM_OT_ExportAllRSZ,
	WM_OT_IncreaseRSZIndex,
	WM_OT_RE4_AddDropItem,
	WM_OT_RE4_EditDropItem,
	WM_OT_RE4_AddNPC,
	WM_OT_RE4_EditNPC,
	WM_OT_OpenPresetFolder,
	WM_OT_SavePreset,
	WM_OT_AddRSZPreset,
	
	ChunkPathPropertyGroup,
	AddItemOperator,
	RemoveItemOperator,
	ReorderItemOperator,
	MESH_UL_ChunkPathListMapEditor,
	REMapToolsPreferences,
	WM_OT_OpenTextureCacheFolder,
	]


def re_scene_import(self, context):
	self.layout.operator(ImportREScene.bl_idname, text="RE RSZ (.scn.20, .user.2, .pfb.17)")
	
def re_scene_export(self, context):
	self.layout.operator(ExportREScene.bl_idname, text="RE RSZ (.scn.20, .user.2, .pfb.17)")

def re_mcol_import(self, context):
	self.layout.operator(ImportRE_MCOL.bl_idname, text="RE MCOL (.mcol.13020)")
	
def re_mcol_export(self, context):
	self.layout.operator(ExportRE_MCOL.bl_idname, text="RE MCOL (.mcol.13020)")
	
def register():
	for classEntry in classes:
		bpy.utils.register_class(classEntry)
	bpy.types.TOPBAR_MT_file_import.append(re_scene_import)
	bpy.types.TOPBAR_MT_file_export.append(re_scene_export)
	bpy.types.TOPBAR_MT_file_import.append(re_mcol_import)
	bpy.types.TOPBAR_MT_file_export.append(re_mcol_export)
	bpy.types.Scene.re_rsz_toolpanel = bpy.props.PointerProperty(type=RE_MapToolPanelPropertyGroup)
	bpy.types.Object.re_rsz_object = bpy.props.PointerProperty(type=RSZ_ObjectGroup)
	bpy.types.Light.re_rsz_pointlight = bpy.props.PointerProperty(type=RSZ_PointLightPropertyGroup)
	bpy.types.Light.re_rsz_spotlight = bpy.props.PointerProperty(type=RSZ_SpotLightPropertyGroup)
	bpy.types.Light.re_rsz_directionallight = bpy.props.PointerProperty(type=RSZ_DirectionalLightPropertyGroup)
def unregister():
	for classEntry in classes:
		bpy.utils.unregister_class(classEntry)
	bpy.types.TOPBAR_MT_file_import.remove(re_scene_import)
	bpy.types.TOPBAR_MT_file_export.remove(re_scene_export)
	bpy.types.TOPBAR_MT_file_import.remove(re_mcol_import)
	bpy.types.TOPBAR_MT_file_export.remove(re_mcol_export)
		
if __name__ == '__main__':
	register()