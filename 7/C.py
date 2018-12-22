import re
# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.txt'
# input_file = file_location.open()

input_file = open("input.txt", "r")

n = int(input_file.readline())
values = dict()

for _ in range(n):
    val = input_file.readline()
    group, student = re.split(r'\t+', val.rstrip('\n'))
    
    if group not in values:
        values[group] = []
    
    values[group].append(student)

input_file.close

output_file = open('output.txt', 'w')

for key in sorted(values):
    output_file.write(key + '\n')
    for student in sorted(values[key]):
        output_file.write(student + '\n')

output_file.close