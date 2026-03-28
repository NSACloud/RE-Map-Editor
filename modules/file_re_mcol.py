#Author: NSA Cloud
from .gen_functions import textColors,raiseWarning,raiseError,getPaddingAmount,read_uint,read_int,read_uint64,read_float,read_short,read_ushort,read_ubyte,read_unicode_string,read_byte,write_uint,write_int,write_uint64,write_float,write_short,write_ushort,write_ubyte,write_unicode_string,write_byte
DEBUG_MODE = False
import os
import struct

def debugprint(string):
	if DEBUG_MODE:
		print(string)
class SIZE_DATA():
	def __init__(self):
		self.MCOL_HEADER_SIZE = 32
		self.BBOX_SIZE = 32
		self.VERTEX_SIZE = 16
		self.FACE_SIZE = 64
class MCOLHeader():
	def __init__(self):
		self.magic = 1280262989
		self.bvhmFileSize = 0
		self.string2Count = 0
		self.null2 = 0
		self.string2Offset = 0
		self.null3 = 0
		self.null4 = 0
	def read(self,file):
		self.magic = read_uint(file)
		if self.magic != 1280262989:
			raiseError("File is not an MCOL file.")
		self.bvhmFileSize = read_uint(file)
		self.string2Count = read_uint(file)
		self.null2 = read_uint(file)
		self.string2Offset = read_uint64(file)
		self.null3 = read_uint(file)
		self.null4 = read_uint(file)

	def write(self,file):
		write_uint(file,self.magic)
		write_uint(file,self.bvhmFileSize)
		write_uint(file,self.string2Count)
		write_uint(file,self.null2)
		write_uint64(file,self.string2Offset)
		write_uint(file,self.null3)
		write_uint(file,self.null4)
		
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

class BVHMHeader():
	def __init__(self):
		self.magic = 1296586306
		self.vertexCount = 0
		self.faceCount = 0
		self.null5 = 0
		self.stringCount = 0
		self.null6 = 0
		self.null7 = 0
		self.null8 = 0
		self.null9 = 0
		self.bboxSize = 0
		self.bboxOffset = 0
		self.vertexOffset = 0
		self.faceOffset = 0
		self.null11 = 0
		self.null12 = 0
		self.stringTableOffset0 = 0
		self.stringTableOffset1 = 0
		self.stringTableOffset2 = 0
		self.stringTableOffset3 = 0
		self.null13 = 0
		self.null14 = 0
		self.boxMinX1 = 0.0
		self.boxMinY1 = 0.0
		self.boxMinZ1 = 0.0
		self.null15 = 0
		self.boxMaxX1 = 0.0
		self.boxMaxY1 = 0.0
		self.boxMaxZ1 = 0.0
		self.null16 = 0
	def read(self,file):
		self.magic = read_uint(file)
		if self.magic != 1296586306:
			raiseError("File is not an MCOL file.")
		self.vertexCount = read_uint(file)
		self.faceCount = read_uint(file)
		self.null5 = read_uint(file)
		self.stringCount = read_uint(file)
		self.null6 = read_uint(file)
		self.null7 = read_uint(file)
		self.null8 = read_uint(file)
		self.null9 = read_uint(file)
		self.bboxSize = read_uint(file)
		self.bboxOffset = read_uint64(file)
		self.vertexOffset = read_uint64(file)
		self.faceOffset = read_uint64(file)
		self.null11 = read_uint(file)
		self.null12 = read_uint(file)
		self.stringTableOffset0 = read_uint64(file)
		self.stringTableOffset1 = read_uint64(file)
		self.stringTableOffset2 = read_uint64(file)
		self.stringTableOffset3 = read_uint64(file)
		self.null13 = read_uint(file)
		self.null14 = read_uint(file)
		self.boxMinX = read_float(file)
		self.boxMinY = read_float(file)
		self.boxMinZ = read_float(file)
		self.null15 = read_uint(file)
		self.boxMaxX = read_float(file)
		self.boxMaxY = read_float(file)
		self.boxMaxZ = read_float(file)
		self.null16 = read_uint(file)

	def write(self,file):
		write_uint(file,self.magic)
		write_uint(file,self.vertexCount)
		write_uint(file,self.faceCount)
		write_uint(file,self.null5)
		write_uint(file,self.stringCount)
		write_uint(file,self.null6)
		write_uint(file,self.null7)
		write_uint(file,self.null8)
		write_uint(file,self.null9)
		write_uint(file,self.bboxSize)
		write_uint64(file,self.bboxOffset)
		write_uint64(file,self.vertexOffset)
		write_uint64(file,self.faceOffset)
		write_uint(file,self.null11)
		write_uint(file,self.null12)
		write_uint64(file,self.stringTableOffset0)
		write_uint64(file,self.stringTableOffset1)
		write_uint64(file,self.stringTableOffset2)
		write_uint64(file,self.stringTableOffset3)
		write_uint(file,self.null13)
		write_uint(file,self.null14)
		write_float(file,self.boxMinX)
		write_float(file,self.boxMinY)
		write_float(file,self.boxMinZ)
		write_uint(file,self.null15)
		write_float(file,self.boxMaxX)
		write_float(file,self.boxMaxY)
		write_float(file,self.boxMaxZ)
		write_uint(file,self.null16)
		
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)
class BBoxHeader():
	def __init__(self):
		self.bboxCount = 0
		self.null17 = 0
		self.null18 = 0
		self.null19 = 0
	def read(self,file):
		self.bboxCount = read_uint(file)
		self.null17 = read_uint(file)
		self.null18 = read_uint(file)
		self.null19 = read_uint(file)
		

	def write(self,file):
		write_uint(file,self.bboxCount)
		write_uint(file,self.null17)
		write_uint(file,self.null18)
		write_uint(file,self.null19)
		
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

