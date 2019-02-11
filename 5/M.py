import numpy as np

N, M = map(int, input().split())

a = np.array(list(map(int, input().split())))
i = np.array(list(map(int, input().split())))

np.add.at(a, i - 1, 1)
print(' '.join(map(str, a)))