s = input().lower().replace(' ', '')

reversed_s = s[::-1]

if s == reversed_s:
	print('True')
else:
	print('False')