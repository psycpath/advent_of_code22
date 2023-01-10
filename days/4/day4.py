print('\nOutput for challenge day 4\n')

with open('days/4/input.txt') as file:
    lines = file.readlines()

total = list()
totalintersections = list()

for line in lines:

#Getting the numbers from the range as integers
    line = line.strip()
    pair = line.split(",")

    first_range = pair[0]
    second_range = pair[1]
    first_range = first_range.split("-")
    second_range = second_range.split("-")

    range1_start = int(first_range [0])
    range1_end = int(first_range [1])
    range2_start = int(second_range [0])
    range2_end = int(second_range [1])

    set1 = set()
    set2 = set()

#Creates and adds the whole range to set1 and set2
    for numbers in range(range1_start, range1_end + 1):
        set1.add(numbers)
    for numbers in range(range2_start, range2_end + 1):
        set2.add(numbers)

    if set1.issubset(set2):
        total.append(1)
    elif set2.issubset(set1):
        total.append(1)

    #Part 2--
    if set1.intersection(set2) != set():
        totalintersections.append(1)

print("The Amount of fully contained sets is:", (sum(total)))
print("The amount of sets with intersections is:",sum(totalintersections))
print()
