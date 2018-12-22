# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.txt'
# input_file = file_location.open()

input_file = open("input.txt", "r")
content = input_file.read()

A, B = map(int, content.split())

input_file.close

output_file = open('output.txt', 'w')

if ((A + B - 1) % 4 != 0) or (A < 1) or (B > 1000000):
    output_file.write("0")
else:
    output_file.write(str(A + B - 1))

output_file.close