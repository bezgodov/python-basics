import numpy as np

p = int(input())
a = list(map(int, input().split()))
n, m = list(map(int, input().split()))

a = np.reshape(a, (n, m))

for line in a:
    print(' '.join(map(str, line)))