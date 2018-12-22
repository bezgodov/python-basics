n, m = map(int, input().split())

a = list(map(int, input().split()))
indexes = list(map(int, input().split()))

for i in indexes:
	a[i - 1] += 1

print(' '.join(map(str,a)))