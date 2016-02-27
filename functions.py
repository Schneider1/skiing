def remove_voc(instring):
	outstring = ""
	for s in instring:
		if not s in ("a","e","i","o","u"):
			outstring += s
	return outstring