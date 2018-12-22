# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.txt'
# input_file = file_location.open()

input_file = open('input.txt', "r")

res = [0] * 10

n = int(input_file.readline())

for i in range(n):
	res[(int(input_file.readline()) - 1)] += 1

input_file.close

output_file = open('output.txt', 'w')

output_file.write(' '.join(map(str, res)))

output_file.close