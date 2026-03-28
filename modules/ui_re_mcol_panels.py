import bpy

from bpy.types import (Panel,
					   Menu,
					   Operator,
					   PropertyGroup,
					   )


def tag_redraw(context, space_type="PROPERTIES", region_type="WINDOW"):
	for window in context.window_manager.windows:
		for area in window.screen.areas:
			if area.spaces[0].type == space_type:
				for region in area.regions:
					if region.type == region_type:
						region.tag_redraw()



class OBJECT_PT_RE_MapTools_Object_Panel(Panel):
	bl_label = "RE RSZ: Object Tools"
	bl_idname = "OBJECT_PT_re_map_tools_object_panel"
	bl_space_type = "VIEW_3D"   
	bl_region_type = "UI"
	bl_category = "RE Map Tools"

	@classmethod
	def poll(self,context):
		return context.active_object is not None

	def draw(self, context):
		
		re_rsz_toolpanel = context.scene.re_rsz_toolpanel
		layout = self.layout
		layout.label(text="Instance Tools")
		layout.separator()
		layout.operator("re_rsz.add_object")
		layout.operator("re_rsz.reindex_tree")
		layout.prop(re_rsz_toolpanel,"indexAmount")
		layout.operator("re_rsz.increase_rsz_index")
		layout.label(text="Mesh Tools")
		layout.separator()
		layout.label(text="Mesh Path:")
		layout.prop(re_rsz_toolpanel,"meshPath")
		layout.operator("re_rsz.add_mesh")
		layout.operator("re_rsz.reload_meshes")
		layout.label(text="Light Tools")
		layout.separator()
		layout.operator("re_rsz.add_point_light")
		layout.operator("re_rsz.add_spot_light")
		layout.operator("re_rsz.add_directional_light")
		layout.label(text="Effect Tools")
		layout.separator()
		layout.label(text="Stage EPV Path:")
		layout.prop(re_rsz_toolpanel,"epvPath")
		layout.operator("re_rsz.add_epv")
	
class OBJECT_PT_RE_MapTools_Export_Panel(Panel):
	bl_label = "RE RSZ: Export"
	bl_idname = "OBJECT_PT_re_map_tools_export_panel"
	bl_space_type = "VIEW_3D"   
	bl_region_type = "UI"
	bl_category = "RE Map Tools"

	@classmethod
	def poll(self,context):
		return context.active_object is not None

	def draw(self, context):
		
		re_rsz_toolpanel = context.scene.re_rsz_toolpanel
		layout = self.layout
		layout.operator("re_rsz.export_all")
		
		
class OBJECT_PT_RE_MapTools_Visibility_Panel(Panel):
	bl_label = "RE RSZ: Visibility"
	bl_idname = "OBJECT_PT_re_map_tools_visibility_panel"
	bl_space_type = "VIEW_3D"   
	bl_region_type = "UI"
	bl_category = "RE Map Tools"

	@classmethod
	def poll(self,context):
		return context.active_object is not None

	def draw(self, context):
		re_rsz_toolpanel = context.scene.re_rsz_toolpanel
		layout = self.layout
		layout.prop(re_rsz_toolpanel,"showGameObjectNames")
		layout.prop(re_rsz_toolpanel,"showRelationLines")

class OBJECT_PT_RSZObjectPointersPanel(Panel):
	bl_label = "RE RSZ Object Pointers"
	bl_idname = "OBJECT_PT_rsz_object_pointer_panel"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_category = "RE RSZ Object Pointers"
	bl_context = "object"

	@classmethod
	def poll(self,context):
		return context and context.object.mode == "OBJECT" and context.active_object.get("TYPE",None) == "RSZ_INSTANCE" or context.active_object.get("TYPE",None) == "RSZ_EXTERNAL_USERDATA"

	def draw(self, context):
		layout = self.layout
		object = context.active_object
		re_rsz_object = object.re_rsz_object
		split = layout.split(factor=0.01)
		col1 = split.column()
		col2 = split.column()
		col2.alignment='RIGHT'
		col2.use_property_split = True
		col2.prop(re_rsz_object,"rszIndex")
		col2.prop(re_rsz_object,"rszObjectPointers")
		
