import sys
a = list(map(int, input().split()))

a_min = sys.maxsize
a_max = -sys.maxsize
indexes = []

for index, i in enumerate(a):
	if i >= a_max:
		if i > a_max:
			del(indexes[:])
		indexes.append(index)
		a_max = i
	if i < a_min:
		a_min = i

for i in indexes:
	a[i] = a_min

print(' '.join(map(str, a)))