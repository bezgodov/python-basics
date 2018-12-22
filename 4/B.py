a = list(map(str, input().split()))

b = {i[1]: i for i in a}

print(' '.join([b[i] for i in sorted(b)]))

# print(' '.join(sorted(a, key=lambda x: x[1])))