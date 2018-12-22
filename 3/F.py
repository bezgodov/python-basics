a = list(map(int, input().split()))

res = 0
for i in a:
	res += abs(i)

print(res)