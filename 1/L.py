# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.txt'
# input_file = file_location.open()

input_file=open("input.txt", "r")

H_out, M_out = map(int, input_file.readline().split())
H_way, M_way = map(int, input_file.readline().split())

input_file.close

output_file = open('output.txt', 'w')

hours = (H_out + H_way) % 24
minutes = (M_out + M_way) % 60

hours += int((M_out + M_way) / 60)

output_file.write(str(hours % 24) + " " + str(minutes))
output_file.close