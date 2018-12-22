n, k = map(int, input().split())

a = list(map(str, input().split()))
print(' '.join(list(a[k:] + a[:k])))