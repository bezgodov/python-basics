import numpy as np

S, d, N = list(map(float, input().split()))

print(' '.join(map(str, np.linspace(S, S + d * (N - 1), N))))