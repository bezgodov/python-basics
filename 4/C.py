a, b, c = map(int, input().split())

def gcd(m, n):
	if m == 0:
		return n
	if n == 0:
		return m
	if m > n:
		return gcd(m - n, n)
	else:
		return gcd(m, n - m)

print(gcd(a, b), gcd(a, c), gcd(b, c))