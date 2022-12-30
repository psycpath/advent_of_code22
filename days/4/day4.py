print('\nOutput for challenge day 2\n')

with open('days/4/input.txt') as file:
    lines = file.readlines()

total = list()
totalintersections = list()

for line in lines:
    line = line.strip()
    set1 = line.split(",")

    first_part = set1[0]
    second_part = set1[1]
    first_part = first_part.split("-")
    second_part = second_part.split("-")

    first_part_firstnum = int(first_part [0])
    first_part_secondnum = int(first_part [1])
    second_part_firstnum = int(second_part [0])
    second_part_secondnum = int(second_part [1])

    list1 = list()
    list2 = list()

    for numbers in range(first_part_firstnum, first_part_secondnum + 1):
        list1.append(numbers)

    for numbers in range(second_part_firstnum, second_part_secondnum + 1):
        list2.append(numbers)

    set1 = set(list1)
    set2 = set(list2)

    if set1.issubset(set2):
        total.append(1)

    elif set2.issubset(set1):
        total.append(1)

    if set1.intersection(set2) != set():
        totalintersections.append(1)

print("The Amount of fully contained sets is:", (sum(total)))
print("The amount of sets with intersections is:",sum(totalintersections))
print()
