n = int(input())

a = []
for i in range(n):
	a.append(list(map(int, input().split())))

for j in range(0, n):
	for k in a:
		print(k[j], sep = '', end = ' ', flush = True)
	print(end = "\n")