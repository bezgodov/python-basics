# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.txt'
# input_file = file_location.open()

input_file = open("input.txt", "r")

D, T = map(float, input_file.readline().split())
v = tuple(map(float, input_file.readline().split()))
w = tuple(map(float, input_file.readline().split()))

p = 0
for i in range(len(v)):
    for j in range(len(w)):
        if v[i] != w[j]:
            cur_p = (D - w[j] * T) / (v[i] - w[j]) * v[i]
            if cur_p > p and cur_p <= D:
                p = cur_p

input_file.close

output_file = open('output.txt', 'w')
output_file.write(str(float(p)))
output_file.close