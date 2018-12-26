import numpy as np
N, M = list(map(int, input().split()))

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

a = np.transpose(a)
print(np.dot(a[0], a[len(a) - 1]))