class Vertex():
	def __init__(self):
		self.pos = (0.0,0.0,0.0)
		self.index = 0
		
	def read(self,file):
		self.pos = (read_float(file),read_float(file),read_float(file))
		self.index = read_uint(file)
		
	def write(self,file):
		write_float(file,self.pos[0])
		write_float(file,self.pos[1])
		write_float(file,self.pos[2])
		write_uint(file,self.index)
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

class Face():
	def __init__(self):
		self.null0 = 0
		self.stringIndex = 0
		self.unknRelationIndex0 = 0
		self.null3 = 0
		self.null4 = 0
		self.null5 = 0
		self.null6 = 0
		self.null7 = 0
		self.null8 = 0
		self.null9 = 0
		self.re4_unkn = 0
		self.vertIndex0 = 0
		self.vertIndex1 = 0
		self.vertIndex2 = 0
		self.adjFaceIndex0 = 0
		self.adjFaceIndex1 = 0
		self.adjFaceIndex2 = 0

	def read(self,file,version):
		self.null0 = read_uint(file)
		self.stringIndex = read_uint(file)
		self.unknRelationIndex0 = read_int(file)
		self.null3 = read_uint(file)
		self.null4 = read_uint(file)
		self.null5 = read_uint(file)
		self.null6 = read_uint(file)
		self.null7 = read_uint(file)
		self.null8 = read_uint(file)
		self.null9 = read_uint(file)
		if version >= 20021:
			self.re4_unkn = read_uint(file)
		self.vertIndex0 = read_uint(file)
		self.vertIndex1 = read_uint(file)
		self.vertIndex2 = read_uint(file)
		self.adjFaceIndex0 = read_int(file)
		self.adjFaceIndex1 = read_int(file)
		self.adjFaceIndex2 = read_int(file)
	def write(self,file):
		write_uint(file,self.null0)
		write_uint(file,self.stringIndex)
		write_int(file,self.unknRelationIndex0)
		write_uint(file,self.null3)
		write_uint(file,self.null4)
		write_uint(file,self.null5)
		write_uint(file,self.null6)
		write_uint(file,self.null7)
		write_uint(file,self.null8)
		write_uint(file,self.null9)
		write_uint(file,self.vertIndex0)
		write_uint(file,self.vertIndex1)
		write_uint(file,self.vertIndex2)
		write_int(file,self.adjFaceIndex0)
		write_int(file,self.adjFaceIndex1)
		write_int(file,self.adjFaceIndex2)
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)
class StringTable():
	def __init__(self):
		self.stringOffsetList = []
		self.stringList1 = []
		self.stringList2 = []
	def read(self,file,stringCount,addMCOLHeaderSize = False):
		self.stringOffsetList = []
		self.stringList1 = []
		self.stringList2 = []
		
		if addMCOLHeaderSize:
			extraOffset = 32
		else:
			extraOffset = 0
			
		for i in range(0,stringCount*2):#*2 because of duplicated strings
			self.stringOffsetList.append(read_uint64(file))
		for offset in self.stringOffsetList:
			file.seek(offset+extraOffset)#32 is mcol header size
			self.stringList1.append(read_unicode_string(file))
			#self.stringList2.append(read_unicode_string(file))
	
	def write(self,file):
		for offset in self.stringOffsetList:
			write_uint64(file,offset)
		for string in self.stringList1:#TODO Write strings correctly
			write_unicode_string(file, string)
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

