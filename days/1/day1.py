print('\nOutput for challenge day 1\n')

with open('days/1/input.txt') as file:
    lines = file.readlines()

lines.append('\n')

total = 0
total_sums = list()

# TO ADD TO A LIST: total_sums.append(VALUE)
for line in lines:
    line = line.strip()
    if line == "":
        total_sums.append(total)
        total = 0
        continue

    line = int(line)
    total = total + line
    print(line)

total_sums.sort()
total_sums.reverse()

top_3 = total_sums[0] + total_sums[1] + total_sums[2]

print("Largest element is:", total_sums[0])
print("The top three elves are carrying a total of", top_3)
