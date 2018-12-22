s = input()
n = int(input())

a = s.split(' ')
i = n - 1 if (n - 1 < len(a)) else len(a) - 1
print(a[i])