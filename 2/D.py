n = int(input())

for i in reversed(range(n + 1)):
	if i == 0:
		print('Пуск', '!' * n, sep = '')
	else:
		print(i, '!' * (n - i), sep = '')