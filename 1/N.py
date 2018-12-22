from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

# input_file=open("input.txt", "r")

A, B, t = map(int, input_file.readline().split())

input_file.close

side = [
    "S",
    "E",
    "N",
    "W",
]

koef = (t % ((A + B) * 2))

i = 0
summ = 0
while summ <= koef:
    if i % 2 == 0:
        summ += A
    else:
        summ += B
    i += 1

print(side[(i - 1) % len(side)])
output_file = open('output.txt', 'w')
output_file.write(side[(i - 1) % len(side)])
output_file.close