class BoundingBox():
	def __init__(self):
		self.x1 = 0.0
		self.y1 = 0.0
		self.z1 = 0.0
		self.index = 0
		self.unknFlag = 0
		self.flag = 0
		self.x2 = 0.0
		self.y2 = 0.0
		self.z2 = 0.0
		self.null1 = 0
		
	def read(self,file):
		self.x1 = read_float(file)
		self.y1 = read_float(file)
		self.z1 = read_float(file)
		self.index = read_ushort(file)
		self.unknFlag = read_ubyte(file)
		self.flag = read_ubyte(file)
		self.x2 = read_float(file)
		self.y2 = read_float(file)
		self.z2 = read_float(file)
		self.null1 = read_uint(file)
	
	def write(self,file):
		write_float(file,self.x1)
		write_float(file,self.y1)
		write_float(file,self.z1)
		write_ushort(file,self.index)
		write_ubyte(file,self.unknFlag)
		write_ubyte(file,self.flag)
		write_float(file,self.x2)
		write_float(file,self.y2)
		write_float(file,self.z2)
		write_uint(file,self.null1)
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)
		
class MCOLFile():
	def __init__(self):
		self.sizeData = SIZE_DATA()
		self.mcolHeader = MCOLHeader()
		self.bvhmHeader = BVHMHeader()
		self.bboxHeader = BBoxHeader()
		self.boundingBoxList = []
		self.vertexList = []
		self.faceList = []
		self.stringTable1 = StringTable()
		self.stringTable2 = StringTable()
	def read(self,file,version):
		self.mcolHeader.read(file)
		self.bvhmHeader.read(file)
		
		file.seek(self.bvhmHeader.bboxOffset + self.sizeData.MCOL_HEADER_SIZE)
		self.bboxHeader.read(file)
		for i in range(0,self.bboxHeader.bboxCount):
			bbox = BoundingBox()
			bbox.read(file)
			self.boundingBoxList.append(bbox)
		
		file.seek(self.bvhmHeader.vertexOffset + self.sizeData.MCOL_HEADER_SIZE)
		for i in range(0,self.bvhmHeader.vertexCount):
			vertex = Vertex()
			vertex.read(file)
			self.vertexList.append(vertex)
		
		file.seek(self.bvhmHeader.faceOffset + self.sizeData.MCOL_HEADER_SIZE)
		for i in range(0,self.bvhmHeader.faceCount):
			face = Face()
			face.read(file,version)
			self.faceList.append(face)
		
		file.seek(self.bvhmHeader.stringTableOffset0 + self.sizeData.MCOL_HEADER_SIZE)
		self.stringTable1.read(file,self.bvhmHeader.stringCount,addMCOLHeaderSize=True)
		
		file.seek(self.mcolHeader.string2Offset)
		self.stringTable2.read(file, self.mcolHeader.string2Count,addMCOLHeaderSize=False)
	def recalculateOffsets(self):
		self.bvhmHeader.vertexCount = len(self.vertexList)
		self.bvhmHeader.faceCount = len(self.faceList)
		self.bvhmHeader.bboxSize = len(self.boundingBoxList)*self.sizeData.BBOX_SIZE +16#+16 for bbox header
		self.mcolHeader.string2Count = len(self.stringTable2.stringList1)
		self.bvhmHeader.stringCount = len(self.stringTable1.stringList1)
		
		self.bvhmHeader.bboxOffset = 144#Always 144
		self.bboxHeader.bboxCount = len(self.boundingBoxList)
		self.bvhmHeader.vertexOffset = self.bvhmHeader.bboxOffset + self.bvhmHeader.bboxSize
		self.bvhmHeader.faceOffset = self.bvhmHeader.vertexOffset + self.bvhmHeader.vertexCount * self.sizeData.VERTEX_SIZE
		self.bvhmHeader.stringTableOffset0 = self.bvhmHeader.faceOffset + self.bvhmHeader.faceCount * self.sizeData.FACE_SIZE
		self.bvhmHeader.stringTableOffset1 = self.bvhmHeader.stringTableOffset0
		self.bvhmHeader.stringTableOffset2 = self.bvhmHeader.stringTableOffset0
		self.bvhmHeader.stringTableOffset3 = self.bvhmHeader.stringTableOffset0
		
		startOffset = self.bvhmHeader.stringTableOffset0 + ((self.bvhmHeader.stringCount * 8) * 2)# *8 because int64, *2 because capcom
		for index, string in enumerate(self.stringTable1.stringList1):
			self.stringTable1.stringOffsetList.append(startOffset)
			self.stringTable1.stringOffsetList.append(startOffset)
			startOffset += len(string)*2+2
		self.mcolHeader.bvhmFileSize = startOffset
		self.mcolHeader.string2Offset = startOffset + self.sizeData.MCOL_HEADER_SIZE + getPaddingAmount(startOffset + self.sizeData.MCOL_HEADER_SIZE, 16)
		self.stringTable2.stringOffsetList = self.stringTable1.stringOffsetList.copy()
		offsetDifference = self.mcolHeader.string2Offset - self.bvhmHeader.stringTableOffset0
		for stringIndex,stringOffset in enumerate(self.stringTable2.stringOffsetList):
			self.stringTable2.stringOffsetList[stringIndex] = stringOffset + offsetDifference
	def write(self,file):
		self.recalculateOffsets()
		self.mcolHeader.write(file)
		self.bvhmHeader.write(file)
		
		file.seek(self.bvhmHeader.bboxOffset + self.sizeData.MCOL_HEADER_SIZE)
		self.bboxHeader.write(file)
		for bbox in self.boundingBoxList:
			bbox.write(file)
		
		file.seek(self.bvhmHeader.vertexOffset + self.sizeData.MCOL_HEADER_SIZE)
		for vertex in self.vertexList:
			vertex.write(file)
		
		file.seek(self.bvhmHeader.faceOffset + self.sizeData.MCOL_HEADER_SIZE)
		for face in self.faceList:
			face.write(file)
		
		file.seek(self.bvhmHeader.stringTableOffset0 + self.sizeData.MCOL_HEADER_SIZE)
		self.stringTable1.write(file)
		
		file.seek(self.mcolHeader.string2Offset)
		self.stringTable2.write(file)
def readMCOL(filepath):
	#print(textColors.OKCYAN + "__________________________________\nMDF read started." + textColors.ENDC)
	print("Opening " + filepath)
	try:  
		file = open(filepath,"rb")
	except:
		raiseError("Failed to open " + filepath)
	mcolVersion = int(os.path.splitext(filepath)[1].replace(".",""))
	mcolFile = MCOLFile()
	mcolFile.read(file,mcolVersion)
	file.close()
	#print(textColors.OKGREEN + "__________________________________\nMDF read finished." + textColors.ENDC)
	return mcolFile

def writeMCOL(mcolFile,filepath):
	#print(textColors.OKCYAN + "__________________________________\nMDF write started." + textColors.ENDC)
	print("Opening " + filepath)
	try:
		file = open(filepath,"wb")
	except:
		raiseError("Failed to open " + filepath)
	
	mcolFile.write(file)
	file.close()
	#print(textColors.OKGREEN + "__________________________________\nMDF write finished." + textColors.ENDC)
