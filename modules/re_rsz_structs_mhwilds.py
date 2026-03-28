from .re_rsz_datatypes import InstanceInfo,RSZVariable,RSZInstance

class System_Collections_Generic_Dictionary2via_GameObjectvia_mat4(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "System.Collections.Generic.Dictionary`2<via.GameObject,via.mat4>",typeIDHash=0x77d39618,CRC=0xc0f233f2,isObject = True,tagList=[])
		self.fields = {
		}

class ace_BaseColorCorrectRequester(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.BaseColorCorrectRequester",typeIDHash=0x2565f7a8,CRC=0x64b41717,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ColorCubeGroupList":RSZVariable(name="_ColorCubeGroupList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_BaseColorCorrectRequester_cColorCubeGroupElement(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.BaseColorCorrectRequester.cColorCubeGroupElement",typeIDHash=0x7aeee0a,CRC=0xbb890e7d,isObject = True,tagList=[])
		self.fields = {
		"_Name":RSZVariable(name="_Name",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_BlendRate":RSZVariable(name="_BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ColorCubeLayerList":RSZVariable(name="_ColorCubeLayerList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_BaseColorCorrectRequester_cColorCubeLayerElement(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.BaseColorCorrectRequester.cColorCubeLayerElement",typeIDHash=0x988b3c73,CRC=0x1fd8557f,isObject = True,tagList=[])
		self.fields = {
		"_Label":RSZVariable(name="_Label",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_BlendRate":RSZVariable(name="_BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ColorCube":RSZVariable(name="_ColorCube",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class ace_CCSPassThrough(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.CCSPassThrough",typeIDHash=0xbf7dd557,CRC=0xc750af84,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_CCSPassThroughSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.CCSPassThroughSetting",typeIDHash=0xb2472477,CRC=0x71da5de0,isObject = True,tagList=[])
		self.fields = {
		"_InstanceNum":RSZVariable(name="_InstanceNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_ResultNum":RSZVariable(name="_ResultNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_CharacterTimelineEventActorBase_PosWarpData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.CharacterTimelineEventActorBase.PosWarpData",typeIDHash=0x258c972d,CRC=0xef0c3cc9,isObject = True,tagList=[])
		self.fields = {
		"Type":RSZVariable(name="Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT_Pos__HasValue":RSZVariable(name="STRUCT_Pos__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT_Pos__Value":RSZVariable(name="STRUCT_Pos__Value",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"STRUCT_Rot__HasValue":RSZVariable(name="STRUCT_Rot__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT_Rot__Value":RSZVariable(name="STRUCT_Rot__Value",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		}

class ace_CharacterTimelineEventActorBase_cParamEndMotion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.CharacterTimelineEventActorBase.cParamEndMotion",typeIDHash=0x3785fb4f,CRC=0x617158c2,isObject = True,tagList=[])
		self.fields = {
		"MsgEndMotionSet":RSZVariable(name="MsgEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Frame":RSZVariable(name="Frame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_CharacterTimelineEventActorBase_cParamStartMotion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.CharacterTimelineEventActorBase.cParamStartMotion",typeIDHash=0x67c065f5,CRC=0xe0c748f7,isObject = True,tagList=[])
		self.fields = {
		"MsgStartMotionSet":RSZVariable(name="MsgStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Frame":RSZVariable(name="Frame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_ColliderPool(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.ColliderPool",typeIDHash=0xe617084e,CRC=0x59ca7e2e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_DynamicExposure(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.DynamicExposure",typeIDHash=0x15d67bc6,CRC=0x4e2ded63,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_IsEnable":RSZVariable(name="_IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DynamicEVCurve":RSZVariable(name="_DynamicEVCurve",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_EventMovieHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.EventMovieHolder",typeIDHash=0x9cd525d7,CRC=0x26c846aa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID":RSZVariable(name="_EventID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_MovieHolder":RSZVariable(name="_MovieHolder",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class ace_EventSceneCollection(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.EventSceneCollection",typeIDHash=0x246f01c6,CRC=0x1c0a2ae1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_CatalogName":RSZVariable(name="_CatalogName",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_GUIFade(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.GUIFade",typeIDHash=0x1ec85cad,CRC=0x7270893b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_UseGUIBuffer":RSZVariable(name="_UseGUIBuffer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class ace_GameMessageReceiver(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.GameMessageReceiver",typeIDHash=0xa070bc7f,CRC=0x5c24cdfe,isObject = True,tagList=[])
		self.fields = {
		}

class ace_GameObjectStatusSetManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.GameObjectStatusSetManager",typeIDHash=0xffd6b669,CRC=0x71cb4978,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_GlobalTimeZoneManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.GlobalTimeZoneManager",typeIDHash=0x71eea647,CRC=0xb9ba6e11,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GlobalTimeZoneData":RSZVariable(name="_GlobalTimeZoneData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlaySpeed":RSZVariable(name="_PlaySpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_PlayType":RSZVariable(name="_PlayType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_CurrentFrame":RSZVariable(name="_CurrentFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ArrivalTime":RSZVariable(name="_ArrivalTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"OnPropertyChangeCurrentTimeZone":RSZVariable(name="OnPropertyChangeCurrentTimeZone",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Hour":RSZVariable(name="_Hour",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Minute":RSZVariable(name="_Minute",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Second":RSZVariable(name="_Second",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ArrivalHour":RSZVariable(name="_ArrivalHour",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ArrivalMinute":RSZVariable(name="_ArrivalMinute",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ArrivalSecond":RSZVariable(name="_ArrivalSecond",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_JointConstraintsController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.JointConstraintsController",typeIDHash=0xa07abc8b,CRC=0x37ec002c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_LightController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.LightController",typeIDHash=0x6d89325c,CRC=0xffcda778,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ControlType":RSZVariable(name="_ControlType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_isStoreInitParam":RSZVariable(name="_isStoreInitParam",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsRestoreAtDestruction":RSZVariable(name="_IsRestoreAtDestruction",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class ace_LogViewerService(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.LogViewerService",typeIDHash=0x21bf0102,CRC=0x7716434,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_MeshBoundary(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.MeshBoundary",typeIDHash=0x869a0bfa,CRC=0xfe39b587,isObject = True,tagList=[])
		self.fields = {
		}

class ace_MouseKeyboardManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.MouseKeyboardManager",typeIDHash=0x151f0bc5,CRC=0xd38002eb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PadManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PadManager",typeIDHash=0xf17eae79,CRC=0x43d403e8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GamePlayerAssignInitializer":RSZVariable(name="_GamePlayerAssignInitializer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_PointedSpaceSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PointedSpaceSetting",typeIDHash=0xce827faf,CRC=0xbafaabd2,isObject = True,tagList=[])
		self.fields = {
		}

class ace_PostEffectTrackBaseColorCorrect(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackBaseColorCorrect",typeIDHash=0xd471ba5,CRC=0x447fb06,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackColorCollect(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackColorCollect",typeIDHash=0x2561a90b,CRC=0x2d0d83e9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackDOFCirclar(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackDOFCirclar",typeIDHash=0xf4303243,CRC=0x7a1c42a4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackDOFDefault(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackDOFDefault",typeIDHash=0x1f2794ba,CRC=0x9f8e568f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackDOFTessellation(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackDOFTessellation",typeIDHash=0xa0606117,CRC=0xf6412a03,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackDirtMask(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackDirtMask",typeIDHash=0x5d6177c2,CRC=0xc90c0942,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackDynamicRangeConversion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackDynamicRangeConversion",typeIDHash=0x37149b49,CRC=0xab85aac9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackEcho(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackEcho",typeIDHash=0x1e64cd4f,CRC=0x762ba15c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackExposure(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackExposure",typeIDHash=0x76b9d4e3,CRC=0x5963b116,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackExtraColorCorrect(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackExtraColorCorrect",typeIDHash=0x5b94ac6b,CRC=0x20845294,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackFilmGrain(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackFilmGrain",typeIDHash=0x92070a0e,CRC=0x7b75112e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackFog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackFog",typeIDHash=0x66219872,CRC=0xd5af8b8c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackGeometryAO(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackGeometryAO",typeIDHash=0xae0cf3d1,CRC=0x926b79fc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackHazeFilter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackHazeFilter",typeIDHash=0x8f00ae9a,CRC=0x78a0608c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackImagePlane(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackImagePlane",typeIDHash=0x9fbd884e,CRC=0xa103b015,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackLocalExposure(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackLocalExposure",typeIDHash=0xe7921fd2,CRC=0x7c1c912f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackMotionBlur(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackMotionBlur",typeIDHash=0x8ae7fe82,CRC=0xb5a150df,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackPanini(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackPanini",typeIDHash=0x9368ded8,CRC=0x8e18a655,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackRadialBlur(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackRadialBlur",typeIDHash=0x13ffa751,CRC=0xdac1b2a2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackSSAO(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackSSAO",typeIDHash=0x792ecae6,CRC=0x198d37ee,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackSSR(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackSSR",typeIDHash=0xbc67457,CRC=0x4cb08b16,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackSoftBloom(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackSoftBloom",typeIDHash=0x9023ecd0,CRC=0xd42f04a0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackTemporalAA(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackTemporalAA",typeIDHash=0x579e1d6d,CRC=0xf6b62c5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackTonemap(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackTonemap",typeIDHash=0xe0291cff,CRC=0xb6727775,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackVignette(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackVignette",typeIDHash=0xa1aed958,CRC=0x20c02d0b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackVolumetricFog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackVolumetricFog",typeIDHash=0xe2bf2e5a,CRC=0xfa9600a1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_PostEffectTrackVolumetricFogControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.PostEffectTrackVolumetricFogControl",typeIDHash=0x8e52aaa6,CRC=0xe9f31aa4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_ResourceLoader(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.ResourceLoader",typeIDHash=0xbc00eb79,CRC=0x62e07d7e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_InitialMaxParallelReadingCount":RSZVariable(name="_InitialMaxParallelReadingCount",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_InitialActivateInterval":RSZVariable(name="_InitialActivateInterval",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_TimelineEventDef_cCutSceneEndMotionSetParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.TimelineEventDef.cCutSceneEndMotionSetParam",typeIDHash=0xb289723d,CRC=0x38f83a2f,isObject = True,tagList=[])
		self.fields = {
		"_MotionList":RSZVariable(name="_MotionList",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_StartMotionID":RSZVariable(name="_StartMotionID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_LoopMotionID":RSZVariable(name="_LoopMotionID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EndMotionID":RSZVariable(name="_EndMotionID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT__NextActionID__Category":RSZVariable(name="STRUCT__NextActionID__Category",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT__NextActionID__Index":RSZVariable(name="STRUCT__NextActionID__Index",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_NextActionGUID":RSZVariable(name="_NextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_MotionConnectBank":RSZVariable(name="_MotionConnectBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"STRUCT__StartPos__HasValue":RSZVariable(name="STRUCT__StartPos__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT__StartPos__Value":RSZVariable(name="STRUCT__StartPos__Value",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"STRUCT__StartRot__HasValue":RSZVariable(name="STRUCT__StartRot__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT__StartRot__Value":RSZVariable(name="STRUCT__StartRot__Value",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		}

class ace_TimelineEventDef_cCutSceneStartMotionSetParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.TimelineEventDef.cCutSceneStartMotionSetParam",typeIDHash=0x3cc01340,CRC=0x9567da05,isObject = True,tagList=[])
		self.fields = {
		"_MotionList":RSZVariable(name="_MotionList",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MotionID":RSZVariable(name="_MotionID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_MotionConnectBank":RSZVariable(name="_MotionConnectBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_TimelineEventScheduler(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.TimelineEventScheduler",typeIDHash=0x94b699c2,CRC=0x8a286366,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID":RSZVariable(name="_EventID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_FlowID":RSZVariable(name="_FlowID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_VirtualCamera(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.VirtualCamera",typeIDHash=0xdf3fe39c,CRC=0xddb4a9bc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_VolumeOccludeeController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.VolumeOccludeeController",typeIDHash=0x9c82bcb4,CRC=0x4d957291,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_VolumeOccludeeControllerMesh(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.VolumeOccludeeControllerMesh",typeIDHash=0x9d541860,CRC=0x43606d89,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class ace_WeatherManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.WeatherManager",typeIDHash=0xd43c520b,CRC=0xdb5fca4b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SceneWeatherData":RSZVariable(name="_SceneWeatherData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CurrentWeather":RSZVariable(name="_CurrentWeather",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_cAceAdvancedVibrationBase_cBusInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cAceAdvancedVibrationBase.cBusInfo",typeIDHash=0xee99f4c7,CRC=0xd670796a,isObject = True,tagList=[])
		self.fields = {
		"_BusId":RSZVariable(name="_BusId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_BusAssignId":RSZVariable(name="_BusAssignId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_cDampingParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cDampingParam",typeIDHash=0x91c5fed4,CRC=0x692210bd,isObject = True,tagList=[])
		self.fields = {
		"_Damping":RSZVariable(name="_Damping",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TimeScale":RSZVariable(name="_TimeScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_cGamePlayerAssignInitializer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cGamePlayerAssignInitializer",typeIDHash=0xb363718e,CRC=0xab99548c,isObject = True,tagList=[])
		self.fields = {
		"_GamePlayerConfig":RSZVariable(name="_GamePlayerConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_cSafeEvent2ace_user_data_GlobalTimeZoneData_TimeZoneSystem_Int32(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cSafeEvent`2<ace.user_data.GlobalTimeZoneData.TimeZone,System.Int32>",typeIDHash=0x69c8fcd0,CRC=0xbdf26595,isObject = True,tagList=[])
		self.fields = {
		}

class ace_cSafeEvent2app_cQuestDirector_EM_STATEapp_cEnemyBrowser(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cSafeEvent`2<app.cQuestDirector.EM_STATE,app.cEnemyBrowser>",typeIDHash=0xc739b1bf,CRC=0x96b01cfd,isObject = True,tagList=[])
		self.fields = {
		}

class ace_cStrHash(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cStrHash",typeIDHash=0xe735c367,CRC=0xe07394fe,isObject = True,tagList=[])
		self.fields = {
		"_Hash":RSZVariable(name="_Hash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_cWindDirectional(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.cWindDirectional",typeIDHash=0xc50c4251,CRC=0x72f53dc7,isObject = True,tagList=[])
		self.fields = {
		"IsActive":RSZVariable(name="IsActive",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Life":RSZVariable(name="Life",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Cycle0":RSZVariable(name="Cycle0",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Cycle1":RSZVariable(name="Cycle1",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Speed0":RSZVariable(name="Speed0",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Speed1":RSZVariable(name="Speed1",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"PressureMin":RSZVariable(name="PressureMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"PressureMax":RSZVariable(name="PressureMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Spread":RSZVariable(name="Spread",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LimitSpeedMin":RSZVariable(name="LimitSpeedMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Angle0":RSZVariable(name="Angle0",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"Angle1":RSZVariable(name="Angle1",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"GustType":RSZVariable(name="GustType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"GustSpeed0":RSZVariable(name="GustSpeed0",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustSpeed1":RSZVariable(name="GustSpeed1",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustPressureMax":RSZVariable(name="GustPressureMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustPressureMin":RSZVariable(name="GustPressureMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustSpread":RSZVariable(name="GustSpread",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustCycle0":RSZVariable(name="GustCycle0",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustCycle1":RSZVariable(name="GustCycle1",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustLife0":RSZVariable(name="GustLife0",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustLife1":RSZVariable(name="GustLife1",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"GustAngle0":RSZVariable(name="GustAngle0",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"GustAngle1":RSZVariable(name="GustAngle1",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		}

class ace_model_material_manager_ModelMaterialManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.model_material_manager.ModelMaterialManager",typeIDHash=0x42376110,CRC=0x2be45da6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Holders":RSZVariable(name="_Holders",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_model_material_manager_ModelMaterialManager_AssetHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.model_material_manager.ModelMaterialManager.AssetHolder",typeIDHash=0x625647e1,CRC=0xf068a63c,isObject = True,tagList=[])
		self.fields = {
		"_Id":RSZVariable(name="_Id",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_Data":RSZVariable(name="_Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_model_parts_manager_ModelPartsManager2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.model_parts_manager.ModelPartsManager2",typeIDHash=0x35175fe0,CRC=0xd39792d3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Holders":RSZVariable(name="_Holders",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_model_parts_manager_ModelPartsManager2_AssetHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.model_parts_manager.ModelPartsManager2.AssetHolder",typeIDHash=0xc7f9086,CRC=0x3bbc9165,isObject = True,tagList=[])
		self.fields = {
		"_Id":RSZVariable(name="_Id",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Data":RSZVariable(name="_Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_user_data_ADVibrationPresetList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.ADVibrationPresetList",typeIDHash=0x424644a3,CRC=0xc75c3b55,isObject = True,tagList=[])
		self.fields = {
		"_List":RSZVariable(name="_List",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_GPUScoreCalculateData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.GPUScoreCalculateData",typeIDHash=0x826f0479,CRC=0xdd153e9c,isObject = True,tagList=[])
		self.fields = {
		"_PresetThresholds":RSZVariable(name="_PresetThresholds",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PresetVramThresholds":RSZVariable(name="_PresetVramThresholds",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GPUScoreData":RSZVariable(name="_GPUScoreData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_user_data_GimmickMiniComponentConfig(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.GimmickMiniComponentConfig",typeIDHash=0xbbf870a9,CRC=0x75f49de2,isObject = True,tagList=[])
		self.fields = {
		"_GimmickMcHolderList":RSZVariable(name="_GimmickMcHolderList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_GimmickMiniComponentHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.GimmickMiniComponentHolder",typeIDHash=0x19633f57,CRC=0xcffe7bb1,isObject = True,tagList=[])
		self.fields = {
		"_Params":RSZVariable(name="_Params",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_user_data_GlobalTimeZoneData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.GlobalTimeZoneData",typeIDHash=0xd65dd311,CRC=0xae744b49,isObject = True,tagList=[])
		self.fields = {
		"_TimeZoneList":RSZVariable(name="_TimeZoneList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MaxFrame":RSZVariable(name="_MaxFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_user_data_JointConstraintsUserSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.JointConstraintsUserSetting",typeIDHash=0xf6fa7b33,CRC=0xb1fb73ec,isObject = True,tagList=[])
		self.fields = {
		"ChainSettings":RSZVariable(name="ChainSettings",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ClothSettings":RSZVariable(name="ClothSettings",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"PartsSettings":RSZVariable(name="PartsSettings",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_MeshWindSamplingPoint(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.MeshWindSamplingPoint",typeIDHash=0x92329ef2,CRC=0x8656cf38,isObject = True,tagList=[])
		self.fields = {
		"_DataArray":RSZVariable(name="_DataArray",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Mode":RSZVariable(name="_Mode",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_user_data_ModelMaterialInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.ModelMaterialInfo",typeIDHash=0xf28b3995,CRC=0x171e275b,isObject = True,tagList=[])
		self.fields = {
		"_Conditions":RSZVariable(name="_Conditions",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_ModelPartsInfo2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.ModelPartsInfo2",typeIDHash=0x912e5231,CRC=0x5ae8b84d,isObject = True,tagList=[])
		self.fields = {
		"_Conditions":RSZVariable(name="_Conditions",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsGroupDefinitions":RSZVariable(name="_PartsGroupDefinitions",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_user_data_MotionConnectBank(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.MotionConnectBank",typeIDHash=0xd70db2dc,CRC=0x2f9fa6bb,isObject = True,tagList=[])
		self.fields = {
		"_MotionConnectList":RSZVariable(name="_MotionConnectList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_MotionExtendBank(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.MotionExtendBank",typeIDHash=0xf5aeceea,CRC=0x4bddd64,isObject = True,tagList=[])
		self.fields = {
		"_MotionExtendList":RSZVariable(name="_MotionExtendList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GroupTable":RSZVariable(name="_GroupTable",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_PadVibrationPresetList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.PadVibrationPresetList",typeIDHash=0x57957927,CRC=0x883841b6,isObject = True,tagList=[])
		self.fields = {
		"_List":RSZVariable(name="_List",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_PadVibrationPresetList_cMotorVibration(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.PadVibrationPresetList.cMotorVibration",typeIDHash=0x90808e2e,CRC=0x12e2affa,isObject = True,tagList=[])
		self.fields = {
		"_Time":RSZVariable(name="_Time",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MotorType":RSZVariable(name="_MotorType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Power":RSZVariable(name="_Power",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsTimeAttenuation":RSZVariable(name="_IsTimeAttenuation",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TimeAttenuationType":RSZVariable(name="_TimeAttenuationType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_user_data_PointGraphManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.PointGraphManagerSetting",typeIDHash=0x1eb78534,CRC=0xf6ca5117,isObject = True,tagList=[])
		self.fields = {
		"SystemSetting":RSZVariable(name="SystemSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_PostEffectManagerBaseSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.PostEffectManagerBaseSetting",typeIDHash=0xeeed2045,CRC=0x5a7b8737,isObject = True,tagList=[])
		self.fields = {
		"_TypeList":RSZVariable(name="_TypeList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class ace_user_data_ShellList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.ShellList",typeIDHash=0x12050c0e,CRC=0x168488ff,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PrefabAutoStandby":RSZVariable(name="_PrefabAutoStandby",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class ace_user_data_VortexelGeometryManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.VortexelGeometryManagerSetting",typeIDHash=0x460a2525,CRC=0xc8a40aae,isObject = True,tagList=[])
		self.fields = {
		"_GeometryParam":RSZVariable(name="_GeometryParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ReservedDynamicPrimitiveNumFromScript":RSZVariable(name="_ReservedDynamicPrimitiveNumFromScript",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_RasterHeightRatio":RSZVariable(name="_RasterHeightRatio",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RasterRequestDelayFrame":RSZVariable(name="_RasterRequestDelayFrame",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class ace_user_data_VortexelPhysicsManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.VortexelPhysicsManagerSetting",typeIDHash=0xc14d3b4b,CRC=0xc08f2e28,isObject = True,tagList=[])
		self.fields = {
		"_PhysicsParam":RSZVariable(name="_PhysicsParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class ace_user_data_WeatherData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "ace.user_data.WeatherData",typeIDHash=0x14e87408,CRC=0x4807114,isObject = True,tagList=[])
		self.fields = {
		"_WeatherList":RSZVariable(name="_WeatherList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_AIMapCreateExtraLink(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AIMapCreateExtraLink",typeIDHash=0x46b5a8c4,CRC=0xd9535365,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Filter":RSZVariable(name="_Filter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsOneWay":RSZVariable(name="_IsOneWay",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_AIMapHandleRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AIMapHandleRegister",typeIDHash=0x8bc21402,CRC=0xee5ef025,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AlbumManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AlbumManager",typeIDHash=0x33d931fc,CRC=0x21e47aa2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_RTT_16x9":RSZVariable(name="_RTT_16x9",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_RTT_21x9":RSZVariable(name="_RTT_21x9",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_AnimalBaseCampLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimalBaseCampLayouter",typeIDHash=0x135e129,CRC=0xb1d1d4be,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AnimalBoxSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimalBoxSceneController",typeIDHash=0xbd162673,CRC=0x387954b5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_AnimalMarker":RSZVariable(name="_AnimalMarker",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_AnimalBoxViewSetting":RSZVariable(name="_AnimalBoxViewSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_AnimalExEventLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimalExEventLayouter",typeIDHash=0x5ef51a72,CRC=0xb96c1074,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StageId":RSZVariable(name="_StageId",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_AnimalManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimalManager",typeIDHash=0xab05ba93,CRC=0xeabdc673,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Config":RSZVariable(name="_Config",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_AnimalPopAreaCropLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimalPopAreaCropLayouter",typeIDHash=0x3e78b051,CRC=0xdb9fb429,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AnimalPopAreaLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimalPopAreaLayouter",typeIDHash=0x9d2f2d6e,CRC=0xe1dadc20,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AnimationLodManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AnimationLodManager",typeIDHash=0x9b4e6959,CRC=0xdca264d6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppEffectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppEffectManager",typeIDHash=0xe73af680,CRC=0x87ee8785,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CameraConstParent":RSZVariable(name="_CameraConstParent",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsCacheEnable":RSZVariable(name="_IsCacheEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_AppEngineSingletonCallbackManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppEngineSingletonCallbackManager",typeIDHash=0xf10597ad,CRC=0xb8cf261e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppEventManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppEventManager",typeIDHash=0xa2f7a575,CRC=0xc1fc8eaa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventManagerSetting":RSZVariable(name="_EventManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"ZoneInfo":RSZVariable(name="ZoneInfo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PreEventPosDic":RSZVariable(name="_PreEventPosDic",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_AppEventSystemBridgeManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppEventSystemBridgeManager",typeIDHash=0x29c94ef2,CRC=0x5e7763d5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppFlexibleSwordEventUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppFlexibleSwordEventUpdater",typeIDHash=0xc92933ff,CRC=0x6295267,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"TargetList":RSZVariable(name="TargetList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		}

class app_AppInitializer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppInitializer",typeIDHash=0x2f0886b7,CRC=0xfc762adc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppInstantiateManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppInstantiateManager",typeIDHash=0xa084321f,CRC=0x34b42727,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Option":RSZVariable(name="Option",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_Settings":RSZVariable(name="_Settings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_AppLightController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppLightController",typeIDHash=0x336c499a,CRC=0x9f42d4ed,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Condition":RSZVariable(name="_Condition",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_IntensityZoneName":RSZVariable(name="_IntensityZoneName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_InverseBlendRate":RSZVariable(name="_InverseBlendRate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClampBlendRate":RSZVariable(name="_ClampBlendRate",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		}

class app_AppPadVibrationManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppPadVibrationManager",typeIDHash=0x6c6be149,CRC=0xb3244c82,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DefaultPreset":RSZVariable(name="_DefaultPreset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DefaultADPreset":RSZVariable(name="_DefaultADPreset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ADVibration":RSZVariable(name="_ADVibration",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_AppPointedSpacemanager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppPointedSpacemanager",typeIDHash=0x36e4e12,CRC=0x7c0ab821,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SettingData":RSZVariable(name="_SettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_AppRaycastManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppRaycastManager",typeIDHash=0xe15fc014,CRC=0xf7892346,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppStreamingController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppStreamingController",typeIDHash=0xf9b54376,CRC=0xa5163cb8,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_AppStreamingControllerManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppStreamingControllerManager",typeIDHash=0xe851265c,CRC=0x12701ca1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppStreamingControllerRoot(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppStreamingControllerRoot",typeIDHash=0x3e5b699c,CRC=0x8b6cdcf2,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCompleteFix":RSZVariable(name="_IsCompleteFix",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_AppTimelineEventResourceManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppTimelineEventResourceManager",typeIDHash=0xa73a499,CRC=0x71da8289,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppVortexelEngineManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppVortexelEngineManager",typeIDHash=0xc78bb7a4,CRC=0xe146df8d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_AppWorkRateManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppWorkRateManager",typeIDHash=0x7bbb1b8a,CRC=0xe87d75d1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_WorkRateSetting":RSZVariable(name="_WorkRateSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_AppWorkRateSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.AppWorkRateSetting",typeIDHash=0x88d78dc9,CRC=0xfd1940e7,isObject = True,tagList=[])
		self.fields = {
		"_Data":RSZVariable(name="_Data",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsApplyChildren":RSZVariable(name="IsApplyChildren",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsUseFolderWorkRate":RSZVariable(name="IsUseFolderWorkRate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Timing":RSZVariable(name="Timing",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_BenchmarkStarter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BenchmarkStarter",typeIDHash=0x1b2b74bd,CRC=0x75fa3eb2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_BezierWayBuilder_CenterLine_cParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BezierWayBuilder_CenterLine.cParam",typeIDHash=0xd16f24de,CRC=0xc7f1a3cf,isObject = True,tagList=[])
		self.fields = {
		"_First":RSZVariable(name="_First",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Last":RSZVariable(name="_Last",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Relays":RSZVariable(name="_Relays",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_BezierWayBuilder_CenterLine_cParam_cEdge(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BezierWayBuilder_CenterLine.cParam.cEdge",typeIDHash=0x9dff691c,CRC=0x649fcf5f,isObject = True,tagList=[])
		self.fields = {
		"_WayCtrlRate":RSZVariable(name="_WayCtrlRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_BezierWayBuilder_CenterLine_cParam_cRelay(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BezierWayBuilder_CenterLine.cParam.cRelay",typeIDHash=0x2ca26d13,CRC=0x64019a96,isObject = True,tagList=[])
		self.fields = {
		"_LineRate":RSZVariable(name="_LineRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Distance":RSZVariable(name="_Distance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RollDeg":RSZVariable(name="_RollDeg",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WayDegree":RSZVariable(name="_WayDegree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WayCtrlRate":RSZVariable(name="_WayCtrlRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_Blizzard(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Blizzard",typeIDHash=0xc1935e42,CRC=0xbb35e5ef,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EdgeOpacitySearchDist":RSZVariable(name="_EdgeOpacitySearchDist",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MoveState":RSZVariable(name="_MoveState",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Settings":RSZVariable(name="_Settings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_BlizzardSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BlizzardSetting",typeIDHash=0x7f29a7de,CRC=0x75895216,isObject = True,tagList=[])
		self.fields = {
		"_Requests":RSZVariable(name="_Requests",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Abnormal_Offset":RSZVariable(name="_Abnormal_Offset",dataType="obb",isList=False,alignment=16,value=None,tagSet=[]),
		"_DefaultVisibleData":RSZVariable(name="_DefaultVisibleData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AfterBlizzardVisibleData":RSZVariable(name="_AfterBlizzardVisibleData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_InLinearData":RSZVariable(name="_InLinearData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BlendLightData":RSZVariable(name="_BlendLightData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WindChangeData":RSZVariable(name="_WindChangeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_BootManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BootManager",typeIDHash=0xd2556f62,CRC=0xf195542a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_BootScene(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BootScene",typeIDHash=0x3988a153,CRC=0x6f7afb29,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_BootParam":RSZVariable(name="_BootParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_BurntGroundSplat(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.BurntGroundSplat",typeIDHash=0xb2c90ada,CRC=0x9d38f467,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_CCSGrassCulling(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CCSGrassCulling",typeIDHash=0xe4928c25,CRC=0x7f2f237a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CCSMossCulling(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CCSMossCulling",typeIDHash=0xcb131d5d,CRC=0xa8ec2c13,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CLSPVirtualGround(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CLSPVirtualGround",typeIDHash=0xc348b8db,CRC=0xc1bec40d,isObject = True,tagList=[])
		self.fields = {
		"_HeightDamping":RSZVariable(name="_HeightDamping",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AngleDamping":RSZVariable(name="_AngleDamping",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnableHeightLimit":RSZVariable(name="_EnableHeightLimit",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_HeightLimitRange":RSZVariable(name="_HeightLimitRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"_EnableAngleLimit":RSZVariable(name="_EnableAngleLimit",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_AngleRadLimit":RSZVariable(name="_AngleRadLimit",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CameraManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CameraManager",typeIDHash=0x1bbea8e8,CRC=0x374653b1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_CampCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CampCreator",typeIDHash=0x9f663a7c,CRC=0xb0d389ee,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CatalogActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CatalogActivator",typeIDHash=0x6ac491fa,CRC=0xb7e9f443,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ChainManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ChainManager",typeIDHash=0xa4b0b958,CRC=0x207be4aa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SettingBase":RSZVariable(name="_SettingBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_ChainSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ChainSetting",typeIDHash=0x4d94fbe4,CRC=0xd8f3c6b3,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WindAssetOverwrite":RSZVariable(name="_WindAssetOverwrite",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_WindAssetOverwrite2":RSZVariable(name="_WindAssetOverwrite2",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_WindSamplingPoint":RSZVariable(name="_WindSamplingPoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WindBias":RSZVariable(name="_WindBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_CullingLengthBias":RSZVariable(name="_CullingLengthBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsUpdateSelf":RSZVariable(name="_IsUpdateSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsWindRecieve":RSZVariable(name="_IsWindRecieve",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCullingEnable":RSZVariable(name="_IsCullingEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCreateVolumeOccludee":RSZVariable(name="_IsCreateVolumeOccludee",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_ChainSettingCollection(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ChainSettingCollection",typeIDHash=0x3dd0b54,CRC=0x7c83c7c7,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WindSamplingPoint":RSZVariable(name="_WindSamplingPoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WindBias":RSZVariable(name="_WindBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_CullingLengthBias":RSZVariable(name="_CullingLengthBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT__BlendRate__HasValue":RSZVariable(name="STRUCT__BlendRate__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT__BlendRate__Value":RSZVariable(name="STRUCT__BlendRate__Value",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsUpdateSelf":RSZVariable(name="_IsUpdateSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsWindRecieve":RSZVariable(name="_IsWindRecieve",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCullingEnable":RSZVariable(name="_IsCullingEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCreateVolumeOccludee":RSZVariable(name="_IsCreateVolumeOccludee",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_ChainSub2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ChainSub2",typeIDHash=0xa82a28d8,CRC=0x99330e6c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CharaMakeBlendShapeController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharaMakeBlendShapeController",typeIDHash=0x768ccd58,CRC=0x2aae68d5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CharaMakeSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharaMakeSceneController",typeIDHash=0xa517a359,CRC=0xb5dc761a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SceneHunterObject":RSZVariable(name="_SceneHunterObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_ScenePalicoObject":RSZVariable(name="_ScenePalicoObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightSources":RSZVariable(name="_LightSources",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_HunterRotatableLights":RSZVariable(name="_HunterRotatableLights",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_PalicoRotatableLights":RSZVariable(name="_PalicoRotatableLights",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_HunterLightRotateSpeed":RSZVariable(name="_HunterLightRotateSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_PalicoLightRotateSpeed":RSZVariable(name="_PalicoLightRotateSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterEditBuilder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterEditBuilder",typeIDHash=0x27dd6c92,CRC=0x95a02b4b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MannequinCatalog":RSZVariable(name="_MannequinCatalog",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_CharacterEditRegion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterEditRegion",typeIDHash=0x23f9647a,CRC=0x1077f96c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_RegionNameHash":RSZVariable(name="_RegionNameHash",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EditValudeDefinition":RSZVariable(name="_EditValudeDefinition",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EditValueMaterialDefinition":RSZVariable(name="_EditValueMaterialDefinition",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NodeNameHash":RSZVariable(name="_NodeNameHash",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MotionBank":RSZVariable(name="_MotionBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_LayerIndex":RSZVariable(name="_LayerIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_BankID":RSZVariable(name="_BankID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterEditRegionRoot(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterEditRegionRoot",typeIDHash=0x8deea1d8,CRC=0x97b4ce77,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"UnappliedSincePartsChanged":RSZVariable(name="UnappliedSincePartsChanged",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase",typeIDHash=0xb65ecae1,CRC=0xcaa5544e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipParamStartMotionSet":RSZVariable(name="_ClipParamStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSet":RSZVariable(name="_ClipParamEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CheckerFrame":RSZVariable(name="_CheckerFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnableIngameAdjust":RSZVariable(name="_EnableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableRootScaleDisable":RSZVariable(name="DisableRootScaleDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ToContinuance":RSZVariable(name="ToContinuance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WarpData":RSZVariable(name="_WarpData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandData":RSZVariable(name="_SandData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetData":RSZVariable(name="_WetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MadData":RSZVariable(name="_MadData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OilData":RSZVariable(name="_OilData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SnowData":RSZVariable(name="_SnowData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsEventObj":RSZVariable(name="IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClothResetPose":RSZVariable(name="_ClothResetPose",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGpuClothCollision":RSZVariable(name="_ClipParamGpuClothCollision",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteMotionFrame":RSZVariable(name="_OverwriteMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceDisableIngameAdjust":RSZVariable(name="ForceDisableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StencilFadeTarget":RSZVariable(name="_StencilFadeTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableESIAllDisable":RSZVariable(name="_EnableESIAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverrideChainMotion":RSZVariable(name="_OverrideChainMotion",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstrainParentData":RSZVariable(name="_ConstrainParentData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsForceFixedMotion":RSZVariable(name="_IsForceFixedMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsForceNoneMotion":RSZVariable(name="_IsForceNoneMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableInterpolateMotion":RSZVariable(name="_EnableInterpolateMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceSkipMotion":RSZVariable(name="_DisableForceSkipMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceNextCutChainReset":RSZVariable(name="_ForceNextCutChainReset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndNextActionGUID":RSZVariable(name="_EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_SkipEndActionStopDisable":RSZVariable(name="_SkipEndActionStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionNextMoveStart":RSZVariable(name="_SkipEndActionNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionClothWarp":RSZVariable(name="_SkipEndActionClothWarp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionStartDisable":RSZVariable(name="_IsSkipEndMotionStartDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionAllDisable":RSZVariable(name="_IsSkipEndMotionAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionPosGroundAdjust":RSZVariable(name="_EndMotionPosGroundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionRotFlatQuat":RSZVariable(name="_EndMotionRotFlatQuat",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialSettingData":RSZVariable(name="_MaterialSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainReduceSettingData":RSZVariable(name="_ChainReduceSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainStabilizeSettingData":RSZVariable(name="_ChainStabilizeSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NextActionVariationSettingData":RSZVariable(name="_NextActionVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshMaterialVariationSettingData":RSZVariable(name="_MeshMaterialVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsVariationSettingData":RSZVariable(name="_PartsVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SeamlessInRotateAdjustData":RSZVariable(name="_SeamlessInRotateAdjustData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiningJointOffsetData":RSZVariable(name="_DiningJointOffsetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpDataWithBindEnd":RSZVariable(name="_WarpDataWithBindEnd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGalleryEndMotionSet":RSZVariable(name="_ClipParamGalleryEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GalleryStartMotionFrame":RSZVariable(name="_GalleryStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverrideStartMotionFrame":RSZVariable(name="_OverrideStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_ChainReduceSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.ChainReduceSettingData",typeIDHash=0x56f51fbc,CRC=0x5c2d7d6b,isObject = True,tagList=[])
		self.fields = {
		"ChainReduceIndex":RSZVariable(name="ChainReduceIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"EnableChainReduceObj":RSZVariable(name="EnableChainReduceObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableChainReduceObj":RSZVariable(name="DisableChainReduceObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ChainReduceBase":RSZVariable(name="ChainReduceBase",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ChainForceRate":RSZVariable(name="ChainForceRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_ChainStabilizeSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.ChainStabilizeSettingData",typeIDHash=0xb66aa6cd,CRC=0x112e55ca,isObject = True,tagList=[])
		self.fields = {
		"OverrideStabilizeNum":RSZVariable(name="OverrideStabilizeNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_ClothResetPoseData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.ClothResetPoseData",typeIDHash=0x70f568c9,CRC=0xf99ec9f7,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Resource":RSZVariable(name="Resource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"ClothName":RSZVariable(name="ClothName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_ConstrainParentData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.ConstrainParentData",typeIDHash=0x2987f166,CRC=0x4093df97,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetNpcID":RSZVariable(name="TargetNpcID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"JointName":RSZVariable(name="JointName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_DiningJointOffsetData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.DiningJointOffsetData",typeIDHash=0x70720877,CRC=0xc99beee3,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsRoot":RSZVariable(name="IsRoot",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetJointName":RSZVariable(name="TargetJointName",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TargetJointNameList":RSZVariable(name="TargetJointNameList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CharacterTimelineEventActorBase_MadParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.MadParam",typeIDHash=0x7e51b43,CRC=0x1dff3bde,isObject = True,tagList=[])
		self.fields = {
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_MaterialSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.MaterialSettingData",typeIDHash=0x38ab88dd,CRC=0x85319803,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"MaterialNameHash":RSZVariable(name="MaterialNameHash",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ParamNameHash":RSZVariable(name="ParamNameHash",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ParamType":RSZVariable(name="ParamType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ParamFloat":RSZVariable(name="ParamFloat",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ParamFloat4":RSZVariable(name="ParamFloat4",dataType="float4",isList=False,alignment=4,value=None,tagSet=[]),
		"ParamColor":RSZVariable(name="ParamColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"ParamColorF":RSZVariable(name="ParamColorF",dataType="float4",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_MeshMaterialVariationSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.MeshMaterialVariationSettingData",typeIDHash=0x82dc67f8,CRC=0xa76acc6e,isObject = True,tagList=[])
		self.fields = {
		"GroupID":RSZVariable(name="GroupID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"VariationID":RSZVariable(name="VariationID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"MeshRes":RSZVariable(name="MeshRes",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"MeshMaterialRes":RSZVariable(name="MeshMaterialRes",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_CharacterTimelineEventActorBase_NextActionVariationSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.NextActionVariationSettingData",typeIDHash=0x1ac40444,CRC=0x4cbd9830,isObject = True,tagList=[])
		self.fields = {
		"VariationID":RSZVariable(name="VariationID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"EndNextActionGUID":RSZVariable(name="EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"IsStopDisable":RSZVariable(name="IsStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsStopOnly":RSZVariable(name="IsStopOnly",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_OilParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.OilParam",typeIDHash=0x6eaef48b,CRC=0xf221b152,isObject = True,tagList=[])
		self.fields = {
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_OverrideChainMotion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.OverrideChainMotion",typeIDHash=0x62812446,CRC=0x874656d5,isObject = True,tagList=[])
		self.fields = {
		"TargetName":RSZVariable(name="TargetName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"ChainMotion":RSZVariable(name="ChainMotion",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"ChainMotionList":RSZVariable(name="ChainMotionList",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"MotID":RSZVariable(name="MotID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"Frame":RSZVariable(name="Frame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_ParamGpuClothCollision(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.ParamGpuClothCollision",typeIDHash=0xf4aeaab4,CRC=0x71edc48c,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_CollisionTarget":RSZVariable(name="_CollisionTarget",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_PartsVariationSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.PartsVariationSettingData",typeIDHash=0xbee7d299,CRC=0xac57bc71,isObject = True,tagList=[])
		self.fields = {
		"GroupID":RSZVariable(name="GroupID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"VariationID":RSZVariable(name="VariationID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsOtherVariationInverse":RSZVariable(name="IsOtherVariationInverse",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"PartsID":RSZVariable(name="PartsID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsDisp":RSZVariable(name="IsDisp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_SandParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.SandParam",typeIDHash=0xd47c6edb,CRC=0xfab0ef17,isObject = True,tagList=[])
		self.fields = {
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_SeamlessInRotateAdjustData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.SeamlessInRotateAdjustData",typeIDHash=0xe8205ddc,CRC=0xa05a98d3,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetPos":RSZVariable(name="TargetPos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"RotateSpeed":RSZVariable(name="RotateSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"SuccessRotate":RSZVariable(name="SuccessRotate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_SnowParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.SnowParam",typeIDHash=0x4b2e0717,CRC=0xa58e856a,isObject = True,tagList=[])
		self.fields = {
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorBase_WetParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorBase.WetParam",typeIDHash=0xb9934545,CRC=0x3a067296,isObject = True,tagList=[])
		self.fields = {
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorEnemy(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorEnemy",typeIDHash=0xa2c416f5,CRC=0x15942958,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipParamStartMotionSet":RSZVariable(name="_ClipParamStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSet":RSZVariable(name="_ClipParamEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CheckerFrame":RSZVariable(name="_CheckerFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnableIngameAdjust":RSZVariable(name="_EnableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableRootScaleDisable":RSZVariable(name="DisableRootScaleDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ToContinuance":RSZVariable(name="ToContinuance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WarpData":RSZVariable(name="_WarpData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandData":RSZVariable(name="_SandData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetData":RSZVariable(name="_WetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MadData":RSZVariable(name="_MadData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OilData":RSZVariable(name="_OilData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SnowData":RSZVariable(name="_SnowData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsEventObj":RSZVariable(name="IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClothResetPose":RSZVariable(name="_ClothResetPose",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGpuClothCollision":RSZVariable(name="_ClipParamGpuClothCollision",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteMotionFrame":RSZVariable(name="_OverwriteMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceDisableIngameAdjust":RSZVariable(name="ForceDisableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StencilFadeTarget":RSZVariable(name="_StencilFadeTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableESIAllDisable":RSZVariable(name="_EnableESIAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverrideChainMotion":RSZVariable(name="_OverrideChainMotion",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstrainParentData":RSZVariable(name="_ConstrainParentData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsForceFixedMotion":RSZVariable(name="_IsForceFixedMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsForceNoneMotion":RSZVariable(name="_IsForceNoneMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableInterpolateMotion":RSZVariable(name="_EnableInterpolateMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceSkipMotion":RSZVariable(name="_DisableForceSkipMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceNextCutChainReset":RSZVariable(name="_ForceNextCutChainReset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndNextActionGUID":RSZVariable(name="_EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_SkipEndActionStopDisable":RSZVariable(name="_SkipEndActionStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionNextMoveStart":RSZVariable(name="_SkipEndActionNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionClothWarp":RSZVariable(name="_SkipEndActionClothWarp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionStartDisable":RSZVariable(name="_IsSkipEndMotionStartDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionAllDisable":RSZVariable(name="_IsSkipEndMotionAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionPosGroundAdjust":RSZVariable(name="_EndMotionPosGroundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionRotFlatQuat":RSZVariable(name="_EndMotionRotFlatQuat",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialSettingData":RSZVariable(name="_MaterialSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainReduceSettingData":RSZVariable(name="_ChainReduceSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainStabilizeSettingData":RSZVariable(name="_ChainStabilizeSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NextActionVariationSettingData":RSZVariable(name="_NextActionVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshMaterialVariationSettingData":RSZVariable(name="_MeshMaterialVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsVariationSettingData":RSZVariable(name="_PartsVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SeamlessInRotateAdjustData":RSZVariable(name="_SeamlessInRotateAdjustData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiningJointOffsetData":RSZVariable(name="_DiningJointOffsetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpDataWithBindEnd":RSZVariable(name="_WarpDataWithBindEnd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGalleryEndMotionSet":RSZVariable(name="_ClipParamGalleryEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GalleryStartMotionFrame":RSZVariable(name="_GalleryStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverrideStartMotionFrame":RSZVariable(name="_OverrideStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ModelPartsDataList":RSZVariable(name="_ModelPartsDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ModelMaterialDataList":RSZVariable(name="_ModelMaterialDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Em0151_LightControl":RSZVariable(name="_Em0151_LightControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IkLegRateControl":RSZVariable(name="_IkLegRateControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CharacterTimelineEventActorEnemy_Em0151_LightControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorEnemy.Em0151_LightControl",typeIDHash=0xb1747b15,CRC=0xc09ae3f5,isObject = True,tagList=[])
		self.fields = {
		"LightOff":RSZVariable(name="LightOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorEnemy_IkLegRateControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorEnemy.IkLegRateControl",typeIDHash=0xf836ce27,CRC=0xda3a8bec,isObject = True,tagList=[])
		self.fields = {
		"_EnableRateControl":RSZVariable(name="_EnableRateControl",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_BlendRate":RSZVariable(name="_BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorEnemy_ModelMaterialData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorEnemy.ModelMaterialData",typeIDHash=0x568eb67f,CRC=0x4c0dc401,isObject = True,tagList=[])
		self.fields = {
		"ResId":RSZVariable(name="ResId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ConditionIndex":RSZVariable(name="ConditionIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ConditionGUID":RSZVariable(name="ConditionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorEnemy_ModelPartsData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorEnemy.ModelPartsData",typeIDHash=0x6750336e,CRC=0x437a5a5e,isObject = True,tagList=[])
		self.fields = {
		"ResId":RSZVariable(name="ResId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ConditionIndex":RSZVariable(name="ConditionIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorHuman_ParamEndSubMotion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorHuman.ParamEndSubMotion",typeIDHash=0x6e030a59,CRC=0x3889634c,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"SetID":RSZVariable(name="SetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"SetEndLoopID":RSZVariable(name="SetEndLoopID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"SetEndID":RSZVariable(name="SetEndID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"MsgEndSubMotionSet":RSZVariable(name="MsgEndSubMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Frame":RSZVariable(name="Frame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorHuman_ParamSlingerAmmo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorHuman.ParamSlingerAmmo",typeIDHash=0xeefa0f5a,CRC=0xf969a3b7,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"AmmoType":RSZVariable(name="AmmoType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"AmmoNum":RSZVariable(name="AmmoNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorHuman_ParamStartSubMotion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorHuman.ParamStartSubMotion",typeIDHash=0xe01b558e,CRC=0xb8d91bba,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"SetID":RSZVariable(name="SetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"MsgStartSubMotionSet":RSZVariable(name="MsgStartSubMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Frame":RSZVariable(name="Frame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorNpc(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorNpc",typeIDHash=0xcc10b7c7,CRC=0xff82ed58,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipParamStartMotionSet":RSZVariable(name="_ClipParamStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSet":RSZVariable(name="_ClipParamEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CheckerFrame":RSZVariable(name="_CheckerFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnableIngameAdjust":RSZVariable(name="_EnableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableRootScaleDisable":RSZVariable(name="DisableRootScaleDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ToContinuance":RSZVariable(name="ToContinuance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WarpData":RSZVariable(name="_WarpData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandData":RSZVariable(name="_SandData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetData":RSZVariable(name="_WetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MadData":RSZVariable(name="_MadData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OilData":RSZVariable(name="_OilData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SnowData":RSZVariable(name="_SnowData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsEventObj":RSZVariable(name="IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClothResetPose":RSZVariable(name="_ClothResetPose",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGpuClothCollision":RSZVariable(name="_ClipParamGpuClothCollision",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteMotionFrame":RSZVariable(name="_OverwriteMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceDisableIngameAdjust":RSZVariable(name="ForceDisableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StencilFadeTarget":RSZVariable(name="_StencilFadeTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableESIAllDisable":RSZVariable(name="_EnableESIAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverrideChainMotion":RSZVariable(name="_OverrideChainMotion",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstrainParentData":RSZVariable(name="_ConstrainParentData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsForceFixedMotion":RSZVariable(name="_IsForceFixedMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsForceNoneMotion":RSZVariable(name="_IsForceNoneMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableInterpolateMotion":RSZVariable(name="_EnableInterpolateMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceSkipMotion":RSZVariable(name="_DisableForceSkipMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceNextCutChainReset":RSZVariable(name="_ForceNextCutChainReset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndNextActionGUID":RSZVariable(name="_EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_SkipEndActionStopDisable":RSZVariable(name="_SkipEndActionStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionNextMoveStart":RSZVariable(name="_SkipEndActionNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionClothWarp":RSZVariable(name="_SkipEndActionClothWarp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionStartDisable":RSZVariable(name="_IsSkipEndMotionStartDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionAllDisable":RSZVariable(name="_IsSkipEndMotionAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionPosGroundAdjust":RSZVariable(name="_EndMotionPosGroundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionRotFlatQuat":RSZVariable(name="_EndMotionRotFlatQuat",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialSettingData":RSZVariable(name="_MaterialSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainReduceSettingData":RSZVariable(name="_ChainReduceSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainStabilizeSettingData":RSZVariable(name="_ChainStabilizeSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NextActionVariationSettingData":RSZVariable(name="_NextActionVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshMaterialVariationSettingData":RSZVariable(name="_MeshMaterialVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsVariationSettingData":RSZVariable(name="_PartsVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SeamlessInRotateAdjustData":RSZVariable(name="_SeamlessInRotateAdjustData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiningJointOffsetData":RSZVariable(name="_DiningJointOffsetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpDataWithBindEnd":RSZVariable(name="_WarpDataWithBindEnd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGalleryEndMotionSet":RSZVariable(name="_ClipParamGalleryEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GalleryStartMotionFrame":RSZVariable(name="_GalleryStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverrideStartMotionFrame":RSZVariable(name="_OverrideStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"PorterRideAdjust":RSZVariable(name="PorterRideAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"PorterRideAdjustRoot":RSZVariable(name="PorterRideAdjustRoot",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"PorterRideIngame":RSZVariable(name="PorterRideIngame",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClipParamStartSubMotionSet":RSZVariable(name="_ClipParamStartSubMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndSubMotionSet":RSZVariable(name="_ClipParamEndSubMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RidePorter":RSZVariable(name="_RidePorter",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IngameRidePorterContinue":RSZVariable(name="_IngameRidePorterContinue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionWithWeaponOn":RSZVariable(name="_EndMotionWithWeaponOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SetSlingerAmmo":RSZVariable(name="_SetSlingerAmmo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_HideSlingerAmmo":RSZVariable(name="_HideSlingerAmmo",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"RidePorter":RSZVariable(name="RidePorter",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_BindTargetPorter":RSZVariable(name="_BindTargetPorter",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsPorterRideSecondery":RSZVariable(name="_IsPorterRideSecondery",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_PorterRideSeconderyNpcOtomo":RSZVariable(name="_PorterRideSeconderyNpcOtomo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ClipParamLinearAct":RSZVariable(name="_ClipParamLinearAct",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WpDrawOff":RSZVariable(name="_WpDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_PorterStickDrawOff":RSZVariable(name="_PorterStickDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MantleDrawOn":RSZVariable(name="_MantleDrawOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MantleDrawOff":RSZVariable(name="_MantleDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_InnnerArmor":RSZVariable(name="_InnnerArmor",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DiningArmor":RSZVariable(name="_DiningArmor",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceFaceDrawOn":RSZVariable(name="_DisableForceFaceDrawOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_NpcChainPresetData":RSZVariable(name="_NpcChainPresetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsDispSettingDatas":RSZVariable(name="_PartsDispSettingDatas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CharacterTimelineEventActorNpc_NpcChainPresetData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorNpc.NpcChainPresetData",typeIDHash=0x602b7488,CRC=0x6254ef77,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"OverWritePresetID":RSZVariable(name="OverWritePresetID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorNpc_ParamLinearAct(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorNpc.ParamLinearAct",typeIDHash=0x64a40475,CRC=0xcf12f46b,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_FSM_Type":RSZVariable(name="_FSM_Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PointGraphNo":RSZVariable(name="_PointGraphNo",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_SkipPointGraphNo":RSZVariable(name="_SkipPointGraphNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorNpc_PartsDispSettingData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorNpc.PartsDispSettingData",typeIDHash=0xf5cefd2f,CRC=0x424c9362,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetType":RSZVariable(name="TargetType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"PartsNum":RSZVariable(name="PartsNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsPartsEnable":RSZVariable(name="IsPartsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorOtomo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorOtomo",typeIDHash=0xef5feecd,CRC=0x97eba1d7,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipParamStartMotionSet":RSZVariable(name="_ClipParamStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSet":RSZVariable(name="_ClipParamEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CheckerFrame":RSZVariable(name="_CheckerFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnableIngameAdjust":RSZVariable(name="_EnableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableRootScaleDisable":RSZVariable(name="DisableRootScaleDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ToContinuance":RSZVariable(name="ToContinuance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WarpData":RSZVariable(name="_WarpData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandData":RSZVariable(name="_SandData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetData":RSZVariable(name="_WetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MadData":RSZVariable(name="_MadData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OilData":RSZVariable(name="_OilData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SnowData":RSZVariable(name="_SnowData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsEventObj":RSZVariable(name="IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClothResetPose":RSZVariable(name="_ClothResetPose",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGpuClothCollision":RSZVariable(name="_ClipParamGpuClothCollision",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteMotionFrame":RSZVariable(name="_OverwriteMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceDisableIngameAdjust":RSZVariable(name="ForceDisableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StencilFadeTarget":RSZVariable(name="_StencilFadeTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableESIAllDisable":RSZVariable(name="_EnableESIAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverrideChainMotion":RSZVariable(name="_OverrideChainMotion",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstrainParentData":RSZVariable(name="_ConstrainParentData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsForceFixedMotion":RSZVariable(name="_IsForceFixedMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsForceNoneMotion":RSZVariable(name="_IsForceNoneMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableInterpolateMotion":RSZVariable(name="_EnableInterpolateMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceSkipMotion":RSZVariable(name="_DisableForceSkipMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceNextCutChainReset":RSZVariable(name="_ForceNextCutChainReset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndNextActionGUID":RSZVariable(name="_EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_SkipEndActionStopDisable":RSZVariable(name="_SkipEndActionStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionNextMoveStart":RSZVariable(name="_SkipEndActionNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionClothWarp":RSZVariable(name="_SkipEndActionClothWarp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionStartDisable":RSZVariable(name="_IsSkipEndMotionStartDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionAllDisable":RSZVariable(name="_IsSkipEndMotionAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionPosGroundAdjust":RSZVariable(name="_EndMotionPosGroundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionRotFlatQuat":RSZVariable(name="_EndMotionRotFlatQuat",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialSettingData":RSZVariable(name="_MaterialSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainReduceSettingData":RSZVariable(name="_ChainReduceSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainStabilizeSettingData":RSZVariable(name="_ChainStabilizeSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NextActionVariationSettingData":RSZVariable(name="_NextActionVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshMaterialVariationSettingData":RSZVariable(name="_MeshMaterialVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsVariationSettingData":RSZVariable(name="_PartsVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SeamlessInRotateAdjustData":RSZVariable(name="_SeamlessInRotateAdjustData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiningJointOffsetData":RSZVariable(name="_DiningJointOffsetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpDataWithBindEnd":RSZVariable(name="_WarpDataWithBindEnd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGalleryEndMotionSet":RSZVariable(name="_ClipParamGalleryEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GalleryStartMotionFrame":RSZVariable(name="_GalleryStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverrideStartMotionFrame":RSZVariable(name="_OverrideStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WpDrawOff":RSZVariable(name="_WpDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WpOnForce":RSZVariable(name="_WpOnForce",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WpOffForce":RSZVariable(name="_WpOffForce",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClipParamStartMotionSetRiding":RSZVariable(name="_ClipParamStartMotionSetRiding",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSetRiding":RSZVariable(name="_ClipParamEndMotionSetRiding",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamOtomoRide":RSZVariable(name="_ClipParamOtomoRide",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CharacterTimelineEventActorOtomo_ParamEndMotionRiding(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorOtomo.ParamEndMotionRiding",typeIDHash=0xac1f3da,CRC=0xd3022e8d,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"MsgEndMotionSet":RSZVariable(name="MsgEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"NpcID":RSZVariable(name="NpcID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"OtomoRidePosType":RSZVariable(name="OtomoRidePosType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Frame":RSZVariable(name="Frame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"noRide":RSZVariable(name="noRide",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorOtomo_ParamOtomoRide(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorOtomo.ParamOtomoRide",typeIDHash=0x68367c85,CRC=0xb3629124,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"isRiding":RSZVariable(name="isRiding",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"NpcID":RSZVariable(name="NpcID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"OtomoRidePosType":RSZVariable(name="OtomoRidePosType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorOtomo_ParamStartMotionRiding(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorOtomo.ParamStartMotionRiding",typeIDHash=0x9cebff3a,CRC=0x9bbbfc7e,isObject = True,tagList=[])
		self.fields = {
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"MsgStartMotionSet":RSZVariable(name="MsgStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Frame":RSZVariable(name="Frame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorPlayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorPlayer",typeIDHash=0xe5f4bf0d,CRC=0xd5f9112e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipParamStartMotionSet":RSZVariable(name="_ClipParamStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSet":RSZVariable(name="_ClipParamEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CheckerFrame":RSZVariable(name="_CheckerFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnableIngameAdjust":RSZVariable(name="_EnableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableRootScaleDisable":RSZVariable(name="DisableRootScaleDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ToContinuance":RSZVariable(name="ToContinuance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WarpData":RSZVariable(name="_WarpData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandData":RSZVariable(name="_SandData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetData":RSZVariable(name="_WetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MadData":RSZVariable(name="_MadData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OilData":RSZVariable(name="_OilData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SnowData":RSZVariable(name="_SnowData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsEventObj":RSZVariable(name="IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClothResetPose":RSZVariable(name="_ClothResetPose",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGpuClothCollision":RSZVariable(name="_ClipParamGpuClothCollision",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteMotionFrame":RSZVariable(name="_OverwriteMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceDisableIngameAdjust":RSZVariable(name="ForceDisableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StencilFadeTarget":RSZVariable(name="_StencilFadeTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableESIAllDisable":RSZVariable(name="_EnableESIAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverrideChainMotion":RSZVariable(name="_OverrideChainMotion",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstrainParentData":RSZVariable(name="_ConstrainParentData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsForceFixedMotion":RSZVariable(name="_IsForceFixedMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsForceNoneMotion":RSZVariable(name="_IsForceNoneMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableInterpolateMotion":RSZVariable(name="_EnableInterpolateMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceSkipMotion":RSZVariable(name="_DisableForceSkipMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceNextCutChainReset":RSZVariable(name="_ForceNextCutChainReset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndNextActionGUID":RSZVariable(name="_EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_SkipEndActionStopDisable":RSZVariable(name="_SkipEndActionStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionNextMoveStart":RSZVariable(name="_SkipEndActionNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionClothWarp":RSZVariable(name="_SkipEndActionClothWarp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionStartDisable":RSZVariable(name="_IsSkipEndMotionStartDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionAllDisable":RSZVariable(name="_IsSkipEndMotionAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionPosGroundAdjust":RSZVariable(name="_EndMotionPosGroundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionRotFlatQuat":RSZVariable(name="_EndMotionRotFlatQuat",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialSettingData":RSZVariable(name="_MaterialSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainReduceSettingData":RSZVariable(name="_ChainReduceSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainStabilizeSettingData":RSZVariable(name="_ChainStabilizeSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NextActionVariationSettingData":RSZVariable(name="_NextActionVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshMaterialVariationSettingData":RSZVariable(name="_MeshMaterialVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsVariationSettingData":RSZVariable(name="_PartsVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SeamlessInRotateAdjustData":RSZVariable(name="_SeamlessInRotateAdjustData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiningJointOffsetData":RSZVariable(name="_DiningJointOffsetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpDataWithBindEnd":RSZVariable(name="_WarpDataWithBindEnd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGalleryEndMotionSet":RSZVariable(name="_ClipParamGalleryEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GalleryStartMotionFrame":RSZVariable(name="_GalleryStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverrideStartMotionFrame":RSZVariable(name="_OverrideStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"PorterRideAdjust":RSZVariable(name="PorterRideAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"PorterRideAdjustRoot":RSZVariable(name="PorterRideAdjustRoot",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"PorterRideIngame":RSZVariable(name="PorterRideIngame",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClipParamStartSubMotionSet":RSZVariable(name="_ClipParamStartSubMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndSubMotionSet":RSZVariable(name="_ClipParamEndSubMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RidePorter":RSZVariable(name="_RidePorter",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IngameRidePorterContinue":RSZVariable(name="_IngameRidePorterContinue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionWithWeaponOn":RSZVariable(name="_EndMotionWithWeaponOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SetSlingerAmmo":RSZVariable(name="_SetSlingerAmmo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_HideSlingerAmmo":RSZVariable(name="_HideSlingerAmmo",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceBodyMotion":RSZVariable(name="_ForceBodyMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_FemaleAdjustRate":RSZVariable(name="_FemaleAdjustRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ClipParamEndMotionFemale":RSZVariable(name="_ClipParamEndMotionFemale",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndSubMotionFemale":RSZVariable(name="_ClipParamEndSubMotionFemale",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WpActionData":RSZVariable(name="_WpActionData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WpChange":RSZVariable(name="_WpChange",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WpDrawOff":RSZVariable(name="_WpDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WpDrawOn":RSZVariable(name="_WpDrawOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ReserveWpDrawOff":RSZVariable(name="_ReserveWpDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ReserveWpDrawOn":RSZVariable(name="_ReserveWpDrawOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_HeadArmorDrawOff":RSZVariable(name="_HeadArmorDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_HeadArmorDrawOff_Food":RSZVariable(name="_HeadArmorDrawOff_Food",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_BodyArmorDrawOff":RSZVariable(name="_BodyArmorDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ArmCoverDrawOff":RSZVariable(name="_ArmCoverDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SlingerObjDrawOff":RSZVariable(name="_SlingerObjDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_InsectDrawOn":RSZVariable(name="_InsectDrawOn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TargetPorterIDVal":RSZVariable(name="_TargetPorterIDVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_RidingWpAttachType":RSZVariable(name="_RidingWpAttachType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorPlayer_ParamEndMotionFemale(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorPlayer.ParamEndMotionFemale",typeIDHash=0x18496cdc,CRC=0xcc9fa51a,isObject = True,tagList=[])
		self.fields = {
		"_MotionListFemale":RSZVariable(name="_MotionListFemale",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MotionConnectBankFemale":RSZVariable(name="_MotionConnectBankFemale",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_CharacterTimelineEventActorPlayer_ParamEndSubMotionFemale(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorPlayer.ParamEndSubMotionFemale",typeIDHash=0xda33f454,CRC=0x3c21e4d2,isObject = True,tagList=[])
		self.fields = {
		"SetID":RSZVariable(name="SetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"_MotionListFemale":RSZVariable(name="_MotionListFemale",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_CharacterTimelineEventActorPlayer_WpActionInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorPlayer.WpActionInfo",typeIDHash=0x41455cdd,CRC=0x1cd116f7,isObject = True,tagList=[])
		self.fields = {
		"WpCommonID":RSZVariable(name="WpCommonID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"JointMaskID":RSZVariable(name="JointMaskID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BlendRate":RSZVariable(name="BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsAction":RSZVariable(name="IsAction",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"FrameRate":RSZVariable(name="FrameRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorPorter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorPorter",typeIDHash=0x426a9bbc,CRC=0xb193e291,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipParamStartMotionSet":RSZVariable(name="_ClipParamStartMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamEndMotionSet":RSZVariable(name="_ClipParamEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CheckerFrame":RSZVariable(name="_CheckerFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnableIngameAdjust":RSZVariable(name="_EnableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableRootScaleDisable":RSZVariable(name="DisableRootScaleDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ToContinuance":RSZVariable(name="ToContinuance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WarpData":RSZVariable(name="_WarpData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandData":RSZVariable(name="_SandData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetData":RSZVariable(name="_WetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MadData":RSZVariable(name="_MadData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OilData":RSZVariable(name="_OilData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SnowData":RSZVariable(name="_SnowData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsEventObj":RSZVariable(name="IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ClothResetPose":RSZVariable(name="_ClothResetPose",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGpuClothCollision":RSZVariable(name="_ClipParamGpuClothCollision",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteMotionFrame":RSZVariable(name="_OverwriteMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceDisableIngameAdjust":RSZVariable(name="ForceDisableIngameAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StencilFadeTarget":RSZVariable(name="_StencilFadeTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableESIAllDisable":RSZVariable(name="_EnableESIAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverrideChainMotion":RSZVariable(name="_OverrideChainMotion",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstrainParentData":RSZVariable(name="_ConstrainParentData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsForceFixedMotion":RSZVariable(name="_IsForceFixedMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsForceNoneMotion":RSZVariable(name="_IsForceNoneMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableInterpolateMotion":RSZVariable(name="_EnableInterpolateMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableForceSkipMotion":RSZVariable(name="_DisableForceSkipMotion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceNextCutChainReset":RSZVariable(name="_ForceNextCutChainReset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndNextActionGUID":RSZVariable(name="_EndNextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"_SkipEndActionStopDisable":RSZVariable(name="_SkipEndActionStopDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionNextMoveStart":RSZVariable(name="_SkipEndActionNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SkipEndActionClothWarp":RSZVariable(name="_SkipEndActionClothWarp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionStartDisable":RSZVariable(name="_IsSkipEndMotionStartDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsSkipEndMotionAllDisable":RSZVariable(name="_IsSkipEndMotionAllDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionPosGroundAdjust":RSZVariable(name="_EndMotionPosGroundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EndMotionRotFlatQuat":RSZVariable(name="_EndMotionRotFlatQuat",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialSettingData":RSZVariable(name="_MaterialSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainReduceSettingData":RSZVariable(name="_ChainReduceSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChainStabilizeSettingData":RSZVariable(name="_ChainStabilizeSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NextActionVariationSettingData":RSZVariable(name="_NextActionVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshMaterialVariationSettingData":RSZVariable(name="_MeshMaterialVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartsVariationSettingData":RSZVariable(name="_PartsVariationSettingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SeamlessInRotateAdjustData":RSZVariable(name="_SeamlessInRotateAdjustData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiningJointOffsetData":RSZVariable(name="_DiningJointOffsetData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpDataWithBindEnd":RSZVariable(name="_WarpDataWithBindEnd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipParamGalleryEndMotionSet":RSZVariable(name="_ClipParamGalleryEndMotionSet",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GalleryStartMotionFrame":RSZVariable(name="_GalleryStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverrideStartMotionFrame":RSZVariable(name="_OverrideStartMotionFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EndSpeedSetting":RSZVariable(name="_EndSpeedSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ReinDrawOff":RSZVariable(name="_ReinDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SaddleDrawOff":RSZVariable(name="_SaddleDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ReinStableType":RSZVariable(name="_ReinStableType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_DisableGroundDetect":RSZVariable(name="_DisableGroundDetect",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CharacterTimelineEventActorPorter_EndSpeedSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CharacterTimelineEventActorPorter.EndSpeedSetting",typeIDHash=0xc5d25106,CRC=0xe8a4a3d0,isObject = True,tagList=[])
		self.fields = {
		"Speed":RSZVariable(name="Speed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"SpeedPrev":RSZVariable(name="SpeedPrev",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_ChatManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ChatManager",typeIDHash=0x757828f0,CRC=0x8029bbca,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ClothManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ClothManager",typeIDHash=0x8180deeb,CRC=0x3a7b1bb1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SettingBase":RSZVariable(name="_SettingBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_ClothSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ClothSetting",typeIDHash=0xf493f5a7,CRC=0x7c9234a,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WindSamplingPoint":RSZVariable(name="_WindSamplingPoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WindBias":RSZVariable(name="_WindBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsUpdateSelf":RSZVariable(name="_IsUpdateSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsWindRecieve":RSZVariable(name="_IsWindRecieve",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCullingEnable":RSZVariable(name="_IsCullingEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCreateVolumeOccludee":RSZVariable(name="_IsCreateVolumeOccludee",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_ClothSettingCollection(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ClothSettingCollection",typeIDHash=0xb3b3d390,CRC=0x65ca6fab,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WindSamplingPoint":RSZVariable(name="_WindSamplingPoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WindBias":RSZVariable(name="_WindBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsWindRecieve":RSZVariable(name="_IsWindRecieve",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCullingEnable":RSZVariable(name="_IsCullingEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCreateVolumeOccludee":RSZVariable(name="_IsCreateVolumeOccludee",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CloudScape2ParamTransition(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CloudScape2ParamTransition",typeIDHash=0x6fb1cae0,CRC=0xab4d6d1d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EnvChangeDatas":RSZVariable(name="_EnvChangeDatas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_JunctionChangeData":RSZVariable(name="_JunctionChangeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GameCountData":RSZVariable(name="_GameCountData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CloudScape2ParamTransition_cEnvChangeData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CloudScape2ParamTransition.cEnvChangeData",typeIDHash=0x1379757c,CRC=0xecd1880d,isObject = True,tagList=[])
		self.fields = {
		"_BlendGroupName":RSZVariable(name="_BlendGroupName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_TemporalBlendVal":RSZVariable(name="_TemporalBlendVal",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeInTime":RSZVariable(name="_FadeInTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CloudScape2ParamTransition_cGameCountData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CloudScape2ParamTransition.cGameCountData",typeIDHash=0xc63c59b,CRC=0x1d20ad79,isObject = True,tagList=[])
		self.fields = {
		"_StartCount":RSZVariable(name="_StartCount",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EndCount":RSZVariable(name="_EndCount",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_TemporalBlendVal":RSZVariable(name="_TemporalBlendVal",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeInTime":RSZVariable(name="_FadeInTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CloudScape2ParamTransition_cJunctionChangeData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CloudScape2ParamTransition.cJunctionChangeData",typeIDHash=0x82830347,CRC=0xc7aebce9,isObject = True,tagList=[])
		self.fields = {
		"_Enable":RSZVariable(name="_Enable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TemporalBlendVal":RSZVariable(name="_TemporalBlendVal",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TransitionTime":RSZVariable(name="_TransitionTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ProceedDiffThreshold":RSZVariable(name="_ProceedDiffThreshold",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_ColliderSwitcher(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ColliderSwitcher",typeIDHash=0xcde46068,CRC=0x3d62c58e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CollisionShapePresetController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CollisionShapePresetController",typeIDHash=0x278c2bbe,CRC=0x7d821629,isObject = True,tagList=[])
		self.fields = {
		"_Enabled":RSZVariable(name="_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VirtualGround":RSZVariable(name="_VirtualGround",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_ColorCorrectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ColorCorrectManager",typeIDHash=0x1c8b0491,CRC=0x2414c0c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ConcertLightController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ConcertLightController",typeIDHash=0x2181ab7a,CRC=0xeae5c4bc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_ConstraintLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ConstraintLight",typeIDHash=0xbe97c2e9,CRC=0x96b665c1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"UpdateTiming":RSZVariable(name="UpdateTiming",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"TargetGameObject":RSZVariable(name="TargetGameObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"IsApplyTargetRotate":RSZVariable(name="IsApplyTargetRotate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LightTargetGameObject":RSZVariable(name="LightTargetGameObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"IsLookAtLightTarget":RSZVariable(name="IsLookAtLightTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"EffectiveRangeRate":RSZVariable(name="EffectiveRangeRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsEnableEffectiveRangeRate":RSZVariable(name="IsEnableEffectiveRangeRate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LocalPositionOffset":RSZVariable(name="LocalPositionOffset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"LocalRotationOffset":RSZVariable(name="LocalRotationOffset",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		}

class app_ContentsManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ContentsManager",typeIDHash=0xb1c21975,CRC=0xf27736b1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ContextDynamicInstaintiateManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ContextDynamicInstaintiateManager",typeIDHash=0xb38b76cc,CRC=0x554c10b5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ContextInstantiateLimiter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ContextInstantiateLimiter",typeIDHash=0x7460ab4,CRC=0xecb35b80,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ContextLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ContextLayouter",typeIDHash=0x11cb8271,CRC=0x9b510496,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ContextEnabled":RSZVariable(name="_ContextEnabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_LayoutTypeEm":RSZVariable(name="_LayoutTypeEm",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_LayoutType":RSZVariable(name="_LayoutType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_ContextManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ContextManager",typeIDHash=0x1c023128,CRC=0x4d0e24c8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CrawlRoute(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CrawlRoute",typeIDHash=0x79af68ee,CRC=0xf747b8c9,isObject = True,tagList=[])
		self.fields = {
		"_RouteInfoList":RSZVariable(name="_RouteInfoList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CrawlRoute_cCrawlRouteInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CrawlRoute.cCrawlRouteInfo",typeIDHash=0xe134f07c,CRC=0x26f66d5f,isObject = True,tagList=[])
		self.fields = {
		"Point1Pos":RSZVariable(name="Point1Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Point2Pos":RSZVariable(name="Point2Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_CustomComputeShaderManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CustomComputeShaderManager",typeIDHash=0x8d8e81fb,CRC=0x35e521c5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CutSceneConstraintRoot(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneConstraintRoot",typeIDHash=0x6370464,CRC=0xd4ff02d3,isObject = True,tagList=[])
		self.fields = {
		}

class app_CutSceneEffectFrameSyncronizer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneEffectFrameSyncronizer",typeIDHash=0xbeff60a4,CRC=0xf9758976,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CutSceneEffectValiationController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneEffectValiationController",typeIDHash=0x13da2442,CRC=0x7ba709d8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EmitterCtrl":RSZVariable(name="_EmitterCtrl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EventID_Serializable":RSZVariable(name="_EventID_Serializable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CutSceneEffectValiationController_MeshMaterialEmitterControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneEffectValiationController.MeshMaterialEmitterControl",typeIDHash=0x34511ac9,CRC=0xb55af928,isObject = True,tagList=[])
		self.fields = {
		"_EmitterParamList":RSZVariable(name="_EmitterParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CutSceneEffectValiationController_MeshMaterialEmitterControl_EmitterParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneEffectValiationController.MeshMaterialEmitterControl.EmitterParam",typeIDHash=0xa3728413,CRC=0x65589b32,isObject = True,tagList=[])
		self.fields = {
		"VarParamList":RSZVariable(name="VarParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsOr":RSZVariable(name="IsOr",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Mesh":RSZVariable(name="Mesh",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"Material":RSZVariable(name="Material",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_CutSceneEffectValiationController_VariationParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneEffectValiationController.VariationParam",typeIDHash=0x3d8908e0,CRC=0x32c4cec8,isObject = True,tagList=[])
		self.fields = {
		"GroupId":RSZVariable(name="GroupId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"VariationId":RSZVariable(name="VariationId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CutSceneGalleryManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneGalleryManager",typeIDHash=0xd12b68ea,CRC=0x5f7f856d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_CutSceneItemListVariationController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneItemListVariationController",typeIDHash=0x7de061a4,CRC=0x689c20c6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID_Serializable":RSZVariable(name="_EventID_Serializable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MainItemParam":RSZVariable(name="_MainItemParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ItemParamList":RSZVariable(name="_ItemParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CutSceneItemListVariationController_ItemParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneItemListVariationController.ItemParam",typeIDHash=0x49a2526,CRC=0xc21c0407,isObject = True,tagList=[])
		self.fields = {
		"VarParamList":RSZVariable(name="VarParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TargetObj":RSZVariable(name="TargetObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"IsOr":RSZVariable(name="IsOr",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CutSceneItemListVariationController_VariationParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneItemListVariationController.VariationParam",typeIDHash=0xfb7663bb,CRC=0x9a816080,isObject = True,tagList=[])
		self.fields = {
		"GroupId":RSZVariable(name="GroupId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"VariationId":RSZVariable(name="VariationId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CutScenePropsController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutScenePropsController",typeIDHash=0xef8310b7,CRC=0xf076f46e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_CutSceneSettingList":RSZVariable(name="_CutSceneSettingList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CutScenePropsController_CutSceneSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutScenePropsController.CutSceneSetting",typeIDHash=0xe0622d16,CRC=0x9070f5d8,isObject = True,tagList=[])
		self.fields = {
		"NameHash":RSZVariable(name="NameHash",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CutSceneID_Serializable":RSZVariable(name="CutSceneID_Serializable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CutScenePropsControllerManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutScenePropsControllerManager",typeIDHash=0x6206499d,CRC=0xb6637887,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ClipHideControlParamList":RSZVariable(name="_ClipHideControlParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipStreamingControlParamList":RSZVariable(name="_ClipStreamingControlParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ClipEmissiveControlParamList":RSZVariable(name="_ClipEmissiveControlParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_CutScenePropsControllerManagerBase1_ClipEmissiveControlParamapp_CutScenePropsController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutScenePropsControllerManagerBase`1.ClipEmissiveControlParam<app.CutScenePropsController>",typeIDHash=0x61a0cae6,CRC=0x89b3c6ce,isObject = True,tagList=[])
		self.fields = {
		"TargetNameHash":RSZVariable(name="TargetNameHash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"EmissiveIntensity":RSZVariable(name="EmissiveIntensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EmissivePower":RSZVariable(name="EmissivePower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CutScenePropsControllerManagerBase1_ClipHideControlParamapp_CutScenePropsController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutScenePropsControllerManagerBase`1.ClipHideControlParam<app.CutScenePropsController>",typeIDHash=0x2a16791b,CRC=0x51c0f204,isObject = True,tagList=[])
		self.fields = {
		"TargetNameHash":RSZVariable(name="TargetNameHash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"IsVisible":RSZVariable(name="IsVisible",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_CutScenePropsControllerManagerBase1_ClipStreamingControlParamapp_CutScenePropsController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutScenePropsControllerManagerBase`1.ClipStreamingControlParam<app.CutScenePropsController>",typeIDHash=0x5af4577f,CRC=0x67e1af3d,isObject = True,tagList=[])
		self.fields = {
		"TargetNameHash":RSZVariable(name="TargetNameHash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_CutSceneZoneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.CutSceneZoneController",typeIDHash=0xa82304bd,CRC=0x5570315d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ColliderSetResourceHolder":RSZVariable(name="_ColliderSetResourceHolder",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_DLCStoreSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DLCStoreSceneController",typeIDHash=0x2c98130d,CRC=0xcc54e4e6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DefaultCameraTarget":RSZVariable(name="_DefaultCameraTarget",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		}

class app_DPGIParamTransition(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DPGIParamTransition",typeIDHash=0x838ebb22,CRC=0xcb8b1179,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EnvChangeDatas":RSZVariable(name="_EnvChangeDatas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_JunctionChangeData":RSZVariable(name="_JunctionChangeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LayerChangeDatas":RSZVariable(name="_LayerChangeDatas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GameCountDatas":RSZVariable(name="_GameCountDatas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_DPGIParamTransition_cEnvChangeData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DPGIParamTransition.cEnvChangeData",typeIDHash=0xa502c705,CRC=0xc4752a9b,isObject = True,tagList=[])
		self.fields = {
		"_NearDivisionNum":RSZVariable(name="_NearDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FarDivisionNum":RSZVariable(name="_FarDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_BlendGroupName":RSZVariable(name="_BlendGroupName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeInTime":RSZVariable(name="_FadeInTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_DPGIParamTransition_cGameCountData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DPGIParamTransition.cGameCountData",typeIDHash=0x68b1b9a1,CRC=0x31b013e4,isObject = True,tagList=[])
		self.fields = {
		"_NearDivisionNum":RSZVariable(name="_NearDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FarDivisionNum":RSZVariable(name="_FarDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_StartCount":RSZVariable(name="_StartCount",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EndCount":RSZVariable(name="_EndCount",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeInTime":RSZVariable(name="_FadeInTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_DPGIParamTransition_cJunctionChangeData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DPGIParamTransition.cJunctionChangeData",typeIDHash=0x4edf8ea,CRC=0x4f814a75,isObject = True,tagList=[])
		self.fields = {
		"_NearDivisionNum":RSZVariable(name="_NearDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FarDivisionNum":RSZVariable(name="_FarDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Enable":RSZVariable(name="_Enable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TransitionTime":RSZVariable(name="_TransitionTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ProceedDiffThreshold":RSZVariable(name="_ProceedDiffThreshold",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_DPGIParamTransition_cLayerChangeData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DPGIParamTransition.cLayerChangeData",typeIDHash=0x4889dc33,CRC=0xd94ea50c,isObject = True,tagList=[])
		self.fields = {
		"_NearDivisionNum":RSZVariable(name="_NearDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FarDivisionNum":RSZVariable(name="_FarDivisionNum",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_LabelName":RSZVariable(name="_LabelName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_TransitionTime":RSZVariable(name="_TransitionTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ProceedDiffThreshold":RSZVariable(name="_ProceedDiffThreshold",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_StayTime":RSZVariable(name="_StayTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_DelayJobManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DelayJobManager",typeIDHash=0x222a2ffd,CRC=0x538183fd,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_DemoMediator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DemoMediator",typeIDHash=0xeb47b4ae,CRC=0x81c040f2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_DialogueAfterCharacterControlManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DialogueAfterCharacterControlManager",typeIDHash=0x817afcf6,CRC=0xe47d2461,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_DialogueBeautyLightRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DialogueBeautyLightRegister",typeIDHash=0xdcaa6a,CRC=0x53b00dcf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_DialogueCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DialogueCatalog",typeIDHash=0x51a3b66c,CRC=0xd1389676,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ResourceArray":RSZVariable(name="_ResourceArray",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_DialogueCatalog_Resource(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DialogueCatalog.Resource",typeIDHash=0x3d62b4b7,CRC=0xca2762e5,isObject = True,tagList=[])
		self.fields = {
		"_Data":RSZVariable(name="_Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_DialogueManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DialogueManager",typeIDHash=0x7153f622,CRC=0x9c46d948,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ManagerSetting":RSZVariable(name="_ManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TimelineEventManager":RSZVariable(name="_TimelineEventManager",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RequestAbsorber":RSZVariable(name="_RequestAbsorber",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_DialogueResourceManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DialogueResourceManager",typeIDHash=0x7feee2f8,CRC=0x9f83292,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_DistanceFieldManagerController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DistanceFieldManagerController",typeIDHash=0x204cd1b3,CRC=0x34ec8818,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_DynamicProbeGIController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DynamicProbeGIController",typeIDHash=0x425bfbcb,CRC=0xd63f69a2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ForceDisableScreenProbe":RSZVariable(name="ForceDisableScreenProbe",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ForceLayer2Lighting":RSZVariable(name="ForceLayer2Lighting",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Layer2LightingBounds":RSZVariable(name="Layer2LightingBounds",dataType="obb",isList=True,alignment=16,value=None,tagSet=[]),
		}

class app_DynamicSingletonInstantiateManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.DynamicSingletonInstantiateManager",typeIDHash=0x69036ae0,CRC=0xc78ad7ce,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EggMaterialControllerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EggMaterialControllerSetting",typeIDHash=0xe75f4e6a,CRC=0xf07742a7,isObject = True,tagList=[])
		self.fields = {
		"_StartAlphaTestRef":RSZVariable(name="_StartAlphaTestRef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EndAlphaTestRef":RSZVariable(name="_EndAlphaTestRef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EmPropLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EmPropLayouter",typeIDHash=0xbe6bb856,CRC=0x25b5d906,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EmPropManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EmPropManager",typeIDHash=0x33652525,CRC=0x5d40151f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Config":RSZVariable(name="_Config",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_EnemyAreaMovePointLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyAreaMovePointLayouter",typeIDHash=0x8ef33ce3,CRC=0xef009c0f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnemyAreaMoveRouteLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyAreaMoveRouteLayouter",typeIDHash=0x51b26221,CRC=0xe1615fe2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnemyArenaStrollLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyArenaStrollLayouter",typeIDHash=0x2b5946fd,CRC=0xddfa9ba3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"EnemyCategory":RSZVariable(name="EnemyCategory",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EnemyCombatAreaMovePointLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyCombatAreaMovePointLayouter",typeIDHash=0xbc4628cc,CRC=0x36ce3944,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnemyCommonSceneActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyCommonSceneActivator",typeIDHash=0x18f01b3b,CRC=0xc511be33,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnemyLayoutSceneActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyLayoutSceneActivator",typeIDHash=0x3dfa86c5,CRC=0xc4eb40a0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnemyManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyManager",typeIDHash=0x5ec73d92,CRC=0x4860f13e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MudShellList":RSZVariable(name="_MudShellList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_EnemyPackageCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyPackageCatalog",typeIDHash=0x826a2aee,CRC=0x6e78ea25,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EnemyPackageList":RSZVariable(name="_EnemyPackageList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_EnemyScarBabSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyScarBabSetting",typeIDHash=0x12e6c29f,CRC=0xd1c9919a,isObject = True,tagList=[])
		self.fields = {
		"_ScarBabResource":RSZVariable(name="_ScarBabResource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MaxInstanceNum":RSZVariable(name="_MaxInstanceNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaxScarNum":RSZVariable(name="_MaxScarNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_ScarParamNam":RSZVariable(name="_ScarParamNam",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_UseCommonParamLength":RSZVariable(name="_UseCommonParamLength",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EnemyStrollLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyStrollLayouter",typeIDHash=0xc0aee5d7,CRC=0x7719378f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StageKind":RSZVariable(name="_StageKind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"EnemyCategory":RSZVariable(name="EnemyCategory",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EnemyTargetLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyTargetLayouter",typeIDHash=0x6b552430,CRC=0x934a340b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StageKind":RSZVariable(name="_StageKind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DataCategory":RSZVariable(name="_DataCategory",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnemyCategory":RSZVariable(name="_EnemyCategory",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EnemyWorldAnalyzer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnemyWorldAnalyzer",typeIDHash=0x4e59c31f,CRC=0xdfa3722c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnvBABUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnvBABUpdater",typeIDHash=0xde2aedde,CRC=0xeb34ef9e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_BAB":RSZVariable(name="_BAB",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_EnvMaterialData":RSZVariable(name="_EnvMaterialData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ShaderTimerData":RSZVariable(name="_ShaderTimerData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_EnvironmentEffectControlManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnvironmentEffectControlManager",typeIDHash=0xc688bef,CRC=0x4f2aba3b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EnvironmentEffectController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnvironmentEffectController",typeIDHash=0x8cfcd124,CRC=0x7ad201fd,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"EmitTimeDataList":RSZVariable(name="EmitTimeDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EnvironmentEffectController_EmitTimeData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnvironmentEffectController.EmitTimeData",typeIDHash=0xd7b71855,CRC=0x7c3f8643,isObject = True,tagList=[])
		self.fields = {
		"_UseType":RSZVariable(name="_UseType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"StartTime_Hour":RSZVariable(name="StartTime_Hour",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"StartTime_Minutes":RSZVariable(name="StartTime_Minutes",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"StartTime_Second":RSZVariable(name="StartTime_Second",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"EndTime_Hour":RSZVariable(name="EndTime_Hour",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"EndTime_Minutes":RSZVariable(name="EndTime_Minutes",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"EndTime_Second":RSZVariable(name="EndTime_Second",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"Weather":RSZVariable(name="Weather",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"SpeicalCondition":RSZVariable(name="SpeicalCondition",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"HowToFinish":RSZVariable(name="HowToFinish",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"AppearTime":RSZVariable(name="AppearTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"VanishTime":RSZVariable(name="VanishTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"AllElement":RSZVariable(name="AllElement",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ElementIDBit":RSZVariable(name="ElementIDBit",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EnvironmentManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EnvironmentManager",typeIDHash=0x9a226565,CRC=0x19113eaf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvSectionUserData":RSZVariable(name="_EnvSectionUserData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvSectionParamUserData":RSZVariable(name="_EnvSectionParamUserData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_EquipLightController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EquipLightController",typeIDHash=0x40ce30f4,CRC=0x4bb8b4e8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EventCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventCatalog",typeIDHash=0xd68f5530,CRC=0xf0c54322,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_KeyName":RSZVariable(name="_KeyName",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Kind":RSZVariable(name="_Kind",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EventList":RSZVariable(name="_EventList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EventResourceList":RSZVariable(name="_EventResourceList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_EventClipActionCommon(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon",typeIDHash=0x758b15ee,CRC=0x83643bdb,isObject = True,tagList=[])
		self.fields = {
		"_FadeParam":RSZVariable(name="_FadeParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SkipRenderCut":RSZVariable(name="_SkipRenderCut",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PlayMovie":RSZVariable(name="_PlayMovie",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MovieFade":RSZVariable(name="_MovieFade",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ChangeWorkRate":RSZVariable(name="_ChangeWorkRate",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StartFsm":RSZVariable(name="_StartFsm",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ReTargetPauseObj":RSZVariable(name="_ReTargetPauseObj",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AllChainReduce":RSZVariable(name="_AllChainReduce",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CameraCancelPLMove":RSZVariable(name="_CameraCancelPLMove",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RequestPadVibration":RSZVariable(name="_RequestPadVibration",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SetEventOffset":RSZVariable(name="_SetEventOffset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DisableEventOffset":RSZVariable(name="_DisableEventOffset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AllActorStain":RSZVariable(name="_AllActorStain",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MotionFrameAdjust":RSZVariable(name="_MotionFrameAdjust",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TimelineNodeRebind":RSZVariable(name="_TimelineNodeRebind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TimelineRebind":RSZVariable(name="_TimelineRebind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NonActorVisible":RSZVariable(name="_NonActorVisible",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SpeedTreeControl":RSZVariable(name="_SpeedTreeControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DisableRenderCutScene":RSZVariable(name="_DisableRenderCutScene",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverwriteSynchroFrame":RSZVariable(name="_OverwriteSynchroFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DisableFrameGeneration":RSZVariable(name="_DisableFrameGeneration",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EventCameraControl":RSZVariable(name="_EventCameraControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionCommon_AllActorStain(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.AllActorStain",typeIDHash=0x60e1ab19,CRC=0x7722da74,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SandEnable":RSZVariable(name="_SandEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SandRate":RSZVariable(name="_SandRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WetEnable":RSZVariable(name="_WetEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WetRate":RSZVariable(name="_WetRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MadEnable":RSZVariable(name="_MadEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MadRate":RSZVariable(name="_MadRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OilEnable":RSZVariable(name="_OilEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OilRate":RSZVariable(name="_OilRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SnowEnable":RSZVariable(name="_SnowEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SnowRate":RSZVariable(name="_SnowRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_AllChainReduce(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.AllChainReduce",typeIDHash=0x8777c7b8,CRC=0x903b94e0,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UseIdSetting":RSZVariable(name="_UseIdSetting",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"UseAllActorReduceObj":RSZVariable(name="UseAllActorReduceObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_CameraCancelPLMove(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.CameraCancelPLMove",typeIDHash=0x7be94464,CRC=0xa71dcb8,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_ChangeWorkRate(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.ChangeWorkRate",typeIDHash=0x2d44e12c,CRC=0x3364b334,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EnableCurveRate":RSZVariable(name="EnableCurveRate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"CurveRate":RSZVariable(name="CurveRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DisableWorkRate":RSZVariable(name="DisableWorkRate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_DisableEventOffset(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.DisableEventOffset",typeIDHash=0x7763632b,CRC=0x7aee8a04,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_DisableFrameGeneration(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.DisableFrameGeneration",typeIDHash=0xc950120a,CRC=0x4466c5c7,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_DisableRenderCutScene(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.DisableRenderCutScene",typeIDHash=0x19073002,CRC=0xbc6a26ad,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_EventCameraControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.EventCameraControl",typeIDHash=0x55cb083a,CRC=0xae269cb0,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ForceEventCameraDisable":RSZVariable(name="_ForceEventCameraDisable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_FadeParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.FadeParam",typeIDHash=0xe0574905,CRC=0xee0c73d7,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"FadeRate":RSZVariable(name="FadeRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsPlayableFade":RSZVariable(name="IsPlayableFade",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Type":RSZVariable(name="Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsSkipExecuteFade":RSZVariable(name="_IsSkipExecuteFade",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_MotionFrameAdjust(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.MotionFrameAdjust",typeIDHash=0x969b175e,CRC=0x11105c55,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableRoundAdjust":RSZVariable(name="_EnableRoundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableRoundAdjust":RSZVariable(name="_DisableRoundAdjust",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_MovieFadeParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.MovieFadeParam",typeIDHash=0x2291d9dc,CRC=0xff0572d8,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"FadeRate":RSZVariable(name="FadeRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_NonActorVisible(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.NonActorVisible",typeIDHash=0x9176b01e,CRC=0x3a2fb055,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsVisible":RSZVariable(name="_IsVisible",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_OverwriteSynchroFrame(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.OverwriteSynchroFrame",typeIDHash=0xe6d30e21,CRC=0xccb4c00b,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverwriteFrame":RSZVariable(name="_OverwriteFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_PlayMovieParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.PlayMovieParam",typeIDHash=0xe10d865e,CRC=0xe3eaf0c6,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsPreLoad":RSZVariable(name="IsPreLoad",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Resource":RSZVariable(name="Resource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"Frame":RSZVariable(name="Frame",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"StartWithFade":RSZVariable(name="StartWithFade",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_ReTargetPauseObj(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.ReTargetPauseObj",typeIDHash=0x433c0475,CRC=0xbab39e07,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_RequestPadVibration(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.RequestPadVibration",typeIDHash=0x90b64e24,CRC=0x1b8f7e98,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VibrationParam":RSZVariable(name="_VibrationParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ForceClipVib":RSZVariable(name="_ForceClipVib",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_SetEventOffset(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.SetEventOffset",typeIDHash=0xad7d0a21,CRC=0x1a61153b,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OffsetPos":RSZVariable(name="_OffsetPos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_OffsetRot":RSZVariable(name="_OffsetRot",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		}

class app_EventClipActionCommon_SkipRenderCut(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.SkipRenderCut",typeIDHash=0xd97d7f4d,CRC=0xf8c8a56c,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_SpeedTreeControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.SpeedTreeControl",typeIDHash=0x27cbee40,CRC=0x9df49fc8,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_OverwriteLodBias":RSZVariable(name="_OverwriteLodBias",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_OverwriteCullingDispSize":RSZVariable(name="_OverwriteCullingDispSize",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_StartFsm(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.StartFsm",typeIDHash=0x4854401d,CRC=0xa359d08a,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"FsmId":RSZVariable(name="FsmId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_TimelineNodeRebind(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.TimelineNodeRebind",typeIDHash=0x83627bd0,CRC=0x6651da37,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ObjectName":RSZVariable(name="ObjectName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"NodeType":RSZVariable(name="NodeType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionCommon_TimelineRebind(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionCommon.TimelineRebind",typeIDHash=0x751e67c1,CRC=0x4ba49174,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableCharaSetup":RSZVariable(name="_DisableCharaSetup",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionEffect(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionEffect",typeIDHash=0x3c501777,CRC=0xa286ff8d,isObject = True,tagList=[])
		self.fields = {
		"_DisableESI":RSZVariable(name="_DisableESI",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DisableGroundSurfaceTrail":RSZVariable(name="_DisableGroundSurfaceTrail",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionEffect_DisableESI(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionEffect.DisableESI",typeIDHash=0xc87133aa,CRC=0x57264d7f,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionEffect_DisableGroundSurfaceTrail(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionEffect.DisableGroundSurfaceTrail",typeIDHash=0xb6ef485a,CRC=0xac850d54,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionEnemy(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionEnemy",typeIDHash=0xda24c6d5,CRC=0x8d2890ec,isObject = True,tagList=[])
		self.fields = {
		"ClipActionHideEmProps":RSZVariable(name="ClipActionHideEmProps",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionEnemy_ClipActionHideEmProp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionEnemy.ClipActionHideEmProp",typeIDHash=0xe734c58c,CRC=0x9182d9f5,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetEmPropID":RSZVariable(name="TargetEmPropID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ZoneEnable":RSZVariable(name="ZoneEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Zone":RSZVariable(name="Zone",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Sphere']),
		}

class app_EventClipActionGUI(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI",typeIDHash=0x24079fb3,CRC=0xd84e8e9f,isObject = True,tagList=[])
		self.fields = {
		"_DispGUI":RSZVariable(name="_DispGUI",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnemyNameGUIParam":RSZVariable(name="_EnemyNameGUIParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NpcNameGUIParam":RSZVariable(name="_NpcNameGUIParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AreaNameGUIParam":RSZVariable(name="_AreaNameGUIParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Evc0001SubTitleParam":RSZVariable(name="_Evc0001SubTitleParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StencilFadeParam":RSZVariable(name="_StencilFadeParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SetBlurParam":RSZVariable(name="_SetBlurParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TitleLogo":RSZVariable(name="_TitleLogo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StaffRoll00Param":RSZVariable(name="_StaffRoll00Param",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StaffRoll01Param":RSZVariable(name="_StaffRoll01Param",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StaffRoll02Param":RSZVariable(name="_StaffRoll02Param",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StaffRoll03Param":RSZVariable(name="_StaffRoll03Param",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionGUI_AreaNameGUIParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.AreaNameGUIParam",typeIDHash=0x8e0bd61a,CRC=0x88f5c9f5,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"StageType":RSZVariable(name="StageType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"LifeAreaType":RSZVariable(name="LifeAreaType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_DispGUI(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.DispGUI",typeIDHash=0x9a3f0a89,CRC=0x4fbd09fa,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GUILinkTypeVal":RSZVariable(name="GUILinkTypeVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"DisableInGallery":RSZVariable(name="DisableInGallery",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"BrightnessAdjustmentForOverlay":RSZVariable(name="BrightnessAdjustmentForOverlay",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"SaturateAdjustmentForOverlay":RSZVariable(name="SaturateAdjustmentForOverlay",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_EnemyNameGUIParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.EnemyNameGUIParam",typeIDHash=0xffffa069,CRC=0x4ca4c370,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"EmIDVal":RSZVariable(name="EmIDVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RoleId":RSZVariable(name="RoleId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"AlignType":RSZVariable(name="AlignType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Pos":RSZVariable(name="Pos",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_Evc0001SubTitleParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.Evc0001SubTitleParam",typeIDHash=0xa77d5030,CRC=0x32a8a9f1,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"CloseOnly":RSZVariable(name="CloseOnly",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_NpcNameGUIParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.NpcNameGUIParam",typeIDHash=0xbfd82a9d,CRC=0xc28cf754,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"NpcIDVal":RSZVariable(name="NpcIDVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Pos":RSZVariable(name="Pos",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_SetBlurParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.SetBlurParam",typeIDHash=0xfc1aca8e,CRC=0x7dbc4e7c,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsBlurEnable":RSZVariable(name="IsBlurEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_StaffRoll00Param(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.StaffRoll00Param",typeIDHash=0x17fe177d,CRC=0x4ca32808,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroupNo":RSZVariable(name="GroupNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Pos":RSZVariable(name="Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_StaffRoll01Param(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.StaffRoll01Param",typeIDHash=0x42a1987f,CRC=0xe04b38f4,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroupNo":RSZVariable(name="GroupNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_StaffRoll02Param(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.StaffRoll02Param",typeIDHash=0xef261d45,CRC=0xbe08d94c,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Time":RSZVariable(name="Time",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Rate":RSZVariable(name="Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_StaffRoll03Param(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.StaffRoll03Param",typeIDHash=0x4802a356,CRC=0xf9c4fb56,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroupNo":RSZVariable(name="GroupNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Pos":RSZVariable(name="Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_StencilFadeParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.StencilFadeParam",typeIDHash=0x1bbc0109,CRC=0x70782d9c,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"FadeRate":RSZVariable(name="FadeRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionGUI_TitleLogo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGUI.TitleLogo",typeIDHash=0x79d9191f,CRC=0x7116b159,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick",typeIDHash=0x6f54fe95,CRC=0x530f12cd,isObject = True,tagList=[])
		self.fields = {
		"Gm004_Shake":RSZVariable(name="Gm004_Shake",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm003_Lightning":RSZVariable(name="Gm003_Lightning",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm002_DisableDragParam":RSZVariable(name="Gm002_DisableDragParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm400_025_CtrlParam":RSZVariable(name="Gm400_025_CtrlParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm558_CtrlParam":RSZVariable(name="Gm558_CtrlParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GimmickDrawOffParam":RSZVariable(name="GimmickDrawOffParam",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GimmickDisableParam":RSZVariable(name="GimmickDisableParam",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm002_DisableParam":RSZVariable(name="Gm002_DisableParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm564_SetPendulumParam":RSZVariable(name="Gm564_SetPendulumParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"DummyInTentParam":RSZVariable(name="DummyInTentParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gm656_StateChangeParam":RSZVariable(name="Gm656_StateChangeParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionGimmick_DummyInTent(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.DummyInTent",typeIDHash=0xbab4fcef,CRC=0xc989a131,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_GimmickDisable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.GimmickDisable",typeIDHash=0xd90d0d98,CRC=0xdde8b50d,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_Target":RSZVariable(name="_Target",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Zone":RSZVariable(name="_Zone",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Sphere']),
		}

class app_EventClipActionGimmick_GimmickDrawOff(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.GimmickDrawOff",typeIDHash=0x1606ed23,CRC=0x69762931,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_Target":RSZVariable(name="_Target",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Zone":RSZVariable(name="_Zone",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Sphere']),
		}

class app_EventClipActionGimmick_Gm002_Disable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm002_Disable",typeIDHash=0x55a63b3,CRC=0x79701a86,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_Target":RSZVariable(name="_Target",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Zone":RSZVariable(name="_Zone",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Sphere']),
		"_DisableTime":RSZVariable(name="_DisableTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm002_DisableDrag(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm002_DisableDrag",typeIDHash=0x63ae6947,CRC=0xdfa99017,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEnableLightning":RSZVariable(name="IsEnableLightning",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm003_LightningParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm003_LightningParam",typeIDHash=0x7a66b412,CRC=0x76f1d966,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEnableLightning":RSZVariable(name="IsEnableLightning",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm004_ShakeParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm004_ShakeParam",typeIDHash=0x23118c70,CRC=0xd4fd9bf0,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEnableShake":RSZVariable(name="IsEnableShake",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm400_025_Ctrl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm400_025_Ctrl",typeIDHash=0xfc9fc46b,CRC=0x81fb4606,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableBarrel":RSZVariable(name="DisableBarrel",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableHammer":RSZVariable(name="DisableHammer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm558_Ctrl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm558_Ctrl",typeIDHash=0x80bd9f0d,CRC=0x273b6cd4,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableCrush":RSZVariable(name="DisableCrush",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisableWater":RSZVariable(name="DisableWater",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm564_SetPendulum(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm564_SetPendulum",typeIDHash=0x8a0a9849,CRC=0xbb1f6352,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisablePendulum":RSZVariable(name="DisablePendulum",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionGimmick_Gm656_StateChange(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionGimmick.Gm656_StateChange",typeIDHash=0xf74c8c46,CRC=0x4df53c38,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionManager",typeIDHash=0xafc41f3,CRC=0xeb31cc98,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ParamText":RSZVariable(name="_ParamText",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamCommon":RSZVariable(name="_ParamCommon",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamPl":RSZVariable(name="_ParamPl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamEm":RSZVariable(name="_ParamEm",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamNpc":RSZVariable(name="_ParamNpc",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamGUI":RSZVariable(name="_ParamGUI",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamStage":RSZVariable(name="_ParamStage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamGimmick":RSZVariable(name="_ParamGimmick",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamStory":RSZVariable(name="_ParamStory",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ParamEffect":RSZVariable(name="_ParamEffect",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsEnableAction":RSZVariable(name="_IsEnableAction",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionNpc(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionNpc",typeIDHash=0x1e239d24,CRC=0x685df8df,isObject = True,tagList=[])
		self.fields = {
		"_AddObstaclePoint":RSZVariable(name="_AddObstaclePoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionNpc_AddObstaclePoint(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionNpc.AddObstaclePoint",typeIDHash=0xfc939513,CRC=0xa9717926,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"NpcID":RSZVariable(name="NpcID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Pos":RSZVariable(name="_Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_Rad":RSZVariable(name="_Rad",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionPlayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionPlayer",typeIDHash=0x7ea48514,CRC=0x55156e69,isObject = True,tagList=[])
		self.fields = {
		"_SetSlingerParam":RSZVariable(name="_SetSlingerParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ContinueBonFire":RSZVariable(name="_ContinueBonFire",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionPlayer_ContinueBonFire(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionPlayer.ContinueBonFire",typeIDHash=0x4ed28bf,CRC=0xa7386a49,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionPlayer_SetSlingerParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionPlayer.SetSlingerParam",typeIDHash=0xd8185b6d,CRC=0x831f109b,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"AmmoType":RSZVariable(name="AmmoType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"AmmoNum":RSZVariable(name="AmmoNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStage(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage",typeIDHash=0xeec905fc,CRC=0xd1a396df,isObject = True,tagList=[])
		self.fields = {
		"SetEnvironment":RSZVariable(name="SetEnvironment",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SetTime":RSZVariable(name="SetTime",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SetSandStorm":RSZVariable(name="SetSandStorm",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"PauseSandStorm":RSZVariable(name="PauseSandStorm",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SetSand":RSZVariable(name="SetSand",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"WindFlag":RSZVariable(name="WindFlag",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"StageLoad":RSZVariable(name="StageLoad",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SetFieldLoadPosition":RSZVariable(name="SetFieldLoadPosition",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"StageSwitch":RSZVariable(name="StageSwitch",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionStage_PauseSandStormParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.PauseSandStormParam",typeIDHash=0x129ae855,CRC=0xec350245,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionStage_SetEnvironmentParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.SetEnvironmentParam",typeIDHash=0x1ede20e3,CRC=0x49b49292,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"EnvironmentTypeID":RSZVariable(name="EnvironmentTypeID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BlendRate":RSZVariable(name="BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStage_SetFieldLoadPositionParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.SetFieldLoadPositionParam",typeIDHash=0x300732e7,CRC=0x7ab5712b,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsAdd":RSZVariable(name="_IsAdd",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_Pos":RSZVariable(name="_Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_EventClipActionStage_SetSandParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.SetSandParam",typeIDHash=0xc195f4c6,CRC=0xf50088e0,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroundChangePos":RSZVariable(name="GroundChangePos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_EventClipActionStage_SetSandStormParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.SetSandStormParam",typeIDHash=0xcf3bb6b4,CRC=0xec5adc9b,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEnableSandStorm":RSZVariable(name="IsEnableSandStorm",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SandStormType":RSZVariable(name="_SandStormType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionStage_SetTimeParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.SetTimeParam",typeIDHash=0xa130c9b4,CRC=0xc46cdc34,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Time":RSZVariable(name="Time",dataType="int3",isList=False,alignment=4,value=None,tagSet=[]),
		"IsChangeEnv":RSZVariable(name="IsChangeEnv",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionStage_SetWindFlag(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.SetWindFlag",typeIDHash=0xa99fd4ae,CRC=0x4da6279b,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableGPUFlag":RSZVariable(name="_DisableGPUFlag",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableFlag":RSZVariable(name="_DisableFlag",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionStage_StageLoadParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.StageLoadParam",typeIDHash=0xcd6bb384,CRC=0x82bebe80,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"stageId":RSZVariable(name="stageId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStage_StageSwitchParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStage.StageSwitchParam",typeIDHash=0x6682b12e,CRC=0x25c97020,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"switchId":RSZVariable(name="switchId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStory(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory",typeIDHash=0x8b317822,CRC=0x658b3d51,isObject = True,tagList=[])
		self.fields = {
		"SendStoryGameMessage":RSZVariable(name="SendStoryGameMessage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SetStoryEventFlag":RSZVariable(name="SetStoryEventFlag",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SwitchPrologueStage":RSZVariable(name="SwitchPrologueStage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CloseDummyUI":RSZVariable(name="CloseDummyUI",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TitleLoadCheck":RSZVariable(name="TitleLoadCheck",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TitleLoadCutSkip":RSZVariable(name="TitleLoadCutSkip",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TitleFieldDrawOn":RSZVariable(name="TitleFieldDrawOn",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionStory_CloseDummyUIParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.CloseDummyUIParam",typeIDHash=0xe113e3d2,CRC=0xb07e5933,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionStory_SendStoryGameMessageParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.SendStoryGameMessageParam",typeIDHash=0xbab0d22e,CRC=0x816cdd6f,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GameMessageIndex":RSZVariable(name="GameMessageIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStory_SetStoryEventFlagParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.SetStoryEventFlagParam",typeIDHash=0xeda2c3ff,CRC=0x2ede8f,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Param":RSZVariable(name="Param",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionStory_StoryFlagParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.StoryFlagParam",typeIDHash=0x50cd9464,CRC=0xb841317b,isObject = True,tagList=[])
		self.fields = {
		"MissionID":RSZVariable(name="MissionID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"FlagNo":RSZVariable(name="FlagNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"FlagVal":RSZVariable(name="FlagVal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionStory_SwitchPrologueStageParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.SwitchPrologueStageParam",typeIDHash=0x987c50f0,CRC=0x19cc60ee,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ActionType":RSZVariable(name="ActionType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStory_TitleFieldDrawOnParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.TitleFieldDrawOnParam",typeIDHash=0xc5ccce4b,CRC=0xe94e3395,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableNextUpdate":RSZVariable(name="_EnableNextUpdate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionStory_TitleLoadCheckParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.TitleLoadCheckParam",typeIDHash=0x3d51c65e,CRC=0xcf565351,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_Type":RSZVariable(name="_Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_LoopCutNo":RSZVariable(name="_LoopCutNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventClipActionStory_TitleLoadCutSkipParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionStory.TitleLoadCutSkipParam",typeIDHash=0x32016de7,CRC=0x7ed87770,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventClipActionText(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionText",typeIDHash=0xb3f705dd,CRC=0xe565ae27,isObject = True,tagList=[])
		self.fields = {
		"_DispText":RSZVariable(name="_DispText",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventClipActionText_DispText(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventClipActionText.DispText",typeIDHash=0x6e21b044,CRC=0x8eea491d,isObject = True,tagList=[])
		self.fields = {
		"EventIdVal":RSZVariable(name="EventIdVal",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"isEnable":RSZVariable(name="isEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ActorType":RSZVariable(name="ActorType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"NpcId":RSZVariable(name="NpcId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"MessageId":RSZVariable(name="MessageId",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"OverRideNameGuid":RSZVariable(name="OverRideNameGuid",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"isClosedCaption":RSZVariable(name="isClosedCaption",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisplayLanguage":RSZVariable(name="DisplayLanguage",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventConditionManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventConditionManager",typeIDHash=0xf6e39e2a,CRC=0xba4f2cc6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EventEffectBreathController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventEffectBreathController",typeIDHash=0xd0f383ec,CRC=0x82240d39,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_RequestParam":RSZVariable(name="_RequestParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OverrideEfcPrefab":RSZVariable(name="_OverrideEfcPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventEffectBreathController_RequestParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventEffectBreathController.RequestParam",typeIDHash=0xfb195d04,CRC=0x992d2f57,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ElementID":RSZVariable(name="ElementID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsOffsetEnable":RSZVariable(name="IsOffsetEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Offset":RSZVariable(name="Offset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"IsOverrideDistanceEnable":RSZVariable(name="IsOverrideDistanceEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"OverrideDistance":RSZVariable(name="OverrideDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EventColor":RSZVariable(name="EventColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"EventScale":RSZVariable(name="EventScale",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"EventRotation":RSZVariable(name="EventRotation",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"SimpleExternParameter":RSZVariable(name="SimpleExternParameter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ExternParameters":RSZVariable(name="ExternParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventEffectBreathController_SimpleExternParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventEffectBreathController.SimpleExternParam",typeIDHash=0x5e1273f4,CRC=0xd6ce1a54,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Name":RSZVariable(name="Name",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"FloatValue":RSZVariable(name="FloatValue",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventEffectControlManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventEffectControlManager",typeIDHash=0x96c13e33,CRC=0x23011e36,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_BreathControl":RSZVariable(name="_BreathControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventEffectRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventEffectRegister",typeIDHash=0xa8cb7b5a,CRC=0x7dba308,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID":RSZVariable(name="_EventID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventEffectTextureStreaming(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventEffectTextureStreaming",typeIDHash=0x5a68634d,CRC=0x7713ada1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_EventFoliageHide(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventFoliageHide",typeIDHash=0x39ae23f5,CRC=0xb78bf8d2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_IsHide":RSZVariable(name="_IsHide",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventFoliageHideController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventFoliageHideController",typeIDHash=0x60e4e5a3,CRC=0x202e951d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID_Serializable":RSZVariable(name="_EventID_Serializable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EventFsmController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventFsmController",typeIDHash=0x20cd73b3,CRC=0x2d1117af,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_FsmType":RSZVariable(name="_FsmType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EventID_Serializable":RSZVariable(name="_EventID_Serializable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FlowID":RSZVariable(name="_FlowID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_BindTargetDataList":RSZVariable(name="_BindTargetDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LimitCamera":RSZVariable(name="_LimitCamera",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_CameraType":RSZVariable(name="_CameraType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_LimitYaw":RSZVariable(name="_LimitYaw",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_LimitPitch":RSZVariable(name="_LimitPitch",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Time":RSZVariable(name="_Time",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TargetObject":RSZVariable(name="_TargetObject",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Pos":RSZVariable(name="_Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_YawOffset":RSZVariable(name="_YawOffset",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_PitchOffset":RSZVariable(name="_PitchOffset",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsEnableCameraAttachParam":RSZVariable(name="_IsEnableCameraAttachParam",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventFsmController_BindTargetData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventFsmController.BindTargetData",typeIDHash=0x2ada58b4,CRC=0xa8bc7fc8,isObject = True,tagList=[])
		self.fields = {
		"TargetNameHash":RSZVariable(name="TargetNameHash",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"FsmResource":RSZVariable(name="FsmResource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"IsMainFsm":RSZVariable(name="IsMainFsm",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetTreeIndex":RSZVariable(name="TargetTreeIndex",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"IsRestart":RSZVariable(name="IsRestart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEnd":RSZVariable(name="IsEnd",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventGalleryFsmController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventGalleryFsmController",typeIDHash=0xea9b2147,CRC=0x713c19e6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID_Serializable":RSZVariable(name="_EventID_Serializable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_createContextLayout":RSZVariable(name="_createContextLayout",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventLightConstraintSetter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventLightConstraintSetter",typeIDHash=0x840f9bf,CRC=0x72bd059b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TargetParentObject":RSZVariable(name="_TargetParentObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_TargetName":RSZVariable(name="_TargetName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsBindActor":RSZVariable(name="_IsBindActor",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_BindTargetName":RSZVariable(name="_BindTargetName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_ActorType":RSZVariable(name="_ActorType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventLightController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventLightController",typeIDHash=0x39449b45,CRC=0x5eca8179,isObject = True,tagList=[])
		self.fields = {
		}

class app_EventModelSetupper(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventModelSetupper",typeIDHash=0xb3f883c9,CRC=0x3200375a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID":RSZVariable(name="_EventID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ModelPartsData":RSZVariable(name="_ModelPartsData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SetupType":RSZVariable(name="_SetupType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PtID":RSZVariable(name="_PtID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PtTypeSerialize":RSZVariable(name="_PtTypeSerialize",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NpcID":RSZVariable(name="_NpcID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ModelMaterialResDefaultID":RSZVariable(name="ModelMaterialResDefaultID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ModelMaterialDefaultID":RSZVariable(name="ModelMaterialDefaultID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PlSubSkeletonResource":RSZVariable(name="_PlSubSkeletonResource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_PlSubJointResource":RSZVariable(name="_PlSubJointResource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_TitleMode":RSZVariable(name="_TitleMode",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_FoodMode":RSZVariable(name="_FoodMode",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_PhobiaOptionTarget":RSZVariable(name="_PhobiaOptionTarget",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_EventModelSetupper_ModelPartsData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventModelSetupper.ModelPartsData",typeIDHash=0x110056f1,CRC=0xafe07c86,isObject = True,tagList=[])
		self.fields = {
		"_BodyTarget":RSZVariable(name="_BodyTarget",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_FaceTarget":RSZVariable(name="_FaceTarget",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_FaceTargetSubList":RSZVariable(name="_FaceTargetSubList",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_ModelPartsId":RSZVariable(name="_ModelPartsId",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		}

class app_EventOffsetPositionRoot(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventOffsetPositionRoot",typeIDHash=0x868b1f9a,CRC=0xa6cbdf1f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventIDFixed":RSZVariable(name="_EventIDFixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EventSimulationEffectSetupper(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EventSimulationEffectSetupper",typeIDHash=0x79324cb0,CRC=0xbe70ea7d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_Evm110(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Evm110",typeIDHash=0x9f6c42c8,CRC=0x4eaed344,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventId_Fixed":RSZVariable(name="_EventId_Fixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ChabashiraRate":RSZVariable(name="ChabashiraRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_Evm170(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Evm170",typeIDHash=0xffbc9c19,CRC=0xec3b9dff,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventId_Fixed":RSZVariable(name="_EventId_Fixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_Evm303(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Evm303",typeIDHash=0x84c8680e,CRC=0x4b5bfcf8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventId_Fixed":RSZVariable(name="_EventId_Fixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"TargetObj":RSZVariable(name="TargetObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		}

class app_Evm321(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Evm321",typeIDHash=0x79b1dca7,CRC=0xb1834773,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventId_Fixed":RSZVariable(name="_EventId_Fixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_EvmRope(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EvmRope",typeIDHash=0x266e8832,CRC=0x5746ae75,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventId_Fixed":RSZVariable(name="_EventId_Fixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsNoPl":RSZVariable(name="_IsNoPl",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VisualDataList":RSZVariable(name="_VisualDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_EvmRope_VisualData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EvmRope.VisualData",typeIDHash=0xc2748d5d,CRC=0xc53e5c80,isObject = True,tagList=[])
		self.fields = {
		"ArmorSeries_Fixed":RSZVariable(name="ArmorSeries_Fixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"GenderType":RSZVariable(name="GenderType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"MeshRes":RSZVariable(name="MeshRes",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"MaterialRes":RSZVariable(name="MaterialRes",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"EfcRes":RSZVariable(name="EfcRes",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_EvmZoneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.EvmZoneController",typeIDHash=0x50fff4,CRC=0x13e3ac8b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_FacialController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FacialController",typeIDHash=0x7d73e023,CRC=0x6ec8eb07,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SeqFacialInterpolateFrame":RSZVariable(name="_SeqFacialInterpolateFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SeqFacialInterpolateFrameMax":RSZVariable(name="_SeqFacialInterpolateFrameMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsMorriver":RSZVariable(name="_IsMorriver",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsRyujin":RSZVariable(name="_IsRyujin",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsRyujin_L":RSZVariable(name="_IsRyujin_L",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsCollab00":RSZVariable(name="_IsCollab00",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_JointMapNoChange":RSZVariable(name="_JointMapNoChange",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsWaitSequenceChange":RSZVariable(name="_IsWaitSequenceChange",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsEventObj":RSZVariable(name="_IsEventObj",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsEventObjFemale":RSZVariable(name="_IsEventObjFemale",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableCharaMakeMotionBank":RSZVariable(name="_DisableCharaMakeMotionBank",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_FacilityActingParamRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FacilityActingParamRegister",typeIDHash=0xf95bf5b5,CRC=0x6c750a1d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ParamList":RSZVariable(name="_ParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_FacilityHide(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FacilityHide",typeIDHash=0xb0fe8e63,CRC=0xd270219,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_FacilityManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FacilityManager",typeIDHash=0xb3a58ab6,CRC=0x63f7afdf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_FadeManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FadeManager",typeIDHash=0xd90b6e36,CRC=0x4a680e3c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_FadeRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FadeRegister",typeIDHash=0x791b5d99,CRC=0x72121bc9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Layer":RSZVariable(name="_Layer",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Type":RSZVariable(name="_Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Segment":RSZVariable(name="_Segment",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Color":RSZVariable(name="_Color",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_FieldDef_STAGE_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FieldDef.STAGE_Serializable",typeIDHash=0x1f19a73,CRC=0xa25f5edb,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_FieldJunctionEntrancePointRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FieldJunctionEntrancePointRegister",typeIDHash=0xca880336,CRC=0xc682270f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_FieldSceneActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FieldSceneActivator",typeIDHash=0xcf625f2c,CRC=0x3f544dc4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_FieldTimelineBlendRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FieldTimelineBlendRegister",typeIDHash=0x82eb67a3,CRC=0x5b49d94a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_FloatingObjectMove(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FloatingObjectMove",typeIDHash=0x831aa66f,CRC=0xb0d4c6bb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_FloatingObjectMoveSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FloatingObjectMoveSetting",typeIDHash=0x77e92d9c,CRC=0xad4d64e7,isObject = True,tagList=[])
		self.fields = {
		"_MoveScale":RSZVariable(name="_MoveScale",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"_MoveSpeed":RSZVariable(name="_MoveSpeed",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"_RotateSpeed":RSZVariable(name="_RotateSpeed",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		}

class app_FlowMapSetterToFluidController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FlowMapSetterToFluidController",typeIDHash=0x4343652b,CRC=0xb5dc4282,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TargetMatIndex":RSZVariable(name="_TargetMatIndex",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_FlyStone(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FlyStone",typeIDHash=0x70ed55a3,CRC=0x96fe706e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_FlyStoneSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FlyStoneSetting",typeIDHash=0x8243e72f,CRC=0x5da91946,isObject = True,tagList=[])
		self.fields = {
		"_Lv1RuinExternStart":RSZVariable(name="_Lv1RuinExternStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv1RuinExternEnd":RSZVariable(name="_Lv1RuinExternEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv1FertilityExternStart":RSZVariable(name="_Lv1FertilityExternStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv1FertilityExternEnd":RSZVariable(name="_Lv1FertilityExternEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv2RuinExternStart":RSZVariable(name="_Lv2RuinExternStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv2RuinExternEnd":RSZVariable(name="_Lv2RuinExternEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv2FertilityExternStart":RSZVariable(name="_Lv2FertilityExternStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv2FertilityExternEnd":RSZVariable(name="_Lv2FertilityExternEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv3FertilityExternStart":RSZVariable(name="_Lv3FertilityExternStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Lv3FertilityExternEnd":RSZVariable(name="_Lv3FertilityExternEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_FoliageDispOffController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FoliageDispOffController",typeIDHash=0x63fb5d1d,CRC=0x9d688dd,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_IsSpeedTreeOnly":RSZVariable(name="_IsSpeedTreeOnly",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_FoliageManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FoliageManager",typeIDHash=0x29436ab4,CRC=0xe529c134,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_FoliageSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.FoliageSetting",typeIDHash=0xf3742da3,CRC=0x95afa203,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableDispOffController":RSZVariable(name="_DisableDispOffController",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsPassThrough":RSZVariable(name="_IsPassThrough",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DispType":RSZVariable(name="_DispType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_HeatReceiverParamID":RSZVariable(name="_HeatReceiverParamID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_WetBlend":RSZVariable(name="_WetBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WetBlendLimit":RSZVariable(name="_WetBlendLimit",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopMaskFade":RSZVariable(name="_TopMaskFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_GlobalTopMaskFade":RSZVariable(name="_GlobalTopMaskFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopMaskFadeBias":RSZVariable(name="_TopMaskFadeBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopMaskMapBlend":RSZVariable(name="_TopMaskMapBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EmissiveIntensity":RSZVariable(name="_EmissiveIntensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopBlendVector":RSZVariable(name="_TopBlendVector",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_TriPlanarColor":RSZVariable(name="_TriPlanarColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"_GroundBlendBias":RSZVariable(name="_GroundBlendBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_PassThroughLengthBias":RSZVariable(name="_PassThroughLengthBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ColorParam":RSZVariable(name="_ColorParam",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"_EmissivePower":RSZVariable(name="_EmissivePower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WaveScrollSpeed":RSZVariable(name="_WaveScrollSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IceBlendRate":RSZVariable(name="_IceBlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IceSDFBlendRate":RSZVariable(name="_IceSDFBlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IceNormalVector":RSZVariable(name="_IceNormalVector",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_IceNormalBlend":RSZVariable(name="_IceNormalBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_AlphaTestRef":RSZVariable(name="_AlphaTestRef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnvironmentGUID":RSZVariable(name="_EnvironmentGUID",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=[]),
		"_ShaderTimerGUID":RSZVariable(name="_ShaderTimerGUID",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=[]),
		"_EditMaterialFlag":RSZVariable(name="_EditMaterialFlag",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsBurn":RSZVariable(name="_IsBurn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialValues":RSZVariable(name="_MaterialValues",dataType="ubyte",isList=True,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MaterialParamIndexArray":RSZVariable(name="_MaterialParamIndexArray",dataType="ushort",isList=True,alignment=2,value=None,tagSet=[]),
		"_IsCullingByDistance":RSZVariable(name="_IsCullingByDistance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_GA(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GA",typeIDHash=0x4b5601b2,CRC=0xe5d3d405,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GCManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GCManager",typeIDHash=0x6b31929d,CRC=0xb9b92246,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GIPointCloudsController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GIPointCloudsController",typeIDHash=0x529b2c8f,CRC=0x6f01f7e1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SecondaryColorInterpolation":RSZVariable(name="SecondaryColorInterpolation",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"TertiaryColorInterpolation":RSZVariable(name="TertiaryColorInterpolation",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_GUI3DMapSystemCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUI3DMapSystemCreator",typeIDHash=0xe3dab013,CRC=0xda947cc0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GUICameraPrefab":RSZVariable(name="_GUICameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GUIGroundCameraPrefab":RSZVariable(name="_GUIGroundCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GUILightPrefab":RSZVariable(name="_GUILightPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_GUIActionGuideConUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUIActionGuideConUpdater",typeIDHash=0xb9c204e0,CRC=0xcee6a05e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GUIBarcodeMakerController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUIBarcodeMakerController",typeIDHash=0x4d8e6ea0,CRC=0x7a8c80d5,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_GUICreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUICreator",typeIDHash=0xd0a0f178,CRC=0x7d58185e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_IdSetting":RSZVariable(name="_IdSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GUIManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUIManager",typeIDHash=0x6b759066,CRC=0x27d21715,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ActiveSkillItem2":RSZVariable(name="ActiveSkillItem2",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_VirtualMouseEnable":RSZVariable(name="_VirtualMouseEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SelectedLureItemId":RSZVariable(name="_SelectedLureItemId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsWaitingOpenProfile":RSZVariable(name="IsWaitingOpenProfile",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_NewBenefitList":RSZVariable(name="_NewBenefitList",dataType="int",isList=True,alignment=4,value=None,tagSet=[]),
		}

class app_GUIMapBeaconManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUIMapBeaconManager",typeIDHash=0x7c376145,CRC=0x8358de1b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GUIPrefabCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUIPrefabCatalog",typeIDHash=0x5e189479,CRC=0xf036781,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GUIList":RSZVariable(name="_GUIList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GUISystemSetup(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GUISystemSetup",typeIDHash=0xc71b7,CRC=0x3740c9f3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GameFlowManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GameFlowManager",typeIDHash=0x7612a242,CRC=0xd0be5c33,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GameInputManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GameInputManager",typeIDHash=0x291b23b1,CRC=0xcbd39837,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MouseSensitivityHorizontal":RSZVariable(name="_MouseSensitivityHorizontal",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MouseSensitivityVertical":RSZVariable(name="_MouseSensitivityVertical",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_GameMiniEventManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GameMiniEventManager",typeIDHash=0xf472d4b5,CRC=0x252300b9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GameVisibleController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GameVisibleController",typeIDHash=0xaffa8f38,CRC=0xe396efc3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GimmickAssetHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GimmickAssetHolder",typeIDHash=0x551282e2,CRC=0xba8c226e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MiniComponentHolder":RSZVariable(name="_MiniComponentHolder",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonParam":RSZVariable(name="_CommonParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AaaUniqueParam":RSZVariable(name="_AaaUniqueParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BbbUniqueParam":RSZVariable(name="_BbbUniqueParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ShellList":RSZVariable(name="_ShellList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GimmickCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GimmickCreator",typeIDHash=0x92d92a56,CRC=0xdcf32825,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GimmickManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GimmickManager",typeIDHash=0x2b71a9c8,CRC=0x5d93e875,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MiniComponentConfig":RSZVariable(name="_MiniComponentConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"IsLoadGimmickContext":RSZVariable(name="IsLoadGimmickContext",dataType="bool",isList=True,alignment=1,value=None,tagSet=[]),
		}

class app_GimmickPrefabCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GimmickPrefabCatalog",typeIDHash=0x3ae2663b,CRC=0x8c7298ca,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GimmickListConfig":RSZVariable(name="_GimmickListConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GimmickPrepare(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GimmickPrepare",typeIDHash=0x9bf15ef4,CRC=0xad174d6e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_Gm100(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Gm100",typeIDHash=0xb376da79,CRC=0xabf11332,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_Gm100_000Break(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Gm100_000Break",typeIDHash=0xb6708b41,CRC=0x1aa8e052,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_Gm100_100(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Gm100_100",typeIDHash=0xca5864f2,CRC=0x6ff92b8e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_Gm100_103(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Gm100_103",typeIDHash=0xacfb704b,CRC=0xd7445799,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_Gm100_105(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Gm100_105",typeIDHash=0x258b935c,CRC=0x4d92cb65,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GraphicsManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GraphicsManager",typeIDHash=0x55540c38,CRC=0xd4a744a1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SettingBase":RSZVariable(name="SettingBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"GraphicsPreset":RSZVariable(name="GraphicsPreset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GPUScoreCalculateData":RSZVariable(name="_GPUScoreCalculateData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GraphicsSettingUsedVramSize":RSZVariable(name="_GraphicsSettingUsedVramSize",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ScarBabSetting":RSZVariable(name="_ScarBabSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StainMeshSetting":RSZVariable(name="_StainMeshSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StageRayTracingData":RSZVariable(name="_StageRayTracingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GraphicsSettingUsedVramSize(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GraphicsSettingUsedVramSize",typeIDHash=0xc682c032,CRC=0xc1f21c6e,isObject = True,tagList=[])
		self.fields = {
		"_VramSizeData":RSZVariable(name="_VramSizeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_GroundDispController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GroundDispController",typeIDHash=0x9122be7d,CRC=0x1ab3353a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GroundID":RSZVariable(name="_GroundID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsDispInZone":RSZVariable(name="_IsDispInZone",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ZoneNameHash":RSZVariable(name="_ZoneNameHash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_GroundHeightController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GroundHeightController",typeIDHash=0x4268dd07,CRC=0xf6c433aa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EditArea":RSZVariable(name="_EditArea",dataType="aabb",isList=False,alignment=16,value=None,tagSet=[]),
		"_DeformTextureResolution":RSZVariable(name="_DeformTextureResolution",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_DeformTextureResolutionOffset":RSZVariable(name="_DeformTextureResolutionOffset",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_GroundManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GroundManager",typeIDHash=0xcc5eb726,CRC=0x842d8a4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GroundHeightEditData":RSZVariable(name="_GroundHeightEditData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Zone_st103":RSZVariable(name="_Zone_st103",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Zone_st104":RSZVariable(name="_Zone_st104",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GroundSectionRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GroundSectionRegister",typeIDHash=0x5ccbf21,CRC=0x3b7f46e9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GroundSplatRegionController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GroundSplatRegionController",typeIDHash=0x744a89e1,CRC=0xe7804b1d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GroundSurfaceTrailRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GroundSurfaceTrailRegister",typeIDHash=0xba21a544,CRC=0xf33aea9d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SurfaceType":RSZVariable(name="_SurfaceType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_GuideInsectCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GuideInsectCreator",typeIDHash=0xc783649f,CRC=0x4e079f3a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GuideInsectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GuideInsectManager",typeIDHash=0x8c9f681a,CRC=0x462c4e82,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_GuideInsectPrefabCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GuideInsectPrefabCatalog",typeIDHash=0x81ad80ab,CRC=0xe899c66e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_GuideInsectList":RSZVariable(name="_GuideInsectList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_GuildCardSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.GuildCardSceneController",typeIDHash=0x14da51db,CRC=0x802c26c3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SceneHunterObject":RSZVariable(name="_SceneHunterObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_ScenePalicoObject":RSZVariable(name="_ScenePalicoObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_SceneSeikretObject":RSZVariable(name="_SceneSeikretObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightTimelineObject":RSZVariable(name="_LightTimelineObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		}

class app_Hammock(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Hammock",typeIDHash=0xbb44ce84,CRC=0xb2779b9f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"BlendRate":RSZVariable(name="BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ParentJointIndex":RSZVariable(name="ParentJointIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Gravity":RSZVariable(name="Gravity",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"SpringForce":RSZVariable(name="SpringForce",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Damping":RSZVariable(name="Damping",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ElasticCoef":RSZVariable(name="ElasticCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CogLerpSpeed":RSZVariable(name="CogLerpSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"RollPerMeter":RSZVariable(name="RollPerMeter",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"RollEffectMaxDistance":RSZVariable(name="RollEffectMaxDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"RollEffectZRate":RSZVariable(name="RollEffectZRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EnableCollision":RSZVariable(name="EnableCollision",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"CenterIndex":RSZVariable(name="CenterIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Groups":RSZVariable(name="Groups",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Links":RSZVariable(name="Links",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_Hammock_Group(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.Hammock.Group",typeIDHash=0x199f6512,CRC=0xd03d5184,isObject = True,tagList=[])
		self.fields = {
		"Enable":RSZVariable(name="Enable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Valid":RSZVariable(name="Valid",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"SpringRate":RSZVariable(name="SpringRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"JointIndex":RSZVariable(name="JointIndex",dataType="int",isList=True,alignment=4,value=None,tagSet=[]),
		"Nodes":RSZVariable(name="Nodes",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CalcNodes":RSZVariable(name="CalcNodes",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"RootBaseLocalMat":RSZVariable(name="RootBaseLocalMat",dataType="mat4",isList=False,alignment=16,value=None,tagSet=[]),
		"EndBaseLocalMat":RSZVariable(name="EndBaseLocalMat",dataType="mat4",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_HeavyRain(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.HeavyRain",typeIDHash=0x4717fdd4,CRC=0x23b3ad4a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EdgeOpacitySearchDist":RSZVariable(name="_EdgeOpacitySearchDist",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MoveState":RSZVariable(name="_MoveState",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_HeavyRainLightRate":RSZVariable(name="_HeavyRainLightRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Settings":RSZVariable(name="_Settings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_HeavyRainSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.HeavyRainSetting",typeIDHash=0xd596df6,CRC=0x83e23d2,isObject = True,tagList=[])
		self.fields = {
		"_Requests":RSZVariable(name="_Requests",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DefaultVisibleData":RSZVariable(name="_DefaultVisibleData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AfterSandStormVisibleData":RSZVariable(name="_AfterSandStormVisibleData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CalcParamRadius":RSZVariable(name="_CalcParamRadius",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_InnerRateLinearData":RSZVariable(name="_InnerRateLinearData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WindChangeData":RSZVariable(name="_WindChangeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_HitController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.HitController",typeIDHash=0xeb5b7848,CRC=0x855b51ad,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_HunterActionDataStorage(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.HunterActionDataStorage",typeIDHash=0x36002375,CRC=0x6780b508,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_HunterDef_SLINGER_AMMO_TYPE_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.HunterDef.SLINGER_AMMO_TYPE_Serializable",typeIDHash=0x809dcd63,CRC=0x592abdeb,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_HunterDoll(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.HunterDoll",typeIDHash=0xeea805f9,CRC=0xaae9b1ef,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DollType":RSZVariable(name="_DollType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_MCTBank":RSZVariable(name="_MCTBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MEXBank":RSZVariable(name="_MEXBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_JointComponentsOrderedEnemy(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.JointComponentsOrderedEnemy",typeIDHash=0xfa6799d6,CRC=0x806212ec,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_LayoutSwitchRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LayoutSwitchRegister",typeIDHash=0x6cb196a5,CRC=0x90c3cc5e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_LifeAreaSwitch(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LifeAreaSwitch",typeIDHash=0x7275ca4c,CRC=0x24f1d9df,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StoryPackageFlag":RSZVariable(name="_StoryPackageFlag",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_LightBlendGroupZone(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LightBlendGroupZone",typeIDHash=0x19bca3ab,CRC=0x410f172f,isObject = True,tagList=[])
		self.fields = {
		}

class app_LightControlZoneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LightControlZoneController",typeIDHash=0x20ff6b93,CRC=0xca1e3c69,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_LightControlZoneManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LightControlZoneManager",typeIDHash=0x17bc080e,CRC=0x7c379a1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_LightEffectController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LightEffectController",typeIDHash=0x62e428cf,CRC=0x206978e5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_LightEffectType":RSZVariable(name="_LightEffectType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_WeatherLightEffectType":RSZVariable(name="_WeatherLightEffectType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_LobbyLiveCameraRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LobbyLiveCameraRegister",typeIDHash=0x94104d4b,CRC=0x444c2819,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_LogoController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.LogoController",typeIDHash=0xa33787ec,CRC=0x7478d3ce,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_MainCameraAttacher(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MainCameraAttacher",typeIDHash=0x85a2a50e,CRC=0x6ef415f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ManualBehaviorTreeSecureUser(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ManualBehaviorTreeSecureUser",typeIDHash=0xf5203554,CRC=0xe9187cb6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_MasterFieldCollector(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MasterFieldCollector",typeIDHash=0x21eecda6,CRC=0xb52af8ec,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DrawGridsInfo":RSZVariable(name="_DrawGridsInfo",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ColGridsInfo":RSZVariable(name="_ColGridsInfo",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PlantGridsInfo":RSZVariable(name="_PlantGridsInfo",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TreeGridsInfo":RSZVariable(name="_TreeGridsInfo",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NotIncludeAreas":RSZVariable(name="_NotIncludeAreas",dataType="int",isList=True,alignment=4,value=None,tagSet=[]),
		}

class app_MasterFieldCollector_cGridInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MasterFieldCollector.cGridInfo",typeIDHash=0xacdd75de,CRC=0x526fa25b,isObject = True,tagList=[])
		self.fields = {
		"_FolderName":RSZVariable(name="_FolderName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_GridMin":RSZVariable(name="_GridMin",dataType="int3",isList=False,alignment=4,value=None,tagSet=[]),
		"_GridMax":RSZVariable(name="_GridMax",dataType="int3",isList=False,alignment=4,value=None,tagSet=[]),
		"_CellSize":RSZVariable(name="_CellSize",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_CellHeight":RSZVariable(name="_CellHeight",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_MasterFieldManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MasterFieldManager",typeIDHash=0x39f52457,CRC=0xc5c6ecd9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SceJumpWarpInfo":RSZVariable(name="SceJumpWarpInfo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ManagerSetting":RSZVariable(name="_ManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_UnloadOrderSetting":RSZVariable(name="_UnloadOrderSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_MasterFieldManager_SceneJumpWarpInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MasterFieldManager.SceneJumpWarpInfo",typeIDHash=0x3aded70d,CRC=0x79f3a7d2,isObject = True,tagList=[])
		self.fields = {
		}

class app_MeshManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MeshManager",typeIDHash=0x69775687,CRC=0x6d5809c7,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_MeshPatternController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MeshPatternController",typeIDHash=0x4fc0d76a,CRC=0xed10022e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_MeshSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MeshSetting",typeIDHash=0xbc86cc1f,CRC=0xfbb315c6,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_LodSelectionAlogrithm":RSZVariable(name="_LodSelectionAlogrithm",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_AssetNo":RSZVariable(name="_AssetNo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsMargeBoundaryInController":RSZVariable(name="_IsMargeBoundaryInController",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsMargeBoundaryDrawOff":RSZVariable(name="_IsMargeBoundaryDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsPassThrough":RSZVariable(name="_IsPassThrough",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MeshMaterialLOD":RSZVariable(name="_MeshMaterialLOD",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WetBlend":RSZVariable(name="_WetBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WetBlendLimit":RSZVariable(name="_WetBlendLimit",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopMaskFade":RSZVariable(name="_TopMaskFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopMaskFadeBias":RSZVariable(name="_TopMaskFadeBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_GlobalTopMaskFade":RSZVariable(name="_GlobalTopMaskFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopMaskMapBlend":RSZVariable(name="_TopMaskMapBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EmissiveIntensity":RSZVariable(name="_EmissiveIntensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TopBlendVector":RSZVariable(name="_TopBlendVector",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_TriPlanarColor":RSZVariable(name="_TriPlanarColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"_DispType":RSZVariable(name="_DispType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_HeatReceiverParamID":RSZVariable(name="_HeatReceiverParamID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_GroundBlendBias":RSZVariable(name="_GroundBlendBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_PassThroughLengthBias":RSZVariable(name="_PassThroughLengthBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ColorParam":RSZVariable(name="_ColorParam",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"_AlphaTestRef":RSZVariable(name="_AlphaTestRef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EmissivePower":RSZVariable(name="_EmissivePower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WaveScrollSpeed":RSZVariable(name="_WaveScrollSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IceBlendRate":RSZVariable(name="_IceBlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IceSDFBlendRate":RSZVariable(name="_IceSDFBlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IceNormalVector":RSZVariable(name="_IceNormalVector",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_IceNormalBlend":RSZVariable(name="_IceNormalBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnvironmentGUID":RSZVariable(name="_EnvironmentGUID",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=[]),
		"_ShaderTimerGUID":RSZVariable(name="_ShaderTimerGUID",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=[]),
		"_EditMaterialFlag":RSZVariable(name="_EditMaterialFlag",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsBurn":RSZVariable(name="_IsBurn",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_MeshSettingController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MeshSettingController",typeIDHash=0xa693d847,CRC=0xe2bcb133,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsUpdateChild":RSZVariable(name="_IsUpdateChild",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsMargeBoundaryInController":RSZVariable(name="_IsMargeBoundaryInController",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsMargeBoundaryDrawOff":RSZVariable(name="_IsMargeBoundaryDrawOff",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_MeteorShower(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MeteorShower",typeIDHash=0x9d6a551c,CRC=0x3a20e5a0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_NoneRate":RSZVariable(name="_NoneRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SmallRate":RSZVariable(name="_SmallRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MediumRate":RSZVariable(name="_MediumRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_LargeRate":RSZVariable(name="_LargeRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_MissionActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MissionActivator",typeIDHash=0xff67ce2e,CRC=0x102c427f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_MissionBeaconManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MissionBeaconManager",typeIDHash=0x7896b05e,CRC=0x1cc133ad,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MissionBeaconPrefab":RSZVariable(name="_MissionBeaconPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_MissionManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MissionManager",typeIDHash=0xccb511de,CRC=0x4cff92bf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MissionTalkCollider":RSZVariable(name="_MissionTalkCollider",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"St101StoryDisableAreaNoBit":RSZVariable(name="St101StoryDisableAreaNoBit",dataType="int64",isList=False,alignment=8,value=None,tagSet=[]),
		"St102StoryDisableAreaNoBit":RSZVariable(name="St102StoryDisableAreaNoBit",dataType="int64",isList=False,alignment=8,value=None,tagSet=[]),
		"St103StoryDisableAreaNoBit":RSZVariable(name="St103StoryDisableAreaNoBit",dataType="int64",isList=False,alignment=8,value=None,tagSet=[]),
		"St104StoryDisableAreaNoBit":RSZVariable(name="St104StoryDisableAreaNoBit",dataType="int64",isList=False,alignment=8,value=None,tagSet=[]),
		"St105StoryDisableAreaNoBit":RSZVariable(name="St105StoryDisableAreaNoBit",dataType="int64",isList=False,alignment=8,value=None,tagSet=[]),
		"_MissionSetting":RSZVariable(name="_MissionSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"IsChangeManageMissionSideToMain":RSZVariable(name="IsChangeManageMissionSideToMain",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_WorkRateSetting":RSZVariable(name="_WorkRateSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"IsShowGalleryLog":RSZVariable(name="IsShowGalleryLog",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsGameOver":RSZVariable(name="_IsGameOver",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT_WeaponRecommendData_RecommendWeaponType":RSZVariable(name="STRUCT_WeaponRecommendData_RecommendWeaponType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT_WeaponRecommendData_RequestCount":RSZVariable(name="STRUCT_WeaponRecommendData_RequestCount",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT_WeaponRecommendData_LastSelectedChoice":RSZVariable(name="STRUCT_WeaponRecommendData_LastSelectedChoice",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"HuntingEnemyEvent":RSZVariable(name="HuntingEnemyEvent",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_MissionWorkRateSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MissionWorkRateSetting",typeIDHash=0x1eb97c3,CRC=0x2435e9d1,isObject = True,tagList=[])
		self.fields = {
		"_WorkRateData":RSZVariable(name="_WorkRateData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_MoonParamOverride(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MoonParamOverride",typeIDHash=0xf7324495,CRC=0xefb6ce7a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_OptionsVariationList":RSZVariable(name="_OptionsVariationList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TextureVariationList":RSZVariable(name="_TextureVariationList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_MoonParamOverride_MaskOptions(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MoonParamOverride.MaskOptions",typeIDHash=0xebc6a10d,CRC=0x5ff3f8ae,isObject = True,tagList=[])
		self.fields = {
		"MaskTexture":RSZVariable(name="MaskTexture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"CustomMaskPosition":RSZVariable(name="CustomMaskPosition",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"CustomMaskUVScale":RSZVariable(name="CustomMaskUVScale",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"CustomMaskRotation":RSZVariable(name="CustomMaskRotation",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CustomMaskAlpha":RSZVariable(name="CustomMaskAlpha",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_MoonParamOverride_MoonTexture(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.MoonParamOverride.MoonTexture",typeIDHash=0xab8b69ca,CRC=0xf6ce0d44,isObject = True,tagList=[])
		self.fields = {
		"Texture":RSZVariable(name="Texture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_NPCCustomizeSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NPCCustomizeSceneController",typeIDHash=0xac1f6f15,CRC=0x61bc07e4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_LightSources":RSZVariable(name="_LightSources",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_RotatableLights":RSZVariable(name="_RotatableLights",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightRotateSpeed":RSZVariable(name="_LightRotateSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EndType":RSZVariable(name="_EndType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_NavSafePosDataRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NavSafePosDataRegister",typeIDHash=0xa9a47220,CRC=0xe9c0547e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_NavSafePosData":RSZVariable(name="_NavSafePosData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_NavSafePosManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NavSafePosManager",typeIDHash=0x35b62a4d,CRC=0x12a3376d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_NetHttpRequestService(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NetHttpRequestService",typeIDHash=0xac76430d,CRC=0xb5303f3b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_NetworkManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NetworkManager",typeIDHash=0xfc1d28e8,CRC=0x7497b0f8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_NetSendInterval":RSZVariable(name="_NetSendInterval",dataType="float",isList=True,alignment=4,value=None,tagSet=[]),
		"OodleNetworkRuntimeData":RSZVariable(name="OodleNetworkRuntimeData",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"OodleCheckProtocol":RSZVariable(name="OodleCheckProtocol",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_NpcAI_PointRegister_Interact(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NpcAI_PointRegister_Interact",typeIDHash=0xecf488b6,CRC=0x1c7a132d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_PointType":RSZVariable(name="_PointType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_NpcDef_ID_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NpcDef.ID_Serializable",typeIDHash=0xa44e7b8d,CRC=0x99a768c2,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_NpcDef_NPC_CONTEXT_LAYOUT_TYPE_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NpcDef.NPC_CONTEXT_LAYOUT_TYPE_Serializable",typeIDHash=0xbfaf2088,CRC=0x8bad29c3,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_NpcManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NpcManager",typeIDHash=0xcb3d14d1,CRC=0x22b0f2cb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_NpcPackageCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NpcPackageCatalog",typeIDHash=0x4a3f5de6,CRC=0x6b604fce,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_NpcPackageList":RSZVariable(name="_NpcPackageList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcAccessoryPackages":RSZVariable(name="_NpcAccessoryPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcCustomVariList_U00001":RSZVariable(name="_NpcCustomVariList_U00001",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcCustomVAttachmentariList_U00001":RSZVariable(name="_NpcCustomVAttachmentariList_U00001",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcCustomVariList_U00002":RSZVariable(name="_NpcCustomVariList_U00002",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcCustomVariList_U00010":RSZVariable(name="_NpcCustomVariList_U00010",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcEmCommonPackages":RSZVariable(name="_NpcEmCommonPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcPartnerPackages":RSZVariable(name="_NpcPartnerPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_NpcPlayableCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.NpcPlayableCreator",typeIDHash=0x2d6bbe6c,CRC=0x654c8297,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_OBTRomManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OBTRomManager",typeIDHash=0x5f8c022d,CRC=0x16e6f17d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ObjectStreamingCaller(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ObjectStreamingCaller",typeIDHash=0xfe7ce2d8,CRC=0x94649901,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_OilGroundSplat(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OilGroundSplat",typeIDHash=0xa6d8bdfe,CRC=0xf359f618,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_OtomoCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OtomoCreator",typeIDHash=0x7673ef9c,CRC=0xc4603c03,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Phase":RSZVariable(name="_Phase",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_OtomoDoll(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OtomoDoll",typeIDHash=0x9e5c8ca8,CRC=0x4db02d95,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DollType":RSZVariable(name="_DollType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_EquipAppearanceSaveIndex":RSZVariable(name="_EquipAppearanceSaveIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_OtomoEquipPartsCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OtomoEquipPartsCatalog",typeIDHash=0xb30b8cc8,CRC=0xb0eb3928,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_OtomoEquipList":RSZVariable(name="_OtomoEquipList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OtomoEarPartsList":RSZVariable(name="_OtomoEarPartsList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OtomoFarPartsList":RSZVariable(name="_OtomoFarPartsList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PartnerOtomoEquipList":RSZVariable(name="_PartnerOtomoEquipList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PartnerOtomoEarPartsList":RSZVariable(name="_PartnerOtomoEarPartsList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PartnerOtomoFarPartsList":RSZVariable(name="_PartnerOtomoFarPartsList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_OtomoManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OtomoManager",typeIDHash=0x8aadfd10,CRC=0x4051a8b6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_OtomoZoneRegisterer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.OtomoZoneRegisterer",typeIDHash=0x62384400,CRC=0x4cdf7524,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ColliderSetType":RSZVariable(name="_ColliderSetType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_PQSManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PQSManager",typeIDHash=0xa0631516,CRC=0x1beda57,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PartsSwitch(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PartsSwitch",typeIDHash=0x93fd65ec,CRC=0x930c4609,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PauseManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PauseManager",typeIDHash=0x71a44baf,CRC=0x3f55b8d9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PhysicsManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PhysicsManager",typeIDHash=0x437e4e3e,CRC=0x5cc51e87,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PlayerArmorListCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerArmorListCatalog",typeIDHash=0x11130757,CRC=0x9c116730,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ArmorList":RSZVariable(name="_ArmorList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"AmuletPrefabList":RSZVariable(name="AmuletPrefabList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PlayerCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerCreator",typeIDHash=0x2e48ddeb,CRC=0x60b221a0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PlayerInputUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerInputUpdater",typeIDHash=0x63894f95,CRC=0xbb399056,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PlayerLayoutResident(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerLayoutResident",typeIDHash=0x5167289a,CRC=0x4449446d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PlayerManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerManager",typeIDHash=0xe4f35bbc,CRC=0x438bd39a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PlayerMantleListCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerMantleListCatalog",typeIDHash=0x37264f97,CRC=0xf76318bc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MantleList":RSZVariable(name="_MantleList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PlayerWeaponListCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PlayerWeaponListCatalog",typeIDHash=0xbc3ef11d,CRC=0xf3c25db3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_AllWeaponPack":RSZVariable(name="_AllWeaponPack",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PointGraphDef_NPC_INTERACT_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PointGraphDef.NPC_INTERACT_Serializable",typeIDHash=0xaeb35149,CRC=0xbd56f9b,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_PointGraphManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PointGraphManager",typeIDHash=0xf94b70fc,CRC=0x770dde92,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ManagerSetting":RSZVariable(name="ManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PorterCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PorterCreator",typeIDHash=0xd63d723e,CRC=0x7548bda6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_FixedID":RSZVariable(name="_FixedID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_PorterDef_ID_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PorterDef.ID_Serializable",typeIDHash=0xa7c1f622,CRC=0x67541be2,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_PorterDef_VISUAL_SETTING_TYPE_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PorterDef.VISUAL_SETTING_TYPE_Serializable",typeIDHash=0x5d9fd03,CRC=0xdc3d94a,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_PorterEquipCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PorterEquipCatalog",typeIDHash=0x4ffd112c,CRC=0xbd3493bc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EquipList":RSZVariable(name="_EquipList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PorterManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PorterManager",typeIDHash=0x24d32f15,CRC=0xe86851b4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DebugEnableDelayJobIndex":RSZVariable(name="_DebugEnableDelayJobIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_PorterPrefabCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PorterPrefabCatalog",typeIDHash=0xafff557c,CRC=0x648bc90f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_PorterList":RSZVariable(name="_PorterList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PostEffectBaseLightTrackRequester(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PostEffectBaseLightTrackRequester",typeIDHash=0xed599e82,CRC=0x65bef6d0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PostEffectCutSceneTrackRequester(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PostEffectCutSceneTrackRequester",typeIDHash=0xf6a05c9a,CRC=0x9d90a43b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_PostEffectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PostEffectManager",typeIDHash=0x1eb3ee4e,CRC=0x9acbf243,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SettingBase":RSZVariable(name="_SettingBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_PropsSwitchRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.PropsSwitchRegister",typeIDHash=0xab4490f5,CRC=0x1e69c86a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ProxyLODActiveStreaming(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ProxyLODActiveStreaming",typeIDHash=0xd696d731,CRC=0x7d2d7747,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StageFixedID":RSZVariable(name="_StageFixedID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Index":RSZVariable(name="_Index",dataType="int3",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsMeshEmpty":RSZVariable(name="_IsMeshEmpty",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_RailCameraDataRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RailCameraDataRegister",typeIDHash=0x2454fd4a,CRC=0x891b5fa1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_RecitalPackageCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RecitalPackageCatalog",typeIDHash=0x2b2ee02,CRC=0xaf0b76ae,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SongPackageList":RSZVariable(name="_SongPackageList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_RegisterToEnvPos(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RegisterToEnvPos",typeIDHash=0x562a09,CRC=0x9b633f98,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Stage":RSZVariable(name="_Stage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_RegisterToSoundMasterField(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RegisterToSoundMasterField",typeIDHash=0x48c2db72,CRC=0xcf071ac1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Stage":RSZVariable(name="_Stage",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_RegisterZone(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RegisterZone",typeIDHash=0xf56e9337,CRC=0x6bd84849,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ColliderSetType":RSZVariable(name="_ColliderSetType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_RegisterZoneEnemyArea(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RegisterZoneEnemyArea",typeIDHash=0xcecc6af1,CRC=0x7a4157f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ColliderSetType":RSZVariable(name="_ColliderSetType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_RegisterZoneNpcGenerate(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RegisterZoneNpcGenerate",typeIDHash=0x8f082f9b,CRC=0x4c586d1d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ColliderSetType":RSZVariable(name="_ColliderSetType",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_RoutePointGraphManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RoutePointGraphManager",typeIDHash=0xdc8c9d,CRC=0x5aec99e4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_RoutePointGraphRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.RoutePointGraphRegister",typeIDHash=0xa32348f7,CRC=0x410f68eb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SameHierarchySceneActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SameHierarchySceneActivator",typeIDHash=0xdd279c67,CRC=0x5dd795ef,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SandGroundSplat(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SandGroundSplat",typeIDHash=0xf9fc7596,CRC=0xbac22d83,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SandGroundSplatSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SandGroundSplatSetting",typeIDHash=0x72dddbf2,CRC=0x49cc8582,isObject = True,tagList=[])
		self.fields = {
		"_AllSplatTexture":RSZVariable(name="_AllSplatTexture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_GroundSplatBaseSetting":RSZVariable(name="_GroundSplatBaseSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SandStormType_SANDSTORM_TYPE_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SandStormType.SANDSTORM_TYPE_Serializable",typeIDHash=0x3275d7c3,CRC=0x4fae433,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SaveDataManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SaveDataManager",typeIDHash=0xb0b1d22d,CRC=0x8df6aa11,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"CurrentUserDataIndex":RSZVariable(name="CurrentUserDataIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SaveSelectSceneCameraController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SaveSelectSceneCameraController",typeIDHash=0x7825f86,CRC=0xa763766a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SaveSelectSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SaveSelectSceneController",typeIDHash=0x8613f043,CRC=0x257cd670,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_HunterObject":RSZVariable(name="_HunterObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_OtomoObject":RSZVariable(name="_OtomoObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_SeikretObject":RSZVariable(name="_SeikretObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		}

class app_SceneSwitchRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SceneSwitchRegister",typeIDHash=0x641cd763,CRC=0x304c7994,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Index":RSZVariable(name="_Index",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SeikretDoll(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SeikretDoll",typeIDHash=0x6c61a611,CRC=0x160edd29,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DollType":RSZVariable(name="_DollType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ParamCommon":RSZVariable(name="_ParamCommon",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SeikretEditSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SeikretEditSceneController",typeIDHash=0x50c932c9,CRC=0x4f694a7c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SceneSeikretObject":RSZVariable(name="_SceneSeikretObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightSources":RSZVariable(name="_LightSources",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_RotatableLights":RSZVariable(name="_RotatableLights",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightRotateSpeed":RSZVariable(name="_LightRotateSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_ShadowDistanceController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ShadowDistanceController",typeIDHash=0xa42f8088,CRC=0xfe3468b8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ShellManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ShellManager",typeIDHash=0x385e461c,CRC=0x5e413cdb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ShowRomManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ShowRomManager",typeIDHash=0x26991cab,CRC=0x7f59bcca,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SimpleFan(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SimpleFan",typeIDHash=0x51d62d0c,CRC=0x81b5247b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"MaxUpdateDistCommon":RSZVariable(name="MaxUpdateDistCommon",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"JointNameList":RSZVariable(name="JointNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"FanList":RSZVariable(name="FanList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SimpleFan_Fan(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SimpleFan.Fan",typeIDHash=0xed0f60b,CRC=0xf975d4ac,isObject = True,tagList=[])
		self.fields = {
		"IsDebugDraw":RSZVariable(name="IsDebugDraw",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"JointName":RSZVariable(name="JointName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"BaseAxis":RSZVariable(name="BaseAxis",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"IsAxisEdit":RSZVariable(name="IsAxisEdit",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"SpeedDegree":RSZVariable(name="SpeedDegree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsDisturbance":RSZVariable(name="IsDisturbance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisturbanceDegreeRange":RSZVariable(name="DisturbanceDegreeRange",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"DisturbancePeriodRange":RSZVariable(name="DisturbancePeriodRange",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"DisturbanceDegree":RSZVariable(name="DisturbanceDegree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DisturbancePeriod":RSZVariable(name="DisturbancePeriod",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ChangeSec":RSZVariable(name="ChangeSec",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SimplePendulum(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SimplePendulum",typeIDHash=0xa1e487dc,CRC=0x448136f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"MaxUpdateDistCommon":RSZVariable(name="MaxUpdateDistCommon",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaxSoundDist":RSZVariable(name="MaxSoundDist",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"JointNameList":RSZVariable(name="JointNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"PendulumList":RSZVariable(name="PendulumList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SimplePendulum_Pendulum(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SimplePendulum.Pendulum",typeIDHash=0x660a8978,CRC=0x74c3956a,isObject = True,tagList=[])
		self.fields = {
		"IsDebugDraw":RSZVariable(name="IsDebugDraw",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"JointName":RSZVariable(name="JointName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"LocalAxis":RSZVariable(name="LocalAxis",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Degree":RSZVariable(name="Degree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Length":RSZVariable(name="Length",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Period":RSZVariable(name="Period",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsDisturbance":RSZVariable(name="IsDisturbance",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DisturbanceDegreeRange":RSZVariable(name="DisturbanceDegreeRange",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"DisturbancePeriodRange":RSZVariable(name="DisturbancePeriodRange",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"DisturbanceDegree":RSZVariable(name="DisturbanceDegree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DisturbancePeriod":RSZVariable(name="DisturbancePeriod",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsTwist":RSZVariable(name="IsTwist",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TwistLocalAxis":RSZVariable(name="TwistLocalAxis",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"TwistInitialDegree":RSZVariable(name="TwistInitialDegree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"TwistDegreeRange":RSZVariable(name="TwistDegreeRange",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"TwistPeriodRange":RSZVariable(name="TwistPeriodRange",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"TwistDegree":RSZVariable(name="TwistDegree",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"TwistPeriod":RSZVariable(name="TwistPeriod",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SituationalActionGeneralAdministrator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SituationalActionGeneralAdministrator",typeIDHash=0x984952e3,CRC=0x74ea69a7,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundCatalogManager1_SoundCatalogRegisterapp_snd_user_data_CatalogCategory(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundCatalogManager`1.SoundCatalogRegister<app.snd_user_data.CatalogCategory>",typeIDHash=0x3de08c0f,CRC=0x13d532ff,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_CatalogList":RSZVariable(name="_CatalogList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundCharaMakeActor(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundCharaMakeActor",typeIDHash=0x2e83eae6,CRC=0x123c874d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Character":RSZVariable(name="_Character",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundControlledZoneGeneratorColliders(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundControlledZoneGeneratorColliders",typeIDHash=0x644a7ac9,CRC=0x7997bec6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ZoneGeneratorId":RSZVariable(name="_ZoneGeneratorId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundCullingController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundCullingController",typeIDHash=0x7b1c7e24,CRC=0x61d41f4e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Settings":RSZVariable(name="_Settings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundEffectTriggerSource(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundEffectTriggerSource",typeIDHash=0x76198ba0,CRC=0x7f5b31b9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ParingId":RSZVariable(name="_ParingId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundEnvBaseManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundEnvBaseManager",typeIDHash=0x8e1798c1,CRC=0xae375132,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundEnvPosManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundEnvPosManager",typeIDHash=0x54ce5812,CRC=0x38cc3dd4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Settings":RSZVariable(name="_Settings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundGUICatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundGUICatalog",typeIDHash=0xc51c01fa,CRC=0x3f4af68b,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ResourceList":RSZVariable(name="_ResourceList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundGUITriggerManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundGUITriggerManager",typeIDHash=0x53c0d408,CRC=0x776b0c1f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundGenerator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundGenerator",typeIDHash=0x4f64d7b8,CRC=0x8849b1c1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TriggerIds":RSZVariable(name="_TriggerIds",dataType="uint",isList=True,alignment=4,value=None,tagSet=[]),
		"_StopTriggerIds":RSZVariable(name="_StopTriggerIds",dataType="uint",isList=True,alignment=4,value=None,tagSet=[]),
		"_PlayOnStart":RSZVariable(name="_PlayOnStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UpdateClosest":RSZVariable(name="_UpdateClosest",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundLayeredRandomGenerator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundLayeredRandomGenerator",typeIDHash=0xefe260ce,CRC=0xc0083114,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_LayerSettingsList":RSZVariable(name="_LayerSettingsList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_RangeXZ":RSZVariable(name="_RangeXZ",dataType="float2",isList=False,alignment=4,value=None,tagSet=[]),
		"_UniqueIndex":RSZVariable(name="_UniqueIndex",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_SoundLayeredRandomGenerator_LayerSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundLayeredRandomGenerator.LayerSettings",typeIDHash=0x84bfac45,CRC=0xf3758895,isObject = True,tagList=[])
		self.fields = {
		"_Elevation":RSZVariable(name="_Elevation",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TriggerSettingsList":RSZVariable(name="_TriggerSettingsList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SoundLayeredRandomGenerator_LayerSettings_TriggerSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundLayeredRandomGenerator.LayerSettings.TriggerSettings",typeIDHash=0x3208fd39,CRC=0x6a18f317,isObject = True,tagList=[])
		self.fields = {
		"_TriggerId":RSZVariable(name="_TriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_TriggerInterval":RSZVariable(name="_TriggerInterval",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Duration":RSZVariable(name="_Duration",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_InterpolationTime":RSZVariable(name="_InterpolationTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EaseType":RSZVariable(name="_EaseType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundListenerApp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundListenerApp",typeIDHash=0xcd99b90b,CRC=0x511bf64b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ListenerIdx":RSZVariable(name="_ListenerIdx",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_SyncFOV":RSZVariable(name="_SyncFOV",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SyncNearClipPlane":RSZVariable(name="_SyncNearClipPlane",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableAxisY":RSZVariable(name="_EnableAxisY",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_InvertAxisZ":RSZVariable(name="_InvertAxisZ",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_Offset":RSZVariable(name="_Offset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_OffsetSougankyou":RSZVariable(name="_OffsetSougankyou",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_OffsetPhoto":RSZVariable(name="_OffsetPhoto",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_OffsetAngleLR":RSZVariable(name="_OffsetAngleLR",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundManagerApp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundManagerApp",typeIDHash=0x20334f59,CRC=0x545d458a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ManagerSettings":RSZVariable(name="_ManagerSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AppSettings":RSZVariable(name="_AppSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundManagerUpdater_AfterPosition(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundManagerUpdater_AfterPosition",typeIDHash=0xe875a800,CRC=0x66f31a9e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundManagerUpdater_AfterPostReqInfo_BeforePosition(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundManagerUpdater_AfterPostReqInfo_BeforePosition",typeIDHash=0x84df96a7,CRC=0x6899e1a9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundManagerUpdater_BeforePostReqInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundManagerUpdater_BeforePostReqInfo",typeIDHash=0xdba5cc55,CRC=0xf0ef8ac6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundManagerUpdater_PostReqInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundManagerUpdater_PostReqInfo",typeIDHash=0x733b054a,CRC=0xc9e2c83b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundManagerUpdater_Postion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundManagerUpdater_Postion",typeIDHash=0x8f13867a,CRC=0x9ecb2c16,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Index":RSZVariable(name="_Index",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundMotionSequenceApp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundMotionSequenceApp",typeIDHash=0x16266900,CRC=0x18d74f1b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MotionStatusSettingListData":RSZVariable(name="_MotionStatusSettingListData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_UpdateSequenceCategoryBits":RSZVariable(name="_UpdateSequenceCategoryBits",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_UpdateOnlyDrawSelf":RSZVariable(name="_UpdateOnlyDrawSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_SoundMusicCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundMusicCatalog",typeIDHash=0x47c84f0a,CRC=0x1f03b603,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Resource":RSZVariable(name="_Resource",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundMusicGenerator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundMusicGenerator",typeIDHash=0x3bb64fdf,CRC=0xd869b734,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TriggerIds":RSZVariable(name="_TriggerIds",dataType="uint",isList=True,alignment=4,value=None,tagSet=[]),
		"_StopTriggerIds":RSZVariable(name="_StopTriggerIds",dataType="uint",isList=True,alignment=4,value=None,tagSet=[]),
		"_PlayOnStart":RSZVariable(name="_PlayOnStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UpdateClosest":RSZVariable(name="_UpdateClosest",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_FadeOutTime":RSZVariable(name="_FadeOutTime",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_OnPlayStateList":RSZVariable(name="_OnPlayStateList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OnStopStateList":RSZVariable(name="_OnStopStateList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SoundMusicManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundMusicManager",typeIDHash=0xc4325a56,CRC=0x269b8946,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundNpcContainer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundNpcContainer",typeIDHash=0x7bfeb38e,CRC=0xdb59dc28,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TriggerOnlyDrawSelf":RSZVariable(name="_TriggerOnlyDrawSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UserDataList":RSZVariable(name="_UserDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HunterNpcUserDataList":RSZVariable(name="_HunterNpcUserDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundNpcResourceActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundNpcResourceActivator",typeIDHash=0x91d1e5ee,CRC=0xa3138ef0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundNpcResourceCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundNpcResourceCatalog",typeIDHash=0x434951b9,CRC=0xa1a7848b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_NpcResources":RSZVariable(name="_NpcResources",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SoundOtomoCharaMakeVoiceController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundOtomoCharaMakeVoiceController",typeIDHash=0x5186e86f,CRC=0x4a2d5f6a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_LoadMediaBank":RSZVariable(name="_LoadMediaBank",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_SoundPlayerCharaMakeVoiceController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundPlayerCharaMakeVoiceController",typeIDHash=0x6cc384c2,CRC=0xa394a2b7,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_LoadMediaBank":RSZVariable(name="_LoadMediaBank",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_SoundResourceActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundResourceActivator",typeIDHash=0xd52cf923,CRC=0x13f9d907,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ResourcePrefab":RSZVariable(name="_ResourcePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Condition":RSZVariable(name="_Condition",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundSpatialAudioDataRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundSpatialAudioDataRegister",typeIDHash=0x3b7a13af,CRC=0xf7a6f00e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Reverb":RSZVariable(name="_Reverb",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RoomsAndPortals":RSZVariable(name="_RoomsAndPortals",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundSpatialAudioLabel(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundSpatialAudioLabel",typeIDHash=0x79d30162,CRC=0x52eca88,isObject = True,tagList=[])
		self.fields = {
		"_Label":RSZVariable(name="_Label",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundSpatialAudioManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundSpatialAudioManager",typeIDHash=0x72ea4a59,CRC=0xadae50fa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundStoryContainerRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundStoryContainerRegister",typeIDHash=0x27d26633,CRC=0x6ce73014,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_SoundTitleActor(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundTitleActor",typeIDHash=0x81a85f9e,CRC=0x7a56be6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundVariousManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundVariousManager",typeIDHash=0xc8343e3c,CRC=0x942a772b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundVibrationContainer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundVibrationContainer",typeIDHash=0x99774430,CRC=0x96afb47e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_VibrationData":RSZVariable(name="_VibrationData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ADVibrationData":RSZVariable(name="_ADVibrationData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_VibTriggerList":RSZVariable(name="_VibTriggerList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_SoundZoneGeneratorCollidersApp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundZoneGeneratorCollidersApp",typeIDHash=0x6ab9917b,CRC=0xee897b2f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundZoneGeneratorVfxHelper(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundZoneGeneratorVfxHelper",typeIDHash=0x510ac20a,CRC=0xe3c7da46,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SoundZoneLifeAreaColliders(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundZoneLifeAreaColliders",typeIDHash=0x1ebaa0be,CRC=0x99c54fcc,isObject = True,tagList=[])
		self.fields = {
		"_LifeArea":RSZVariable(name="_LifeArea",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SoundZoneWaterColliders(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SoundZoneWaterColliders",typeIDHash=0x58ba45fd,CRC=0x867f2f6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SpeedTreeManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SpeedTreeManager",typeIDHash=0x5d7d3d5,CRC=0xc5f6b0b2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_St100Register(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.St100Register",typeIDHash=0x77ad207d,CRC=0xdb30bad6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StageAreaLoadManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageAreaLoadManager",typeIDHash=0xed59dc5c,CRC=0xe4c5721f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StageEffectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageEffectManager",typeIDHash=0xaade884c,CRC=0xe5897e24,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StageLoadSceneRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageLoadSceneRegister",typeIDHash=0x52235df8,CRC=0xbe78b3b3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Stage":RSZVariable(name="_Stage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StageMark(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageMark",typeIDHash=0x10bbce94,CRC=0x517e614c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StageModelMotionController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageModelMotionController",typeIDHash=0xd46d83d9,CRC=0x90efa539,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_LoopMotionID":RSZVariable(name="_LoopMotionID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_LoopStartFrame":RSZVariable(name="_LoopStartFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SingleMotionIDList":RSZVariable(name="_SingleMotionIDList",dataType="uint",isList=True,alignment=4,value=None,tagSet=[]),
		"_EyeOpenTime":RSZVariable(name="_EyeOpenTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EyeCloseTime":RSZVariable(name="_EyeCloseTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StageSettingHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageSettingHolder",typeIDHash=0x41787a25,CRC=0x60cbdc82,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StageNo":RSZVariable(name="_StageNo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StageSetting":RSZVariable(name="_StageSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_StageUnloadOrderSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageUnloadOrderSetting",typeIDHash=0xb112d600,CRC=0xf1fcaa38,isObject = True,tagList=[])
		self.fields = {
		"_Data":RSZVariable(name="_Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StageZoneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageZoneController",typeIDHash=0x824d27cb,CRC=0xca6ea76e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StageZoneSwitcher(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StageZoneSwitcher",typeIDHash=0x804c24c8,CRC=0x168b0191,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StageFixed":RSZVariable(name="_StageFixed",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StainMeshController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StainMeshController",typeIDHash=0xce514949,CRC=0x3978ff3d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_WholeCtrlType":RSZVariable(name="_WholeCtrlType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_HeightCtrlType":RSZVariable(name="_HeightCtrlType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StainMeshSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StainMeshSetting",typeIDHash=0xfed8bb55,CRC=0x45ce7a2e,isObject = True,tagList=[])
		self.fields = {
		"_StainBabResource":RSZVariable(name="_StainBabResource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MaxInstanceNum":RSZVariable(name="_MaxInstanceNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_UseParamLength":RSZVariable(name="_UseParamLength",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_StainSeparator":RSZVariable(name="_StainSeparator",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaterialData":RSZVariable(name="_MaterialData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandStormDryTime":RSZVariable(name="_SandStormDryTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SandGroundDryTime":RSZVariable(name="_SandGroundDryTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SnowDynamicTexFade":RSZVariable(name="_SnowDynamicTexFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SnowDynamicTexContrast":RSZVariable(name="_SnowDynamicTexContrast",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_HeightStainSeparator":RSZVariable(name="_HeightStainSeparator",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_SnowHeight":RSZVariable(name="_SnowHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_HumanData":RSZVariable(name="_HumanData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EmData":RSZVariable(name="_EmData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EmZakoData":RSZVariable(name="_EmZakoData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AnimalData":RSZVariable(name="_AnimalData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PtData":RSZVariable(name="_PtData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OtomoData":RSZVariable(name="_OtomoData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StainEndSeparator":RSZVariable(name="_StainEndSeparator",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_StaticCompoundExecutor(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StaticCompoundExecutor",typeIDHash=0x20c25d4c,CRC=0x26ca999c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StdCld2Controller(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller",typeIDHash=0x2666716a,CRC=0xe7472baf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"General":RSZVariable(name="General",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"LayerHeightRange":RSZVariable(name="LayerHeightRange",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MainLayerModeling":RSZVariable(name="MainLayerModeling",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CirrusLayerModeling":RSZVariable(name="CirrusLayerModeling",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Wind":RSZVariable(name="Wind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MediumProperties":RSZVariable(name="MediumProperties",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"AmbientLight":RSZVariable(name="AmbientLight",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MultiScattering":RSZVariable(name="MultiScattering",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"SystemParams":RSZVariable(name="SystemParams",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StdCld2Controller_StdCld2AmbientLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2AmbientLight",typeIDHash=0x8dfe43ea,CRC=0x379a989,isObject = True,tagList=[])
		self.fields = {
		"AmbientLightFadeByGradFrom":RSZVariable(name="AmbientLightFadeByGradFrom",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"AmbientLightFadeByGradTo":RSZVariable(name="AmbientLightFadeByGradTo",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"AmbientLightIntensityAtFadeStart":RSZVariable(name="AmbientLightIntensityAtFadeStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"AmbientLightIntensityAtFadeEnd":RSZVariable(name="AmbientLightIntensityAtFadeEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"AmbientLightFadeCurveContrast":RSZVariable(name="AmbientLightFadeCurveContrast",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"AmbientLightHeightEq":RSZVariable(name="AmbientLightHeightEq",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CirrusLayerAmbientLightColor":RSZVariable(name="CirrusLayerAmbientLightColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"CirrusLayerAmbientLightIntensity":RSZVariable(name="CirrusLayerAmbientLightIntensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ApIntensity":RSZVariable(name="ApIntensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ApDensityScale":RSZVariable(name="ApDensityScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2AmbientLight_StdCld2SingleAmbientEqualizer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2AmbientLight.StdCld2SingleAmbientEqualizer",typeIDHash=0x6f3e4e3e,CRC=0x5ed9086,isObject = True,tagList=[])
		self.fields = {
		"Color":RSZVariable(name="Color",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"Intensity":RSZVariable(name="Intensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"TargetHeight":RSZVariable(name="TargetHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Q":RSZVariable(name="Q",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2CirrusLayerModeling(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2CirrusLayerModeling",typeIDHash=0x3b08892d,CRC=0xce9282fe,isObject = True,tagList=[])
		self.fields = {
		"CirrusLayerCloud":RSZVariable(name="CirrusLayerCloud",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CirrusLayerAreaMask":RSZVariable(name="CirrusLayerAreaMask",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StdCld2Controller_StdCld2CirrusLayerModeling_StdCld2CirrusLayerMediumProps(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2CirrusLayerModeling.StdCld2CirrusLayerMediumProps",typeIDHash=0x23236a06,CRC=0x30b483a8,isObject = True,tagList=[])
		self.fields = {
		"CloudTextureScale":RSZVariable(name="CloudTextureScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"BaseDensity":RSZVariable(name="BaseDensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CloudType":RSZVariable(name="CloudType",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CloudContrast":RSZVariable(name="CloudContrast",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Rotation":RSZVariable(name="Rotation",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2CirrusLayerModeling_StdCld2CirrusLayerWeatherCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2CirrusLayerModeling.StdCld2CirrusLayerWeatherCreator",typeIDHash=0xd53543e6,CRC=0xda40cd4c,isObject = True,tagList=[])
		self.fields = {
		"MaskBaseScale":RSZVariable(name="MaskBaseScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskScaleSelector":RSZVariable(name="MaskScaleSelector",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskValueRangeMin":RSZVariable(name="MaskValueRangeMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskValueRangeMax":RSZVariable(name="MaskValueRangeMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ValueCurveTangentA":RSZVariable(name="ValueCurveTangentA",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ValueCurveTangentB":RSZVariable(name="ValueCurveTangentB",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DistortionStrength":RSZVariable(name="DistortionStrength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskSeed":RSZVariable(name="MaskSeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2General(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2General",typeIDHash=0x35452917,CRC=0x7ebf624a,isObject = True,tagList=[])
		self.fields = {
		"Enable":RSZVariable(name="Enable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2LayerHeightRange(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2LayerHeightRange",typeIDHash=0x2f3db788,CRC=0x7272d691,isObject = True,tagList=[])
		self.fields = {
		"MainLayerBottomHeight":RSZVariable(name="MainLayerBottomHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MainLayerTopHeight":RSZVariable(name="MainLayerTopHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CirrusLayerBottomHeight":RSZVariable(name="CirrusLayerBottomHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CirrusLayerTopHeight":RSZVariable(name="CirrusLayerTopHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling",typeIDHash=0x64d72ffa,CRC=0x30a5f345,isObject = True,tagList=[])
		self.fields = {
		"MainLayerDensity":RSZVariable(name="MainLayerDensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MainLayerWeather":RSZVariable(name="MainLayerWeather",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gradient":RSZVariable(name="Gradient",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"DetailNoise":RSZVariable(name="DetailNoise",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2DensityParams(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2DensityParams",typeIDHash=0xb62b0e7,CRC=0xa8a252d0,isObject = True,tagList=[])
		self.fields = {
		"BaseDensity":RSZVariable(name="BaseDensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DensityToneCurveTangentA":RSZVariable(name="DensityToneCurveTangentA",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DensityToneCurveTangentB":RSZVariable(name="DensityToneCurveTangentB",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2DetailNoiseCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2DetailNoiseCreator",typeIDHash=0xc04e91b2,CRC=0xb8095e4f,isObject = True,tagList=[])
		self.fields = {
		"DetailNoiseScaleLow":RSZVariable(name="DetailNoiseScaleLow",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseScaleHigh":RSZVariable(name="DetailNoiseScaleHigh",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseBaseStrength":RSZVariable(name="DetailNoiseBaseStrength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Low0":RSZVariable(name="Low0",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Low1":RSZVariable(name="Low1",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Low2":RSZVariable(name="Low2",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Low3":RSZVariable(name="Low3",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"StrengthSumLow":RSZVariable(name="StrengthSumLow",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"High0":RSZVariable(name="High0",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"High1":RSZVariable(name="High1",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"High2":RSZVariable(name="High2",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"High3":RSZVariable(name="High3",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"StrengthSumHigh":RSZVariable(name="StrengthSumHigh",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2GradientCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2GradientCreator",typeIDHash=0xe6f65bd2,CRC=0x2136136e,isObject = True,tagList=[])
		self.fields = {
		"GradientA":RSZVariable(name="GradientA",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GradientB":RSZVariable(name="GradientB",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GradientC":RSZVariable(name="GradientC",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GradientD":RSZVariable(name="GradientD",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2MainLayerCircleMaskProperties(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2MainLayerCircleMaskProperties",typeIDHash=0x672c04b2,CRC=0x5ed5a351,isObject = True,tagList=[])
		self.fields = {
		"MaskMode":RSZVariable(name="MaskMode",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskCenter":RSZVariable(name="MaskCenter",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"MaskCenterObject":RSZVariable(name="MaskCenterObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"MaskRadiusRangeKm":RSZVariable(name="MaskRadiusRangeKm",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"MaskStrength":RSZVariable(name="MaskStrength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskCurveTangentA":RSZVariable(name="MaskCurveTangentA",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskCurveTangentB":RSZVariable(name="MaskCurveTangentB",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2MainLayerSingleNoiseProperties(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2MainLayerSingleNoiseProperties",typeIDHash=0x2e466ab1,CRC=0x895ded91,isObject = True,tagList=[])
		self.fields = {
		"Scale":RSZVariable(name="Scale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Amount":RSZVariable(name="Amount",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"NoiseStrength":RSZVariable(name="NoiseStrength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DistortionStrength":RSZVariable(name="DistortionStrength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"NoiseOffset3D":RSZVariable(name="NoiseOffset3D",dataType="float3",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2MainLayerWeatherCreator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2MainLayerWeatherCreator",typeIDHash=0x4cc5f59c,CRC=0x28f4bcf8,isObject = True,tagList=[])
		self.fields = {
		"NoiseA":RSZVariable(name="NoiseA",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"NoiseB":RSZVariable(name="NoiseB",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"NoiseC":RSZVariable(name="NoiseC",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"NoiseD":RSZVariable(name="NoiseD",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"NoiseE":RSZVariable(name="NoiseE",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"NoiseF":RSZVariable(name="NoiseF",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CircleMask":RSZVariable(name="CircleMask",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2SingleDetailNoise(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2SingleDetailNoise",typeIDHash=0xfbbe7afe,CRC=0xfebfac67,isObject = True,tagList=[])
		self.fields = {
		"NoiseType":RSZVariable(name="NoiseType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"Strength":RSZVariable(name="Strength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CurveTangentA":RSZVariable(name="CurveTangentA",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CurveTangentB":RSZVariable(name="CurveTangentB",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MainLayerModeling_StdCld2SingleGradient(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MainLayerModeling.StdCld2SingleGradient",typeIDHash=0x31ea1208,CRC=0x7b51ad9f,isObject = True,tagList=[])
		self.fields = {
		"Strength":RSZVariable(name="Strength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"BaseHeightRangeMin":RSZVariable(name="BaseHeightRangeMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"BaseHeightRangeMax":RSZVariable(name="BaseHeightRangeMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LeftBorderPosition":RSZVariable(name="LeftBorderPosition",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LeftBorderHeightRangeMin":RSZVariable(name="LeftBorderHeightRangeMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LeftBorderHeightRangeMax":RSZVariable(name="LeftBorderHeightRangeMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"VerticalSheer":RSZVariable(name="VerticalSheer",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DistortionStrength":RSZVariable(name="DistortionStrength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DistortionShrinkX":RSZVariable(name="DistortionShrinkX",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DistortionSharpness":RSZVariable(name="DistortionSharpness",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"DistortionScaleSelector":RSZVariable(name="DistortionScaleSelector",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MediumProperties(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MediumProperties",typeIDHash=0xd768373a,CRC=0xf65a58be,isObject = True,tagList=[])
		self.fields = {
		"Albedo":RSZVariable(name="Albedo",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"EccentricityA":RSZVariable(name="EccentricityA",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EccentricityB":RSZVariable(name="EccentricityB",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EccentricityMixer":RSZVariable(name="EccentricityMixer",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2MultiScattering(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2MultiScattering",typeIDHash=0x4173d267,CRC=0xcd2f606c,isObject = True,tagList=[])
		self.fields = {
		"MultiScatContribution":RSZVariable(name="MultiScatContribution",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatAttenuation":RSZVariable(name="MultiScatAttenuation",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatEccentricity":RSZVariable(name="MultiScatEccentricity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatFadeByGradFrom":RSZVariable(name="MultiScatFadeByGradFrom",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatFadeByGradTo":RSZVariable(name="MultiScatFadeByGradTo",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatIntensityAtFadeStart":RSZVariable(name="MultiScatIntensityAtFadeStart",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatIntensityAtFadeEnd":RSZVariable(name="MultiScatIntensityAtFadeEnd",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MultiScatFadeCurveContrast":RSZVariable(name="MultiScatFadeCurveContrast",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2SystemParams(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2SystemParams",typeIDHash=0xde415549,CRC=0xb33bbc2c,isObject = True,tagList=[])
		self.fields = {
		"TemporalBlendRate":RSZVariable(name="TemporalBlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MainRaymarchMaxLengthKm":RSZVariable(name="MainRaymarchMaxLengthKm",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MainRaymarchNum":RSZVariable(name="MainRaymarchNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"AdaptiveRaymarch":RSZVariable(name="AdaptiveRaymarch",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ShadowRaymarchMaxLengthKm":RSZVariable(name="ShadowRaymarchMaxLengthKm",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ShadowRaymarchNum":RSZVariable(name="ShadowRaymarchNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"MainRaymarchResolution":RSZVariable(name="MainRaymarchResolution",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IBLRaymarchResolution":RSZVariable(name="IBLRaymarchResolution",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IBLRaymarchScale":RSZVariable(name="IBLRaymarchScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IBLPartialDrawFrame":RSZVariable(name="IBLPartialDrawFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ResourceOption":RSZVariable(name="ResourceOption",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ResourceDataset":RSZVariable(name="ResourceDataset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"AmbientLightLutResolution":RSZVariable(name="AmbientLightLutResolution",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"CirrusLayerWeatherTextureResolution":RSZVariable(name="CirrusLayerWeatherTextureResolution",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqLow0":RSZVariable(name="DetailNoiseFreqLow0",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqLow1":RSZVariable(name="DetailNoiseFreqLow1",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqLow2":RSZVariable(name="DetailNoiseFreqLow2",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqLow3":RSZVariable(name="DetailNoiseFreqLow3",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqHigh0":RSZVariable(name="DetailNoiseFreqHigh0",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqHigh1":RSZVariable(name="DetailNoiseFreqHigh1",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqHigh2":RSZVariable(name="DetailNoiseFreqHigh2",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"DetailNoiseFreqHigh3":RSZVariable(name="DetailNoiseFreqHigh3",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_StdCld2Controller_StdCld2Winds(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2Controller.StdCld2Winds",typeIDHash=0x9498168c,CRC=0x647af917,isObject = True,tagList=[])
		self.fields = {
		"MainLayerBaseWindVelocityMps":RSZVariable(name="MainLayerBaseWindVelocityMps",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"MainLayerDetailLowRelativeWindVeolcityMps":RSZVariable(name="MainLayerDetailLowRelativeWindVeolcityMps",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"MainLayerDetailHighRelativeWindVeolcityMps":RSZVariable(name="MainLayerDetailHighRelativeWindVeolcityMps",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"CirrusLayerWindVelocityMps":RSZVariable(name="CirrusLayerWindVelocityMps",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		}

class app_StdCld2ResourceDataset(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StdCld2ResourceDataset",typeIDHash=0x1ca28a15,CRC=0xaf80a98e,isObject = True,tagList=[])
		self.fields = {
		"stdCld2ResourceDataList":RSZVariable(name="stdCld2ResourceDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_StoryZoneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StoryZoneController",typeIDHash=0x1b3aaae0,CRC=0x136faa4b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"isQuest":RSZVariable(name="isQuest",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_StreetManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StreetManager",typeIDHash=0x3c402c86,CRC=0x9b84a35c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_StreetPointGraphRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.StreetPointGraphRegister",typeIDHash=0xc469f13,CRC=0x51ee8eec,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_SwimRail(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SwimRail",typeIDHash=0x35b2ed7b,CRC=0xe604e1d5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_RailInfoList":RSZVariable(name="_RailInfoList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SwimRail_cSwimRailInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SwimRail.cSwimRailInfo",typeIDHash=0x2ab054b6,CRC=0x13bdad9f,isObject = True,tagList=[])
		self.fields = {
		"Point1Pos":RSZVariable(name="Point1Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Point2Pos":RSZVariable(name="Point2Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"TargetRate1":RSZVariable(name="TargetRate1",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"TargetRate2":RSZVariable(name="TargetRate2",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"BezierDivideNum":RSZVariable(name="BezierDivideNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BezierParam":RSZVariable(name="BezierParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"UniqueIndex":RSZVariable(name="UniqueIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SwitchSceneActiveByEnvironment(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SwitchSceneActiveByEnvironment",typeIDHash=0xd4e10e8e,CRC=0xedfbe663,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_STAGE":RSZVariable(name="_STAGE",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Datas":RSZVariable(name="_Datas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SwitchSceneActiveByEnvironment_cData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SwitchSceneActiveByEnvironment.cData",typeIDHash=0x5cd9f6a8,CRC=0x1c0c40cb,isObject = True,tagList=[])
		self.fields = {
		"_Area":RSZVariable(name="_Area",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Slot":RSZVariable(name="_Slot",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Data_Ruin":RSZVariable(name="_Data_Ruin",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Data_Abnormal":RSZVariable(name="_Data_Abnormal",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Data_Fertility":RSZVariable(name="_Data_Fertility",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_SwitchSceneActiveByEnvironment_cData_cEnvSwitchData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SwitchSceneActiveByEnvironment.cData.cEnvSwitchData",typeIDHash=0x35730cb9,CRC=0x4e86ac9f,isObject = True,tagList=[])
		self.fields = {
		"_Rate":RSZVariable(name="_Rate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Prop":RSZVariable(name="_Prop",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_SyncLightBehaviorGlobalTime(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.SyncLightBehaviorGlobalTime",typeIDHash=0xd56285de,CRC=0xc2988829,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"DisableSyncTime":RSZVariable(name="DisableSyncTime",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_TentCustomizeSceneController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TentCustomizeSceneController",typeIDHash=0x33f2b899,CRC=0xe8350bd9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TentMarker":RSZVariable(name="_TentMarker",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_FacilityMarkers":RSZVariable(name="_FacilityMarkers",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightSources":RSZVariable(name="_LightSources",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_RotatableLights":RSZVariable(name="_RotatableLights",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_Floor":RSZVariable(name="_Floor",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_LightRotateSpeed":RSZVariable(name="_LightRotateSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_ThermalConductorManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ThermalConductorManager",typeIDHash=0x7f8416f5,CRC=0x13e8bd19,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HeatSourceSetting":RSZVariable(name="_HeatSourceSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HeatReceiverSetting":RSZVariable(name="_HeatReceiverSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_TimeHistory(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TimeHistory",typeIDHash=0xcf982445,CRC=0x1d915585,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_TimelineEventDefine_CutSceneStartSubMotionSetParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TimelineEventDefine.CutSceneStartSubMotionSetParam",typeIDHash=0xb974ee2c,CRC=0x81a4ceb8,isObject = True,tagList=[])
		self.fields = {
		"_MotionList":RSZVariable(name="_MotionList",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MotionSetID":RSZVariable(name="_MotionSetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"_MotionConnectBank":RSZVariable(name="_MotionConnectBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MotionExtendBank":RSZVariable(name="_MotionExtendBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_IsRidePorter":RSZVariable(name="_IsRidePorter",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_TimelineEventDefine_CutSceneSubEndMotionSetParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TimelineEventDefine.CutSceneSubEndMotionSetParam",typeIDHash=0x13e54e69,CRC=0x73065344,isObject = True,tagList=[])
		self.fields = {
		"_MotionList":RSZVariable(name="_MotionList",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_StartMotionSetID":RSZVariable(name="_StartMotionSetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"_LoopMotionSetID":RSZVariable(name="_LoopMotionSetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"_EndMotionSetID":RSZVariable(name="_EndMotionSetID",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"STRUCT__NextActionID__Category":RSZVariable(name="STRUCT__NextActionID__Category",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT__NextActionID__Index":RSZVariable(name="STRUCT__NextActionID__Index",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_NextActionGUID":RSZVariable(name="_NextActionGUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"STRUCT__NextSubActionID__Category":RSZVariable(name="STRUCT__NextSubActionID__Category",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"STRUCT__NextSubActionID__Index":RSZVariable(name="STRUCT__NextSubActionID__Index",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_MotionConnectBank":RSZVariable(name="_MotionConnectBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MotionExtendBank":RSZVariable(name="_MotionExtendBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SkipNextMoveStart":RSZVariable(name="_SkipNextMoveStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsRidePorter":RSZVariable(name="_IsRidePorter",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT__StartPos__HasValue":RSZVariable(name="STRUCT__StartPos__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT__StartPos__Value":RSZVariable(name="STRUCT__StartPos__Value",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"STRUCT__StartRot__HasValue":RSZVariable(name="STRUCT__StartRot__HasValue",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"STRUCT__StartRot__Value":RSZVariable(name="STRUCT__StartRot__Value",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		}

class app_TimelineEventDefine_ID_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TimelineEventDefine.ID_Serializable",typeIDHash=0x8e56cb54,CRC=0xd2630d4e,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_TimelineEventPlayOffsetSetter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TimelineEventPlayOffsetSetter",typeIDHash=0xa7134874,CRC=0xf8524782,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_TimelineEventResourceCollection(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TimelineEventResourceCollection",typeIDHash=0x75997d5c,CRC=0x16d27594,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EventID":RSZVariable(name="_EventID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_FlowID":RSZVariable(name="_FlowID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_TitleCameraController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TitleCameraController",typeIDHash=0x80f1959e,CRC=0x3a84124f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_TitleController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TitleController",typeIDHash=0xe62d277e,CRC=0x2795f5d5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_TitleFieldSceneActivator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TitleFieldSceneActivator",typeIDHash=0xc446b8be,CRC=0xe010b078,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_TorchGingerMotionController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.TorchGingerMotionController",typeIDHash=0xfc690966,CRC=0x73eadb4c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MinWaitMotionTime":RSZVariable(name="_MinWaitMotionTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaxWaitMotionTime":RSZVariable(name="_MaxWaitMotionTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MinFlowerMotionSpeed":RSZVariable(name="_MinFlowerMotionSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaxFlowerMotionSpeed":RSZVariable(name="_MaxFlowerMotionSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MinCloseMotionSpeed":RSZVariable(name="_MinCloseMotionSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaxCloseMotionSpeed":RSZVariable(name="_MaxCloseMotionSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_UIInputUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.UIInputUpdater",typeIDHash=0x3a42b751,CRC=0xc3fe1d2e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_UnderWaterChain(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.UnderWaterChain",typeIDHash=0xed683451,CRC=0x911c076d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_ChainParameter":RSZVariable(name="_ChainParameter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ClothParameter":RSZVariable(name="_ClothParameter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_UpdateSwitcher(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.UpdateSwitcher",typeIDHash=0xbc337a4,CRC=0x307f16fa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_VFXObjInstantiater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VFXObjInstantiater",typeIDHash=0xc4ed28aa,CRC=0x167d4b1d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Data":RSZVariable(name="_Data",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_VFXObjInstantiater_Data(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VFXObjInstantiater.Data",typeIDHash=0xbef0f6f6,CRC=0x8bdf89fe,isObject = True,tagList=[])
		self.fields = {
		"Prefab":RSZVariable(name="Prefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"FOLDER":RSZVariable(name="FOLDER",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"LAYER":RSZVariable(name="LAYER",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_VariousDataManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VariousDataManager",typeIDHash=0xf2b86567,CRC=0x59ab9d4b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_VolumeDecalCullingController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VolumeDecalCullingController",typeIDHash=0xe42cbef4,CRC=0x82df9c36,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_VolumeDecalSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VolumeDecalSetting",typeIDHash=0xf17677cc,CRC=0x2bdfd221,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_IsEditTopMaskFade":RSZVariable(name="_IsEditTopMaskFade",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TopMaskFade":RSZVariable(name="_TopMaskFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsEditGlobalBlend_TopMaskFade":RSZVariable(name="_IsEditGlobalBlend_TopMaskFade",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_GlobalBlend_TopMaskFade":RSZVariable(name="_GlobalBlend_TopMaskFade",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_VortexelGeometryManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VortexelGeometryManager",typeIDHash=0x43a319f3,CRC=0x98ced277,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_LowSetting":RSZVariable(name="_LowSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_VortexelPhysicsManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VortexelPhysicsManager",typeIDHash=0x9391ffcc,CRC=0xcc3ed205,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_VoxelManager2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VoxelManager2",typeIDHash=0x2172bcc2,CRC=0x932e45a3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_SettingBase":RSZVariable(name="_SettingBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_VoxelStaticDataRegister(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.VoxelStaticDataRegister",typeIDHash=0x47d8a04b,CRC=0xfc0cd6b6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_VoxelData":RSZVariable(name="_VoxelData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Offset":RSZVariable(name="_Offset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_Priority":RSZVariable(name="_Priority",dataType="short",isList=False,alignment=2,value=None,tagSet=[]),
		}

class app_WarpLocationOptimizer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.WarpLocationOptimizer",typeIDHash=0x8bd5525f,CRC=0x9a8b312,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_WarpLocationSetPack":RSZVariable(name="_WarpLocationSetPack",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WarpRule":RSZVariable(name="_WarpRule",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_WaterFluidEffectController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.WaterFluidEffectController",typeIDHash=0x159b86cc,CRC=0x85474ebf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_WindDirectional(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.WindDirectional",typeIDHash=0x861ab5f5,CRC=0xd65c86f1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_EnableWindGlobalAnimation":RSZVariable(name="_EnableWindGlobalAnimation",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Wind":RSZVariable(name="Wind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_WindManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.WindManager",typeIDHash=0x6bec351b,CRC=0xaa45cd4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"WindManagerSettingBase":RSZVariable(name="WindManagerSettingBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AnimationController":RSZVariable(name="_AnimationController",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_ZoneAreaFeildPointLayouter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ZoneAreaFeildPointLayouter",typeIDHash=0xc98bbdb4,CRC=0x55397456,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_ZoneDef_COLLIDERSET_TYPE_Serializable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ZoneDef.COLLIDERSET_TYPE_Serializable",typeIDHash=0x40d795fe,CRC=0xc08cf091,isObject = True,tagList=[])
		self.fields = {
		"_Value":RSZVariable(name="_Value",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_ZoneManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.ZoneManager",typeIDHash=0xc892048e,CRC=0x54c425b7,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_accessory_AccessoryManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.accessory.AccessoryManager",typeIDHash=0x171c43b5,CRC=0xb7fb3982,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_aliora_g3hk9p2x4l_Y6NVSD9X3J(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.aliora.g3hk9p2x4l.Y6NVSD9X3J",typeIDHash=0x29728d05,CRC=0x2b1fa159,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_cADVibration(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cADVibration",typeIDHash=0xccec0b14,CRC=0x189414f4,isObject = True,tagList=[])
		self.fields = {
		"_BusInfoTbl":RSZVariable(name="_BusInfoTbl",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SineWavResource_L":RSZVariable(name="_SineWavResource_L",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_SineWavResource_R":RSZVariable(name="_SineWavResource_R",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_cBootParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cBootParam",typeIDHash=0x670cf47a,CRC=0x6e468c8b,isObject = True,tagList=[])
		self.fields = {
		"_FromTitle":RSZVariable(name="_FromTitle",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TargetSceneJumpParam":RSZVariable(name="_TargetSceneJumpParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_cDialogueSituationRequestAbsorber(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cDialogueSituationRequestAbsorber",typeIDHash=0x6aeb591e,CRC=0xb7e440b9,isObject = True,tagList=[])
		self.fields = {
		"_AISituationParam":RSZVariable(name="_AISituationParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_cDialogueTimelineEventManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cDialogueTimelineEventManager",typeIDHash=0xfcc921a,CRC=0x6d52988e,isObject = True,tagList=[])
		self.fields = {
		"_EventTable":RSZVariable(name="_EventTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_cEm5222_00EggMaterialController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cEm5222_00EggMaterialController",typeIDHash=0xf9817ba4,CRC=0x9376c9c3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Setting":RSZVariable(name="_Setting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_cEventEffectBreathUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cEventEffectBreathUpdater",typeIDHash=0x685a6c45,CRC=0x4585ebc1,isObject = True,tagList=[])
		self.fields = {
		"_BreathEfc":RSZVariable(name="_BreathEfc",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OffsetDefault":RSZVariable(name="_OffsetDefault",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_EnableJointDistanceDefault":RSZVariable(name="_EnableJointDistanceDefault",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_cFieldSceneParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cFieldSceneParam",typeIDHash=0x10b61830,CRC=0xb9e38ec3,isObject = True,tagList=[])
		self.fields = {
		}

class app_cGameSceneFadeParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cGameSceneFadeParam",typeIDHash=0xce00dcb2,CRC=0xb6656439,isObject = True,tagList=[])
		self.fields = {
		"FadeType":RSZVariable(name="FadeType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"FadeOutTime":RSZVariable(name="FadeOutTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"FadeInTime":RSZVariable(name="FadeInTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"FadeOutDurationTime":RSZVariable(name="FadeOutDurationTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_cGameSceneJumpParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cGameSceneJumpParam",typeIDHash=0xcd4b59b4,CRC=0xecb56eb4,isObject = True,tagList=[])
		self.fields = {
		"_GameSceneParam":RSZVariable(name="_GameSceneParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FadeParam":RSZVariable(name="_FadeParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WarpSituationType":RSZVariable(name="_WarpSituationType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_WarpGimmickID":RSZVariable(name="_WarpGimmickID",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_cNameHash(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cNameHash",typeIDHash=0x7091fa,CRC=0x71e7564d,isObject = True,tagList=[])
		self.fields = {
		"_Hash":RSZVariable(name="_Hash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_cWindGlobalAnimationController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.cWindGlobalAnimationController",typeIDHash=0x19beeb8b,CRC=0x9fe41634,isObject = True,tagList=[])
		self.fields = {
		"_AnimationData":RSZVariable(name="_AnimationData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_dev1lab_AnalysisLogManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.dev1lab.AnalysisLogManager",typeIDHash=0xd7a1508a,CRC=0x7b9deab3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class app_model_blend_shape_manager_ModelBlendShapeManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.model_blend_shape_manager.ModelBlendShapeManager",typeIDHash=0x32f89a7c,CRC=0x2bc866de,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Holders":RSZVariable(name="_Holders",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_model_blend_shape_manager_ModelBlendShapeManager_AssetHolder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.model_blend_shape_manager.ModelBlendShapeManager.AssetHolder",typeIDHash=0xb62c2af6,CRC=0x9afb5f9e,isObject = True,tagList=[])
		self.fields = {
		"_Id":RSZVariable(name="_Id",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_Data":RSZVariable(name="_Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_snd_user_data_SoundCatalogDataApp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundCatalogDataApp",typeIDHash=0xc779baac,CRC=0xd18dffe9,isObject = True,tagList=[])
		self.fields = {
		"_Category":RSZVariable(name="_Category",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Instantiate":RSZVariable(name="_Instantiate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_PrefabDataList":RSZVariable(name="_PrefabDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_snd_user_data_SoundCatalogUser(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundCatalogUser",typeIDHash=0xd52d2523,CRC=0x19c158c9,isObject = True,tagList=[])
		self.fields = {
		"_CategoryList":RSZVariable(name="_CategoryList",dataType="int",isList=True,alignment=4,value=None,tagSet=[]),
		}

class app_snd_user_data_SoundCullingSettingsApp(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundCullingSettingsApp",typeIDHash=0x2e397c1f,CRC=0x2d2e9b0f,isObject = True,tagList=[])
		self.fields = {
		"_DistanceSq":RSZVariable(name="_DistanceSq",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_TypeDistList":RSZVariable(name="_TypeDistList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_snd_user_data_SoundEnvPosSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundEnvPosSettings",typeIDHash=0x27bb9a55,CRC=0xad9a4dca,isObject = True,tagList=[])
		self.fields = {
		"_FoliageContactCullingDistanceSq":RSZVariable(name="_FoliageContactCullingDistanceSq",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FoliageContactAntiRepeatTime":RSZVariable(name="_FoliageContactAntiRepeatTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FoliageSearchRange":RSZVariable(name="_FoliageSearchRange",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FoliageTriggerSettingsList":RSZVariable(name="_FoliageTriggerSettingsList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RiverSearchRange":RSZVariable(name="_RiverSearchRange",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RiverTriggerSettingsList":RSZVariable(name="_RiverTriggerSettingsList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_snd_user_data_SoundManagerAppSettingsData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundManagerAppSettingsData",typeIDHash=0x948575b0,CRC=0x6da8ccf8,isObject = True,tagList=[])
		self.fields = {
		"_InitializeStateDataList":RSZVariable(name="_InitializeStateDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CullingSettings":RSZVariable(name="_CullingSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EarlyRefrectionSettings":RSZVariable(name="_EarlyRefrectionSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ReverbSettings":RSZVariable(name="_ReverbSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RoomsAndPortalsSettings":RSZVariable(name="_RoomsAndPortalsSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OnResetTitleTriggerId":RSZVariable(name="_OnResetTitleTriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_LoadingStateList":RSZVariable(name="_LoadingStateList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EventFadeRtpcId":RSZVariable(name="_EventFadeRtpcId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_StoryFadeRtpcId":RSZVariable(name="_StoryFadeRtpcId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_SceneFadeRtpcId":RSZVariable(name="_SceneFadeRtpcId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_AppFadeRtpcId":RSZVariable(name="_AppFadeRtpcId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_StageStateListData":RSZVariable(name="_StageStateListData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PauseSettingsData":RSZVariable(name="_PauseSettingsData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CharaMakeSettings":RSZVariable(name="_CharaMakeSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DialogueSettings":RSZVariable(name="_DialogueSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OptionSettings":RSZVariable(name="_OptionSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SquadSettings":RSZVariable(name="_SquadSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DynamicSkipRate":RSZVariable(name="_DynamicSkipRate",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MissionSlowActionList":RSZVariable(name="_MissionSlowActionList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EffectTriggerTargetList":RSZVariable(name="_EffectTriggerTargetList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EffectSourceTargetList":RSZVariable(name="_EffectSourceTargetList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvironmentGameSyncs":RSZVariable(name="_EnvironmentGameSyncs",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MinorGameSyncs":RSZVariable(name="_MinorGameSyncs",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ScaredInTent":RSZVariable(name="_ScaredInTent",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Vibration":RSZVariable(name="_Vibration",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CustomizedDistanceRtpc":RSZVariable(name="_CustomizedDistanceRtpc",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WaterCollidersSettings":RSZVariable(name="_WaterCollidersSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcReactionExEmote01TriggerId":RSZVariable(name="_NpcReactionExEmote01TriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_snd_user_data_SoundReverbBusListData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundReverbBusListData",typeIDHash=0x34844382,CRC=0xb45f6ccf,isObject = True,tagList=[])
		self.fields = {
		"_IRBank":RSZVariable(name="_IRBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_OwnerStage":RSZVariable(name="_OwnerStage",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ReverbInfoList":RSZVariable(name="_ReverbInfoList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_snd_user_data_SoundRoomsAndPortalsListData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundRoomsAndPortalsListData",typeIDHash=0x9a5e52ed,CRC=0x9ee432,isObject = True,tagList=[])
		self.fields = {
		"_Stage":RSZVariable(name="_Stage",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_RoomList":RSZVariable(name="_RoomList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PortalList":RSZVariable(name="_PortalList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_snd_user_data_SoundVibrationTriggerListData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.snd_user_data.SoundVibrationTriggerListData",typeIDHash=0xdd35f005,CRC=0xed605bc5,isObject = True,tagList=[])
		self.fields = {
		"_VibrationTriggerList":RSZVariable(name="_VibrationTriggerList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_st102_a16_90_MaterialController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.st102_a16_90_MaterialController",typeIDHash=0x3fb7e2fc,CRC=0xe3a3b05,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_Data":RSZVariable(name="_Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_AmuletPrefabList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AmuletPrefabList",typeIDHash=0x8ff54e84,CRC=0x88bf7a10,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_AnimalBoxViewSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AnimalBoxViewSetting",typeIDHash=0xef00a1e6,CRC=0x3e2622d1,isObject = True,tagList=[])
		self.fields = {
		"_CameraSettings":RSZVariable(name="_CameraSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RotationSpeed":RSZVariable(name="_RotationSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MouseRotationSpeed":RSZVariable(name="_MouseRotationSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_DefaultViewData":RSZVariable(name="_DefaultViewData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_AnimalConfig(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AnimalConfig",typeIDHash=0xad065b88,CRC=0xedc1a06a,isObject = True,tagList=[])
		self.fields = {
		"_GeneralConfig":RSZVariable(name="_GeneralConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EachIdConfig":RSZVariable(name="_EachIdConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EachAreaConfig":RSZVariable(name="_EachAreaConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EachPlatformConfig":RSZVariable(name="_EachPlatformConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_UpdateConfig":RSZVariable(name="_UpdateConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EntryConfig":RSZVariable(name="_EntryConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PopAreaConfig":RSZVariable(name="_PopAreaConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PopAreaCropConfig":RSZVariable(name="_PopAreaCropConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TimeZoneConfig":RSZVariable(name="_TimeZoneConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CaptureConfig":RSZVariable(name="_CaptureConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BaseCampConfig":RSZVariable(name="_BaseCampConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PreviewConfig":RSZVariable(name="_PreviewConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_AppGraphicsSettingPreset(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AppGraphicsSettingPreset",typeIDHash=0x6413b210,CRC=0x66b531c4,isObject = True,tagList=[])
		self.fields = {
		"_RendererSetting":RSZVariable(name="_RendererSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MeshRendererSetting":RSZVariable(name="_MeshRendererSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LightRendererSetting":RSZVariable(name="_LightRendererSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MPMR":RSZVariable(name="_MPMR",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RangeCompression":RSZVariable(name="_RangeCompression",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OpenColorIOManager":RSZVariable(name="_OpenColorIOManager",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DynamicResolutionParamList":RSZVariable(name="_DynamicResolutionParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StreamingTextureSettingList":RSZVariable(name="_StreamingTextureSettingList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RayTracingManagerSetting":RSZVariable(name="_RayTracingManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ShadowDistanceSettings":RSZVariable(name="_ShadowDistanceSettings",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_AppInstantiateManagerSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AppInstantiateManagerSettings",typeIDHash=0x7b02c22f,CRC=0x46499f74,isObject = True,tagList=[])
		self.fields = {
		"_OneFrameInstantiateLimit":RSZVariable(name="_OneFrameInstantiateLimit",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_OneFrameInstantiateLimitMicroSeconds":RSZVariable(name="_OneFrameInstantiateLimitMicroSeconds",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_OneFrameInstantiateLimitOnLoad":RSZVariable(name="_OneFrameInstantiateLimitOnLoad",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_OneFrameInstantiateLimitOnLoadMicroSeconds":RSZVariable(name="_OneFrameInstantiateLimitOnLoadMicroSeconds",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SortInterval":RSZVariable(name="_SortInterval",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_CategorySortCoef":RSZVariable(name="_CategorySortCoef",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_CategorySortOrders":RSZVariable(name="_CategorySortOrders",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DistanceSortCoef":RSZVariable(name="_DistanceSortCoef",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_DistanceSortOrders":RSZVariable(name="_DistanceSortOrders",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_AppThermalConductorManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AppThermalConductorManagerSetting",typeIDHash=0x9b88a736,CRC=0x84e4d4f1,isObject = True,tagList=[])
		self.fields = {
		"ThermalConductorParam":RSZVariable(name="ThermalConductorParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RecoveryNumOneTime":RSZVariable(name="_RecoveryNumOneTime",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_CreateHeatReceiverNumOneTime":RSZVariable(name="_CreateHeatReceiverNumOneTime",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_CreateHeatReceiverTotalNumOneTime":RSZVariable(name="_CreateHeatReceiverTotalNumOneTime",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_HeatReceiverControllerNum":RSZVariable(name="_HeatReceiverControllerNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_RecoveryTimeEnvironmentChange":RSZVariable(name="_RecoveryTimeEnvironmentChange",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_BurningMapSize":RSZVariable(name="_BurningMapSize",dataType="int2",isList=False,alignment=4,value=None,tagSet=[]),
		"_BurningMapResetLength":RSZVariable(name="_BurningMapResetLength",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"_BurningMapBuffer":RSZVariable(name="_BurningMapBuffer",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_ResolutionInv":RSZVariable(name="_ResolutionInv",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_AppVoxelData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.AppVoxelData",typeIDHash=0x696e6973,CRC=0x4b263ba6,isObject = True,tagList=[])
		self.fields = {
		"_Buffer":RSZVariable(name="_Buffer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WallDataArray":RSZVariable(name="_WallDataArray",dataType="ubyte",isList=True,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_WallDataIndexArray":RSZVariable(name="_WallDataIndexArray",dataType="ushort",isList=True,alignment=2,value=None,tagSet=[]),
		"_NavNodeAttrArray":RSZVariable(name="_NavNodeAttrArray",dataType="uint64",isList=True,alignment=8,value=None,tagSet=[]),
		"_CeilingDistArray":RSZVariable(name="_CeilingDistArray",dataType="float",isList=True,alignment=4,value=None,tagSet=[]),
		"_EditArea":RSZVariable(name="_EditArea",dataType="aabb",isList=True,alignment=16,value=None,tagSet=[]),
		}

class app_user_data_BurntGroundSplatSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.BurntGroundSplatSetting",typeIDHash=0x270a569a,CRC=0x24398bb5,isObject = True,tagList=[])
		self.fields = {
		"_WeightRate":RSZVariable(name="_WeightRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SplatRandomOffsetScale":RSZVariable(name="_SplatRandomOffsetScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_UpdateTimeSpan":RSZVariable(name="_UpdateTimeSpan",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ClearTexture":RSZVariable(name="_ClearTexture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_GroundSplatBaseSetting":RSZVariable(name="_GroundSplatBaseSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_CameraManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.CameraManagerSetting",typeIDHash=0x7a184b7f,CRC=0xfbeb8dc1,isObject = True,tagList=[])
		self.fields = {
		"_AdjustPaniniRangeParam":RSZVariable(name="_AdjustPaniniRangeParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DitherDepthParam":RSZVariable(name="_DitherDepthParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DiscoveryParam":RSZVariable(name="_DiscoveryParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TentCameraSetting":RSZVariable(name="_TentCameraSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MiniCampCameraSetting":RSZVariable(name="_MiniCampCameraSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GuildCardCameraSetting":RSZVariable(name="_GuildCardCameraSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FacilityCameraSetting":RSZVariable(name="_FacilityCameraSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PhotoCameraSetting":RSZVariable(name="_PhotoCameraSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PhotoPostSetting":RSZVariable(name="_PhotoPostSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DialogueCameraParamList":RSZVariable(name="_DialogueCameraParamList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EquipData":RSZVariable(name="_EquipData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_InterpolationCameraPrefab":RSZVariable(name="_InterpolationCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EventCameraPrefab":RSZVariable(name="_EventCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EventIntepolationCameraPrefab":RSZVariable(name="_EventIntepolationCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CutsceneCameraPrefab":RSZVariable(name="_CutsceneCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CutsceneInCameraPrefab":RSZVariable(name="_CutsceneInCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DialogueCameraPrefab":RSZVariable(name="_DialogueCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TentCameraPrefab":RSZVariable(name="_TentCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MiniCampCameraPrefab":RSZVariable(name="_MiniCampCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FacilityCameraPrefab":RSZVariable(name="_FacilityCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CharaMakeCameraPrefab":RSZVariable(name="_CharaMakeCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConstCameraPrefab":RSZVariable(name="_ConstCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PhotoCameraPrefab":RSZVariable(name="_PhotoCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MotionCameraPrefab":RSZVariable(name="_MotionCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MotionBlendCameraPrefab":RSZVariable(name="_MotionBlendCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SubspaceRenderCameraPrefab":RSZVariable(name="_SubspaceRenderCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FacilityRenderCameraPrefab":RSZVariable(name="_FacilityRenderCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AttachEmptyObjectPrefab":RSZVariable(name="_AttachEmptyObjectPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PhotoCameraAgentPrefab":RSZVariable(name="_PhotoCameraAgentPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_ChainManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.ChainManagerSetting",typeIDHash=0xa3a1f4a6,CRC=0x23f22e7b,isObject = True,tagList=[])
		self.fields = {
		"_ChainSettingNum":RSZVariable(name="_ChainSettingNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ChainSettingCollectionNum":RSZVariable(name="_ChainSettingCollectionNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_CullingLength":RSZVariable(name="_CullingLength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_CullingBaseFOV":RSZVariable(name="_CullingBaseFOV",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_CharacterMannequinCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.CharacterMannequinCatalog",typeIDHash=0x1fe4c30,CRC=0x82cc7d40,isObject = True,tagList=[])
		self.fields = {
		"_Entries":RSZVariable(name="_Entries",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_ClothManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.ClothManagerSetting",typeIDHash=0x972d1404,CRC=0xce67efc8,isObject = True,tagList=[])
		self.fields = {
		"_ClothSettingNum":RSZVariable(name="_ClothSettingNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ClothSettingCollectionNum":RSZVariable(name="_ClothSettingCollectionNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_CullingLength":RSZVariable(name="_CullingLength",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_CullingBaseFOV":RSZVariable(name="_CullingBaseFOV",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_ConcertLightSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.ConcertLightSetting",typeIDHash=0x2d1e99d1,CRC=0xfe0631e1,isObject = True,tagList=[])
		self.fields = {
		"_PatternContainer":RSZVariable(name="_PatternContainer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EVPatternContainer":RSZVariable(name="_EVPatternContainer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Post":RSZVariable(name="_Post",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_DialogueAISituationParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.DialogueAISituationParam",typeIDHash=0x1497a90c,CRC=0x90395e01,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_DialogueCatalogData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.DialogueCatalogData",typeIDHash=0xf7cbe92,CRC=0x42473d6,isObject = True,tagList=[])
		self.fields = {
		"_ResourceArray":RSZVariable(name="_ResourceArray",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ResourceArrayMulti":RSZVariable(name="_ResourceArrayMulti",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsAllAlwaysLoad":RSZVariable(name="_IsAllAlwaysLoad",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_user_data_DialogueManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.DialogueManagerSetting",typeIDHash=0xa5df6192,CRC=0xe7c40f2,isObject = True,tagList=[])
		self.fields = {
		"_MotPackDataList":RSZVariable(name="_MotPackDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ExtendMotPackDataList":RSZVariable(name="_ExtendMotPackDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TrackDataList":RSZVariable(name="_TrackDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FacialTrackData":RSZVariable(name="_FacialTrackData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ConfigData":RSZVariable(name="_ConfigData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CameraData":RSZVariable(name="_CameraData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnemyGetOutData":RSZVariable(name="_EnemyGetOutData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EvmBasePrefab":RSZVariable(name="_EvmBasePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EffectBasePrefab":RSZVariable(name="_EffectBasePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AdditionalMessagePrefab":RSZVariable(name="_AdditionalMessagePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SubOrder2OrderTable":RSZVariable(name="_SubOrder2OrderTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_LimitedExcute_MissionClear":RSZVariable(name="_LimitedExcute_MissionClear",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NetworkJumpTable":RSZVariable(name="_NetworkJumpTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MsgDataList":RSZVariable(name="_MsgDataList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DialogueContentsMaskData":RSZVariable(name="_DialogueContentsMaskData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BranchExecuteHolder":RSZVariable(name="_BranchExecuteHolder",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AutoLipVolumeMax":RSZVariable(name="_AutoLipVolumeMax",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_AutoLipVolumeMin":RSZVariable(name="_AutoLipVolumeMin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_CostumeAutoLipVolumeOffset":RSZVariable(name="_CostumeAutoLipVolumeOffset",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_AutoLipInterpolationFrame":RSZVariable(name="_AutoLipInterpolationFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_DialogueTimelineEventTable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.DialogueTimelineEventTable",typeIDHash=0x1c0e27b4,CRC=0xa9f9b28f,isObject = True,tagList=[])
		self.fields = {
		"_EventArray":RSZVariable(name="_EventArray",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_EditValueDefinition(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EditValueDefinition",typeIDHash=0x2f2484fe,CRC=0xa5a626ea,isObject = True,tagList=[])
		self.fields = {
		"_Entries":RSZVariable(name="_Entries",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_EditValueMaterialDefinition(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EditValueMaterialDefinition",typeIDHash=0x23b3a1d3,CRC=0x84b8c2b1,isObject = True,tagList=[])
		self.fields = {
		"_Entries":RSZVariable(name="_Entries",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_EffectManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EffectManagerSetting",typeIDHash=0x97d00501,CRC=0xc3edf2a1,isObject = True,tagList=[])
		self.fields = {
		"_HitmarkColorList":RSZVariable(name="_HitmarkColorList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_HitmarkColorGroupNameList":RSZVariable(name="_HitmarkColorGroupNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"_BloodColorExternName":RSZVariable(name="_BloodColorExternName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_AirColorDefault":RSZVariable(name="_AirColorDefault",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaterialNameAir":RSZVariable(name="_MaterialNameAir",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_DragonMilkColor":RSZVariable(name="_DragonMilkColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaterialNameDragonMilk":RSZVariable(name="_MaterialNameDragonMilk",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaterialIDHitTerrainCol":RSZVariable(name="_MaterialIDHitTerrainCol",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaterialAttrHitTerrainCol":RSZVariable(name="_MaterialAttrHitTerrainCol",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_FootLandingSetting":RSZVariable(name="_FootLandingSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GroundSmokeSetting":RSZVariable(name="_GroundSmokeSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PointCloudSetting":RSZVariable(name="_PointCloudSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EffectCollisionDataDefault":RSZVariable(name="_EffectCollisionDataDefault",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_EffectCollisionDataList":RSZVariable(name="_EffectCollisionDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GroupColorSettingDefault":RSZVariable(name="_GroupColorSettingDefault",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GroupColorSettingList":RSZVariable(name="_GroupColorSettingList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DrawOffEffectSetting":RSZVariable(name="_DrawOffEffectSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EffectDecalV2CullingDistanceSqr":RSZVariable(name="_EffectDecalV2CullingDistanceSqr",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EffectDecalV2UpdateSpan":RSZVariable(name="_EffectDecalV2UpdateSpan",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_EmPropConfig(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EmPropConfig",typeIDHash=0xad02c5b0,CRC=0x52051c16,isObject = True,tagList=[])
		self.fields = {
		"_GeneralConfig":RSZVariable(name="_GeneralConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EachIdConfig":RSZVariable(name="_EachIdConfig",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CullingSetting":RSZVariable(name="_CullingSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_EnemyManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnemyManagerSetting",typeIDHash=0x81ab65a7,CRC=0xdfa09ace,isObject = True,tagList=[])
		self.fields = {
		"_CameraShake":RSZVariable(name="_CameraShake",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Common":RSZVariable(name="_Common",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonData":RSZVariable(name="_CommonData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ProcessCullingData":RSZVariable(name="_ProcessCullingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ProcessIntervalData":RSZVariable(name="_ProcessIntervalData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CameraImpactList":RSZVariable(name="_CameraImpactList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GroundDetectData":RSZVariable(name="_GroundDetectData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Difficulty2":RSZVariable(name="_Difficulty2",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DifficultyZako":RSZVariable(name="_DifficultyZako",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RandomSize":RSZVariable(name="_RandomSize",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RandomSizeFish":RSZVariable(name="_RandomSizeFish",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Size":RSZVariable(name="_Size",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickDamage":RSZVariable(name="_GimmickDamage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StageDamage":RSZVariable(name="_StageDamage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Danger":RSZVariable(name="_Danger",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HerdMasterCtrlParams":RSZVariable(name="_HerdMasterCtrlParams",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WeakAttr":RSZVariable(name="_WeakAttr",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BadCondition2":RSZVariable(name="_BadCondition2",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BadConditionPriset":RSZVariable(name="_BadConditionPriset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FeelPreset":RSZVariable(name="_FeelPreset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SensePreset":RSZVariable(name="_SensePreset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EmAttackBadConditionPriset":RSZVariable(name="_EmAttackBadConditionPriset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CombatEmConditionPreset":RSZVariable(name="_CombatEmConditionPreset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemyExSetList":RSZVariable(name="_EnemyExSetList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_Grapple":RSZVariable(name="_Grapple",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemyCategoryList":RSZVariable(name="_EnemyCategoryList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MouthPositioning":RSZVariable(name="_MouthPositioning",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StageResident":RSZVariable(name="_StageResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MudShellSurveillanceData":RSZVariable(name="_MudShellSurveillanceData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_EnemyPackageList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnemyPackageList",typeIDHash=0xf8ffdca7,CRC=0xe0120e6c,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_EnvMaterialParamData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnvMaterialParamData",typeIDHash=0xdb5e3cc8,CRC=0xd597286a,isObject = True,tagList=[])
		self.fields = {
		"_MaterialParamInfoValiations":RSZVariable(name="_MaterialParamInfoValiations",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MaterialParamInfoDefo":RSZVariable(name="_MaterialParamInfoDefo",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ValiationSize":RSZVariable(name="_ValiationSize",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_EnvShaderTimerData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnvShaderTimerData",typeIDHash=0x975d5d48,CRC=0xf17fd7ca,isObject = True,tagList=[])
		self.fields = {
		"_TimerDataList":RSZVariable(name="_TimerDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_EnvironmentManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnvironmentManagerSetting",typeIDHash=0xbcb227e1,CRC=0xf1ae644a,isObject = True,tagList=[])
		self.fields = {
		"_EnvironmentListData":RSZVariable(name="_EnvironmentListData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvironmentManagerInitializeData":RSZVariable(name="_EnvironmentManagerInitializeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvironmentRepopTimeData":RSZVariable(name="_EnvironmentRepopTimeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvMaterialParamData":RSZVariable(name="_EnvMaterialParamData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AbnormalMuddyStreamStartTime":RSZVariable(name="_AbnormalMuddyStreamStartTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_EnvironmentSectionData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnvironmentSectionData",typeIDHash=0x43516c1a,CRC=0x1acd631e,isObject = True,tagList=[])
		self.fields = {
		"_SectionGlobalDatas":RSZVariable(name="_SectionGlobalDatas",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_JanctionTransitionTime_Default":RSZVariable(name="_JanctionTransitionTime_Default",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_JunctionTransitionTimes":RSZVariable(name="_JunctionTransitionTimes",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SectionDataList":RSZVariable(name="_SectionDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_EnvironmentSectionParamData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EnvironmentSectionParamData",typeIDHash=0xa25435a9,CRC=0xb1fc8391,isObject = True,tagList=[])
		self.fields = {
		"SandGround":RSZVariable(name="SandGround",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"ForestGround":RSZVariable(name="ForestGround",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"OilGround":RSZVariable(name="OilGround",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"SandStormWaitSeconds":RSZVariable(name="SandStormWaitSeconds",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"HeavyRainWaitSeconds":RSZVariable(name="HeavyRainWaitSeconds",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"HeatWaveWaitSeconds":RSZVariable(name="HeatWaveWaitSeconds",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BlizzardWaitSeconds":RSZVariable(name="BlizzardWaitSeconds",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"cEm5222_00EggExpandTime":RSZVariable(name="cEm5222_00EggExpandTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"cEm5222_00EggShrinkTime":RSZVariable(name="cEm5222_00EggShrinkTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_EventManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.EventManagerSetting",typeIDHash=0xd8736e34,CRC=0xdbba9225,isObject = True,tagList=[])
		self.fields = {
		"_EventPadVibrationParam":RSZVariable(name="_EventPadVibrationParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DefaultCameraInterpolateTime":RSZVariable(name="_DefaultCameraInterpolateTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_FacilityActingParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.FacilityActingParam",typeIDHash=0xa2ee5220,CRC=0x11cbd994,isObject = True,tagList=[])
		self.fields = {
		"_FacilityID":RSZVariable(name="_FacilityID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FacilityCloseDist":RSZVariable(name="_FacilityCloseDist",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FacilityCloseTime":RSZVariable(name="_FacilityCloseTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FacilityOpenAngle":RSZVariable(name="_FacilityOpenAngle",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FacilityCloseAngle":RSZVariable(name="_FacilityCloseAngle",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsWaitLeavePlayer":RSZVariable(name="_IsWaitLeavePlayer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_IsNaviMovePlayer":RSZVariable(name="_IsNaviMovePlayer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableSkipNaviMovePlayer":RSZVariable(name="_DisableSkipNaviMovePlayer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UseFadeInOut":RSZVariable(name="_UseFadeInOut",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TurnToPlayerInFade":RSZVariable(name="_TurnToPlayerInFade",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ColliderPrefab":RSZVariable(name="_ColliderPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ActingData":RSZVariable(name="_ActingData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Detail":RSZVariable(name="_Detail",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_FoliageManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.FoliageManagerSetting",typeIDHash=0xd4451d6c,CRC=0xda78174a,isObject = True,tagList=[])
		self.fields = {
		"_MaxFoliageSettingNum":RSZVariable(name="_MaxFoliageSettingNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_UseRayOffset":RSZVariable(name="_UseRayOffset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnableUserVertexShaderDynamicShadow":RSZVariable(name="_EnableUserVertexShaderDynamicShadow",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UseTextureStreamingDistanceThreshold":RSZVariable(name="_UseTextureStreamingDistanceThreshold",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_TextureStreamingDistanceThreshold":RSZVariable(name="_TextureStreamingDistanceThreshold",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsEnableLodGpuMode":RSZVariable(name="_IsEnableLodGpuMode",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_LodGpuModeInstanceNum":RSZVariable(name="_LodGpuModeInstanceNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_GrassCullingSetting":RSZVariable(name="_GrassCullingSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MossCullingSetting":RSZVariable(name="_MossCullingSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_GUICreateIDSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GUICreateIDSetting",typeIDHash=0xbd2560ac,CRC=0x2ec73c33,isObject = True,tagList=[])
		self.fields = {
		"_Layer":RSZVariable(name="_Layer",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_GUIList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GUIList",typeIDHash=0x8a3c27ee,CRC=0x674aa51a,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_GameInputManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GameInputManagerSetting",typeIDHash=0xb436bb05,CRC=0x82da0a56,isObject = True,tagList=[])
		self.fields = {
		"_RawKeyDefinitionPad":RSZVariable(name="_RawKeyDefinitionPad",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RawKeyDefinitonMkb":RSZVariable(name="_RawKeyDefinitonMkb",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_KeySuccessTypeSetting":RSZVariable(name="_KeySuccessTypeSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PadPlayerGameKeyDefData":RSZVariable(name="_PadPlayerGameKeyDefData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PadUIGameKeyDefData":RSZVariable(name="_PadUIGameKeyDefData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MkbPlayerGameKeyDefData":RSZVariable(name="_MkbPlayerGameKeyDefData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlayerGameInputConvertInfo":RSZVariable(name="_PlayerGameInputConvertInfo",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MkbUIGameKeyDefData":RSZVariable(name="_MkbUIGameKeyDefData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DevGameKeyDefData":RSZVariable(name="_DevGameKeyDefData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_GameMiniEventSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GameMiniEventSetting",typeIDHash=0x5c9826f5,CRC=0x85ce7844,isObject = True,tagList=[])
		self.fields = {
		"_TalkParam":RSZVariable(name="_TalkParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ObserveParam":RSZVariable(name="_ObserveParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FindCampArea":RSZVariable(name="_FindCampArea",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FieldIntro":RSZVariable(name="_FieldIntro",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BowlingParam":RSZVariable(name="_BowlingParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_GimmickCommonParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GimmickCommonParam",typeIDHash=0x1264c8d3,CRC=0x282e08a,isObject = True,tagList=[])
		self.fields = {
		"_FieldInfos":RSZVariable(name="_FieldInfos",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ID":RSZVariable(name="_ID",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IsActiveCullingCollision":RSZVariable(name="_IsActiveCullingCollision",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_CanClimbGimmick":RSZVariable(name="_CanClimbGimmick",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DistToSendGroundChangeMsg":RSZVariable(name="_DistToSendGroundChangeMsg",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsObstacleGimmick":RSZVariable(name="_IsObstacleGimmick",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class app_user_data_GimmickListConfig(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GimmickListConfig",typeIDHash=0xc95087a3,CRC=0xbb32df86,isObject = True,tagList=[])
		self.fields = {
		"_GimmickList":RSZVariable(name="_GimmickList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_GimmickManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GimmickManagerSetting",typeIDHash=0x469d85db,CRC=0xcc642aab,isObject = True,tagList=[])
		self.fields = {
		"_CampSetting":RSZVariable(name="_CampSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnvironmentSetManagerSetting":RSZVariable(name="_EnvironmentSetManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StageDamageSetting":RSZVariable(name="_StageDamageSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CountManagerSetting":RSZVariable(name="_CountManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EruptManagerSetting":RSZVariable(name="_EruptManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_LimeStoneManagerSetting":RSZVariable(name="_LimeStoneManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_LightningManagerSetting":RSZVariable(name="_LightningManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TrapSetting":RSZVariable(name="_TrapSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BowlingSetting":RSZVariable(name="_BowlingSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_Gm100_100_BbbUniqueParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.Gm100_100_BbbUniqueParam",typeIDHash=0x39d6c086,CRC=0xafd580b1,isObject = True,tagList=[])
		self.fields = {
		"_FieldInfos":RSZVariable(name="_FieldInfos",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SpringForce":RSZVariable(name="_SpringForce",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Damping":RSZVariable(name="_Damping",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ElasticCoef":RSZVariable(name="_ElasticCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_CogLerpSpeed":RSZVariable(name="_CogLerpSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RollPerMeter":RSZVariable(name="_RollPerMeter",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RollEffectMaxDistance":RSZVariable(name="_RollEffectMaxDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RollEffectZRate":RSZVariable(name="_RollEffectZRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_BlendRateTimerLimit":RSZVariable(name="_BlendRateTimerLimit",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_Gm100_103_BbbUniqueParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.Gm100_103_BbbUniqueParam",typeIDHash=0x2464fa1c,CRC=0x96e7577c,isObject = True,tagList=[])
		self.fields = {
		"_FieldInfos":RSZVariable(name="_FieldInfos",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MediumBPM":RSZVariable(name="_MediumBPM",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FastBPM":RSZVariable(name="_FastBPM",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_Gm100_AaaUniqueParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.Gm100_AaaUniqueParam",typeIDHash=0x54cce6e5,CRC=0xdd4166c6,isObject = True,tagList=[])
		self.fields = {
		"_FieldInfos":RSZVariable(name="_FieldInfos",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_GraphicsManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GraphicsManagerSetting",typeIDHash=0xeb180a83,CRC=0x5e6e4416,isObject = True,tagList=[])
		self.fields = {
		"_GlobalMaterialParam":RSZVariable(name="_GlobalMaterialParam",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_GlobalMaterialParamInstanceNum":RSZVariable(name="_GlobalMaterialParamInstanceNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"CullingLengthChain":RSZVariable(name="CullingLengthChain",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"CullingLengthCloth":RSZVariable(name="CullingLengthCloth",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_LodSelectionAlogrithm":RSZVariable(name="_LodSelectionAlogrithm",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_DissolveCameraNearParam":RSZVariable(name="_DissolveCameraNearParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ShaderTimerParamList":RSZVariable(name="_ShaderTimerParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BeltConveyorSetting":RSZVariable(name="_BeltConveyorSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_StreamingExpirationFrameCount":RSZVariable(name="_StreamingExpirationFrameCount",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_Dialogue_StreamingExpirationFrameCount":RSZVariable(name="_Dialogue_StreamingExpirationFrameCount",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_FoliageBABStaticParam":RSZVariable(name="_FoliageBABStaticParam",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_FoliageBABStaticParamNum":RSZVariable(name="_FoliageBABStaticParamNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_ShadowRotationThreshold":RSZVariable(name="_ShadowRotationThreshold",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_GroundHeightEditData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GroundHeightEditData",typeIDHash=0x7c4068d4,CRC=0x63903784,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_GroundManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GroundManagerSetting",typeIDHash=0x4687baf6,CRC=0xf4d062d4,isObject = True,tagList=[])
		self.fields = {
		"_MaxEditNum":RSZVariable(name="_MaxEditNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_MaxEditNum_WithoutCollision":RSZVariable(name="_MaxEditNum_WithoutCollision",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_PhysicsFilterInfos":RSZVariable(name="_PhysicsFilterInfos",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_DynamicsFilterInfos":RSZVariable(name="_DynamicsFilterInfos",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_SurfaceTrailMaxNum":RSZVariable(name="_SurfaceTrailMaxNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_SurfaceTrailTexture":RSZVariable(name="_SurfaceTrailTexture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_SurfaceTrailPatternNum":RSZVariable(name="_SurfaceTrailPatternNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PreloadKeepFrame":RSZVariable(name="_PreloadKeepFrame",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_GroundSplatRegionSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GroundSplatRegionSetting",typeIDHash=0xe529d498,CRC=0x63b7c4d,isObject = True,tagList=[])
		self.fields = {
		"_Settings":RSZVariable(name="_Settings",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_GuideInsectList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.GuideInsectList",typeIDHash=0x5718f64a,CRC=0xa395754b,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_HeatReceiverSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.HeatReceiverSetting",typeIDHash=0x90ef8100,CRC=0x4abe6f0a,isObject = True,tagList=[])
		self.fields = {
		"_Params":RSZVariable(name="_Params",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnvironmentParams":RSZVariable(name="_EnvironmentParams",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_HeatSourceSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.HeatSourceSetting",typeIDHash=0xe0bda11d,CRC=0xe8a30a3c,isObject = True,tagList=[])
		self.fields = {
		"_Params":RSZVariable(name="_Params",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_LobbyLiveCameraSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.LobbyLiveCameraSetting",typeIDHash=0xbdd8c83,CRC=0x97444951,isObject = True,tagList=[])
		self.fields = {
		"_CameraPrefab":RSZVariable(name="_CameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FarCameraPrefab":RSZVariable(name="_FarCameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_VirtualWorkPrefab":RSZVariable(name="_VirtualWorkPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Basic":RSZVariable(name="_Basic",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WorkData":RSZVariable(name="_WorkData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ScheduleData":RSZVariable(name="_ScheduleData",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_IntervalScheduleData":RSZVariable(name="_IntervalScheduleData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_MantleList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.MantleList",typeIDHash=0x43df4af3,CRC=0x20f3a93e,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_MasterFieldManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.MasterFieldManagerSetting",typeIDHash=0xde106e4f,CRC=0x8769bdb6,isObject = True,tagList=[])
		self.fields = {
		"_LoadSetting":RSZVariable(name="_LoadSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DrawSetting":RSZVariable(name="_DrawSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_MeshManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.MeshManagerSetting",typeIDHash=0xdf06e1b7,CRC=0x107e6ea9,isObject = True,tagList=[])
		self.fields = {
		"_Base":RSZVariable(name="_Base",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PassThrough":RSZVariable(name="_PassThrough",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Culling":RSZVariable(name="_Culling",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Wind":RSZVariable(name="_Wind",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_JointConstraints":RSZVariable(name="_JointConstraints",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Visible":RSZVariable(name="_Visible",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AOGeometry":RSZVariable(name="_AOGeometry",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ShellFur":RSZVariable(name="_ShellFur",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BlendShape":RSZVariable(name="_BlendShape",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandCover":RSZVariable(name="_SandCover",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WetCover":RSZVariable(name="_WetCover",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BaseFOV":RSZVariable(name="_BaseFOV",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_MissionManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.MissionManagerSetting",typeIDHash=0xd8a6cd5a,CRC=0x5003fec8,isObject = True,tagList=[])
		self.fields = {
		"_MissionCameraAttachParam":RSZVariable(name="_MissionCameraAttachParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HunterRankCapData":RSZVariable(name="_HunterRankCapData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HaltParam":RSZVariable(name="_HaltParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HaltParamQuest":RSZVariable(name="_HaltParamQuest",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HaltStorySituationParam":RSZVariable(name="_HaltStorySituationParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestSetting":RSZVariable(name="_QuestSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StoryMapStageData":RSZVariable(name="_StoryMapStageData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StoryFlagPackingData":RSZVariable(name="_StoryFlagPackingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StoryBaseCampChangeData":RSZVariable(name="_StoryBaseCampChangeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MissionActivityData":RSZVariable(name="_MissionActivityData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SetMissionBeaconPosList":RSZVariable(name="_SetMissionBeaconPosList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StoryDisableCommonArea":RSZVariable(name="_StoryDisableCommonArea",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StoryDefaultQuestStartPoint":RSZVariable(name="_StoryDefaultQuestStartPoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SideMissionSummarySetting":RSZVariable(name="_SideMissionSummarySetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MissionPriorityData":RSZVariable(name="_MissionPriorityData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MissionPriorityFreeData":RSZVariable(name="_MissionPriorityFreeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_MissionResident(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.MissionResident",typeIDHash=0xa6845bc9,CRC=0xcb84e9e8,isObject = True,tagList=[])
		self.fields = {
		"_MissionListData":RSZVariable(name="_MissionListData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_MissionResidentCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.MissionResidentCatalog",typeIDHash=0x37219fcb,CRC=0x3a701db4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_MissionResident":RSZVariable(name="_MissionResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_ModelBlendShapeInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.ModelBlendShapeInfo",typeIDHash=0x195ad262,CRC=0xe96bb085,isObject = True,tagList=[])
		self.fields = {
		"_Conditions":RSZVariable(name="_Conditions",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_NavSafePosUserData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NavSafePosUserData",typeIDHash=0x4028a265,CRC=0x8eed4779,isObject = True,tagList=[])
		self.fields = {
		"_NavSafePosList":RSZVariable(name="_NavSafePosList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_NpcAccessoryPackages(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcAccessoryPackages",typeIDHash=0x67f59c63,CRC=0x77e5cf93,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AccessoryEnum":RSZVariable(name="_AccessoryEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_NpcCustomAttachmentVariList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcCustomAttachmentVariList",typeIDHash=0x9d5d5c4b,CRC=0x442c6026,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnumMaker":RSZVariable(name="_EnumMaker",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_NpcCustomVariList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcCustomVariList",typeIDHash=0x7377a4a4,CRC=0xa832d35e,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnumMaker":RSZVariable(name="_EnumMaker",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_NpcEmCommonPackages(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcEmCommonPackages",typeIDHash=0x8601366,CRC=0x51c2ca81,isObject = True,tagList=[])
		self.fields = {
		"_EnumMaker":RSZVariable(name="_EnumMaker",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_NpcManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcManagerSetting",typeIDHash=0x786ac45c,CRC=0x53e0b13b,isObject = True,tagList=[])
		self.fields = {
		"_GroupAIManagerPackages":RSZVariable(name="_GroupAIManagerPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FieldUnitManagerPackages":RSZVariable(name="_FieldUnitManagerPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CombiMgrPrefab":RSZVariable(name="_CombiMgrPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FormationManagerPrefab":RSZVariable(name="_FormationManagerPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RoutePointDataPrefab":RSZVariable(name="_RoutePointDataPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LinearActPrefab":RSZVariable(name="_LinearActPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WorldAnalyzerPrefab":RSZVariable(name="_WorldAnalyzerPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AIThinkPackages":RSZVariable(name="_AIThinkPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AIThinkPackages_Alone":RSZVariable(name="_AIThinkPackages_Alone",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ProcessCullingData":RSZVariable(name="_ProcessCullingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TalkCollsionPrefab":RSZVariable(name="_TalkCollsionPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DesireCategoryPackages":RSZVariable(name="_DesireCategoryPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SpeechSubCategoryPackages":RSZVariable(name="_SpeechSubCategoryPackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_NpcPackageList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcPackageList",typeIDHash=0xc22e4170,CRC=0x5636db9c,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_NpcPartnerPackages(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.NpcPartnerPackages",typeIDHash=0x4559256,CRC=0x320a2cb2,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_OnlyAreaSplatSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.OnlyAreaSplatSetting",typeIDHash=0x9945863d,CRC=0xaeaea79a,isObject = True,tagList=[])
		self.fields = {
		"_GroundSplatBaseSetting":RSZVariable(name="_GroundSplatBaseSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_OtomoEquipList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.OtomoEquipList",typeIDHash=0x4aaf7561,CRC=0xc992f9cd,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_OtomoPartsList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.OtomoPartsList",typeIDHash=0x7d84d0f2,CRC=0x9afb26cc,isObject = True,tagList=[])
		self.fields = {
		"_PartsPrefabList":RSZVariable(name="_PartsPrefabList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_OtomoResident(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.OtomoResident",typeIDHash=0x55f64253,CRC=0x9b58f8e8,isObject = True,tagList=[])
		self.fields = {
		"_GlobalParam":RSZVariable(name="_GlobalParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OtomoPrefab":RSZVariable(name="_OtomoPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ReplicaOtomoPrefab":RSZVariable(name="_ReplicaOtomoPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GoaTreeStorage":RSZVariable(name="_GoaTreeStorage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcOtomoPrefab":RSZVariable(name="_NpcOtomoPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PartnerOtomoCreateDataPackage":RSZVariable(name="_PartnerOtomoCreateDataPackage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_OtomoResidentCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.OtomoResidentCatalog",typeIDHash=0x6283eb0a,CRC=0x3487dffa,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_OtomoResident":RSZVariable(name="_OtomoResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PlayerAllWeaponPack(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PlayerAllWeaponPack",typeIDHash=0xfa94edb5,CRC=0xfe055f86,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Wp10InsectList":RSZVariable(name="_Wp10InsectList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WeaponCharmPrefabList":RSZVariable(name="_WeaponCharmPrefabList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PlayerArmorList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PlayerArmorList",typeIDHash=0x7710cd4e,CRC=0xfbe0dbc3,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FemaleDataList":RSZVariable(name="_FemaleDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_PlayerManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PlayerManagerSetting",typeIDHash=0x485fdeb9,CRC=0x858bace7,isObject = True,tagList=[])
		self.fields = {
		"_InteractManagerSetting":RSZVariable(name="_InteractManagerSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PlayerResident(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PlayerResident",typeIDHash=0xa260f605,CRC=0xdab8a688,isObject = True,tagList=[])
		self.fields = {
		"_PlayerPrefab":RSZVariable(name="_PlayerPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ReplicaPlayerPrefab":RSZVariable(name="_ReplicaPlayerPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CameraPrefab":RSZVariable(name="_CameraPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MaleSkeleton":RSZVariable(name="_MaleSkeleton",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_FemaleSkeleton":RSZVariable(name="_FemaleSkeleton",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MaleJointConstraints":RSZVariable(name="_MaleJointConstraints",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_FemaleJointConstraints":RSZVariable(name="_FemaleJointConstraints",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_MaleFace":RSZVariable(name="_MaleFace",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FemaleFace":RSZVariable(name="_FemaleFace",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RopePrefab":RSZVariable(name="_RopePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_YokuryuuPrefab":RSZVariable(name="_YokuryuuPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TentStovePrefab":RSZVariable(name="_TentStovePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TentKettlePrefab":RSZVariable(name="_TentKettlePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FishingFloatPrefab":RSZVariable(name="_FishingFloatPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BasicLeftKnifePrefab":RSZVariable(name="_BasicLeftKnifePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BasicRightKnifePrefab":RSZVariable(name="_BasicRightKnifePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GhillieSuitPrefab":RSZVariable(name="_GhillieSuitPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CagePrefab":RSZVariable(name="_CagePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GlobalParam":RSZVariable(name="_GlobalParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlayerCommandList":RSZVariable(name="_PlayerCommandList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PcPlayerCommandList":RSZVariable(name="_PcPlayerCommandList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MaleTalkMotionBank":RSZVariable(name="_MaleTalkMotionBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_FemaleTalkMotionBank":RSZVariable(name="_FemaleTalkMotionBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MaleBodyEditMotionBank":RSZVariable(name="_MaleBodyEditMotionBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_FemaleBodyEditMotionBank":RSZVariable(name="_FemaleBodyEditMotionBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_WeaponsResident":RSZVariable(name="_WeaponsResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlayerItemParam":RSZVariable(name="_PlayerItemParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlayerEffectParam":RSZVariable(name="_PlayerEffectParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonActionBTable":RSZVariable(name="_CommonActionBTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonSubActionBTable":RSZVariable(name="_CommonSubActionBTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ActionCameraMotionBank":RSZVariable(name="_ActionCameraMotionBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_CameraAttachParam":RSZVariable(name="_CameraAttachParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonCameraShake":RSZVariable(name="_CommonCameraShake",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonCameraImpact":RSZVariable(name="_CommonCameraImpact",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PostEffectSceneBank":RSZVariable(name="_PostEffectSceneBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ZoneCameraAttachParam":RSZVariable(name="_ZoneCameraAttachParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_RecoilParamList":RSZVariable(name="_RecoilParamList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonCameraWork":RSZVariable(name="_CommonCameraWork",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FacilityCameraWork":RSZVariable(name="_FacilityCameraWork",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ZonePostEffectSceneBank":RSZVariable(name="_ZonePostEffectSceneBank",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MoveBankPack":RSZVariable(name="_MoveBankPack",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_JointDelayPack":RSZVariable(name="_JointDelayPack",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonPadVibration":RSZVariable(name="_CommonPadVibration",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonADVibration":RSZVariable(name="_CommonADVibration",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AmuletColorData":RSZVariable(name="_AmuletColorData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PlayerResidentAdd(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PlayerResidentAdd",typeIDHash=0x57e885a6,CRC=0x84166315,isObject = True,tagList=[])
		self.fields = {
		"_ExEmote00Epvr":RSZVariable(name="_ExEmote00Epvr",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ExEmote00FacePrefab":RSZVariable(name="_ExEmote00FacePrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ExEmote00GuestColors":RSZVariable(name="_ExEmote00GuestColors",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PlayerResidentCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PlayerResidentCatalog",typeIDHash=0x95616c7d,CRC=0x1a5c25e8,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_PlayerResident":RSZVariable(name="_PlayerResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlayerResidentAdd":RSZVariable(name="_PlayerResidentAdd",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PorterEquipList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PorterEquipList",typeIDHash=0x60d9fea,CRC=0xa952be81,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_PorterList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PorterList",typeIDHash=0xc82d18ee,CRC=0x3b4ded0d,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_PorterParamCommon(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PorterParamCommon",typeIDHash=0x7f10762e,CRC=0x30af5e08,isObject = True,tagList=[])
		self.fields = {
		"_JointConst":RSZVariable(name="_JointConst",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PorterDamageActionData":RSZVariable(name="_PorterDamageActionData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PorterDodgeDamageTypeData":RSZVariable(name="_PorterDodgeDamageTypeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SaddleData":RSZVariable(name="_SaddleData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ReinData":RSZVariable(name="_ReinData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StirrupData":RSZVariable(name="_StirrupData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WeaponBagsData":RSZVariable(name="_WeaponBagsData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SlopeIkSupporterParam":RSZVariable(name="_SlopeIkSupporterParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_IkHandleCorrectionParam":RSZVariable(name="_IkHandleCorrectionParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EyeCtrlParam":RSZVariable(name="_EyeCtrlParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EyeBlinkCycle":RSZVariable(name="_EyeBlinkCycle",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Communicate":RSZVariable(name="_Communicate",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_TerrainCheck":RSZVariable(name="_TerrainCheck",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MoveControl":RSZVariable(name="_MoveControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NavigationControl":RSZVariable(name="_NavigationControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ColliderControl":RSZVariable(name="_ColliderControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SensorHit":RSZVariable(name="_SensorHit",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IkLegSpineData":RSZVariable(name="_IkLegSpineData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_IkCtrlData":RSZVariable(name="_IkCtrlData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ManualAutoJump":RSZVariable(name="_ManualAutoJump",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_OfferControl":RSZVariable(name="_OfferControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ExteriorScan":RSZVariable(name="_ExteriorScan",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Gesture":RSZVariable(name="_Gesture",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WaitPointGesture":RSZVariable(name="_WaitPointGesture",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Glide":RSZVariable(name="_Glide",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BTable":RSZVariable(name="_BTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SpeedTree":RSZVariable(name="_SpeedTree",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CombatPositioning":RSZVariable(name="_CombatPositioning",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_NoCombatPositioning":RSZVariable(name="_NoCombatPositioning",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_HidePositioning":RSZVariable(name="_HidePositioning",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DodgeStamina":RSZVariable(name="_DodgeStamina",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WaitPointBase":RSZVariable(name="_WaitPointBase",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WaitPointGimmick":RSZVariable(name="_WaitPointGimmick",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_AutoAreaPatrol":RSZVariable(name="_AutoAreaPatrol",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LookAt":RSZVariable(name="_LookAt",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"LookedPos":RSZVariable(name="LookedPos",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EmoteControl":RSZVariable(name="_EmoteControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Gimmick":RSZVariable(name="Gimmick",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Event":RSZVariable(name="_Event",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ActionAgentPrefab":RSZVariable(name="_ActionAgentPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_SandSinkParam":RSZVariable(name="_SandSinkParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_JointEffectPack":RSZVariable(name="_JointEffectPack",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HeatCheckParam":RSZVariable(name="_HeatCheckParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PartsReduction":RSZVariable(name="_PartsReduction",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MotionPartsStabilizer":RSZVariable(name="_MotionPartsStabilizer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PointQuery":RSZVariable(name="_PointQuery",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_CommEmote":RSZVariable(name="_CommEmote",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_RideRushAttack":RSZVariable(name="_RideRushAttack",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_DamageEar":RSZVariable(name="_DamageEar",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Grill":RSZVariable(name="_Grill",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_Fishing":RSZVariable(name="_Fishing",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_PorterResident(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PorterResident",typeIDHash=0x7842f109,CRC=0x13d163be,isObject = True,tagList=[])
		self.fields = {
		"_PorterEquipVisualSettingList":RSZVariable(name="_PorterEquipVisualSettingList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_PorterResidentCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.PorterResidentCatalog",typeIDHash=0x8877a6ed,CRC=0xca8413cd,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_PorterResident":RSZVariable(name="_PorterResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_RayTracingForStageData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.RayTracingForStageData",typeIDHash=0x920e3e33,CRC=0x98c20d51,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_RecitalSongPackageList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.RecitalSongPackageList",typeIDHash=0x68fa6e95,CRC=0x2469171d,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_SpeedTreeManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.SpeedTreeManagerSetting",typeIDHash=0x681c6529,CRC=0xf6624439,isObject = True,tagList=[])
		self.fields = {
		"_MaxWindSpeed":RSZVariable(name="_MaxWindSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_RipplingWindRate":RSZVariable(name="_RipplingWindRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_VortexelWindResponse":RSZVariable(name="_VortexelWindResponse",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EnablePushCollision":RSZVariable(name="_EnablePushCollision",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EnablePushCollisionMesh":RSZVariable(name="_EnablePushCollisionMesh",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_PushCollisionBufferNum":RSZVariable(name="_PushCollisionBufferNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PushCollisionNum":RSZVariable(name="_PushCollisionNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PushCollisionBuffer":RSZVariable(name="_PushCollisionBuffer",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_EnableDualHeightFieldTrail":RSZVariable(name="_EnableDualHeightFieldTrail",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DualHeightFieldTrailSetting":RSZVariable(name="_DualHeightFieldTrailSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FloorPushCollisionNum":RSZVariable(name="_FloorPushCollisionNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_FloorPushBias":RSZVariable(name="_FloorPushBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_FloorPushSphereBias":RSZVariable(name="_FloorPushSphereBias",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_StageSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.StageSetting",typeIDHash=0x51be95ec,CRC=0x4640c85c,isObject = True,tagList=[])
		self.fields = {
		"_GridLoadRelation":RSZVariable(name="_GridLoadRelation",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_IsUseLoadRelationManually":RSZVariable(name="_IsUseLoadRelationManually",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_GridLoadRelationManually":RSZVariable(name="_GridLoadRelationManually",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ProxyLODRange":RSZVariable(name="_ProxyLODRange",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ProxyLODRangePC":RSZVariable(name="_ProxyLODRangePC",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsUseProxyLODYRange":RSZVariable(name="_IsUseProxyLODYRange",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_ProxyLODYPosRange":RSZVariable(name="_ProxyLODYPosRange",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ProxyLODYNegRange":RSZVariable(name="_ProxyLODYNegRange",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_PlantGridRange":RSZVariable(name="_PlantGridRange",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_TreeGridRange":RSZVariable(name="_TreeGridRange",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_Grid32Mergin":RSZVariable(name="_Grid32Mergin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Grid64Mergin":RSZVariable(name="_Grid64Mergin",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsUseLoadSupport":RSZVariable(name="_IsUseLoadSupport",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_LoadSupportRange":RSZVariable(name="_LoadSupportRange",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_SurfaceTrailZoneData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.SurfaceTrailZoneData",typeIDHash=0x35911e9,CRC=0x66319dd0,isObject = True,tagList=[])
		self.fields = {
		"_ZoneAABB":RSZVariable(name="_ZoneAABB",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_TimelineEventDynamicResourceDataCatalog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.TimelineEventDynamicResourceDataCatalog",typeIDHash=0xc87d1d1d,CRC=0x1084a628,isObject = True,tagList=[])
		self.fields = {
		"_ResourceArray":RSZVariable(name="_ResourceArray",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class app_user_data_TimelineEventResourceList(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.TimelineEventResourceList",typeIDHash=0x128c8971,CRC=0x5009c7ec,isObject = True,tagList=[])
		self.fields = {
		"_ResourceArray":RSZVariable(name="_ResourceArray",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_UnderwaterChainParameter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.UnderwaterChainParameter",typeIDHash=0xacab5fe7,CRC=0x882ea57b,isObject = True,tagList=[])
		self.fields = {
		"_CoordJoint":RSZVariable(name="_CoordJoint",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_ForceDirRotationOffset":RSZVariable(name="_ForceDirRotationOffset",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		"_ForceDirMaxAngle":RSZVariable(name="_ForceDirMaxAngle",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ForceCycleDuration":RSZVariable(name="_ForceCycleDuration",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"_ForceDamping":RSZVariable(name="_ForceDamping",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_DelayOffsetTimeRange":RSZVariable(name="_DelayOffsetTimeRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"_ForceTimeRange":RSZVariable(name="_ForceTimeRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"_ForceCoef":RSZVariable(name="_ForceCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ParameterFixMode":RSZVariable(name="_ParameterFixMode",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_GravityRate":RSZVariable(name="_GravityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_DampingRate":RSZVariable(name="_DampingRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Gravity":RSZVariable(name="_Gravity",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"_Damping":RSZVariable(name="_Damping",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_VariousDataManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.VariousDataManagerSetting",typeIDHash=0x35e9644e,CRC=0x7e560c72,isObject = True,tagList=[])
		self.fields = {
		"_ItemSetting":RSZVariable(name="_ItemSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_MenuSetting":RSZVariable(name="_MenuSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_GameSystemSetting":RSZVariable(name="_GameSystemSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnemyData":RSZVariable(name="_EnemyData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemyQuestData":RSZVariable(name="_EnemyQuestData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemyPartsTypeData":RSZVariable(name="_EnemyPartsTypeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemySpeciesData":RSZVariable(name="_EnemySpeciesData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemyReportSetting":RSZVariable(name="_EnemyReportSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PanelTutorialData":RSZVariable(name="_PanelTutorialData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TipsData":RSZVariable(name="_TipsData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TutorialCategoryData":RSZVariable(name="_TutorialCategoryData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickBasicData":RSZVariable(name="_GimmickBasicData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickTextData":RSZVariable(name="_GimmickTextData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickControlData":RSZVariable(name="_GimmickControlData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ExGimmickEventData":RSZVariable(name="_ExGimmickEventData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ExAnimalEventData":RSZVariable(name="_ExAnimalEventData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ActionTutorialData":RSZVariable(name="_ActionTutorialData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ActionGuideSetting":RSZVariable(name="_ActionGuideSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PressWeight":RSZVariable(name="_PressWeight",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MinimumShellPrefab":RSZVariable(name="_MinimumShellPrefab",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EquipDatas":RSZVariable(name="_EquipDatas",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MapDrawSettingData":RSZVariable(name="_MapDrawSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MapStageDrawData":RSZVariable(name="_MapStageDrawData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StageLocation":RSZVariable(name="_StageLocation",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AreaFieldZonePackages":RSZVariable(name="_AreaFieldZonePackages",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DarkAreaData":RSZVariable(name="_DarkAreaData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MapModelData":RSZVariable(name="_MapModelData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcResident":RSZVariable(name="_NpcResident",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CameraFieldOffset":RSZVariable(name="_CameraFieldOffset",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_HandNoise":RSZVariable(name="_HandNoise",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PostCommon":RSZVariable(name="_PostCommon",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CharaMakeCatalogue":RSZVariable(name="_CharaMakeCatalogue",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EventCameraShake":RSZVariable(name="_EventCameraShake",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PlEnum":RSZVariable(name="_PlEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_PorterEnum":RSZVariable(name="_PorterEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CameraEnum":RSZVariable(name="_CameraEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EmEnum":RSZVariable(name="_EmEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NpcEnum":RSZVariable(name="_NpcEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickEnum":RSZVariable(name="_GimmickEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FieldEnum":RSZVariable(name="_FieldEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ExEnum":RSZVariable(name="_ExEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GUIEnum":RSZVariable(name="_GUIEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DialogueEnum":RSZVariable(name="_DialogueEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GroundEnum":RSZVariable(name="_GroundEnum",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GUIVariousData":RSZVariable(name="_GUIVariousData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FacilitySetting":RSZVariable(name="_FacilitySetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_EnemyRewardSettingData":RSZVariable(name="_EnemyRewardSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickRewardSettingData":RSZVariable(name="_GimmickRewardSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickAddRewardSettingData":RSZVariable(name="_GimmickAddRewardSettingData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GimmickCollectNumTable":RSZVariable(name="_GimmickCollectNumTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_FacialData":RSZVariable(name="_FacialData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SkillData":RSZVariable(name="_SkillData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SkillCommonData":RSZVariable(name="_SkillCommonData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CharacterEditData":RSZVariable(name="_CharacterEditData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SeikretEditData":RSZVariable(name="_SeikretEditData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TentCustomizeData":RSZVariable(name="_TentCustomizeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NPCCustomizeData":RSZVariable(name="_NPCCustomizeData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TutorialTextureData":RSZVariable(name="_TutorialTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_TutorialMovieData":RSZVariable(name="_TutorialMovieData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OptionTextureData":RSZVariable(name="_OptionTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_OtSupportMovieData":RSZVariable(name="_OtSupportMovieData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ActionGuidanceTextureData":RSZVariable(name="_ActionGuidanceTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ActionGuidanceMovieData":RSZVariable(name="_ActionGuidanceMovieData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ActionGuidanceGaugeTextureData":RSZVariable(name="_ActionGuidanceGaugeTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GalleryTextureData":RSZVariable(name="_GalleryTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DLCStoreTextureData":RSZVariable(name="_DLCStoreTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_BackgroundTextureData":RSZVariable(name="_BackgroundTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_LobbyDiningMenuTextureData":RSZVariable(name="_LobbyDiningMenuTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GUIEnemyIconTextureData":RSZVariable(name="_GUIEnemyIconTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_WeaponIntroductionData":RSZVariable(name="_WeaponIntroductionData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ExFieldParam":RSZVariable(name="_ExFieldParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestAwardData":RSZVariable(name="_QuestAwardData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommonQuestRewardData":RSZVariable(name="_CommonQuestRewardData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_AddQuestRewardData":RSZVariable(name="_AddQuestRewardData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestRewardNumTableData":RSZVariable(name="_QuestRewardNumTableData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SeasonSkillNumTableData":RSZVariable(name="_SeasonSkillNumTableData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestRewardLotProbabilityTable":RSZVariable(name="_QuestRewardLotProbabilityTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestRewardVariousData":RSZVariable(name="_QuestRewardVariousData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestRewardSetting":RSZVariable(name="_QuestRewardSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ExQuestRewardSetting":RSZVariable(name="_ExQuestRewardSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_QuestRewardRateData":RSZVariable(name="_QuestRewardRateData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MissionRewardData":RSZVariable(name="_MissionRewardData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DefaultAnimationLodParameter":RSZVariable(name="_DefaultAnimationLodParameter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StaffRoll00DispData":RSZVariable(name="_StaffRoll00DispData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StaffRoll01DispData":RSZVariable(name="_StaffRoll01DispData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StaffRoll02DispData":RSZVariable(name="_StaffRoll02DispData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_StaffRoll03DispData":RSZVariable(name="_StaffRoll03DispData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_CommunicationDataSetting":RSZVariable(name="_CommunicationDataSetting",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_PorterDodgeTypeDamage":RSZVariable(name="_PorterDodgeTypeDamage",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GUILoadTextureData":RSZVariable(name="_GUILoadTextureData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MapBackPrefabData":RSZVariable(name="_MapBackPrefabData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ShaderCollection":RSZVariable(name="_ShaderCollection",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnemyCountData":RSZVariable(name="_EnemyCountData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_SupportNpcIntroData":RSZVariable(name="_SupportNpcIntroData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DlcProductIdList":RSZVariable(name="_DlcProductIdList",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_DlcLinkData":RSZVariable(name="_DlcLinkData",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NewMarkFlagIndexes_OuterArmor":RSZVariable(name="_NewMarkFlagIndexes_OuterArmor",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_NewMarkFlagIndexes_OtomoOuterArmor":RSZVariable(name="_NewMarkFlagIndexes_OtomoOuterArmor",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_VramSize":RSZVariable(name="_VramSize",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_GraphicsOptionLoadLevel":RSZVariable(name="_GraphicsOptionLoadLevel",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_MapZoomMax_TriggerPower":RSZVariable(name="_MapZoomMax_TriggerPower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MapZoomMax_TriggerFreq":RSZVariable(name="_MapZoomMax_TriggerFreq",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MapZoomMax_TriggerStartPos":RSZVariable(name="_MapZoomMax_TriggerStartPos",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MapZoomMax_TriggerEndPos":RSZVariable(name="_MapZoomMax_TriggerEndPos",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MapZoomMax_TriggerEndPower":RSZVariable(name="_MapZoomMax_TriggerEndPower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_MapZoomMax_TriggerZoomInThreshold":RSZVariable(name="_MapZoomMax_TriggerZoomInThreshold",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_VoxelManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.VoxelManagerSetting",typeIDHash=0x323d464e,CRC=0x5e01e9ee,isObject = True,tagList=[])
		self.fields = {
		"_UpdateDataNum":RSZVariable(name="_UpdateDataNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_UpdateChunkNum":RSZVariable(name="_UpdateChunkNum",dataType="ushort",isList=False,alignment=2,value=None,tagSet=[]),
		"_UpdateBlockNum":RSZVariable(name="_UpdateBlockNum",dataType="ushort",isList=False,alignment=2,value=None,tagSet=[]),
		"_UpdateRegion":RSZVariable(name="_UpdateRegion",dataType="aabb",isList=False,alignment=16,value=None,tagSet=[]),
		"_WriteCommandNum":RSZVariable(name="_WriteCommandNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_VoxelDataNum":RSZVariable(name="_VoxelDataNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_WarpLocationSetPack(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.WarpLocationSetPack",typeIDHash=0x99a96b81,CRC=0x253c5f02,isObject = True,tagList=[])
		self.fields = {
		"_Sets":RSZVariable(name="_Sets",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_WarpRuleDatabase(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.WarpRuleDatabase",typeIDHash=0x90c98583,CRC=0x61602137,isObject = True,tagList=[])
		self.fields = {
		"_Elements":RSZVariable(name="_Elements",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class app_user_data_WaterFluidEffectSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.WaterFluidEffectSetting",typeIDHash=0x1644e223,CRC=0xd2d74522,isObject = True,tagList=[])
		self.fields = {
		"_SimulationScale":RSZVariable(name="_SimulationScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_SimulationResolution":RSZVariable(name="_SimulationResolution",dataType="vec2",isList=False,alignment=16,value=None,tagSet=[]),
		"_EffectResourceHolder":RSZVariable(name="_EffectResourceHolder",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class app_user_data_WindGlobalAnimationData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.WindGlobalAnimationData",typeIDHash=0x66446d49,CRC=0xe6da6249,isObject = True,tagList=[])
		self.fields = {
		"_DataList":RSZVariable(name="_DataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_BlendTime":RSZVariable(name="_BlendTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_WindManagerSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.WindManagerSetting",typeIDHash=0xb610b185,CRC=0x3c563a3d,isObject = True,tagList=[])
		self.fields = {
		"CommandNum":RSZVariable(name="CommandNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"WindSpeedParamPreset":RSZVariable(name="WindSpeedParamPreset",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"VortexelTurbulenceParam":RSZVariable(name="VortexelTurbulenceParam",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ChainWindResource":RSZVariable(name="ChainWindResource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"ChainWindResource2":RSZVariable(name="ChainWindResource2",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"WindAnimationChain":RSZVariable(name="WindAnimationChain",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"WindGainChain":RSZVariable(name="WindGainChain",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"WindLimitChain":RSZVariable(name="WindLimitChain",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"WindGainCloth":RSZVariable(name="WindGainCloth",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"WindLimitCloth":RSZVariable(name="WindLimitCloth",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_WindScaleTransitionTime":RSZVariable(name="_WindScaleTransitionTime",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_PointedSpaceHashList":RSZVariable(name="_PointedSpaceHashList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_WindSpeedTotalReset":RSZVariable(name="_WindSpeedTotalReset",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_user_data_st102_a16_90MaterialControlData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.user_data.st102_a16_90MaterialControlData",typeIDHash=0x28dcbc88,CRC=0x3a796d46,isObject = True,tagList=[])
		self.fields = {
		"_SearchDist":RSZVariable(name="_SearchDist",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_InitVolumeBlend":RSZVariable(name="_InitVolumeBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_InitSmoothstep_Max":RSZVariable(name="_InitSmoothstep_Max",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_VolumeBlendSpeed":RSZVariable(name="_VolumeBlendSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_Smoothstep_MaxSpeed":RSZVariable(name="_Smoothstep_MaxSpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class app_zone_user_data_ZoneCutSceneInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "app.zone_user_data.ZoneCutSceneInfo",typeIDHash=0xaa764bea,CRC=0xa40579d2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"_ZoneType":RSZVariable(name="_ZoneType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_SeamlessInType":RSZVariable(name="_SeamlessInType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class soundlib_SoundBankListData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundBankListData",typeIDHash=0x41d71261,CRC=0xd30c3fce,isObject = True,tagList=[])
		self.fields = {
		"_BankList":RSZVariable(name="_BankList",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class soundlib_SoundContainer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundContainer",typeIDHash=0x1f6d61a9,CRC=0x3e6d5380,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_TriggerOnlyDrawSelf":RSZVariable(name="_TriggerOnlyDrawSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_UserDataList":RSZVariable(name="_UserDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class soundlib_SoundContainerListData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundContainerListData",typeIDHash=0xc4af76a2,CRC=0x9b4a1c9f,isObject = True,tagList=[])
		self.fields = {
		"_UserDataList":RSZVariable(name="_UserDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class soundlib_SoundManagerSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundManagerSettings",typeIDHash=0x450c43dd,CRC=0x82fc231b,isObject = True,tagList=[])
		self.fields = {
		"_SetMuteEventId":RSZVariable(name="_SetMuteEventId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_ResetMuteEventId":RSZVariable(name="_ResetMuteEventId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_SystemBank":RSZVariable(name="_SystemBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_SystemBankId":RSZVariable(name="_SystemBankId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_PauseAllEvent":RSZVariable(name="_PauseAllEvent",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_ResumeAllEvent":RSZVariable(name="_ResumeAllEvent",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_PlayPositionGetterSilentEvent":RSZVariable(name="_PlayPositionGetterSilentEvent",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_VolGameParIdList":RSZVariable(name="_VolGameParIdList",dataType="uint",isList=True,alignment=4,value=None,tagSet=[]),
		"_SrcPositionUpdateFreq":RSZVariable(name="_SrcPositionUpdateFreq",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=[]),
		"_GeneratorClosestUpdateFreq":RSZVariable(name="_GeneratorClosestUpdateFreq",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_DictCapacity_GameObjectInfo_RequestInfo":RSZVariable(name="_DictCapacity_GameObjectInfo_RequestInfo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_DictCapacity_ResidualResources":RSZVariable(name="_DictCapacity_ResidualResources",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ListCapacity_RequestInfo":RSZVariable(name="_ListCapacity_RequestInfo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ListCapacity_EndOf_StoppedEvent":RSZVariable(name="_ListCapacity_EndOf_StoppedEvent",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ListCapacity_UnloadContainerResources":RSZVariable(name="_ListCapacity_UnloadContainerResources",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ListCapacity_WaitingRequestInfo":RSZVariable(name="_ListCapacity_WaitingRequestInfo",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_ListCapacity_UpdatedReqIdPlayingId":RSZVariable(name="_ListCapacity_UpdatedReqIdPlayingId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_SubManagerInstanceSettings":RSZVariable(name="_SubManagerInstanceSettings",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class soundlib_SoundOBB(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundOBB",typeIDHash=0x3e03553e,CRC=0x2bdce590,isObject = True,tagList=[])
		self.fields = {
		"_OBB":RSZVariable(name="_OBB",dataType="obb",isList=False,alignment=16,value=None,tagSet=[]),
		}

class soundlib_SoundStateInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundStateInfo",typeIDHash=0x29d1bbc6,CRC=0xc8143409,isObject = True,tagList=[])
		self.fields = {
		"_StateGroupId":RSZVariable(name="_StateGroupId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_StateId":RSZVariable(name="_StateId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class soundlib_SoundZoneGenerator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "soundlib.SoundZoneGenerator",typeIDHash=0xf23df2f3,CRC=0x87b934c1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_StaticCollider":RSZVariable(name="_StaticCollider",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_AnimationCurve(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.AnimationCurve",typeIDHash=0xeab06d4b,CRC=0xd8a2551d,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="vec4",isList=True,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_Camera(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.Camera",typeIDHash=0x4a26743,CRC=0x64562846,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_Folder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.Folder",typeIDHash=0xaea2d9cc,CRC=0x76400e51,isObject = True,tagList=[])
		self.fields = {
		"folderName":RSZVariable(name="folderName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"scnPath":RSZVariable(name="scnPath",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v06":RSZVariable(name="v06",dataType="unkndata24",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_GameObject(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.GameObject",typeIDHash=0xc902a417,CRC=0xf24c1ee2,isObject = True,tagList=[])
		self.fields = {
		"gameObjectName":RSZVariable(name="gameObjectName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"renderProperty":RSZVariable(name="renderProperty",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_Prefab(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.Prefab",typeIDHash=0xf53c28f9,CRC=0xa0e05e19,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_SerialCodeEventHandler(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.SerialCodeEventHandler",typeIDHash=0x9d5a5cc8,CRC=0xc69ae4f5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_Transform(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.Transform",typeIDHash=0xdfac3046,CRC=0x4fededa7,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_behaviortree_BehaviorTree_CoreHandle(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.behaviortree.BehaviorTree.CoreHandle",typeIDHash=0xd2a0ad29,CRC=0x9ba73e98,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="unkndata24",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_behaviortree_ManualBehaviorTree(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.behaviortree.ManualBehaviorTree",typeIDHash=0xf24e67b9,CRC=0xd0228a70,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_character_CollisionShapePreset(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.character.CollisionShapePreset",typeIDHash=0x6c00c472,CRC=0x37889ac2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_character_CollisionShapePresetInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.character.CollisionShapePresetInfo",typeIDHash=0xaddf3bf7,CRC=0x64134253,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_dynamics_GpuCloth(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.dynamics.GpuCloth",typeIDHash=0x31d3746a,CRC=0xf228e296,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int2",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v69":RSZVariable(name="v69",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v74":RSZVariable(name="v74",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v75":RSZVariable(name="v75",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v82":RSZVariable(name="v82",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v83":RSZVariable(name="v83",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v84":RSZVariable(name="v84",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v85":RSZVariable(name="v85",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v86":RSZVariable(name="v86",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_dynamics_HeightFieldEditor(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.dynamics.HeightFieldEditor",typeIDHash=0xbf679a32,CRC=0x91ff863d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v6":RSZVariable(name="v6",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_dynamics_Ragdoll(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.dynamics.Ragdoll",typeIDHash=0x9082c452,CRC=0xae97e333,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v23":RSZVariable(name="v23",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v35":RSZVariable(name="v35",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_dynamics_RigidBodyMeshSet(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.dynamics.RigidBodyMeshSet",typeIDHash=0xd7781be2,CRC=0x58223c64,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_dynamics_cloth_CurveWind(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.dynamics.cloth.CurveWind",typeIDHash=0x2d0fabba,CRC=0x972acc3b,isObject = True,tagList=[])
		self.fields = {
		"v0_Period":RSZVariable(name="v0_Period",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v1_ScaleCurveX":RSZVariable(name="v1_ScaleCurveX",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_CurveX":RSZVariable(name="v2_CurveX",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v3_ScaleCurveY":RSZVariable(name="v3_ScaleCurveY",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_CurveY":RSZVariable(name="v4_CurveY",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v5_ScaleCurveZ":RSZVariable(name="v5_ScaleCurveZ",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v6_CurveZ":RSZVariable(name="v6_CurveZ",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_ExternParameter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.ExternParameter",typeIDHash=0xfa2a8121,CRC=0xad522689,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_effect_MeshMaterialEmitter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.MeshMaterialEmitter",typeIDHash=0xc683a956,CRC=0xf512ef39,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_effect_fluid_EffectFluid2DTarget(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.fluid.EffectFluid2DTarget",typeIDHash=0x4381fea7,CRC=0x755b5b48,isObject = True,tagList=[])
		self.fields = {
		}

class via_effect_script_EPVDataElement_GroupInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EPVDataElement.GroupInfo",typeIDHash=0x4df6c8aa,CRC=0xb27093d4,isObject = True,tagList=[])
		self.fields = {
		"GroupTypeLv0":RSZVariable(name="GroupTypeLv0",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"GroupTypeLv1":RSZVariable(name="GroupTypeLv1",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"UserVariableNameLv0":RSZVariable(name="UserVariableNameLv0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"UserVariableNameLv1":RSZVariable(name="UserVariableNameLv1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_effect_script_EPVStandard(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EPVStandard",typeIDHash=0x7591ca5b,CRC=0xbb538de1,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"FollowGameObject":RSZVariable(name="FollowGameObject",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_script_EPVStandardData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EPVStandardData",typeIDHash=0xa5e90725,CRC=0xa052068c,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Elements":RSZVariable(name="Elements",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"Version":RSZVariable(name="Version",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"UseVirtualSkeleton":RSZVariable(name="UseVirtualSkeleton",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_EPVStandardData_Element(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EPVStandardData.Element",typeIDHash=0x49c5a434,CRC=0xcdeb29a2,isObject = True,tagList=[])
		self.fields = {
		"efxPaths":RSZVariable(name="efxPaths",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"TriggerId":RSZVariable(name="TriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"StopTriggerId":RSZVariable(name="StopTriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"GUID":RSZVariable(name="GUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"EffectCache":RSZVariable(name="EffectCache",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IgnoreEffectCache":RSZVariable(name="IgnoreEffectCache",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"AntiFlickerOffset":RSZVariable(name="AntiFlickerOffset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroupInfoList":RSZVariable(name="GroupInfoList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"RenderOutputID":RSZVariable(name="RenderOutputID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"AssetGroupNameListLv0":RSZVariable(name="AssetGroupNameListLv0",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"AssetGroupNameListLv1":RSZVariable(name="AssetGroupNameListLv1",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"ID":RSZVariable(name="ID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationType":RSZVariable(name="RelationType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"InitlizationParentScale":RSZVariable(name="InitlizationParentScale",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ParentDegree":RSZVariable(name="ParentDegree",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationChildId":RSZVariable(name="RelationChildId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"JointName":RSZVariable(name="JointName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"UseVirtualSkeletonLocal":RSZVariable(name="UseVirtualSkeletonLocal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"UnparentFrame":RSZVariable(name="UnparentFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Offset":RSZVariable(name="Offset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"RotationOrder":RSZVariable(name="RotationOrder",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BaseRotation":RSZVariable(name="BaseRotation",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationRotationAxis":RSZVariable(name="RelationRotationAxis",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"Rotation":RSZVariable(name="Rotation",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Scale":RSZVariable(name="Scale",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"LifeFrame":RSZVariable(name="LifeFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EndType":RSZVariable(name="EndType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ActionOnProviderDestroy":RSZVariable(name="ActionOnProviderDestroy",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ActionOnParentDisappear":RSZVariable(name="ActionOnParentDisappear",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsCameraDirection":RSZVariable(name="IsCameraDirection",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsVFXRangeTrack_NoEffectWaitIntervalFrame":RSZVariable(name="IsVFXRangeTrack_NoEffectWaitIntervalFrame",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsLanding":RSZVariable(name="IsLanding",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsUseTerrainNormal":RSZVariable(name="IsUseTerrainNormal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"SearchTerrainDistance":RSZVariable(name="SearchTerrainDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsIgnoreLanding":RSZVariable(name="IsIgnoreLanding",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IgnoreLandingPosition":RSZVariable(name="IgnoreLandingPosition",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LandingCoordinateSystem":RSZVariable(name="LandingCoordinateSystem",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"LandingAxis":RSZVariable(name="LandingAxis",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"LandingRotationOffset":RSZVariable(name="LandingRotationOffset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"CamNodeBillbardSec":RSZVariable(name="CamNodeBillbardSec",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"SeparateParentScale":RSZVariable(name="SeparateParentScale",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DelayFrame":RSZVariable(name="DelayFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LoopFrame":RSZVariable(name="LoopFrame",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"LoopDispersionFrame":RSZVariable(name="LoopDispersionFrame",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"PlaySpeed":RSZVariable(name="PlaySpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationMotionSpeed":RSZVariable(name="RelationMotionSpeed",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDefaultMirror":RSZVariable(name="IsDefaultMirror",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsRelationMirror":RSZVariable(name="IsRelationMirror",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"RelationMirrorReverse":RSZVariable(name="RelationMirrorReverse",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationMirrorMotionBlendType":RSZVariable(name="RelationMirrorMotionBlendType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ColorEnable":RSZVariable(name="ColorEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Color":RSZVariable(name="Color",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskEnable":RSZVariable(name="MaskEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"MaskBit":RSZVariable(name="MaskBit",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"ActionOnCulling":RSZVariable(name="ActionOnCulling",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ExternParameters":RSZVariable(name="ExternParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GroupNameParameters":RSZVariable(name="GroupNameParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CustomLOD":RSZVariable(name="CustomLOD",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LODLevels":RSZVariable(name="LODLevels",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"UserBit":RSZVariable(name="UserBit",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_effect_script_EffectCacheManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EffectCacheManager",typeIDHash=0x52ca0e30,CRC=0x42a4e81f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"PoolGameObjectParentObj":RSZVariable(name="PoolGameObjectParentObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_CacheEnable":RSZVariable(name="_CacheEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_MaxCacheNum":RSZVariable(name="_MaxCacheNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_CachePoolNum":RSZVariable(name="_CachePoolNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_DefaultUseCache":RSZVariable(name="_DefaultUseCache",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_EffectCustomExternParameter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EffectCustomExternParameter",typeIDHash=0x2f0768d8,CRC=0xd681537e,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ResourceIndex":RSZVariable(name="ResourceIndex",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"AllResource":RSZVariable(name="AllResource",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_EffectEmitZone(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EffectEmitZone",typeIDHash=0x36617199,CRC=0x80eda706,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"AutoColliderStatic":RSZVariable(name="AutoColliderStatic",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_EffectEmitZoneGroup(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EffectEmitZoneGroup",typeIDHash=0x2deea86a,CRC=0xfb1decbf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"IsEmitOnTrigger":RSZVariable(name="IsEmitOnTrigger",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEmit":RSZVariable(name="IsEmit",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsEmitOffTrigger":RSZVariable(name="IsEmitOffTrigger",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsActiveOnStart":RSZVariable(name="IsActiveOnStart",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TargetObjects":RSZVariable(name="TargetObjects",dataType="guid",isList=True,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"_OutsideTargetGameObject":RSZVariable(name="_OutsideTargetGameObject",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_script_EffectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EffectManager",typeIDHash=0xcb0c7e35,CRC=0xa8edb36,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"IsDisableAllEffect":RSZVariable(name="IsDisableAllEffect",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDisableRecord":RSZVariable(name="IsDisableRecord",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DataInstanceMapIntialCapacity":RSZVariable(name="DataInstanceMapIntialCapacity",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ContainerManagersIntialCapacity":RSZVariable(name="ContainerManagersIntialCapacity",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RootNoParentObj":RSZVariable(name="RootNoParentObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"EPVDataRootObj":RSZVariable(name="EPVDataRootObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"Material2GroupSetType":RSZVariable(name="Material2GroupSetType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"EffectNameType":RSZVariable(name="EffectNameType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"PlayerGameObjectTag":RSZVariable(name="PlayerGameObjectTag",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"MaxEmitNum":RSZVariable(name="MaxEmitNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ContainerParallelNum":RSZVariable(name="ContainerParallelNum",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsEnalbeOnAwakeCheckUseSelf":RSZVariable(name="IsEnalbeOnAwakeCheckUseSelf",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"AllowVoluetricFogNum":RSZVariable(name="AllowVoluetricFogNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"RequestParamType":RSZVariable(name="RequestParamType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"FlickerOffsetRate":RSZVariable(name="FlickerOffsetRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"FlickerOffsetRotaionNum":RSZVariable(name="FlickerOffsetRotaionNum",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"_ObjectEffectManager":RSZVariable(name="_ObjectEffectManager",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EnviromentEffectManager":RSZVariable(name="_EnviromentEffectManager",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"IsDisableDevelopProcess":RSZVariable(name="IsDisableDevelopProcess",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDevelopDrawBloodStamp":RSZVariable(name="IsDevelopDrawBloodStamp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDevelopDrawBloodDecal":RSZVariable(name="IsDevelopDrawBloodDecal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDevelopDrawScarStamp":RSZVariable(name="IsDevelopDrawScarStamp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDevelopDrawScarDecal":RSZVariable(name="IsDevelopDrawScarDecal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDevelopDrawWaterStamp":RSZVariable(name="IsDevelopDrawWaterStamp",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDevelopDrawWaterDecal":RSZVariable(name="IsDevelopDrawWaterDecal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DevEffectPlaySpeed":RSZVariable(name="DevEffectPlaySpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ForceAntiFlickerOffset":RSZVariable(name="ForceAntiFlickerOffset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_EffectManager_LODData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EffectManager.LODData",typeIDHash=0x2e97bbd6,CRC=0xa1263ab4,isObject = True,tagList=[])
		self.fields = {
		"LODLevels":RSZVariable(name="LODLevels",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_script_EnvironmentEffectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EnvironmentEffectManager",typeIDHash=0x6f6817f6,CRC=0x83ffa516,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"IsEnableAutoCulling":RSZVariable(name="IsEnableAutoCulling",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsAutoPlay":RSZVariable(name="IsAutoPlay",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsCullingNotAffectUpdate":RSZVariable(name="IsCullingNotAffectUpdate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ExternalPropertys":RSZVariable(name="ExternalPropertys",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_script_EnvironmentEffectManager_ExternalProperty(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EnvironmentEffectManager.ExternalProperty",typeIDHash=0xb30d6aa5,CRC=0x78b2bf2f,isObject = True,tagList=[])
		self.fields = {
		"IsPlayAll":RSZVariable(name="IsPlayAll",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ElementID":RSZVariable(name="ElementID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"State":RSZVariable(name="State",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ExternParameters":RSZVariable(name="ExternParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_script_EventEffectDataElement(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EventEffectDataElement",typeIDHash=0x74bb82e3,CRC=0xd67313d1,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"TriggerId":RSZVariable(name="TriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"StopTriggerId":RSZVariable(name="StopTriggerId",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"GUID":RSZVariable(name="GUID",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"EffectCache":RSZVariable(name="EffectCache",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IgnoreEffectCache":RSZVariable(name="IgnoreEffectCache",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"AntiFlickerOffset":RSZVariable(name="AntiFlickerOffset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroupInfoList":RSZVariable(name="GroupInfoList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"RenderOutputID":RSZVariable(name="RenderOutputID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"AssetGroupNameListLv0":RSZVariable(name="AssetGroupNameListLv0",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"AssetGroupNameListLv1":RSZVariable(name="AssetGroupNameListLv1",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"ID":RSZVariable(name="ID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationType":RSZVariable(name="RelationType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"InitlizationParentScale":RSZVariable(name="InitlizationParentScale",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ParentDegree":RSZVariable(name="ParentDegree",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationChildId":RSZVariable(name="RelationChildId",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"JointName":RSZVariable(name="JointName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"UseVirtualSkeletonLocal":RSZVariable(name="UseVirtualSkeletonLocal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"UnparentFrame":RSZVariable(name="UnparentFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"Offset":RSZVariable(name="Offset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"RotationOrder":RSZVariable(name="RotationOrder",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BaseRotation":RSZVariable(name="BaseRotation",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationRotationAxis":RSZVariable(name="RelationRotationAxis",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"Rotation":RSZVariable(name="Rotation",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Scale":RSZVariable(name="Scale",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"LifeFrame":RSZVariable(name="LifeFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EndType":RSZVariable(name="EndType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ActionOnProviderDestroy":RSZVariable(name="ActionOnProviderDestroy",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ActionOnParentDisappear":RSZVariable(name="ActionOnParentDisappear",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsCameraDirection":RSZVariable(name="IsCameraDirection",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsVFXRangeTrack_NoEffectWaitIntervalFrame":RSZVariable(name="IsVFXRangeTrack_NoEffectWaitIntervalFrame",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsLanding":RSZVariable(name="IsLanding",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsUseTerrainNormal":RSZVariable(name="IsUseTerrainNormal",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"SearchTerrainDistance":RSZVariable(name="SearchTerrainDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsIgnoreLanding":RSZVariable(name="IsIgnoreLanding",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IgnoreLandingPosition":RSZVariable(name="IgnoreLandingPosition",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LandingCoordinateSystem":RSZVariable(name="LandingCoordinateSystem",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"LandingAxis":RSZVariable(name="LandingAxis",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"LandingRotationOffset":RSZVariable(name="LandingRotationOffset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"CamNodeBillbardSec":RSZVariable(name="CamNodeBillbardSec",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"SeparateParentScale":RSZVariable(name="SeparateParentScale",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DelayFrame":RSZVariable(name="DelayFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LoopFrame":RSZVariable(name="LoopFrame",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"LoopDispersionFrame":RSZVariable(name="LoopDispersionFrame",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"PlaySpeed":RSZVariable(name="PlaySpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationMotionSpeed":RSZVariable(name="RelationMotionSpeed",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsDefaultMirror":RSZVariable(name="IsDefaultMirror",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"IsRelationMirror":RSZVariable(name="IsRelationMirror",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"RelationMirrorReverse":RSZVariable(name="RelationMirrorReverse",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"RelationMirrorMotionBlendType":RSZVariable(name="RelationMirrorMotionBlendType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ColorEnable":RSZVariable(name="ColorEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"Color":RSZVariable(name="Color",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"MaskEnable":RSZVariable(name="MaskEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"MaskBit":RSZVariable(name="MaskBit",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"ActionOnCulling":RSZVariable(name="ActionOnCulling",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ExternParameters":RSZVariable(name="ExternParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"GroupNameParameters":RSZVariable(name="GroupNameParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"CustomLOD":RSZVariable(name="CustomLOD",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LODLevels":RSZVariable(name="LODLevels",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"UserBit":RSZVariable(name="UserBit",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"EventPlaySpeed":RSZVariable(name="EventPlaySpeed",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EventColor":RSZVariable(name="EventColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"TargetGameObject":RSZVariable(name="TargetGameObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"EventJointName":RSZVariable(name="EventJointName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"UseDynamicMovement":RSZVariable(name="UseDynamicMovement",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"EventOffset":RSZVariable(name="EventOffset",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"EventRotation":RSZVariable(name="EventRotation",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"EventScale":RSZVariable(name="EventScale",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"EventExternParameters":RSZVariable(name="EventExternParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"EventGroupNameParameters":RSZVariable(name="EventGroupNameParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_effect_script_EventEffectManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.EventEffectManager",typeIDHash=0x999e88d3,CRC=0x66f008cb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Elements":RSZVariable(name="Elements",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TargetGameObject":RSZVariable(name="TargetGameObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"useVirtualSkeleton":RSZVariable(name="useVirtualSkeleton",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_GroupNameParameter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.GroupNameParameter",typeIDHash=0x23d9e5fa,CRC=0x68bc6d48,isObject = True,tagList=[])
		self.fields = {
		"Enable":RSZVariable(name="Enable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"GroupNameLv0":RSZVariable(name="GroupNameLv0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"GroupNameLv1":RSZVariable(name="GroupNameLv1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_effect_script_ObjectEffectManager2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.ObjectEffectManager2",typeIDHash=0x2609fe06,CRC=0xc93c5e94,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DisableRequestEffect":RSZVariable(name="_DisableRequestEffect",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VFXRangeTrackReversePlayNoRequest":RSZVariable(name="_VFXRangeTrackReversePlayNoRequest",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VFXRangeTrack_NoEffectWaitIntervalFrame":RSZVariable(name="_VFXRangeTrack_NoEffectWaitIntervalFrame",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DataContainer":RSZVariable(name="DataContainer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"ExternalDataContainers":RSZVariable(name="ExternalDataContainers",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TargetGameObject":RSZVariable(name="TargetGameObject",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"ExternalPropertys":RSZVariable(name="ExternalPropertys",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"disableVFXTriggerTrack":RSZVariable(name="disableVFXTriggerTrack",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"disableVFXRangeTrack":RSZVariable(name="disableVFXRangeTrack",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"disableMotionJackCheck":RSZVariable(name="disableMotionJackCheck",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VFXTriggerTrackUseHighestWeight":RSZVariable(name="_VFXTriggerTrackUseHighestWeight",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VFXRangeTrackUseHighestWeight":RSZVariable(name="_VFXRangeTrackUseHighestWeight",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_StaticDataContainer":RSZVariable(name="_StaticDataContainer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_DisableByEmptyDataContainer":RSZVariable(name="_DisableByEmptyDataContainer",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_effect_script_ObjectEffectManager2_ExternalProperty(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.effect.script.ObjectEffectManager2.ExternalProperty",typeIDHash=0x11a6edcd,CRC=0xa85b31ce,isObject = True,tagList=[])
		self.fields = {
		"ContainerID":RSZVariable(name="ContainerID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"ElementID":RSZVariable(name="ElementID",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"State":RSZVariable(name="State",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"ExternParameters":RSZVariable(name="ExternParameters",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_gui_AdditionalMessage(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.gui.AdditionalMessage",typeIDHash=0x816822a1,CRC=0x6165d9ba,isObject = True,tagList=[])
		self.fields = {
		"v0_MessageList":RSZVariable(name="v0_MessageList",dataType="string",isList=True,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_gui_GUI(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.gui.GUI",typeIDHash=0x25f55eb4,CRC=0xbd0da64f,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_landscape_Foliage(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.landscape.Foliage",typeIDHash=0x1bf18610,CRC=0x3d22dbbf,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_landscape_Ground(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.landscape.Ground",typeIDHash=0x8eb0a08e,CRC=0x810314c6,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v48":RSZVariable(name="v48",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v49":RSZVariable(name="v49",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v69":RSZVariable(name="v69",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v82":RSZVariable(name="v82",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v83":RSZVariable(name="v83",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v84":RSZVariable(name="v84",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v85":RSZVariable(name="v85",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v86":RSZVariable(name="v86",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v87":RSZVariable(name="v87",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v88":RSZVariable(name="v88",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v89":RSZVariable(name="v89",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_landscape_GroundDecal(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.landscape.GroundDecal",typeIDHash=0x13df037,CRC=0xa86f67f9,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_Priority":RSZVariable(name="v1_Priority",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_StreamingPriority":RSZVariable(name="v2_StreamingPriority",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"v3_BaseMap":RSZVariable(name="v3_BaseMap",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v4_NormalRoughnessMap":RSZVariable(name="v4_NormalRoughnessMap",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v5_UvScale":RSZVariable(name="v5_UvScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v6_NoUvScaleAlpha":RSZVariable(name="v6_NoUvScaleAlpha",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v7_ColorParam":RSZVariable(name="v7_ColorParam",dataType="vec4",isList=False,alignment=16,value=None,tagSet=[]),
		"v8_NormalAlpha":RSZVariable(name="v8_NormalAlpha",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v9_RoughnessParam":RSZVariable(name="v9_RoughnessParam",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v10_RoughnessAlpha":RSZVariable(name="v10_RoughnessAlpha",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v11_Mask":RSZVariable(name="v11_Mask",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v12_DepthMask":RSZVariable(name="v12_DepthMask",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v13_TopBlend":RSZVariable(name="v13_TopBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v14_TopBlendWidth":RSZVariable(name="v14_TopBlendWidth",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v15_HeightBlend":RSZVariable(name="v15_HeightBlend",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v16_HeightBlendWidth":RSZVariable(name="v16_HeightBlendWidth",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v17_AlphaMapContrast":RSZVariable(name="v17_AlphaMapContrast",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v18_EnableDisplacement":RSZVariable(name="v18_EnableDisplacement",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v19_DisplacementScale":RSZVariable(name="v19_DisplacementScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_landscape_GroundOverlaySplat(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.landscape.GroundOverlaySplat",typeIDHash=0xe71653e6,CRC=0xd4991b2e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_landscape_GroundSurfaceTrail(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.landscape.GroundSurfaceTrail",typeIDHash=0xb6ebebfc,CRC=0x24d2fca0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_ActorLayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.ActorLayer",typeIDHash=0xcc3c1ca4,CRC=0x68e8abb,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_ActorMotion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.ActorMotion",typeIDHash=0x6e765829,CRC=0xe3a6fb73,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_motion_Chain(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.Chain",typeIDHash=0x9d66dbb1,CRC=0xa9acf305,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_Chain2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.Chain2",typeIDHash=0x45301b93,CRC=0x1b00fa6c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_ChainWind(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.ChainWind",typeIDHash=0xfdcea1a0,CRC=0x3ba977dd,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_motion_ChildSecondary(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.ChildSecondary",typeIDHash=0x8d8f9b0b,CRC=0x5259f7a0,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_ConstraintParent(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.ConstraintParent",typeIDHash=0xf53d7bfb,CRC=0xa283d368,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_UpdateMode":RSZVariable(name="v1_UpdateMode",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_UpdateTiming":RSZVariable(name="v2_UpdateTiming",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v03":RSZVariable(name="v03",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v06":RSZVariable(name="v06",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v07":RSZVariable(name="v07",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_CustomSkeleton(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.CustomSkeleton",typeIDHash=0x46a20100,CRC=0x566abf1a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_DummySkeleton(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.DummySkeleton",typeIDHash=0x645fdb44,CRC=0x7af11387,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_motion_DynamicMotionBank(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.DynamicMotionBank",typeIDHash=0xdb4d45d9,CRC=0xb1c5280,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7_MotionBank":RSZVariable(name="v7_MotionBank",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v8_MotionList":RSZVariable(name="v8_MotionList",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_motion_IkLizard(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.IkLizard",typeIDHash=0x94c641cc,CRC=0xa1779a75,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_JointConstraints(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.JointConstraints",typeIDHash=0xeff0c408,CRC=0x6264b81e,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_UpdateMode":RSZVariable(name="v1_UpdateMode",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_UpdateTiming":RSZVariable(name="v2_UpdateTiming",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_JointConstraintsLayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.JointConstraintsLayer",typeIDHash=0x5882a4b,CRC=0xe4a745a2,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_motion_JointExprGraph(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.JointExprGraph",typeIDHash=0x93560e7a,CRC=0xdeb2bb18,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_UpdateMode":RSZVariable(name="v1_UpdateMode",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_UpdateTiming":RSZVariable(name="v2_UpdateTiming",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_JointExprGraphLayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.JointExprGraphLayer",typeIDHash=0x54bffcf6,CRC=0x2d18c265,isObject = True,tagList=[])
		self.fields = {
		"v0_JointExprGraph":RSZVariable(name="v0_JointExprGraph",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v1_EnabledOverrideUpdateTiming":RSZVariable(name="v1_EnabledOverrideUpdateTiming",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v2_OverrideUpdateTiming":RSZVariable(name="v2_OverrideUpdateTiming",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v3_Pause":RSZVariable(name="v3_Pause",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v4_BlendRate":RSZVariable(name="v4_BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_motion_JointSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.JointSetting",typeIDHash=0x96b86263,CRC=0x5cd3721a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_JointSettingElement(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.JointSettingElement",typeIDHash=0xa3669a54,CRC=0xd39f732e,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_Motion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.Motion",typeIDHash=0xf829f958,CRC=0x5c2dde5c,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v15":RSZVariable(name="v15",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v16":RSZVariable(name="v16",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v17":RSZVariable(name="v17",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="unkndata13",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_MotionCamera(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.MotionCamera",typeIDHash=0x1c84556c,CRC=0xc4c53543,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_TreeCameraLayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.TreeCameraLayer",typeIDHash=0x962a088b,CRC=0xd39cefba,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_motion_TreeLayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.motion.TreeLayer",typeIDHash=0xe56de1d9,CRC=0x8995bfda,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_navigation_AIMap(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.AIMap",typeIDHash=0xf6321b27,CRC=0x4258dc23,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_navigation_AIMapEffector(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.AIMapEffector",typeIDHash=0x16212ad0,CRC=0x1b4118f4,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"v03":RSZVariable(name="v03",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ushort",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_navigation_AIMapSection(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.AIMapSection",typeIDHash=0x1e746b19,CRC=0xe723ce0f,isObject = True,tagList=[])
		self.fields = {
		"v0_Maps":RSZVariable(name="v0_Maps",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_navigation_FilterInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.FilterInfo",typeIDHash=0xa3e66934,CRC=0x8fbb2fa0,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_Name":RSZVariable(name="v1_Name",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_Type":RSZVariable(name="v2_Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v3_Cost":RSZVariable(name="v3_Cost",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_NotifyAround":RSZVariable(name="v4_NotifyAround",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v5_NotifyContainsLink":RSZVariable(name="v5_NotifyContainsLink",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v6_NotifyDistance":RSZVariable(name="v6_NotifyDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v7_TraceDestination":RSZVariable(name="v7_TraceDestination",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_navigation_FilterSet(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.FilterSet",typeIDHash=0xab77eb0f,CRC=0x704b0605,isObject = True,tagList=[])
		self.fields = {
		}

class via_navigation_MapHandle(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.MapHandle",typeIDHash=0xb0192a05,CRC=0x95c93d22,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1_Resource":RSZVariable(name="v1_Resource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_navigation_SectionManagerHandle(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.SectionManagerHandle",typeIDHash=0x46583770,CRC=0xea8b819f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1_Resource":RSZVariable(name="v1_Resource",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_navigation_map_InteractionShapeAABB(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.navigation.map.InteractionShapeAABB",typeIDHash=0x6c1b2afc,CRC=0xe0f36694,isObject = True,tagList=[])
		self.fields = {
		}

class via_network_AchievementsLive(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.AchievementsLive",typeIDHash=0x96b01e8e,CRC=0x9838b0af,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_AchievementsSteam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.AchievementsSteam",typeIDHash=0x24107e25,CRC=0x410b1d3b,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_AutoMaster(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.AutoMaster",typeIDHash=0xe5e77628,CRC=0xb984ee7f,isObject = True,tagList=[])
		self.fields = {
		"v0_Guid":RSZVariable(name="v0_Guid",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ContextLamm(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ContextLamm",typeIDHash=0x69270916,CRC=0x42b4f37b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ContextLive(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ContextLive",typeIDHash=0x3e9f4ddb,CRC=0x7967ca6d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ContextPs5Psn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ContextPs5Psn",typeIDHash=0xf3ab354e,CRC=0xbb6ad041,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ContextRebe(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ContextRebe",typeIDHash=0xe1d6f863,CRC=0x925160ae,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ContextSteam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ContextSteam",typeIDHash=0xffd9eaab,CRC=0xa0be1937,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_HttpClient(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.HttpClient",typeIDHash=0x95776c66,CRC=0xcb65250f,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int2",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_IdConverterLamm(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.IdConverterLamm",typeIDHash=0x78fc5bb5,CRC=0xfff9504b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_IdConverterLive(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.IdConverterLive",typeIDHash=0xfa835d3a,CRC=0xa475c1c1,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_IdConverterPs5Psn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.IdConverterPs5Psn",typeIDHash=0xa75c4f52,CRC=0x3e2dc73,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_IdConverterSteam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.IdConverterSteam",typeIDHash=0xe3766781,CRC=0xc13933a0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_InvitationPlayFab(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.InvitationPlayFab",typeIDHash=0x65481965,CRC=0x455f5d04,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_InvitationPs5Psn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.InvitationPs5Psn",typeIDHash=0x852fad92,CRC=0xc60f61d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_InvitationSteam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.InvitationSteam",typeIDHash=0xe4123d31,CRC=0x16a10ca,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_MultiplayCheckerPsn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.MultiplayCheckerPsn",typeIDHash=0xe806b47b,CRC=0x549610dd,isObject = True,tagList=[])
		self.fields = {
		"v0_Guid":RSZVariable(name="v0_Guid",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ProtocolBroadcast(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ProtocolBroadcast",typeIDHash=0x76b108f7,CRC=0x23208a27,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_ProtocolRPC(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.ProtocolRPC",typeIDHash=0xedf79d0,CRC=0x6e26408,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_RemoteProcedure(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.RemoteProcedure",typeIDHash=0x4f6afc8c,CRC=0xbd00e097,isObject = True,tagList=[])
		self.fields = {
		"v0_Guid":RSZVariable(name="v0_Guid",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_SessionLamm(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.SessionLamm",typeIDHash=0x45263717,CRC=0xcfb57da9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_SessionPlayFab(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.SessionPlayFab",typeIDHash=0xab0f2dc9,CRC=0x32ac4877,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_SessionPs5Psn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.SessionPs5Psn",typeIDHash=0x11a9dc89,CRC=0x9cbc1687,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_SessionSteam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.SessionSteam",typeIDHash=0x9a8d4bb1,CRC=0x6623d308,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v12_SearchByUniqueIdOnFriend":RSZVariable(name="v12_SearchByUniqueIdOnFriend",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_network_SyncPlayerSessionPsn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.SyncPlayerSessionPsn",typeIDHash=0x3e1f518d,CRC=0x1ca00c0d,isObject = True,tagList=[])
		self.fields = {
		"v0_Guid":RSZVariable(name="v0_Guid",dataType="guid",isList=False,alignment=8,value=None,tagSet=[]),
		"v1_ServiceLabel":RSZVariable(name="v1_ServiceLabel",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_network_UtilityLamm(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.UtilityLamm",typeIDHash=0xd92a8e60,CRC=0x4023fd77,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_UtilityLive(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.UtilityLive",typeIDHash=0x82d8bfa2,CRC=0x1baf6cfd,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_UtilityPs5Psn(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.UtilityPs5Psn",typeIDHash=0x627068ee,CRC=0x300baded,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_UtilitySteam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.UtilitySteam",typeIDHash=0xdf336d95,CRC=0xb1763ef4,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_network_VoiceChatExtension(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.VoiceChatExtension",typeIDHash=0x785d1944,CRC=0xa598e8c6,isObject = True,tagList=[])
		self.fields = {
		}

class via_network_WebSocketClient(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.network.WebSocketClient",typeIDHash=0x32867957,CRC=0x2c3ab4f2,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int2",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int2",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int2",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_AabbShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.AabbShape",typeIDHash=0xcbc83bfb,CRC=0x67f9efb8,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_AreaShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.AreaShape",typeIDHash=0x1560e3ae,CRC=0xb4b89d96,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="unkndata48",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_BoxShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.BoxShape",typeIDHash=0x39954291,CRC=0x1c387f97,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_CapsuleShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.CapsuleShape",typeIDHash=0x864a4a8e,CRC=0x13304882,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="unkndata48",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_Collider(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.Collider",typeIDHash=0x15d3b4ec,CRC=0xd3ef349d,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v05":RSZVariable(name="v05",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v06":RSZVariable(name="v06",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v07":RSZVariable(name="v07",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_physics_ColliderSet(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.ColliderSet",typeIDHash=0xe80f5f70,CRC=0x3863d8d4,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_physics_Colliders(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.Colliders",typeIDHash=0x9ab154c4,CRC=0x78e9a853,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_CollisionHeightFieldEditor(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.CollisionHeightFieldEditor",typeIDHash=0x2c4f3955,CRC=0xf863139b,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_FilterInfo(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.FilterInfo",typeIDHash=0xdd4a871,CRC=0xfdca9c46,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_HeightFieldShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.HeightFieldShape",typeIDHash=0xc46ba018,CRC=0x47edfed2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_MeshShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.MeshShape",typeIDHash=0xd5371785,CRC=0x45a90a2f,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=True,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="mat4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_RequestSetCollider(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.RequestSetCollider",typeIDHash=0x669fc998,CRC=0x1be418e8,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_RequestSetCollider_RequestSetGroup(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.RequestSetCollider.RequestSetGroup",typeIDHash=0x7c0c2e30,CRC=0x81d1ec59,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_physics_SphereShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.SphereShape",typeIDHash=0xaffd38f9,CRC=0x8bd625cb,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_StaticCompoundChildren(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.StaticCompoundChildren",typeIDHash=0x81956489,CRC=0x35c1353e,isObject = True,tagList=[])
		self.fields = {
		"v0_Manual":RSZVariable(name="v0_Manual",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_physics_StaticCompoundShape(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.StaticCompoundShape",typeIDHash=0x14f90405,CRC=0xfc5e8201,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="aabb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_physics_StaticCompoundShape_Instance(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.StaticCompoundShape.Instance",typeIDHash=0xb3ebfd02,CRC=0xc1a2bc99,isObject = True,tagList=[])
		self.fields = {
		"v0_Shape":RSZVariable(name="v0_Shape",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v1_MaskBits":RSZVariable(name="v1_MaskBits",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_Type":RSZVariable(name="v2_Type",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_physics_UserData(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.UserData",typeIDHash=0xf767c93f,CRC=0x16593069,isObject = True,tagList=[])
		self.fields = {
		}

class via_physics_ZoneGroup(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.physics.ZoneGroup",typeIDHash=0xe7c98aff,CRC=0x32a6b908,isObject = True,tagList=[])
		self.fields = {
		}

class via_pointgraph_PointGraph(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.pointgraph.PointGraph",typeIDHash=0xdcb4f00e,CRC=0xfd6a5d7a,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_effect_EVRefVFXTableContainer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.effect.EVRefVFXTableContainer",typeIDHash=0x88288223,CRC=0x2c6d49b0,isObject = True,tagList=[])
		self.fields = {
		"DefaultTable":RSZVariable(name="DefaultTable",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"TableDataList":RSZVariable(name="TableDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_effect_EffectEVRefVFXManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.effect.EffectEVRefVFXManager",typeIDHash=0xa6752e15,CRC=0x76422bba,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Data":RSZVariable(name="Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		}

class via_relib_effect_EffectGlobalGroupParameter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.effect.EffectGlobalGroupParameter",typeIDHash=0x789ce0d6,CRC=0x4c0ea92b,isObject = True,tagList=[])
		self.fields = {
		}

class via_relib_effect_EffectMaterialGroupManager(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.effect.EffectMaterialGroupManager",typeIDHash=0xc12644f,CRC=0x7e1553eb,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Data":RSZVariable(name="Data",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"GlobalGroupParameter":RSZVariable(name="GlobalGroupParameter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"_ResolveType":RSZVariable(name="_ResolveType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"_AttributeResolveType":RSZVariable(name="_AttributeResolveType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_effect_userdata_EffectMaterialGroupParameterContainer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.effect.userdata.EffectMaterialGroupParameterContainer",typeIDHash=0x2d4a9b28,CRC=0xec7e22c1,isObject = True,tagList=[])
		self.fields = {
		"DefaultGroupParameter":RSZVariable(name="DefaultGroupParameter",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_UserData']),
		"StageDataList":RSZVariable(name="StageDataList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_light_LightActionControlAOEfficiency(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightActionControlAOEfficiency",typeIDHash=0x8e4d5b79,CRC=0x7619c585,isObject = True,tagList=[])
		self.fields = {
		"IsEnable":RSZVariable(name="IsEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ShadowOffAOEfficiency":RSZVariable(name="ShadowOffAOEfficiency",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ShadowOnAOEfficiency":RSZVariable(name="ShadowOnAOEfficiency",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_LightActionDistanceAttenuation(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightActionDistanceAttenuation",typeIDHash=0xd0c4e2be,CRC=0x8cbf5b3d,isObject = True,tagList=[])
		self.fields = {
		"IsDistanceAttenuation":RSZVariable(name="IsDistanceAttenuation",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"EaseType":RSZVariable(name="EaseType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"NearFadeOutStartDistance":RSZVariable(name="NearFadeOutStartDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"NearFadeOutEndDistance":RSZVariable(name="NearFadeOutEndDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"FadeOutStartDistance":RSZVariable(name="FadeOutStartDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"FadeOutEndDistance":RSZVariable(name="FadeOutEndDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IsImprovement":RSZVariable(name="IsImprovement",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_relib_light_LightActionDistanceShadow(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightActionDistanceShadow",typeIDHash=0xec765be7,CRC=0x546c0b19,isObject = True,tagList=[])
		self.fields = {
		"IsDistanceSwitchShadowEnable":RSZVariable(name="IsDistanceSwitchShadowEnable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"ShadowSwitchtShadowEnableStartDistance":RSZVariable(name="ShadowSwitchtShadowEnableStartDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"ShadowSwitchtBackGroundShadowEnableStartDistance":RSZVariable(name="ShadowSwitchtBackGroundShadowEnableStartDistance",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_LightActionKillComponent(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightActionKillComponent",typeIDHash=0x62c69976,CRC=0x5de3c4a4,isObject = True,tagList=[])
		self.fields = {
		"IsUpdatePerFrame":RSZVariable(name="IsUpdatePerFrame",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_relib_light_LightBlinkUserCurvePlayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightBlinkUserCurvePlayer",typeIDHash=0x6c226040,CRC=0xb76c2efe,isObject = True,tagList=[])
		self.fields = {
		"BlinkUserCurve":RSZVariable(name="BlinkUserCurve",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_PlayType":RSZVariable(name="_PlayType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BlinkStartFrame":RSZVariable(name="BlinkStartFrame",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"FrameScaleRange":RSZVariable(name="FrameScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"IntensityScaleRange":RSZVariable(name="IntensityScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"IntensityRate":RSZVariable(name="IntensityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LightColorCoef":RSZVariable(name="LightColorCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"BlinklightColor":RSZVariable(name="BlinklightColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"VolumetricScatteringIntensityCoef":RSZVariable(name="VolumetricScatteringIntensityCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EmissiveColor":RSZVariable(name="EmissiveColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"IsLoop":RSZVariable(name="IsLoop",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LightDelayPlayer":RSZVariable(name="LightDelayPlayer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MaterialControllParamList":RSZVariable(name="MaterialControllParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_light_LightBlinkUserCurvePlayer_MaterialControllParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightBlinkUserCurvePlayer.MaterialControllParam",typeIDHash=0xfd73a6cd,CRC=0xd2c702de,isObject = True,tagList=[])
		self.fields = {
		"RefObj":RSZVariable(name="RefObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"MaterialName":RSZVariable(name="MaterialName",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"VariableName":RSZVariable(name="VariableName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_ParamType":RSZVariable(name="_ParamType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsInfluenceLightColorCoef":RSZVariable(name="IsInfluenceLightColorCoef",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"initValue":RSZVariable(name="initValue",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IntensityScaleRange":RSZVariable(name="IntensityScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"IntensityRate":RSZVariable(name="IntensityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"initColorValue":RSZVariable(name="initColorValue",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"materialNameList":RSZVariable(name="materialNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"variableNameList":RSZVariable(name="variableNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_LightBlinkUserCurveVariationPlayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightBlinkUserCurveVariationPlayer",typeIDHash=0x1d90e094,CRC=0xcacb86fb,isObject = True,tagList=[])
		self.fields = {
		"BlinkUserCurve":RSZVariable(name="BlinkUserCurve",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_PlayType":RSZVariable(name="_PlayType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IntensityRate":RSZVariable(name="IntensityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"LightColorCoef":RSZVariable(name="LightColorCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"VolumetricScatteringIntensityCoef":RSZVariable(name="VolumetricScatteringIntensityCoef",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"EmissiveColor":RSZVariable(name="EmissiveColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"IsLoop":RSZVariable(name="IsLoop",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_VariationIndex":RSZVariable(name="_VariationIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"VariationParamList":RSZVariable(name="VariationParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"LightDelayPlayer":RSZVariable(name="LightDelayPlayer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_light_LightBlinkUserCurveVariationPlayer_VariationParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightBlinkUserCurveVariationPlayer.VariationParam",typeIDHash=0xe216e06,CRC=0x410a310e,isObject = True,tagList=[])
		self.fields = {
		"BlinkStartFrame":RSZVariable(name="BlinkStartFrame",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"FrameScaleRange":RSZVariable(name="FrameScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"IntensityScaleRange":RSZVariable(name="IntensityScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"MaterialControllParamList":RSZVariable(name="MaterialControllParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		"LightColorControl":RSZVariable(name="LightColorControl",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_light_LightBlinkUserCurveVariationPlayer_VariationParam_LightColorControlParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightBlinkUserCurveVariationPlayer.VariationParam.LightColorControlParam",typeIDHash=0x36e83d18,CRC=0x949ba19d,isObject = True,tagList=[])
		self.fields = {
		"IsLightInitColor":RSZVariable(name="IsLightInitColor",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"LightInitColor":RSZVariable(name="LightInitColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_LightBlinkUserCurveVariationPlayer_VariationParam_MaterialControllParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightBlinkUserCurveVariationPlayer.VariationParam.MaterialControllParam",typeIDHash=0xb4df7e01,CRC=0x3cabcf4,isObject = True,tagList=[])
		self.fields = {
		"RefObj":RSZVariable(name="RefObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"Obj":RSZVariable(name="Obj",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MaterialName":RSZVariable(name="MaterialName",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"VariableName":RSZVariable(name="VariableName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_ParamType":RSZVariable(name="_ParamType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"IsInfluenceLightColorCoef":RSZVariable(name="IsInfluenceLightColorCoef",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"initValue":RSZVariable(name="initValue",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"IntensityScaleRange":RSZVariable(name="IntensityScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		"IntensityRate":RSZVariable(name="IntensityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"initColorValue":RSZVariable(name="initColorValue",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"materialNameList":RSZVariable(name="materialNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"variableNameList":RSZVariable(name="variableNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_LightDelayPlayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightDelayPlayer",typeIDHash=0x2f846015,CRC=0x1740fa9b,isObject = True,tagList=[])
		self.fields = {
		"PowerOn":RSZVariable(name="PowerOn",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"PowerOff":RSZVariable(name="PowerOff",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_light_LightDelayPlayer_DelayParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.LightDelayPlayer.DelayParam",typeIDHash=0x917c4788,CRC=0xd81f6040,isObject = True,tagList=[])
		self.fields = {
		"EnableDelay":RSZVariable(name="EnableDelay",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"DelayUserCurve":RSZVariable(name="DelayUserCurve",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_UseEmissiveDelayTracks":RSZVariable(name="_UseEmissiveDelayTracks",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"FrameScaleRange":RSZVariable(name="FrameScaleRange",dataType="float2",isList=False,alignment=4,value=None,tagSet=['REMAP_Range']),
		}

class via_relib_light_ReLibEventLightBehavior(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.ReLibEventLightBehavior",typeIDHash=0x180aca8b,CRC=0xcbeb2199,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_IntensityRate":RSZVariable(name="_IntensityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EmissiveRate":RSZVariable(name="_EmissiveRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_ControlLightBehaviorList":RSZVariable(name="_ControlLightBehaviorList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_ReLibLightBehavior(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.ReLibLightBehavior",typeIDHash=0x3c58b4ff,CRC=0xec2c6fb6,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_DistanceAttenuation":RSZVariable(name="_DistanceAttenuation",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_KillComponent":RSZVariable(name="_KillComponent",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LightActionDistanceShadow":RSZVariable(name="_LightActionDistanceShadow",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_LightActionControlAOEfficiency":RSZVariable(name="_LightActionControlAOEfficiency",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"MainPlayer":RSZVariable(name="MainPlayer",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"GlobalParamIndex":RSZVariable(name="GlobalParamIndex",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"BlinkUserCurvePlayer":RSZVariable(name="BlinkUserCurvePlayer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"BlinkUserCurveVariationPlayer":RSZVariable(name="BlinkUserCurveVariationPlayer",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"TimelineAnimation":RSZVariable(name="TimelineAnimation",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"_EventIntensityRate":RSZVariable(name="_EventIntensityRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_EventEmissiveRate":RSZVariable(name="_EventEmissiveRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"_IsEventIntensityRate":RSZVariable(name="_IsEventIntensityRate",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"_EventIdentifyName":RSZVariable(name="_EventIdentifyName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_light_TimelineUserCurvePlayer(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.TimelineUserCurvePlayer",typeIDHash=0x9cf4692c,CRC=0xe6dde003,isObject = True,tagList=[])
		self.fields = {
		"IsLoop":RSZVariable(name="IsLoop",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"TimelineAnimationUserCurve":RSZVariable(name="TimelineAnimationUserCurve",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"_TimelinePlayType":RSZVariable(name="_TimelinePlayType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"RlinkRateStartAnimationFrame":RSZVariable(name="RlinkRateStartAnimationFrame",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"FrameScale":RSZVariable(name="FrameScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"MaterialControllParamList":RSZVariable(name="MaterialControllParamList",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_light_TimelineUserCurvePlayer_MaterialControllParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.light.TimelineUserCurvePlayer.MaterialControllParam",typeIDHash=0xf98a282,CRC=0x8144fe4c,isObject = True,tagList=[])
		self.fields = {
		"RefObj":RSZVariable(name="RefObj",dataType="guid",isList=False,alignment=8,value=None,tagSet=['REMAP_GameObjectRef']),
		"MaterialName":RSZVariable(name="MaterialName",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"VariableName":RSZVariable(name="VariableName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"_ParamType":RSZVariable(name="_ParamType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"materialNameList":RSZVariable(name="materialNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"variableNameList":RSZVariable(name="variableNameList",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		}

class via_relib_render_ReLibMeshJointSetting(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.render.ReLibMeshJointSetting",typeIDHash=0x2ce94659,CRC=0x9c3b5db4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"_JointParams":RSZVariable(name="_JointParams",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

class via_relib_render_ReLibMeshJointSetting_cJointParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.render.ReLibMeshJointSetting.cJointParam",typeIDHash=0x93839e87,CRC=0x20bc9c39,isObject = True,tagList=[])
		self.fields = {
		"Pos":RSZVariable(name="Pos",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Scale":RSZVariable(name="Scale",dataType="vec3",isList=False,alignment=16,value=None,tagSet=[]),
		"Rotation":RSZVariable(name="Rotation",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['REMAP_Quaternion']),
		"NameHash":RSZVariable(name="NameHash",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_relib_utility_ReLibBarcode2DMaker(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.relib.utility.ReLibBarcode2DMaker",typeIDHash=0x476b0483,CRC=0x994875f5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ByteAddressBuffer":RSZVariable(name="ByteAddressBuffer",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"RenderTargetTexture":RSZVariable(name="RenderTargetTexture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"Material":RSZVariable(name="Material",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_render_AlembicMesh(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.AlembicMesh",typeIDHash=0x7964505b,CRC=0x723c46f5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_AmbientOcclusionGeometry(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.AmbientOcclusionGeometry",typeIDHash=0x66c7b0cc,CRC=0x16114389,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_AmbientOcclusionGeometryElement(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.AmbientOcclusionGeometryElement",typeIDHash=0x90339e5b,CRC=0xd8fe9863,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_Atmosphere2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Atmosphere2",typeIDHash=0x44c1f34a,CRC=0xe2ac66db,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v58":RSZVariable(name="v58",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_BeautyDirectionalLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.BeautyDirectionalLight",typeIDHash=0x42e14db1,CRC=0x30efd3cc,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_BlendShapeController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.BlendShapeController",typeIDHash=0x5ec3103d,CRC=0xf049ebd2,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_BlendShapeMeshRebinder(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.BlendShapeMeshRebinder",typeIDHash=0xa2cf875f,CRC=0x18dc206,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_ByteBufferUpdater(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ByteBufferUpdater",typeIDHash=0x237c63e5,CRC=0x36854676,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_CaptureToTexture(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CaptureToTexture",typeIDHash=0x56a7b0b0,CRC=0x7b872b57,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_Cloudscape2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Cloudscape2",typeIDHash=0x321aacd8,CRC=0xe6acf046,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v15":RSZVariable(name="v15",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v24":RSZVariable(name="v24",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v25":RSZVariable(name="v25",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v35":RSZVariable(name="v35",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v36":RSZVariable(name="v36",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v69":RSZVariable(name="v69",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v82":RSZVariable(name="v82",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v83":RSZVariable(name="v83",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v84":RSZVariable(name="v84",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v85":RSZVariable(name="v85",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v86":RSZVariable(name="v86",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v87":RSZVariable(name="v87",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v88":RSZVariable(name="v88",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v89":RSZVariable(name="v89",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v90":RSZVariable(name="v90",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v91":RSZVariable(name="v91",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v92":RSZVariable(name="v92",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v93":RSZVariable(name="v93",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v94":RSZVariable(name="v94",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_ColorCorrectLinearParams(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ColorCorrectLinearParams",typeIDHash=0x7811aa48,CRC=0x9e9a4b5,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_CustomComputeShader(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CustomComputeShader",typeIDHash=0xbcbb84b6,CRC=0x3d0b670c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_CustomComputeShader_ComputeShaderSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CustomComputeShader.ComputeShaderSettings",typeIDHash=0xa311af49,CRC=0x9bd6eabe,isObject = True,tagList=[])
		self.fields = {
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_CustomComputeShader_ConstantCS(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CustomComputeShader.ConstantCS",typeIDHash=0x3237260d,CRC=0xc7015288,isObject = True,tagList=[])
		self.fields = {
		}

class via_render_CustomComputeShader_ShaderResourceCS(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CustomComputeShader.ShaderResourceCS",typeIDHash=0xa6b02eb7,CRC=0x104fb830,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_CustomFilter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CustomFilter",typeIDHash=0x49df2415,CRC=0xd6458613,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_CustomFilterBeforeTransparent(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.CustomFilterBeforeTransparent",typeIDHash=0xd816531e,CRC=0xbfac4cb9,isObject = True,tagList=[])
		self.fields = {
		}

class via_render_DepthOfField(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.DepthOfField",typeIDHash=0x65503c0f,CRC=0x64f1cfa0,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_DirectionalLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.DirectionalLight",typeIDHash=0x47a4237d,CRC=0xfb057bec,isObject = True,tagList=[])
		self.fields = {
		"Enabled":RSZVariable(name="Enabled",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Intensity":RSZVariable(name="Intensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"RenderOutputID":RSZVariable(name="RenderOutputID",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Color":RSZVariable(name="Color",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"BlackBodyRadiation":RSZVariable(name="BlackBodyRadiation",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Temperature":RSZVariable(name="Temperature",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"BounceIntensity":RSZVariable(name="BounceIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"MinRoughness":RSZVariable(name="MinRoughness",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"AOEfficiency":RSZVariable(name="AOEfficiency",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ImportantLevel":RSZVariable(name="ImportantLevel",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"LightingTarget":RSZVariable(name="LightingTarget",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"LightBakeOption":RSZVariable(name="LightBakeOption",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"UsingSameIntensity":RSZVariable(name="UsingSameIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"VolumetricScatteringIntensity":RSZVariable(name="VolumetricScatteringIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Direction":RSZVariable(name="Direction",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowDistance":RSZVariable(name="ShadowDistance",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowDistanceFromBoundary":RSZVariable(name="ShadowDistanceFromBoundary",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowVariance":RSZVariable(name="ShadowVariance",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"SoftShadowKernel":RSZVariable(name="SoftShadowKernel",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowBias":RSZVariable(name="ShadowBias",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowCastFlag":RSZVariable(name="ShadowCastFlag",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowDepthBias":RSZVariable(name="ShadowDepthBias",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowSlopeBias":RSZVariable(name="ShadowSlopeBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowMinimumAreaSize":RSZVariable(name="ShadowMinimumAreaSize",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowViewScale":RSZVariable(name="ShadowViewScale",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SDSMEnable":RSZVariable(name="SDSMEnable",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SDFGloup":RSZVariable(name="SDFGloup",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"UseSDFShadow":RSZVariable(name="UseSDFShadow",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"CascadeShadowRange":RSZVariable(name="CascadeShadowRange",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"SDFShadowRange":RSZVariable(name="SDFShadowRange",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SDFShadowRayLength":RSZVariable(name="SDFShadowRayLength",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"SDFShadowMaxStep":RSZVariable(name="SDFShadowMaxStep",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"SDFShadowSoftness":RSZVariable(name="SDFShadowSoftness",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"SDFCullingCoef":RSZVariable(name="SDFCullingCoef",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Partition":RSZVariable(name="Partition",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"CullingScaler":RSZVariable(name="CullingScaler",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"MinimumFOV":RSZVariable(name="MinimumFOV",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"MinimumFarPlane":RSZVariable(name="MinimumFarPlane",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"MaximumNearPlane":RSZVariable(name="MaximumNearPlane",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"SSTPath":RSZVariable(name="SSTPath",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"AllowTranslucentShadows":RSZVariable(name="AllowTranslucentShadows",dataType="ushort",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"SSTDitherEnable":RSZVariable(name="SSTDitherEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"BakedShadowBias":RSZVariable(name="BakedShadowBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowMapBoundary":RSZVariable(name="ShadowMapBoundary",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"EnableShadowProjectionTexture":RSZVariable(name="EnableShadowProjectionTexture",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowProjectionTexturePath":RSZVariable(name="ShadowProjectionTexturePath",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ProjectionTextureDirection":RSZVariable(name="ProjectionTextureDirection",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ProjectionScale":RSZVariable(name="ProjectionScale",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ProjectionOffset":RSZVariable(name="ProjectionOffset",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ScrollSpeed":RSZVariable(name="ScrollSpeed",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v66":RSZVariable(name="v66",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="obb",isList=True,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v78":RSZVariable(name="v78",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v82":RSZVariable(name="v82",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v83":RSZVariable(name="v83",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v84":RSZVariable(name="v84",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v85":RSZVariable(name="v85",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v86":RSZVariable(name="v86",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v87":RSZVariable(name="v87",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_DynamicProbeGI(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.DynamicProbeGI",typeIDHash=0xbb28ff2e,CRC=0x85e13f99,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v69":RSZVariable(name="v69",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v82":RSZVariable(name="v82",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v83":RSZVariable(name="v83",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v84":RSZVariable(name="v84",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v85":RSZVariable(name="v85",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v86":RSZVariable(name="v86",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v87":RSZVariable(name="v87",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v88":RSZVariable(name="v88",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v89":RSZVariable(name="v89",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v90":RSZVariable(name="v90",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v91":RSZVariable(name="v91",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v92":RSZVariable(name="v92",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v93":RSZVariable(name="v93",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v94":RSZVariable(name="v94",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v95":RSZVariable(name="v95",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v96":RSZVariable(name="v96",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v97":RSZVariable(name="v97",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v98":RSZVariable(name="v98",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v99":RSZVariable(name="v99",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v100":RSZVariable(name="v100",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v101":RSZVariable(name="v101",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v102":RSZVariable(name="v102",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v103":RSZVariable(name="v103",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v104":RSZVariable(name="v104",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v105":RSZVariable(name="v105",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v106":RSZVariable(name="v106",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v107":RSZVariable(name="v107",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v108":RSZVariable(name="v108",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v109":RSZVariable(name="v109",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v110":RSZVariable(name="v110",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v111":RSZVariable(name="v111",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v112":RSZVariable(name="v112",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v113":RSZVariable(name="v113",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v114":RSZVariable(name="v114",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v115":RSZVariable(name="v115",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v116":RSZVariable(name="v116",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v117":RSZVariable(name="v117",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v118":RSZVariable(name="v118",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v119":RSZVariable(name="v119",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_ExperimentalRayTrace(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ExperimentalRayTrace",typeIDHash=0x72fd01de,CRC=0x357a46fd,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v69":RSZVariable(name="v69",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v82":RSZVariable(name="v82",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v83":RSZVariable(name="v83",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v84":RSZVariable(name="v84",dataType="int",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v85":RSZVariable(name="v85",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v86":RSZVariable(name="v86",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v87":RSZVariable(name="v87",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v88":RSZVariable(name="v88",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v89":RSZVariable(name="v89",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v90":RSZVariable(name="v90",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v91":RSZVariable(name="v91",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v92":RSZVariable(name="v92",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v93":RSZVariable(name="v93",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v94":RSZVariable(name="v94",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v95":RSZVariable(name="v95",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v96":RSZVariable(name="v96",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v97":RSZVariable(name="v97",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v98":RSZVariable(name="v98",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v99":RSZVariable(name="v99",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v100":RSZVariable(name="v100",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v101":RSZVariable(name="v101",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v102":RSZVariable(name="v102",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v103":RSZVariable(name="v103",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v104":RSZVariable(name="v104",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v105":RSZVariable(name="v105",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v106":RSZVariable(name="v106",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v107":RSZVariable(name="v107",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v108":RSZVariable(name="v108",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v109":RSZVariable(name="v109",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v110":RSZVariable(name="v110",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v111":RSZVariable(name="v111",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v112":RSZVariable(name="v112",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v113":RSZVariable(name="v113",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v114":RSZVariable(name="v114",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v115":RSZVariable(name="v115",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v116":RSZVariable(name="v116",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v117":RSZVariable(name="v117",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v118":RSZVariable(name="v118",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v119":RSZVariable(name="v119",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v120":RSZVariable(name="v120",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v121":RSZVariable(name="v121",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v122":RSZVariable(name="v122",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v123":RSZVariable(name="v123",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v124":RSZVariable(name="v124",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v125":RSZVariable(name="v125",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v126":RSZVariable(name="v126",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v127":RSZVariable(name="v127",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v128":RSZVariable(name="v128",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v129":RSZVariable(name="v129",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v130":RSZVariable(name="v130",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v131":RSZVariable(name="v131",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v132":RSZVariable(name="v132",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v133":RSZVariable(name="v133",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v134":RSZVariable(name="v134",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v135":RSZVariable(name="v135",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v136":RSZVariable(name="v136",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v137":RSZVariable(name="v137",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v138":RSZVariable(name="v138",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v139":RSZVariable(name="v139",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v140":RSZVariable(name="v140",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v141":RSZVariable(name="v141",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v142":RSZVariable(name="v142",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v143":RSZVariable(name="v143",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v144":RSZVariable(name="v144",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v145":RSZVariable(name="v145",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v146":RSZVariable(name="v146",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v147":RSZVariable(name="v147",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v148":RSZVariable(name="v148",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v149":RSZVariable(name="v149",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_FFTBloom(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.FFTBloom",typeIDHash=0x690228d7,CRC=0x600d8a3f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_FakeLensflare(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.FakeLensflare",typeIDHash=0x8b435dc4,CRC=0x87c4988e,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_FilterShader(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.FilterShader",typeIDHash=0x80d786d4,CRC=0x68999726,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_Fog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Fog",typeIDHash=0xdaeadb2,CRC=0xc00b2cbd,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v20":RSZVariable(name="v20",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_GIPointCloud(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.GIPointCloud",typeIDHash=0xa2768f71,CRC=0x42dc664f,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_GeometryAOControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.GeometryAOControl",typeIDHash=0xa7d94612,CRC=0xaf9680ff,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_GridFluid2DObstacle(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.GridFluid2DObstacle",typeIDHash=0xa5c38431,CRC=0x7dbe647,isObject = True,tagList=[])
		self.fields = {
		}

class via_render_GridFluid2DWaterObstacle(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.GridFluid2DWaterObstacle",typeIDHash=0xbcd704fd,CRC=0xc954a38,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_Radius":RSZVariable(name="v1_Radius",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_Length":RSZVariable(name="v2_Length",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v3_MovingPower":RSZVariable(name="v3_MovingPower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_DebugDraw":RSZVariable(name="v4_DebugDraw",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_render_IESPointLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.IESPointLight",typeIDHash=0xee3c7c86,CRC=0xc2bdd0b4,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v49":RSZVariable(name="v49",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v52":RSZVariable(name="v52",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LDRColorCorrect(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRColorCorrect",typeIDHash=0x6a77a7d9,CRC=0x883c5397,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v06":RSZVariable(name="v06",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LDRColorDeficiencySimulation(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRColorDeficiencySimulation",typeIDHash=0xe4ede06,CRC=0x5c221ea6,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_render_LDRFilmGrain(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRFilmGrain",typeIDHash=0x71d67a48,CRC=0x7bf74c7,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_RandomUVOffset":RSZVariable(name="v1_RandomUVOffset",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v2_NoisePower":RSZVariable(name="v2_NoisePower",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v3_NoisePowerCroma":RSZVariable(name="v3_NoisePowerCroma",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_NoiseSize":RSZVariable(name="v4_NoiseSize",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"v5_NoiseDensity":RSZVariable(name="v5_NoiseDensity",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v6_NoiseContrast":RSZVariable(name="v6_NoiseContrast",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v7_BlendRate":RSZVariable(name="v7_BlendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_LDRHazeFilter(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRHazeFilter",typeIDHash=0xa78c9e5a,CRC=0xe0a31be5,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LDRImagePlane(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRImagePlane",typeIDHash=0x547c60af,CRC=0x358206a1,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_BlendType":RSZVariable(name="v1_BlendType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_Color":RSZVariable(name="v2_Color",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"v3_LevelRate":RSZVariable(name="v3_LevelRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_LevelRange":RSZVariable(name="v4_LevelRange",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v5_Base":RSZVariable(name="v5_Base",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v6_Alpha":RSZVariable(name="v6_Alpha",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_render_LDRLensDistortion(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRLensDistortion",typeIDHash=0x6ade3d6c,CRC=0x8faca26,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LDRPostProcess(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRPostProcess",typeIDHash=0x2790b073,CRC=0xc02c0882,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LDRRadialBlur(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LDRRadialBlur",typeIDHash=0x73f71492,CRC=0xe09df40e,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LightProbeBlocker(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LightProbeBlocker",typeIDHash=0x385000cc,CRC=0x8b191c91,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LightProbesInterpolatable(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LightProbesInterpolatable",typeIDHash=0x27763fa1,CRC=0xa10f0aae,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v3":RSZVariable(name="v3",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="vec4",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v23":RSZVariable(name="v23",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LightShaftFilterControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LightShaftFilterControl",typeIDHash=0x4f7d08d5,CRC=0x81082794,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_LocalCubemap(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.LocalCubemap",typeIDHash=0xa6697e2d,CRC=0xade60443,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v02":RSZVariable(name="v02",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v06":RSZVariable(name="v06",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ushort",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_MaterialParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.MaterialParam",typeIDHash=0x12e376e4,CRC=0xfe2e22f7,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v01":RSZVariable(name="v01",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v02":RSZVariable(name="v02",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_Mesh(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Mesh",typeIDHash=0xbe980941,CRC=0xe8ea6341,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"meshPath":RSZVariable(name="meshPath",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"mdfPath":RSZVariable(name="mdfPath",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ushort",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['REMAP_Object']),
		"v41":RSZVariable(name="v41",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v69":RSZVariable(name="v69",dataType="ubyte",isList=True,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v80":RSZVariable(name="v80",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v81":RSZVariable(name="v81",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_Moon(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Moon",typeIDHash=0x50bad846,CRC=0xb752c1b7,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v31":RSZVariable(name="v31",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_MotionBlur(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.MotionBlur",typeIDHash=0x511ae18,CRC=0x391c5651,isObject = True,tagList=[])
		self.fields = {
		}

class via_render_Outline(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Outline",typeIDHash=0x64947ee0,CRC=0x742159e4,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_OutlineSettingElement(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.OutlineSettingElement",typeIDHash=0x2aeaf5ea,CRC=0x55419563,isObject = True,tagList=[])
		self.fields = {
		"v0_OutlineColor":RSZVariable(name="v0_OutlineColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		"v1_OutlineThickness":RSZVariable(name="v1_OutlineThickness",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v2_SilhouetteMask":RSZVariable(name="v2_SilhouetteMask",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v3_MaskScale":RSZVariable(name="v3_MaskScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_UseViewNormalDistortion":RSZVariable(name="v4_UseViewNormalDistortion",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v5_ViewNormalDistortion":RSZVariable(name="v5_ViewNormalDistortion",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v6_SilhouetteColor":RSZVariable(name="v6_SilhouetteColor",dataType="color",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_PointLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.PointLight",typeIDHash=0xb4370344,CRC=0xc32b06f7,isObject = True,tagList=[])
		self.fields = {
		"Enabled":RSZVariable(name="Enabled",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Intensity":RSZVariable(name="Intensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"RenderOutputID":RSZVariable(name="RenderOutputID",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Color":RSZVariable(name="Color",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"BlackBodyRadiation":RSZVariable(name="BlackBodyRadiation",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Temperature":RSZVariable(name="Temperature",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"BounceIntensity":RSZVariable(name="BounceIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"MinRoughness":RSZVariable(name="MinRoughness",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"AOEfficiency":RSZVariable(name="AOEfficiency",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ImportantLevel":RSZVariable(name="ImportantLevel",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"LightingTarget":RSZVariable(name="LightingTarget",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"LightBakeOption":RSZVariable(name="LightBakeOption",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"UsingSameIntensity":RSZVariable(name="UsingSameIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"VolumetricScatteringIntensity":RSZVariable(name="VolumetricScatteringIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Radius":RSZVariable(name="Radius",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"InfluenceRadius":RSZVariable(name="InfluenceRadius",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ReferenceEffectiveRange":RSZVariable(name="ReferenceEffectiveRange",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"IlluminanceThreshold":RSZVariable(name="IlluminanceThreshold",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowEnable":RSZVariable(name="ShadowEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"BackGroundShadowEnable":RSZVariable(name="BackGroundShadowEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ForceShadowCacheEnable":RSZVariable(name="ForceShadowCacheEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowCastFlag":RSZVariable(name="ShadowCastFlag",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowLODBias":RSZVariable(name="ShadowLODBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowNearPlane":RSZVariable(name="ShadowNearPlane",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowVariance":RSZVariable(name="ShadowVariance",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowBias":RSZVariable(name="ShadowBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowDepthBias":RSZVariable(name="ShadowDepthBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowSlopeBias":RSZVariable(name="ShadowSlopeBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ProjectionTexture":RSZVariable(name="ProjectionTexture",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v49":RSZVariable(name="v49",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_Primitive(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.Primitive",typeIDHash=0xc8b8aca,CRC=0xe6e1e7f,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_PrimitiveVfxControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.PrimitiveVfxControl",typeIDHash=0x837e5047,CRC=0xb1761063,isObject = True,tagList=[])
		self.fields = {
		"v0_IntensityScale":RSZVariable(name="v0_IntensityScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_PrimitiveVfxSubscene(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.PrimitiveVfxSubscene",typeIDHash=0xb5327770,CRC=0xfcc016b4,isObject = True,tagList=[])
		self.fields = {
		"v0_RenderTarget":RSZVariable(name="v0_RenderTarget",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v1_ResolutionType":RSZVariable(name="v1_ResolutionType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_ProjectionSpotLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ProjectionSpotLight",typeIDHash=0x6c397362,CRC=0x1dfe64a0,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v66":RSZVariable(name="v66",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_RenderOutput(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.RenderOutput",typeIDHash=0x75825c3a,CRC=0xf58869b,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="unkndata24",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_RenderTargetModifier(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.RenderTargetModifier",typeIDHash=0xed5780a9,CRC=0xd4fd0bf4,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_RenderTargetOperator(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.RenderTargetOperator",typeIDHash=0x8d65f911,CRC=0x4380ad,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v16":RSZVariable(name="v16",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_SSAOControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SSAOControl",typeIDHash=0xe8db1df6,CRC=0x27a9fcc5,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_SSRControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SSRControl",typeIDHash=0x4e347180,CRC=0x6eb1e817,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_SSSSSControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SSSSSControl",typeIDHash=0xc7d8e0a,CRC=0xb614d2a2,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_ShellFurMesh(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ShellFurMesh",typeIDHash=0x6c13b6a3,CRC=0xe7620b2d,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_ShellFurParam(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ShellFurParam",typeIDHash=0xc20504c1,CRC=0xfbb3c2bf,isObject = True,tagList=[])
		self.fields = {
		"v0_MaterialName":RSZVariable(name="v0_MaterialName",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1_ForceTwoSide":RSZVariable(name="v1_ForceTwoSide",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v2_ForceAlphaTest":RSZVariable(name="v2_ForceAlphaTest",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v3_ShellCount":RSZVariable(name="v3_ShellCount",dataType="uint",isList=False,alignment=4,value=None,tagSet=[]),
		"v4_ShellThinType":RSZVariable(name="v4_ShellThinType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v5_ShellBottomSave":RSZVariable(name="v5_ShellBottomSave",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v6_GroomingTexCoordType":RSZVariable(name="v6_GroomingTexCoordType",dataType="int",isList=False,alignment=4,value=None,tagSet=[]),
		"v7_GroomingTexture":RSZVariable(name="v7_GroomingTexture",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v8_ShellHeight":RSZVariable(name="v8_ShellHeight",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v9_BendRate":RSZVariable(name="v9_BendRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v10_BendRootRate":RSZVariable(name="v10_BendRootRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v11_NormalTransformRate":RSZVariable(name="v11_NormalTransformRate",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v12_Stiffness":RSZVariable(name="v12_Stiffness",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v13_StiffnessDistribution":RSZVariable(name="v13_StiffnessDistribution",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v14_SpringCoefficient":RSZVariable(name="v14_SpringCoefficient",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v15_Dumping":RSZVariable(name="v15_Dumping",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v16_GravityForceScale":RSZVariable(name="v16_GravityForceScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v17_DirectWindForceScale":RSZVariable(name="v17_DirectWindForceScale",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		"v18_Disable":RSZVariable(name="v18_Disable",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		}

class via_render_SingleClusterMaterialController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SingleClusterMaterialController",typeIDHash=0x27c67536,CRC=0xd77c7466,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_SingleClusterMaterialParamWrapper(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SingleClusterMaterialParamWrapper",typeIDHash=0x871cef11,CRC=0x3e813bb3,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_SoftBloom(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SoftBloom",typeIDHash=0x676e3287,CRC=0xe3bf6252,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_SpotLight(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SpotLight",typeIDHash=0x8d6f0e8,CRC=0xc5d265b0,isObject = True,tagList=[])
		self.fields = {
		"Enabled":RSZVariable(name="Enabled",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Intensity":RSZVariable(name="Intensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"RenderOutputID":RSZVariable(name="RenderOutputID",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Color":RSZVariable(name="Color",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"BlackBodyRadiation":RSZVariable(name="BlackBodyRadiation",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"Temperature":RSZVariable(name="Temperature",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"BounceIntensity":RSZVariable(name="BounceIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"MinRoughness":RSZVariable(name="MinRoughness",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"AOEfficiency":RSZVariable(name="AOEfficiency",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ImportantLevel":RSZVariable(name="ImportantLevel",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"LightingTarget":RSZVariable(name="LightingTarget",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"LightBakeOption":RSZVariable(name="LightBakeOption",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"UsingSameIntensity":RSZVariable(name="UsingSameIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"VolumetricScatteringIntensity":RSZVariable(name="VolumetricScatteringIntensity",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Radius":RSZVariable(name="Radius",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"InfluenceRadius":RSZVariable(name="InfluenceRadius",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"IlluminanceThreshold":RSZVariable(name="IlluminanceThreshold",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Cone":RSZVariable(name="Cone",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Spread":RSZVariable(name="Spread",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"Falloff":RSZVariable(name="Falloff",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowEnable":RSZVariable(name="ShadowEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"BackGroundShadowEnable":RSZVariable(name="BackGroundShadowEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ForceShadowCacheEnable":RSZVariable(name="ForceShadowCacheEnable",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowCastFlag":RSZVariable(name="ShadowCastFlag",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"AllowTranslucentShadows":RSZVariable(name="AllowTranslucentShadows",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowLODBias":RSZVariable(name="ShadowLODBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"UniformShadowEnable":RSZVariable(name="UniformShadowEnable",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowNearPlane":RSZVariable(name="ShadowNearPlane",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowVariance":RSZVariable(name="ShadowVariance",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowBias":RSZVariable(name="ShadowBias",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"ShadowDepthBias":RSZVariable(name="ShadowDepthBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"ShadowSlopeBias":RSZVariable(name="ShadowSlopeBias",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"DetailShadow":RSZVariable(name="DetailShadow",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"DetailFocusTarget":RSZVariable(name="DetailFocusTarget",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_StarrySky(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.StarrySky",typeIDHash=0xcafb19ba,CRC=0xafb62e58,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_StreamingMeshController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.StreamingMeshController",typeIDHash=0xcf318533,CRC=0x409d9b84,isObject = True,tagList=[])
		self.fields = {
		}

class via_render_StreamingTextureController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.StreamingTextureController",typeIDHash=0xb67210e9,CRC=0x173c429c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_SubsurfaceSettings(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.SubsurfaceSettings",typeIDHash=0x7f6852b,CRC=0xe5e64807,isObject = True,tagList=[])
		self.fields = {
		"v0_Enabled":RSZVariable(name="v0_Enabled",dataType="bool",isList=False,alignment=1,value=None,tagSet=[]),
		"v1_Profile":RSZVariable(name="v1_Profile",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		}

class via_render_TessellationFactor(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.TessellationFactor",typeIDHash=0x6e9dbccf,CRC=0x7b1f5b6d,isObject = True,tagList=[])
		self.fields = {
		"v0_SubdivitionRange":RSZVariable(name="v0_SubdivitionRange",dataType="float",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_render_TextureScaler(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.TextureScaler",typeIDHash=0xadeef8bc,CRC=0x87d4a471,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_ToneMapping(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.ToneMapping",typeIDHash=0xd0742287,CRC=0x531448b8,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v19":RSZVariable(name="v19",dataType="guid",isList=False,alignment=8,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v23":RSZVariable(name="v23",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v48":RSZVariable(name="v48",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v54":RSZVariable(name="v54",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v55":RSZVariable(name="v55",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v56":RSZVariable(name="v56",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v57":RSZVariable(name="v57",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v58":RSZVariable(name="v58",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v59":RSZVariable(name="v59",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v60":RSZVariable(name="v60",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v61":RSZVariable(name="v61",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v62":RSZVariable(name="v62",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v63":RSZVariable(name="v63",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v64":RSZVariable(name="v64",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v65":RSZVariable(name="v65",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v66":RSZVariable(name="v66",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v67":RSZVariable(name="v67",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v68":RSZVariable(name="v68",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v69":RSZVariable(name="v69",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v70":RSZVariable(name="v70",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v71":RSZVariable(name="v71",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v72":RSZVariable(name="v72",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v73":RSZVariable(name="v73",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v74":RSZVariable(name="v74",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v75":RSZVariable(name="v75",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v76":RSZVariable(name="v76",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v77":RSZVariable(name="v77",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v78":RSZVariable(name="v78",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v79":RSZVariable(name="v79",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumeDecal(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumeDecal",typeIDHash=0xe7a5938d,CRC=0x9c4d1020,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v20":RSZVariable(name="v20",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v21":RSZVariable(name="v21",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v22":RSZVariable(name="v22",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v23":RSZVariable(name="v23",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v24":RSZVariable(name="v24",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v25":RSZVariable(name="v25",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v26":RSZVariable(name="v26",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v40":RSZVariable(name="v40",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v41":RSZVariable(name="v41",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v42":RSZVariable(name="v42",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v43":RSZVariable(name="v43",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v44":RSZVariable(name="v44",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v45":RSZVariable(name="v45",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v46":RSZVariable(name="v46",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v47":RSZVariable(name="v47",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v48":RSZVariable(name="v48",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v49":RSZVariable(name="v49",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v50":RSZVariable(name="v50",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v51":RSZVariable(name="v51",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v52":RSZVariable(name="v52",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v53":RSZVariable(name="v53",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumeOccludee(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumeOccludee",typeIDHash=0x88fafdb5,CRC=0xc54394f6,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumetricFog(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumetricFog",typeIDHash=0x37a06263,CRC=0xeaace576,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="obb",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v04":RSZVariable(name="v04",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumetricFogControl(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumetricFogControl",typeIDHash=0x9bf46e16,CRC=0xf45feff5,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v14":RSZVariable(name="v14",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v17":RSZVariable(name="v17",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v20":RSZVariable(name="v20",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v21":RSZVariable(name="v21",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v22":RSZVariable(name="v22",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v24":RSZVariable(name="v24",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v25":RSZVariable(name="v25",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v26":RSZVariable(name="v26",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v27":RSZVariable(name="v27",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v28":RSZVariable(name="v28",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v29":RSZVariable(name="v29",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v30":RSZVariable(name="v30",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v31":RSZVariable(name="v31",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v32":RSZVariable(name="v32",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v33":RSZVariable(name="v33",dataType="float3",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v34":RSZVariable(name="v34",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v35":RSZVariable(name="v35",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v36":RSZVariable(name="v36",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v37":RSZVariable(name="v37",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v38":RSZVariable(name="v38",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v39":RSZVariable(name="v39",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumetricFogExpHeightFogProperty(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumetricFogExpHeightFogProperty",typeIDHash=0xc55bef35,CRC=0x12143094,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="int2",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumetricFogMaterialController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumetricFogMaterialController",typeIDHash=0x8f1a1005,CRC=0xde0cbac2,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_render_VolumetricFogMaterialParamWrapper(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.render.VolumetricFogMaterialParamWrapper",typeIDHash=0xc1c97ef0,CRC=0x63b57bc9,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="vec4",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v5":RSZVariable(name="v5",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		}

class via_speedtree_SpeedTreeGlobalController(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.speedtree.SpeedTreeGlobalController",typeIDHash=0xe440d86d,CRC=0xde19436c,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="vec4",isList=False,alignment=16,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_timeline_Timeline(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.timeline.Timeline",typeIDHash=0xa59f1549,CRC=0x9ca27c35,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_timeline_TimelineBlend(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.timeline.TimelineBlend",typeIDHash=0xc4777f2d,CRC=0x94a3ad41,isObject = True,tagList=[])
		self.fields = {
		"v00":RSZVariable(name="v00",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v01":RSZVariable(name="v01",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v02":RSZVariable(name="v02",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v03":RSZVariable(name="v03",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v04":RSZVariable(name="v04",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v05":RSZVariable(name="v05",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v06":RSZVariable(name="v06",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v07":RSZVariable(name="v07",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v08":RSZVariable(name="v08",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v09":RSZVariable(name="v09",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_timeline_TimelineFsm2(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.timeline.TimelineFsm2",typeIDHash=0xaae170f0,CRC=0xfae6f943,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v3":RSZVariable(name="v3",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="string",isList=False,alignment=4,value=None,tagSet=['REMAP_Resource']),
		"v10":RSZVariable(name="v10",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_zivart_ZivaMesh(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.zivart.ZivaMesh",typeIDHash=0xa7a8e160,CRC=0xa2659141,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v1":RSZVariable(name="v1",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v2":RSZVariable(name="v2",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v3":RSZVariable(name="v3",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v4":RSZVariable(name="v4",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v5":RSZVariable(name="v5",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v6":RSZVariable(name="v6",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v7":RSZVariable(name="v7",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v8":RSZVariable(name="v8",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v9":RSZVariable(name="v9",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v10":RSZVariable(name="v10",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v11":RSZVariable(name="v11",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v12":RSZVariable(name="v12",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		"v13":RSZVariable(name="v13",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v14":RSZVariable(name="v14",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v15":RSZVariable(name="v15",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v16":RSZVariable(name="v16",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"v17":RSZVariable(name="v17",dataType="int",isList=True,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v18":RSZVariable(name="v18",dataType="int",isList=False,alignment=4,value=None,tagSet=['UNKNOWN_DATA']),
		"v19":RSZVariable(name="v19",dataType="ubyte",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_zivart_ZivaMeshBody(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.zivart.ZivaMeshBody",typeIDHash=0x249498b9,CRC=0xb0c24084,isObject = True,tagList=[])
		self.fields = {
		"v0":RSZVariable(name="v0",dataType="string",isList=False,alignment=4,value=None,tagSet=[]),
		"v1":RSZVariable(name="v1",dataType="string",isList=True,alignment=4,value=None,tagSet=[]),
		"v2":RSZVariable(name="v2",dataType="ushort",isList=False,alignment=1,value=None,tagSet=['UNKNOWN_DATA']),
		}

class via_zivart_ZivaMeshLayout(RSZInstance):
	def __init__(self):
		self.instanceInfo = InstanceInfo(name = "via.zivart.ZivaMeshLayout",typeIDHash=0x118f2978,CRC=0xd34e3c32,isObject = True,tagList=[])
		self.fields = {
		"v0_ZivaMeshBody":RSZVariable(name="v0_ZivaMeshBody",dataType="int",isList=True,alignment=4,value=None,tagSet=['REMAP_Object']),
		}

