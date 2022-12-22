print('\nOutput for challenge day 1\n')

with open('days/1/input.txt') as file:
    lines = file.readlines()

print(lines[0])

for line in lines:
    if line.strip() != "":
        print(line)