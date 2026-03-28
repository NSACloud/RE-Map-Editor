#Author: NSA Cloud
import bpy
from bpy.props import (StringProperty,
					   BoolProperty,
					   IntProperty,
					   FloatProperty,
					   FloatVectorProperty,
					   IntVectorProperty,
					   EnumProperty,
					   PointerProperty,
					   CollectionProperty
					   )
from math import radians
from .re_rsz_presets import reloadPresets
def update_RelationLinesVis(self, context):
	bpy.context.space_data.overlay.show_relationship_lines = self.showRelationLines

def update_GameObjectNameVis(self, context):
	for obj in bpy.data.objects:
		if obj.get("~instanceType",None) == "via.GameObject":
			obj.show_name = self.showGameObjectNames

def update_DisplayMeshVis(self, context):
	for obj in bpy.data.objects:
		if obj.get("~TYPE",None) == "RSZ_DISPLAY_MESH":
			obj.hide_viewport = not self.showDisplayMeshes

def update_CollisionVis(self, context):
	if bpy.data.collections.get("MCOLData") != None:
		for obj in bpy.data.collections["MCOLData"].objects:
			if obj.get("~TYPE",None) == "MCOL_MESH":
				obj.hide_viewport = not self.showCollisions

def update_CollisionWireframe(self, context):
	if bpy.data.collections.get("MCOLData") != None:
		for obj in bpy.data.collections["MCOLData"].objects:
			if obj.get("~TYPE",None) == "MCOL_MESH":
				if self.collisionWireframe:
					obj.display_type = "WIRE"
				else:
					obj.display_type = "TEXTURED"

def updateRSZIndex(self,context):
	obj = self.id_data
	objType = obj.get("~TYPE",None)
	
	if objType == "RSZ_INSTANCE" or objType == "RSZ_EXTERNAL_USERDATA":
		instanceType = obj.get("~instanceType",None)
		if instanceType == "via.GameObject":
			name = str(obj.re_rsz_object.rszIndex).zfill(3)+"-"+str(obj["gameObjectName"])+" ("+instanceType+")"
		elif instanceType == "via.Folder":
			name = str(obj.re_rsz_object.rszIndex).zfill(3)+"-"+str(obj["folderName"])+" ("+instanceType+")"	
		elif objType == "RSZ_EXTERNAL_USERDATA":
			name = str(obj.re_rsz_object.rszIndex).zfill(3)+"-( EXTERNAL "+instanceType+")"
		else:
			if instanceType == None:
				print(obj.name)
			name = str(obj.re_rsz_object.rszIndex).zfill(3)+"-("+instanceType+")"
		obj.name = name
def updateField(self,context,prop,lightType):#Change attributes on the instance object when the properties on the display object are changed
	#print(prop)
	if lightType == "POINT":
		obj = self.id_data.re_rsz_pointlight.lightObject
	elif lightType == "SPOT":
		obj = self.id_data.re_rsz_spotlight.lightObject
	elif lightType == "SUN":
		obj = self.id_data.re_rsz_directionallight.lightObject
		skyNode = bpy.data.worlds["World"].node_tree.nodes.get("Sky Texture",None)
		
	if obj != None and obj.parent != None:
		propValue = getattr(self,prop)
		obj.parent[prop] = propValue
		if prop == "Color":#Set color of point light object
			try:
				self.id_data.color = propValue[0:3]
			except:
				self.id_data.color = propValue[0:2]
		elif prop == "Intensity":#Set intensity of the light object
			self.id_data.energy = propValue * .0000025
		elif prop == "Strength":#Set intensity of the light object
			self.id_data.energy = propValue * .000025
		elif prop == "Cone":#Set intensity of the light object
			self.id_data.spot_size = radians(propValue)
		elif prop == "Radius":#Set intensity of the light object
			pass	
			#self.id_data.shadow_soft_size = propValue
		elif prop == "ReferenceEffectiveRange":
			self.id_data.cutoff_distance = propValue
		elif prop == "Direction":
			obj.parent.rotation_euler = propValue
			if skyNode != None and skyNode.sky_type == "PREETHAM":
				skyNode.sun_direction = propValue
		#obj[self.name] = 1


