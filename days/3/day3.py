print('\nOutput for challenge day 3\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

intersections = list()
prioritylist = list()

for line in lines:
    line = line.strip()

    set1 = set(line[: len(line)//2])
    set2 = set(line[len(line)//2 : len(line)])

    all_intersections_set = set1.intersection(set2)

    all_intersection_list = list(all_intersections_set)
    intersection = all_intersection_list[0]
    intersections.append(intersection)

for intersection in intersections:
    if intersection.isupper():
        priority = ord(intersection) - 38
    else:
        priority = ord(intersection) - 96

    prioritylist.append(priority)

print("The answer to Day 3 part one is:", sum(prioritylist))
