n = int(input())

a = []
for i in range(2):
	a.append(list(map(int, input().split())))

res = []
for i in range(n):
	res.append(str(a[0][i] + a[1][i]))
print(' '.join(res))