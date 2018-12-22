import re
# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.txt'
# input_file = file_location.open()

input_file = open('d.in', "r")

content = input_file.readline().replace('-', '')
disabled_chars = ['\n', '.', ',', '!', '?']

for char in disabled_chars:
	content = content.replace(char, ' ')

input_file.close

output_file = open('d.out', 'w')
output_file.write(
# print(
	str(
		len(
			[
				w for w in content.split(' ')
					if ((w not in disabled_chars) and (re.match('^[A-Za-z-]*$', w)) and (len(w) > 0))
			]
		)
	)
)
output_file.close