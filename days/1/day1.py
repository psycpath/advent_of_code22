print('\nOutput for challenge day 1\n')

with open('days/1/input_simple.txt') as file:
    lines = file.readlines()

total = 0
for line in lines:
    line = line.strip()
    if line == "":
        continue

    line = int(line)
    total = total + line
print(total)