class OBJECT_PT_RSZPointLightPanel(Panel):
	bl_label = "RE RSZ Point Light"
	bl_idname = "OBJECT_PT_rsz_point_light_panel"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_category = "RE RSZ Point Light"
	bl_context = "object"

	@classmethod
	def poll(self,context):
		return context and context.object.mode == "OBJECT" and context.active_object.type == "LIGHT" and context.active_object.get("TYPE",None) == "RSZ_DISPLAY_POINTLIGHT"

	def draw(self, context):
		layout = self.layout
		object = context.active_object
		#group = object.data.re_rsz_pointlight
		group = object.data.re_rsz_pointlight
		split = layout.split(factor=0.01)
		col1 = split.column()
		col2 = split.column()
		col2.alignment='RIGHT'
		col2.use_property_split = True
		col2.prop(group,"Enabled")
		col2.prop(group,"Intensity")
		col2.prop(group,"RenderOutputID")
		col2.prop(group,"Color")
		col2.prop(group,"BlackBodyRadiation")
		col2.prop(group,"Temperature")
		col2.prop(group,"BounceIntensity")
		col2.prop(group,"MinRoughness")
		col2.prop(group,"AOEfficiency")
		col2.prop(group,"ImportantLevel")
		col2.prop(group,"LightingTarget")
		col2.prop(group,"LightBakeOption")
		col2.prop(group,"UsingSameIntensity")
		col2.prop(group,"VolumetricScatteringIntensity")
		col2.prop(group,"Radius")
		col2.prop(group,"InfluenceRadius")
		col2.prop(group,"ReferenceEffectiveRange")
		col2.prop(group,"IlluminanceThreshold")
		col2.prop(group,"ShadowEnable")
		col2.prop(group,"BackGroundShadowEnable")
		col2.prop(group,"ForceShadowCacheEnable")
		col2.prop(group,"ShadowCastFlag")
		col2.prop(group,"ShadowLODBias")
		col2.prop(group,"ShadowNearPlane")
		col2.prop(group,"ShadowVariance")
		col2.prop(group,"ShadowBias")
		col2.prop(group,"ShadowDepthBias")
		col2.prop(group,"ShadowSlopeBias")
		col2.prop(group,"ProjectionTexture")
	
	
class OBJECT_PT_RSZSpotLightPanel(Panel):
	bl_label = "RE RSZ Spot Light"
	bl_idname = "OBJECT_PT_rsz_spot_light_panel"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_category = "RE RSZ Spot Light"
	bl_context = "object"

	@classmethod
	def poll(self,context):
		return context and context.object.mode == "OBJECT" and context.active_object.type == "LIGHT" and context.active_object.get("TYPE",None) == "RSZ_DISPLAY_SPOTLIGHT"

	def draw(self, context):
		layout = self.layout
		object = context.active_object
		#group = object.data.re_rsz_pointlight
		group = object.data.re_rsz_spotlight
		split = layout.split(factor=0.01)
		col1 = split.column()
		col2 = split.column()
		col2.alignment='RIGHT'
		col2.use_property_split = True
		col2.prop(group,"Enabled")
		col2.prop(group,"Intensity")
		col2.prop(group,"RenderOutputID")
		col2.prop(group,"Color")
		col2.prop(group,"BlackBodyRadiation")
		col2.prop(group,"Temperature")
		col2.prop(group,"BounceIntensity")
		col2.prop(group,"MinRoughness")
		col2.prop(group,"AOEfficiency")
		col2.prop(group,"ImportantLevel")
		col2.prop(group,"LightingTarget")
		col2.prop(group,"LightBakeOption")
		col2.prop(group,"UsingSameIntensity")
		col2.prop(group,"VolumetricScatteringIntensity")
		col2.prop(group,"v14")
		col2.prop(group,"Radius")
		col2.prop(group,"InfluenceRadius")
		col2.prop(group,"IlluminanceThreshold")
		col2.prop(group,"Cone")
		col2.prop(group,"Spread")
		col2.prop(group,"Falloff")
		col2.prop(group,"ShadowEnable")
		col2.prop(group,"BackGroundShadowEnable")
		col2.prop(group,"ForceShadowCacheEnable")
		col2.prop(group,"ShadowCastFlag")
		col2.prop(group,"AllowTranslucentShadows")
		col2.prop(group,"ShadowLODBias")
		col2.prop(group,"UniformShadowEnable")
		col2.prop(group,"ShadowNearPlane")
		col2.prop(group,"ShadowVariance")
		col2.prop(group,"ShadowBias")
		col2.prop(group,"ShadowDepthBias")
		col2.prop(group,"ShadowSlopeBias")
		col2.prop(group,"DetailShadow")
		col2.prop(group,"DetailFocusTarget")