class RE_MapToolPanelPropertyGroup(bpy.types.PropertyGroup):
	
	def getRSZPresets(self,context):
		return reloadPresets(self.game)
	game: EnumProperty(
		name="Game",
		description="Choose which game you're editing. This will affect how RSZ instances are created",
		default = "RE4",
		items=[ ("MHRise", "Monster Hunter Rise", ""),
				("RE2RT", "Resident Evil 2 RT", ""),
				("RE4", "Resident Evil 4", ""),
			   ]
		
		)
	rszPresets: EnumProperty(
		name="",
		description="Set preset to be used by Add RSZ Preset button",
		items= getRSZPresets
		)
	meshPath: StringProperty(
		name="",
		description="Set the path to import the mesh from",
		subtype="FILE_PATH"
	)
	epvPath: StringProperty(
		name="",
		description="Set the path to import the epv from",
		subtype="FILE_PATH"
	)
	showGameObjectNames: BoolProperty(
		name="Show Game Object Names",
		description="Show the names of game objects in the viewport",
		default = True,
		update = update_GameObjectNameVis
	)
	showRelationLines: BoolProperty(
		name="Show Relation Lines",
		description="Show lines indicating object parents. Recommended to disable since they can be very obtrusive with many objects",
		default = True,
		update = update_RelationLinesVis,
	)
	showDisplayMeshes: BoolProperty(
		name="Show Meshes",
		description="Show display meshes",
		default = True,
		update = update_DisplayMeshVis,
	)
	showCollisions: BoolProperty(
		name="Show Collisions",
		description="Show collision meshes",
		default = True,
		update = update_CollisionVis,
	)
	collisionWireframe: BoolProperty(
		name="Wireframe Collision",
		description="Show collisions as wireframe",
		default = True,
		update = update_CollisionWireframe,
	)
	indexAmount: IntProperty(
		name = "Amount",
		description = "Amount to increase RSZ indices of selected objects when pressing increase RSZ index",
		)
	re4ItemSCNRoot: StringProperty(
		name = "SCN",
		description = "The SCN_ROOT object the item should belong to",
		default = "",
		)
	re4ItemUSRRoot: StringProperty(
		name = "USR",
		description = "The USR_ROOT object containing the item save data table",
		default = "",
		)
	chainGroupBObject: StringProperty(
		name = "Chain Group B",
		description = "Chain Group B",#TODO Add description
		default = "",
		)
class RSZ_ObjectPointersGroup(bpy.types.PropertyGroup):
	fieldName: StringProperty(
		name = "Field Name",
		description = "Name of object index field on an RSZ instance object",
		default = "",
		)
	targetObject: PointerProperty(
		type=bpy.types.Object,
		name = "Target Object",
		description = "Object that the field name points to, used to keep track of shifting indices",
		)

class RSZ_ObjectGroup(bpy.types.PropertyGroup):
	rszIndex: IntProperty(
		name = "RSZ Instance Index",
		description = "Index of RSZ instance, used for determining RSZ structure. Set automatically. Do not change unless you know what you're doing",
		update = updateRSZIndex
		)
	activeIndex: IntProperty(
		name = "ObjectPointerListIndex",
		description = "Selected index in list",
		)
	rszObjectPointers: CollectionProperty(
		name = "RSZ Object Pointers",
		description = "",
		type=RSZ_ObjectPointersGroup
		)


