print('\nOutput for challenge day 5\n')
import re

with open('days/5/input.txt') as file:
    lines = file.readlines()[10:]

stack1 =  ["G", "W", "L", "J", "B", "R", "T", "D"]
stack2 =  ["C", "T", "Z", "R"]
stack4 =  ["V", "P", "S", "H", "C", "T", "D"]
stack5 =  ["Z", "D", "L", "T", "P", "G"]
stack6 =  ["D", "C", "Q", "J", "Z", "R", "B", "F"]
stack7 =  ["R", "T", "F", "M", "J", "D", "B", "S"]
stack8 =  ["M", "V", "T", "B", "R", "H", "L"]
stack9 =  ["V", "S", "D", "P", "Q"]

for line in lines:
    line = line.strip()
    numeric_filter = filter(str.isdigit, line)
    numeric_string = "".join(numeric_filter)


    if len(numeric_string) ==3:
        amount_of_crates = numeric_string[0]
        place_of_extraction = numeric_string[1]
        place_of_insertion = numeric_string[2]

    else:
        amount_of_crates = numeric_string[:2]
        place_of_extraction = numeric_string[2]
        place_of_insertion = numeric_string[3]

    amount_of_crates = int(amount_of_crates)
    place_of_extraction = "".join(("stack", place_of_extraction))
    place_of_insertion = "".join(("stack", place_of_insertion))

    place_of_extraction.append(S)

