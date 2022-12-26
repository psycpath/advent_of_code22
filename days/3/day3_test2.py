print('\nOutput for challenge day 2\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

intersections = list()
prioritylist = list()

for line in lines:
    line = line.strip()
    first_compartment = line[slice(0,len(line)//2)]
    second_compartment = line[slice(len(line)//2, len(line))]

    set1 = set(first_compartment)
    set2 = set(second_compartment)
    # .intersection() method always returns a new set and not a single item, so name variable plural
    all_intersections = set1.intersection(set2)
    # since the exercise mentions that the intersection is a single item, we can simply take the first item of the set
    # However, in a set we can not perform indexing, so we have to convert that set into a list and then perform the indexing
    intersection = list(all_intersections)[0]
    intersections.append(intersection)

for intersection in intersections:
    # instead of previous "any(letter.isupper() for letter in intersection)" call, we can now do:
    if intersection.isupper():
        priority = ord(intersection) - 38
    else:
        priority = ord(intersection) - 96

    # the code below is not necessary, since we can simply append the priority to the list
    #result = ', '.join(str(item) for item in priority)
    #result = int(result)
    #prioritylist.append(result)

    # instead do:
    prioritylist.append(priority)

print(sum(prioritylist))