class OBJECT_PT_RSZDirectionalLightPanel(Panel):
	bl_label = "RE RSZ Directional Light"
	bl_idname = "OBJECT_PT_rsz_directional_light_panel"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_category = "RE RSZ Directional Light"
	bl_context = "object"

	@classmethod
	def poll(self,context):
		return context and context.object.mode == "OBJECT" and context.active_object.type == "LIGHT" and context.active_object.get("TYPE",None) == "RSZ_DISPLAY_DIRECTIONALLIGHT"

	def draw(self, context):
		layout = self.layout
		object = context.active_object
		#group = object.data.re_rsz_pointlight
		group = object.data.re_rsz_directionallight
		split = layout.split(factor=0.01)
		col1 = split.column()
		col2 = split.column()
		col2.alignment='RIGHT'
		col2.use_property_split = True
		col2.prop(group,"Enabled")
		col2.prop(group,"Intensity")
		col2.prop(group,"Color")
		col2.prop(group,"Direction")
		col2.prop(group,"RenderOutputID")
		
		col2.prop(group,"BlackBodyRadiation")
		col2.prop(group,"Temperature")
		col2.prop(group,"BounceIntensity")
		col2.prop(group,"MinRoughness")
		col2.prop(group,"AOEfficiency")
		col2.prop(group,"ImportantLevel")
		col2.prop(group,"LightingTarget")
		col2.prop(group,"LightBakeOption")
		col2.prop(group,"UsingSameIntensity")
		col2.prop(group,"VolumetricScatteringIntensity")
		
		col2.prop(group,"v15")
		col2.prop(group,"v16")
		col2.prop(group,"v17")
		col2.prop(group,"v18")
		col2.prop(group,"ShadowDistance")
		col2.prop(group,"ShadowDistanceFromBoundary")
		col2.prop(group,"ShadowVariance")
		col2.prop(group,"SoftShadowKernel")
		col2.prop(group,"ShadowBias")
		col2.prop(group,"ShadowCastFlag")
		col2.prop(group,"ShadowDepthBias")
		col2.prop(group,"ShadowSlopeBias")
		col2.prop(group,"ShadowMinimumAreaSize")
		col2.prop(group,"ShadowViewScale")
		col2.prop(group,"SDSMEnable")
		col2.prop(group,"SDFGloup")
		col2.prop(group,"UseSDFShadow")
		col2.prop(group,"CascadeShadowRange")
		col2.prop(group,"SDFShadowRange")
		col2.prop(group,"SDFShadowRayLength")
		col2.prop(group,"SDFShadowMaxStep")
		col2.prop(group,"SDFShadowSoftness")
		col2.prop(group,"SDFCullingCoef")
		col2.prop(group,"Partition")
		col2.prop(group,"CullingScaler")
		col2.prop(group,"MinimumFOV")
		col2.prop(group,"MinimumFarPlane")
		col2.prop(group,"MaximumNearPlane")
		col2.prop(group,"SSTPath")
		col2.prop(group,"v44")
		col2.prop(group,"v45")
		col2.prop(group,"v46")
		col2.prop(group,"AllowTranslucentShadows")
		col2.prop(group,"SSTDitherEnable")
		col2.prop(group,"BakedShadowBias")
		col2.prop(group,"ShadowMapBoundary")
		col2.prop(group,"v51")
		col2.prop(group,"v52")
		col2.prop(group,"v53")
		col2.prop(group,"EnableShadowProjectionTexture")
		col2.prop(group,"ShadowProjectionTexturePath")
		col2.prop(group,"ProjectionTextureDirection")
		col2.prop(group,"ProjectionScale")
		col2.prop(group,"ProjectionOffset")
		col2.prop(group,"ScrollSpeed")