class RSZ_PointLightPropertyGroup(bpy.types.PropertyGroup):
	lightObject: PointerProperty(
		type=bpy.types.Object,
		name = "Light Object",
		)
	
	Enabled: BoolProperty(
		name = "Enabled",
		description = "",
		update = lambda s, c: updateField(s, c, "Enabled","POINT"),
		)
	Intensity: FloatProperty(
		name = "Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "Intensity","POINT"),
		)
	RenderOutputID: IntProperty(
		name = "Render Output ID",
		description = "",
		update = lambda s, c: updateField(s, c, "RenderOutputID","POINT"),
		)
	Color: FloatVectorProperty(
		name = "Color",
		description = "",
		subtype="COLOR",
		size = 4,
		update = lambda s, c: updateField(s, c, "Color","POINT"),
		)
	"""
	BlackBodyRadiation: BoolProperty(
		name = "Black Body Radiation",
		description = "",
		update = lambda s, c: updateField(s, c, "BlackBodyRadiation","POINT"),
		)
	"""
	Temperature: FloatProperty(
		name = "Temperature",
		description = "",
		update = lambda s, c: updateField(s, c, "Temperature","POINT"),
		)
	"""
	BounceIntensity: FloatProperty(
		name = "Bounce Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "BounceIntensity","POINT"),
		)
	MinRoughness: FloatProperty(
		name = "Min Roughness",
		description = "",
		update = lambda s, c: updateField(s, c, "MinRoughness","POINT"),
		)
	AOEfficiency: FloatProperty(
		name = "AO Efficiency",
		description = "",
		update = lambda s, c: updateField(s, c, "AOEfficiency","POINT"),
		)
	ImportantLevel: IntProperty(
		name = "Important Level",
		description = "",
		update = lambda s, c: updateField(s, c, "ImportantLevel","POINT"),
		)
	LightingTarget: IntProperty(
		name = "Lighting Target",
		description = "",
		update = lambda s, c: updateField(s, c, "LightingTarget","POINT"),
		)
	LightBakeOption: IntProperty(
		name = "Light Bake Option",
		description = "",
		update = lambda s, c: updateField(s, c, "LightBakeOption","POINT"),
		)
	UsingSameIntensity: IntProperty(
		name = "Using Same Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "UsingSameIntensity","POINT"),
		)
	
	VolumetricScatteringIntensity: FloatProperty(
		name = "Volumetric Scattering Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "VolumetricScatteringIntensity","POINT"),
		)
	"""
	Radius: FloatProperty(
		name = "Radius",
		description = "",
		update = lambda s, c: updateField(s, c, "Radius","POINT"),
		)
	"""
	InfluenceRadius: FloatProperty(
		name = "Influence Radius",
		description = "",
		update = lambda s, c: updateField(s, c, "InfluenceRadius","POINT"),
		)
	"""
	ReferenceEffectiveRange: FloatProperty(
		name = "Reference Effective Range",
		description = "",
		update = lambda s, c: updateField(s, c, "ReferenceEffectiveRange","POINT"),
		)
	IlluminanceThreshold: FloatProperty(
		name = "Illuminance Threshold",
		description = "",
		update = lambda s, c: updateField(s, c, "IlluminanceThreshold","POINT"),
		)
	"""
	ShadowEnable: BoolProperty(
		name = "Shadow Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowEnable","POINT"),
		)
	BackGroundShadowEnable: BoolProperty(
		name = "BackGround Shadow Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "BackGroundShadowEnable","POINT"),
		)
	ForceShadowCacheEnable: BoolProperty(
		name = "Force Shadow Cache Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "ForceShadowCacheEnable","POINT"),
		)
	ShadowCastFlag: IntProperty(
		name = "Shadow Cast Flag",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowCastFlag","POINT"),
		)
	ShadowLODBias: IntProperty(
		name = "Shadow LOD Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowLODBias","POINT"),
		)
	ShadowNearPlane: FloatProperty(
		name = "Shadow Near Plane",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowNearPlane","POINT"),
		)
	ShadowVariance: FloatProperty(
		name = "Shadow Variance",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowVariance","POINT"),
		)
	ShadowBias: FloatProperty(
		name = "Shadow Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowBias","POINT"),
		)
	ShadowDepthBias: FloatProperty(
		name = "Shadow Depth Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowDepthBias","POINT"),
		)
	ShadowSlopeBias: FloatProperty(
		name = "Shadow Slope Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowSlopeBias","POINT"),
		)
	ProjectionTexture: StringProperty(
		name = "Projection Texture",
		description = "",
		update = lambda s, c: updateField(s, c, "ProjectionTexture","POINT"),
		)
	"""

