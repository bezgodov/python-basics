def PrintMatrix(mat):
	for i in mat:
		for index, j in enumerate(i):
			if index != len(i) - 1:
				print(j, sep = '', end = " ")
			else:
				print(j, sep = '', end = "\n")
