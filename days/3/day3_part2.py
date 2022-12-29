print('\nOutput for challenge day 2\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

intersections = list()
prioritylist = list()

for i in range(0, len(lines), 3):

    lines[i] = lines[i].strip()
    set1 = set(lines[i])

    lines[i+1] = lines[i+1].strip()
    set2 = set(lines[i+1])

    lines[i+2] = lines[i+2].strip()
    set3 = set(lines[i+2])

    all_intersections_set = set1.intersection(set2, set3)

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

#GEILE HUERSOHNNNNNN, dash eig recht isi gsi für mich chline burschtu
#han eif chli müsse überlege weisch, isch kei google notwendig gsi



