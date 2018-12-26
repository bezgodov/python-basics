N, M, I, J = map(int, input().split())

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

a[I], a[J] = a[J], a[I]

for row in a:
    print(' '.join(map(str, row)))