import numpy as np

N = int(input())

mtx = []

for _ in range(N):
    mtx.append(list(map(int, input().split())))

for row in np.transpose(mtx):
    print(' '.join(map(str, row)))
