res = []
while True:
	try:
		val = input()
	except EOFError:
		break
	else:
		res.append(val)
print(', '.join(res[0:][::2]))
print(', '.join(res[1:][::2]))