class RSZ_SpotLightPropertyGroup(bpy.types.PropertyGroup):
	lightObject: PointerProperty(
		type=bpy.types.Object,
		name = "Light Object",
		)
	
	Enabled: BoolProperty(
		name = "Enabled",
		description = "",
		update = lambda s, c: updateField(s, c, "Enabled","SPOT"),
		)
	Intensity: FloatProperty(
		name = "Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "Intensity","SPOT"),
		)
	RenderOutputID: IntProperty(
		name = "RenderOutputID",
		description = "",
		update = lambda s, c: updateField(s, c, "RenderOutputID","SPOT"),
		)
	Color: FloatVectorProperty(
		name = "Color",
		description = "",
		subtype = "COLOR",
		size = 4,
		update = lambda s, c: updateField(s, c, "Color","SPOT"),
		)
	"""
	BlackBodyRadiation: BoolProperty(
		name = "Black Body Radiation",
		description = "",
		update = lambda s, c: updateField(s, c, "BlackBodyRadiation","SPOT"),
		)
	"""
	Temperature: FloatProperty(
		name = "Temperature",
		description = "",
		update = lambda s, c: updateField(s, c, "Temperature","SPOT"),
		)
	"""
	BounceIntensity: FloatProperty(
		name = "Bounce Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "BounceIntensity","SPOT"),
		)
	
	MinRoughness: FloatProperty(
		name = "Min Roughness",
		description = "",
		update = lambda s, c: updateField(s, c, "MinRoughness","SPOT"),
		)
	AOEfficiency: FloatProperty(
		name = "AO Efficiency",
		description = "",
		update = lambda s, c: updateField(s, c, "AOEfficiency","SPOT"),
		)
	ImportantLevel: IntProperty(
		name = "Important Level",
		description = "",
		update = lambda s, c: updateField(s, c, "ImportantLevel","SPOT"),
		)
	LightingTarget: IntProperty(
		name = "Lighting Target",
		description = "",
		update = lambda s, c: updateField(s, c, "LightingTarget","SPOT"),
		)
	LightBakeOption: IntProperty(
		name = "Light Bake Option",
		description = "",
		update = lambda s, c: updateField(s, c, "LightBakeOption","SPOT"),
		)
	UsingSameIntensity: IntProperty(
		name = "Using Same Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "UsingSameIntensity","SPOT"),
		)
	VolumetricScatteringIntensity: FloatProperty(
		name = "Volumetric Scattering Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "VolumetricScatteringIntensity","SPOT"),
		)
	v14: IntProperty(
		name = "v14",
		description = "",
		update = lambda s, c: updateField(s, c, "v14","SPOT"),
		)
	"""
	Radius: FloatProperty(
		name = "Radius",
		description = "",
		update = lambda s, c: updateField(s, c, "Radius","SPOT"),
		)
	"""
	InfluenceRadius: FloatProperty(
		name = "Influence Radius",
		description = "",
		update = lambda s, c: updateField(s, c, "InfluenceRadius","SPOT"),
		)
	"""
	IlluminanceThreshold: FloatProperty(
		name = "Illuminance Threshold",
		description = "",
		update = lambda s, c: updateField(s, c, "IlluminanceThreshold","SPOT"),
		)
	Cone: FloatProperty(
		name = "Cone",
		description = "",
		update = lambda s, c: updateField(s, c, "Cone","SPOT"),
		)
	Spread: FloatProperty(
		name = "Spread",
		description = "",
		update = lambda s, c: updateField(s, c, "Spread","SPOT"),
		)
	Falloff: FloatProperty(
		name = "Falloff",
		description = "",
		update = lambda s, c: updateField(s, c, "Falloff","SPOT"),
		)
	"""
	ShadowEnable: BoolProperty(
		name = "Shadow Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowEnable","SPOT"),
		)
	BackGroundShadowEnable: BoolProperty(
		name = "BackGround Shadow Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "BackGroundShadowEnable","SPOT"),
		)
	ForceShadowCacheEnable: BoolProperty(
		name = "Force ShadowCache Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "ForceShadowCacheEnable","SPOT"),
		)
	ShadowCastFlag: IntProperty(
		name = "Shadow Cast Flag",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowCastFlag","SPOT"),
		)
	AllowTranslucentShadows: BoolProperty(
		name = "Allow Translucent Shadows",
		description = "",
		update = lambda s, c: updateField(s, c, "AllowTranslucentShadows","SPOT"),
		)
	ShadowLODBias: IntProperty(
		name = "Shadow LOD Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowLODBias","SPOT"),
		)
	UniformShadowEnable: BoolProperty(
		name = "Uniform Shadow Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "UniformShadowEnable","SPOT"),
		)
	ShadowNearPlane: FloatProperty(
		name = "Shadow Near Plane",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowNearPlane","SPOT"),
		)
	ShadowVariance: FloatProperty(
		name = "Shadow Variance",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowVariance","SPOT"),
		)
	ShadowBias: FloatProperty(
		name = "Shadow Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowBias","SPOT"),
		)
	ShadowDepthBias: FloatProperty(
		name = "Shadow Depth Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowDepthBias","SPOT"),
		)
	ShadowSlopeBias: FloatProperty(
		name = "Shadow Slope Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowSlopeBias","SPOT"),
		)
	DetailShadow: FloatProperty(
		name = "Detail Shadow",
		description = "",
		update = lambda s, c: updateField(s, c, "DetailShadow","SPOT"),
		)
	DetailFocusTarget: StringProperty(
		name = "Detail Focus Target",
		description = "",
		update = lambda s, c: updateField(s, c, "DetailFocusTarget","SPOT"),
		)
	"""

