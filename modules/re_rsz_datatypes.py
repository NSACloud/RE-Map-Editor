from .gen_functions import unsignedToSigned,signedToUnsigned,dictString,textColors,raiseWarning,raiseError,read_uint,read_int,read_int64,read_uint64,read_float,read_short,read_ushort,read_ubyte,read_unicode_string,read_byte,write_uint,write_int,write_int64,write_uint64,write_float,write_short,write_ushort,write_ubyte,write_unicode_string,write_byte
from json import loads
DEBUG_MODE = False

def debugprint(string):
	if DEBUG_MODE:
		print(string)

def getPaddedPos(currentPos,alignment):
	paddedPos = ((currentPos*-1)%alignment)+currentPos
	return paddedPos

class InstanceInfo():
	def __init__(self,name = "newInstance",typeIDHash = 0,CRC = 0, isObject = True,tagList = []):
		self.name = name
		self.typeIDHash = typeIDHash
		self.CRC = CRC
		self.isObject = isObject
		self.tagList = set(tagList)#For internal use
		debugprint("\n"+self.name)
	def __str__(self):
		return self.name + "\nHash:"+str(self.typeIDHash)+" | CRC:"+str(self.CRC)+" | Tags:"+str(self.tagList)
def read_int2(file):
	return (read_int(file),read_int(file)) 
def read_uint2(file):
	return (read_uint(file),read_uint(file)) 
def read_int3(file):
	return (read_int(file),read_int(file),read_int(file)) 
def read_uint3(file):
	return (read_uint(file),read_uint(file),read_uint(file))
def read_float2(file):
	result = (read_float(file),read_float(file))
	return result
def read_float3(file):
	result = (read_float(file),read_float(file),read_float(file))
	return result
def read_float4(file):
	result = (read_float(file),read_float(file),read_float(file),read_float(file))
	return result
def read_vec2(file):#Vectors are padded
	result = (read_float(file),read_float(file))
	file.seek(8,1)#vec3's are padded
	return result
def read_vec3(file):
	result = (read_float(file),read_float(file),read_float(file))
	file.seek(4,1)#vec3's are padded
	return result
def read_vec4(file):
	return (read_float(file),read_float(file),read_float(file),read_float(file))
def read_mat4(file):
	return (
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)))
def read_obb(file):
	return (
		 (read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file),read_float(file)))
	"""
	return (
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)))
	"""
def read_aabb(file):
	return (
		 (read_float(file),read_float(file),read_float(file),read_float(file)),
		 (read_float(file),read_float(file),read_float(file),read_float(file)))
def read_rsz_string(file):
	stringSize = read_uint(file)
	#string = file.read(stringSize-2).decode("UTF-16LE")#.replace('\x00', '')#Could call read_unicode_string but this is faster since the length is known beforehand
	if stringSize != 0:
		string = read_unicode_string(file)
	else:
		string = "NULL_STR"#NULL_STR is used to indicate a zero length string, otherwise there's no way to determine if the string size should be 0
	return string

def read_color(file):
	return (read_ubyte(file),read_ubyte(file),read_ubyte(file),read_ubyte(file))
def read_guid(file):
	return str(int.from_bytes(file.read(16),byteorder = "little", signed = False))

def read_unkndata13(file):
	return (tuple(file.read(13)))

def read_unkndata24(file):
	return (read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file))
def read_unkndata48(file):
	return (read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file),read_int(file)) 
def read_bool(file):
	return read_ubyte(file) != 0
	
def write_color(file,color):
	for value in color:
		write_ubyte(file, value)
def write_mat(file,mat):
	for row in mat:
		for value in row:
			write_float(file,value)

def write_vec(file,vec):
	for value in vec:
		write_float(file,value)
def write_paddedvec(file,vec):
	for value in vec:
		write_float(file,value)
	file.seek(16-len(vec)*4,1)
def write_rsz_string(file,string):
	if string != "NULL_STR":
		write_uint(file,len(string)+1)
		write_unicode_string(file, string)
	else:
		write_uint(file,0)
