a = list(map(int, input().split()))

a_copy = a.copy()
shift = 0
for index, el in enumerate(a):
	if el == 0:
		if index - 1 >= 0:
			del a_copy[index - 1 - shift]
			shift += 1

print(' '.join(map(str, a_copy)))