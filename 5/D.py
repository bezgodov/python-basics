from numpy import linalg as LA

vals = list(map(float, input().split()))
print(float(LA.norm(vals, ord = 2)))