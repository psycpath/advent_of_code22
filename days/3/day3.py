print('\nOutput for challenge day 2\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

intersections = list()
prioritylist = list()

for line in lines:
    line = line.strip()
    first_compartment = line[:len(line)//2]
    second_compartment = line[len(line)//2 : len(line)]

    set1 = set(first_compartment)
    set2 = set(second_compartment)

    all_intersections = set1.intersection(set2)

    intersection = list(all_intersections)[0]
    intersections.append(intersection)

for intersection in intersections:
    if intersection.isupper():
        priority = ord(intersection) - 38
    else:
        priority = ord(intersection) - 96

    prioritylist.append(priority)

print(sum(prioritylist))
