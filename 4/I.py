def Join(array, separator = ' '):
	res = ''
	for i in array:
		res += i + separator
	return res[:-len(separator)]