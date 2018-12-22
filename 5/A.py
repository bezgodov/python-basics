from numpy import linalg as LA

vals = list(map(int, input().split()))
print(int(LA.norm(vals, ord = 1)))