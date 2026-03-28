




def hashToString(hash,game = "MHRise"):
	if game == "MHRise":
		from .re_rsz_lookup_mhrise import hashToStringMHRise,stringToHashMHRise,hashToCRCMHRise,getRSZInstanceMHRise
		result = hashToStringMHRise(hash)
	elif game == "RE2RT":
		from .re_rsz_lookup_re2rt import hashToStringRE2RT,stringToHashRE2RT,hashToCRCRE2RT,getRSZInstanceRE2RT
		result = hashToStringRE2RT(hash)
	elif game == "RE4":
		from .re_rsz_lookup_re4 import hashToStringRE4,stringToHashRE4,hashToCRCRE4,getRSZInstanceRE4
		result = hashToStringRE4(hash)
	elif game == "DR":
		from .re_rsz_lookup_dr import hashToStringDR,stringToHashDR,hashToCRCDR,getRSZInstanceDR
		result = hashToStringDR(hash)
	elif game == "MHWILDS":
		from .re_rsz_lookup_mhwilds import hashToStringMHWILDS,stringToHashMHWILDS,hashToCRCMHWILDS,getRSZInstanceMHWILDS
		result = hashToStringMHWILDS(hash)
	return result

def stringToHash(string,game = "MHRise"):
	if game == "MHRise":
		from .re_rsz_lookup_mhrise import hashToStringMHRise,stringToHashMHRise,hashToCRCMHRise,getRSZInstanceMHRise
		result = stringToHashMHRise(string)
	elif game == "RE2RT":
		from .re_rsz_lookup_re2rt import hashToStringRE2RT,stringToHashRE2RT,hashToCRCRE2RT,getRSZInstanceRE2RT
		result = stringToHashRE2RT(string)
	elif game == "RE4":
		from .re_rsz_lookup_re4 import hashToStringRE4,stringToHashRE4,hashToCRCRE4,getRSZInstanceRE4
		result = stringToHashRE4(string)
	elif game == "DR":
		from .re_rsz_lookup_dr import hashToStringDR,stringToHashDR,hashToCRCDR,getRSZInstanceDR
		result = stringToHashDR(string)
	elif game == "MHWILDS":
		from .re_rsz_lookup_mhwilds import hashToStringMHWILDS,stringToHashMHWILDS,hashToCRCMHWILDS,getRSZInstanceMHWILDS
		result = stringToHashMHWILDS(string)
	return result

def hashToCRC(hash,game = "MHRise"):
	if game == "MHRise":
		from .re_rsz_lookup_mhrise import hashToStringMHRise,stringToHashMHRise,hashToCRCMHRise,getRSZInstanceMHRise
		result = hashToCRCMHRise(hash)
	elif game == "RE2RT":
		from .re_rsz_lookup_re2rt import hashToStringRE2RT,stringToHashRE2RT,hashToCRCRE2RT,getRSZInstanceRE2RT
		result = hashToCRCRE2RT(hash)
	elif game == "RE4":
		from .re_rsz_lookup_re4 import hashToStringRE4,stringToHashRE4,hashToCRCRE4,getRSZInstanceRE4
		result = hashToCRCRE4(hash)
	elif game == "DR":
		from .re_rsz_lookup_dr import hashToStringDR,stringToHashDR,hashToCRCDR,getRSZInstanceDR
		result = hashToCRCDR(hash)
	elif game == "MHWILDS":
		from .re_rsz_lookup_mhwilds import hashToStringMHWILDS,stringToHashMHWILDS,hashToCRCMHWILDS,getRSZInstanceMHWILDS
		result = hashToCRCMHWILDS(hash)
	return result

def getRSZInstance(hash,game = "MHRise"):
	if game == "MHRise":
		from .re_rsz_lookup_mhrise import hashToStringMHRise,stringToHashMHRise,hashToCRCMHRise,getRSZInstanceMHRise
		result = getRSZInstanceMHRise(hash)
	elif game == "RE2RT":
		from .re_rsz_lookup_re2rt import hashToStringRE2RT,stringToHashRE2RT,hashToCRCRE2RT,getRSZInstanceRE2RT
		result = getRSZInstanceRE2RT(hash)
	elif game == "RE4":
		from .re_rsz_lookup_re4 import hashToStringRE4,stringToHashRE4,hashToCRCRE4,getRSZInstanceRE4
		result = getRSZInstanceRE4(hash)
	elif game == "DR":
		from .re_rsz_lookup_dr import hashToStringDR,stringToHashDR,hashToCRCDR,getRSZInstanceDR
		result = getRSZInstanceDR(hash)
	elif game == "MHWILDS":
		from .re_rsz_lookup_mhwilds import hashToStringMHWILDS,stringToHashMHWILDS,hashToCRCMHWILDS,getRSZInstanceMHWILDS
		result = getRSZInstanceMHWILDS(hash)
	return result
