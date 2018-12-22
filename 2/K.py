s = input()

disabled_chars = ['.', ',', '!', '?']
print(len([w for w in s.split(' ') if w not in disabled_chars]))