def write_guid(file,guid):
	file.write(int.to_bytes((int(guid)),length = 16,byteorder= "little",signed = False))

def write_bytevec(file,bytevec):
	for value in bytevec:
		write_ubyte(file,value)
def write_intvec(file,intvec):
	for value in intvec:
		write_int(file,value)
def write_uintvec(file,uintvec):
	for value in uintvec:
		write_uint(file,value)
def write_bool(file,value):
	if value:
		write_ubyte(file,1)
	else:
		write_ubyte(file,0)
readDataTypeDict={
	"bool":read_bool,
	"ubyte":read_ubyte,
	"byte":read_byte,
	"ushort":read_ushort,
	"short":read_short,
	"uint":read_uint,
	"int":read_int,
	"uint64":read_uint64,
	"int64":read_int64,
	"float":read_float,
	"float2":read_float2,
	"float3":read_float3,
	"float4":read_float4,
	"vec2":read_vec2,
	"vec3":read_vec3,
	"vec4":read_vec4,
	"string":read_rsz_string,
	"mat4":read_mat4,
	"obb":read_obb,
	"aabb":read_aabb,
	"color":read_color,
	"guid":read_guid,
	"uint2":read_uint2,
	"uint3":read_uint3,
	"int2":read_int2,
	"int3":read_int3,
	"unkndata13":read_unkndata13,
	"unkndata24":read_unkndata24,
	"unkndata48":read_unkndata48,
	
	}

writeDataTypeDict={
	"bool":write_bool,
	"ubyte":write_ubyte,
	"byte":write_byte,
	"ushort":write_ushort,
	"short":write_short,
	"uint":write_uint,
	"int":write_int,
	"uint64":write_uint64,
	"int64":write_int64,
	"float":write_float,
	"float2":write_vec,
	"float3":write_vec,
	"float4":write_vec,
	"vec2":write_paddedvec,
	"vec3":write_paddedvec,
	"vec4":write_vec,
	"string":write_rsz_string,
	"mat4":write_mat,
	"obb":write_vec,
	"aabb":write_mat,
	"color":write_color,
	"guid":write_guid,
	"uint2":write_uintvec,
	"uint3":write_uintvec,
	"int2":write_intvec,
	"int3":write_intvec,
	"unkndata13":write_bytevec,
	"unkndata24":write_intvec,
	"unkndata48":write_intvec,
	}

defaultValueDict={
	"bool":0,
	"ubyte":0,
	"byte":0,
	"ushort":0,
	"short":0,
	"uint":0,
	"int":0,
	"uint64":0,
	"int64":0,
	"float":0.0,
	"float2":(0.0,0.0),
	"float3":(0.0,0.0,0.0),
	"float4":(0.0,0.0,0.0,0.0),
	"vec2":(0.0,0.0),
	"vec3":(0.0,0.0,0.0),
	"vec4":(0.0,0.0,0.0,0.0),
	"string":"",
	"mat4":((0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0)),
	"obb":((0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0)),
	"aabb":((0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0)),
	"color":(0,0,0,255),
	"guid":b'\x00'*16,
	"uint2":(0,0),
	"uint3":(0,0,0),
	"int2":(0,0),
	"int3":(0,0,0),
	"unkndata13":(0,0,0,0,0,0,0,0,0,0,0,0,0),
	"unkndata24":(0,0,0,0,0,0),
	"unkndata48":(0,0,0,0,0,0,0,0,0,0,0,0),
	}

arrayDataTypes = set(["int2","uint2","int3","uint3","float2","float3","float4","vec2","vec3","vec4","mat4","obb","aabb"])
multiDimensionalDataTypes = set(["mat4","obb","aabb"])

