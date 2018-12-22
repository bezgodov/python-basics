import math
a = list(map(float, input().split()))

res = 0.0
for i in a:
	res += pow(i, 2)

print(math.sqrt(res))