class RSZ_DirectionalLightPropertyGroup(bpy.types.PropertyGroup):
	lightObject: PointerProperty(
		type=bpy.types.Object,
		name = "Light Object",
		)
	
	Enabled: BoolProperty(
		name = "Enabled",
		description = "",
		update = lambda s, c: updateField(s, c, "Enabled","SUN"),
		)
	Intensity: FloatProperty(
		name = "Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "Intensity","SUN"),
		)
	RenderOutputID: IntProperty(
		name = "Render Output ID",
		description = "",
		update = lambda s, c: updateField(s, c, "RenderOutputID","SUN"),
		)
	Color: FloatVectorProperty(
		name = "Color",
		description = "",
		subtype="COLOR",
		size = 4,
		update = lambda s, c: updateField(s, c, "Color","SUN"),
		)
	BlackBodyRadiation: BoolProperty(
		name = "Black Body Radiation",
		description = "",
		update = lambda s, c: updateField(s, c, "BlackBodyRadiation","SUN"),
		)
	Temperature: FloatProperty(
		name = "Temperature",
		description = "",
		update = lambda s, c: updateField(s, c, "Temperature","SUN"),
		)
	BounceIntensity: FloatProperty(
		name = "Bounce Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "BounceIntensity","SUN"),
		)
	MinRoughness: FloatProperty(
		name = "Min Roughness",
		description = "",
		update = lambda s, c: updateField(s, c, "MinRoughness","SUN"),
		)
	AOEfficiency: IntProperty(
		name = "AO Efficiency",
		description = "",
		update = lambda s, c: updateField(s, c, "AOEfficiency","SUN"),
		)
	ImportantLevel: IntProperty(
		name = "Important Level",
		description = "",
		update = lambda s, c: updateField(s, c, "ImportantLevel","SUN"),
		)
	LightingTarget: IntProperty(
		name = "Lighting Target",
		description = "",
		update = lambda s, c: updateField(s, c, "LightingTarget","SUN"),
		)
	LightBakeOption: IntProperty(
		name = "Light Bake Option",
		description = "",
		update = lambda s, c: updateField(s, c, "LightBakeOption","SUN"),
		)
	UsingSameIntensity: IntProperty(
		name = "Using Same Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "UsingSameIntensity","SUN"),
		)
	VolumetricScatteringIntensity: FloatProperty(
		name = "Volumetric Scattering Intensity",
		description = "",
		update = lambda s, c: updateField(s, c, "VolumetricScatteringIntensity","SUN"),
		)
	Direction: FloatVectorProperty(
		name = "Direction",
		description = "",
		subtype = "EULER",
		update = lambda s, c: updateField(s, c, "Direction","SUN"),
		)
	v15: BoolProperty(
		name = "v15",
		description = "",
		update = lambda s, c: updateField(s, c, "v15","SUN"),
		)
	v16: BoolProperty(
		name = "v16",
		description = "",
		update = lambda s, c: updateField(s, c, "v16","SUN"),
		)
	v17: BoolProperty(
		name = "v17",
		description = "",
		update = lambda s, c: updateField(s, c, "v17","SUN"),
		)
	v18: IntProperty(
		name = "v18",
		description = "",
		update = lambda s, c: updateField(s, c, "v18","SUN"),
		)
	ShadowDistance: FloatProperty(
		name = "Shadow Distance",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowDistance","SUN"),
		)
	ShadowDistanceFromBoundary: BoolProperty(
		name = "Shadow Distance From Boundary",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowDistanceFromBoundary","SUN"),
		)
	ShadowVariance: FloatProperty(
		name = "Shadow Variance",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowVariance","SUN"),
		)
	SoftShadowKernel: IntProperty(
		name = "Soft Shadow Kernel",
		description = "",
		update = lambda s, c: updateField(s, c, "SoftShadowKernel","SUN"),
		)
	ShadowBias: FloatProperty(
		name = "Shadow Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowBias","SUN"),
		)
	ShadowCastFlag: IntProperty(
		name = "Shadow Cast Flag",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowCastFlag","SUN"),
		)
	ShadowDepthBias: FloatProperty(
		name = "Shadow Depth Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowDepthBias","SUN"),
		)
	ShadowSlopeBias: FloatProperty(
		name = "Shadow Slope Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowSlopeBias","SUN"),
		)
	ShadowMinimumAreaSize: FloatProperty(
		name = "Shadow Minimum Area Size",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowMinimumAreaSize","SUN"),
		)
	ShadowViewScale: FloatVectorProperty(
		name = "Shadow View Scale",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowViewScale","SUN"),
		)
	SDSMEnable: BoolProperty(
		name = "SDSM Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "SDSMEnable","SUN"),
		)
	SDFGloup: BoolProperty(
		name = "SDF Gloup",
		description = "",
		update = lambda s, c: updateField(s, c, "SDFGloup","SUN"),
		)
	UseSDFShadow: BoolProperty(
		name = "Use SDF Shadow",
		description = "",
		update = lambda s, c: updateField(s, c, "UseSDFShadow","SUN"),
		)
	CascadeShadowRange: FloatProperty(
		name = "Cascade Shadow Range",
		description = "",
		update = lambda s, c: updateField(s, c, "CascadeShadowRange","SUN"),
		)
	SDFShadowRange: FloatProperty(
		name = "SDF Shadow Range",
		description = "",
		update = lambda s, c: updateField(s, c, "SDFShadowRange","SUN"),
		)
	SDFShadowRayLength: FloatProperty(
		name = "SDF Shadow Ray Length",
		description = "",
		update = lambda s, c: updateField(s, c, "SDFShadowRayLength","SUN"),
		)
	SDFShadowMaxStep: IntProperty(
		name = "SDF Shadow Max Step",
		description = "",
		update = lambda s, c: updateField(s, c, "SDFShadowMaxStep","SUN"),
		)
	SDFShadowSoftness: IntProperty(
		name = "SDF Shadow Softness",
		description = "",
		update = lambda s, c: updateField(s, c, "SDFShadowSoftness","SUN"),
		)
	SDFCullingCoef: IntProperty(
		name = "SDF Culling Coef",
		description = "",
		update = lambda s, c: updateField(s, c, "SDFCullingCoef","SUN"),
		)
	Partition: FloatVectorProperty(
		name = "Partition",
		size=4,
		description = "",
		update = lambda s, c: updateField(s, c, "Partition","SUN"),
		)
	CullingScaler: FloatVectorProperty(
		name = "Culling Scaler",
		description = "",
		update = lambda s, c: updateField(s, c, "CullingScaler","SUN"),
		)
	MinimumFOV: FloatProperty(
		name = "Minimum FOV",
		description = "",
		update = lambda s, c: updateField(s, c, "MinimumFOV","SUN"),
		)
	MinimumFarPlane: IntProperty(
		name = "Minimum Far Plane",
		description = "",
		update = lambda s, c: updateField(s, c, "MinimumFarPlane","SUN"),
		)
	MaximumNearPlane: IntProperty(
		name = "Maximum Near Plane",
		description = "",
		update = lambda s, c: updateField(s, c, "MaximumNearPlane","SUN"),
		)
	SSTPath: StringProperty(
		name = "SST Path",
		description = "",
		update = lambda s, c: updateField(s, c, "SSTPath","SUN"),
		)
	v44: BoolProperty(
		name = "v44",
		description = "",
		update = lambda s, c: updateField(s, c, "v44","SUN"),
		)
	v45: IntProperty(
		name = "v45",
		description = "",
		update = lambda s, c: updateField(s, c, "v45","SUN"),
		)
	v46: IntProperty(
		name = "v46",
		description = "",
		update = lambda s, c: updateField(s, c, "v46","SUN"),
		)
	AllowTranslucentShadows: BoolProperty(
		name = "Allow Translucent Shadows",
		description = "",
		update = lambda s, c: updateField(s, c, "AllowTranslucentShadows","SUN"),
		)
	SSTDitherEnable: BoolProperty(
		name = "SST Dither Enable",
		description = "",
		update = lambda s, c: updateField(s, c, "SSTDitherEnable","SUN"),
		)
	BakedShadowBias: FloatProperty(
		name = "Baked Shadow Bias",
		description = "",
		update = lambda s, c: updateField(s, c, "BakedShadowBias","SUN"),
		)
	ShadowMapBoundary: IntProperty(
		name = "Shadow Map Boundary",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowMapBoundary","SUN"),
		)
	v51: IntProperty(
		name = "v51",
		description = "",
		update = lambda s, c: updateField(s, c, "v51","SUN"),
		)
	v52: FloatVectorProperty(
		name = "v52",
		description = "",
		size = 20,
		update = lambda s, c: updateField(s, c, "v52","SUN"),
		)
	v53: StringProperty(
		name = "v53",
		description = "",
		update = lambda s, c: updateField(s, c, "v53","SUN"),
		)
	EnableShadowProjectionTexture: BoolProperty(
		name = "Enable Shadow Projection Texture",
		description = "",
		update = lambda s, c: updateField(s, c, "EnableShadowProjectionTexture","SUN"),
		)
	ShadowProjectionTexturePath: StringProperty(
		name = "Shadow Projection Texture Path",
		description = "",
		update = lambda s, c: updateField(s, c, "ShadowProjectionTexturePath","SUN"),
		)
	ProjectionTextureDirection: FloatVectorProperty(
		name = "Projection Texture Direction",
		description = "",
		size = 4,
		update = lambda s, c: updateField(s, c, "ProjectionTextureDirection","SUN"),
		)
	ProjectionScale: FloatVectorProperty(
		name = "Projection Scale",
		description = "",
		update = lambda s, c: updateField(s, c, "ProjectionScale","SUN"),
		)
	ProjectionOffset: IntVectorProperty(
		name = "Projection Offset",
		description = "",
		size = 2,
		update = lambda s, c: updateField(s, c, "ProjectionOffset","SUN"),
		)
	ScrollSpeed: IntVectorProperty(
		name = "Scroll Speed",
		description = "",
		size =2,
		update = lambda s, c: updateField(s, c, "ScrollSpeed","SUN"),
		)

	