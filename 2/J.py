a = list(map(int, input().split()))

res = []
for i in a:
	if i not in res:
		res.append(i)
print(len(res))