class RSZInstance():
	def __init__(self):
		self.fields = {}
	def read(self,file):
		for field in self.fields.values():
			field.read(file)
	def write(self,file):
		for field in self.fields.values():
			try:
				field.write(file)
			except Exception as err:
				print("\n\n"+textColors.FAIL +"Error writing " + field.name + " in " + self.instanceInfo.name + textColors.ENDC+ "\n" + str(field) + "\n\n" + str(err))
				raise
				
			
	def getFields(self):#Returns fields as dict
		return self.fields
	def setFields(self,newFieldDict):#Takes a dict, iterates through each key from instance and sets it from the passed dict
		for fieldName in self.fields:
			#Blender doesn't support unsigned ints so they're converted to ints and back upon export
			newFieldValue = newFieldDict.get(fieldName,None)
			if newFieldValue != None:
				if (self.fields[fieldName].isList or self.fields[fieldName].dataType in multiDimensionalDataTypes) and  self.fields[fieldName].dataType in arrayDataTypes:
					#Blender won't let you have lists inside lists as custom properties, so they're stored as strings.
					try:
						newFieldValue = loads(newFieldValue)#Convert string representation of list into a python list
						#print(newFieldValue)
						print (len(newFieldValue))
					except Exception as err:
						print("\n\n"+textColors.FAIL +"Error setting " + fieldName + " in " + self.instanceInfo.name + textColors.ENDC+ "\n" + str(self.fields[fieldName]) + "\n\n" + str(err))
						print(newFieldValue)
						raise
				elif newFieldValue.__class__.__name__ == "IDPropertyArray":
					newFieldValue = newFieldValue.to_list()
					
					if self.fields[fieldName].isList and self.fields[fieldName].dataType == "uint" :
						newFieldValueList = []
						for newFieldEntry in newFieldValue:
							if newFieldEntry < 0:
								newFieldValueList.append(signedToUnsigned(newFieldEntry))
							else:
								newFieldValueList.append(newFieldEntry)
						newFieldValue = newFieldValueList
					
				elif self.fields[fieldName].dataType == "uint" and newFieldValue < 0:
					newFieldValue = signedToUnsigned(newFieldValue)
				
				
					#print("bpy array")
				self.fields[fieldName].value = newFieldValue
	def __str__(self):
		return dictString(self.__dict__)
class RSZVariable():
	
	
	def __init__(self, name="baseVariable",dataType="uint",isList=False,listSize=0,alignment=4,value=None,tagSet=[]):
		self.name = name
		self.dataType = dataType
		self.isList = isList
		self.listSize = listSize
		self.alignment = alignment
		if value == None:
			if self.isList:
				self.value = []
				for i in range(0,self.listSize):
					self.value.append(defaultValueDict[self.dataType])
			self.value = defaultValueDict[self.dataType]
		else:
			self.value = value
		self.tagSet = set(tagSet)
		
	def __get__(self, instance, owner):
		return self.value
	def __set__(self, instance, newValue):
		#TODO Add validation to setting values
		if self.isList:
			if isinstance(newValue,list):
				value = newValue
				self.listSize = len(newValue)
			else:
				print("ERROR:"+self.name +" must be assigned a list, was assigned a non list variable")
		else:
			self.value = newValue
		self.value = value
	
	
	def read(self,file):
		
		if self.isList:
			file.seek(getPaddedPos(file.tell(), 4))#Lists are always 4 byte aligned
			debugprint(self.name+ " aligned pos " + str(file.tell()))
			self.value = []
			self.listSize = read_uint(file)
			debugprint(self.name + " list size:"+str(self.listSize))
			for i in range(0,self.listSize):
				file.seek(getPaddedPos(file.tell(), self.alignment))
				self.value.append(readDataTypeDict[self.dataType](file))
				
		else:
			
			file.seek(getPaddedPos(file.tell(), self.alignment))
			debugprint(self.name+ " aligned pos " + str(file.tell()))
			self.value = readDataTypeDict[self.dataType](file)
		debugprint(self.name+ " " + str(self.value))
			
	def write(self,file):
		
		if self.isList:
			file.seek(getPaddedPos(file.tell(), 4))
			write_uint(file,len(self.value))
			
			for entry in self.value:
				file.seek(getPaddedPos(file.tell(), self.alignment))
				writeDataTypeDict[self.dataType](file,entry)
		else:
			file.seek(getPaddedPos(file.tell(), self.alignment))
			writeDataTypeDict[self.dataType](file,self.value)
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
	