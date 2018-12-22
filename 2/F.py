n = int(input())

a = []
for i in range(n):
	a.append(input())
a.reverse()
print('\n'.join(a))