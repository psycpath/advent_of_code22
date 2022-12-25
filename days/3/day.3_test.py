print('\nOutput for challenge day 2\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

Allintersections = list()
prioritylist = list()
    
for line in lines:
    line = line.strip()
    first_compartment =  line[slice(0,len(line)//2)]
    second_compartment =  line[slice(len(line)//2, len(line))]

    set1 = (set(first_compartment))
    set2 = (set(second_compartment))
    intersec = (set1.intersection(set2))
    Allintersections.append(intersec)

result = 0
for line in Allintersections:
    prioritylist.append(line)

print(prioritylist)