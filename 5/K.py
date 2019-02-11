import numpy as np

N = int(input())

a1 = np.array(list(map(int, input().split())))
a2 = np.array(list(map(int, input().split())))

print(' '.join(map(str, np.add(a1, a2))))
