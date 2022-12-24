print('\nOutput for challenge day 2\n')

with open('days/2/input.txt') as file:
    lines = file.readlines()

total = list()


for line in lines:
    line = line.strip()
    if  line == "A X":
        total.append(4)
    elif line == "B X":
        total.append(1)
    elif line == "C X":
        total.append(7)
    elif line == "A Y":
        total.append(8)
    elif line == "B Y":
        total.append(5)
    elif line == "C Y":
        total.append(2)
    elif line == "A Z":
        total.append(3)
    elif line == "B Z":
        total.append(9)
    elif line == "C Z":
        total.append(6)

print(sum(total))
        

    

