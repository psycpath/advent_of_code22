print('\nOutput for challenge day 2\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

All_compartments = list()
    
    
for line in lines:
    line = line.strip()
    first_compartment =  line[slice(0,len(line)//2)]
    second_compartment =  line[slice(len(line)//2, len(line))]
    All_compartments.append(first_compartment and second_compartment)

print(All_compartments)



