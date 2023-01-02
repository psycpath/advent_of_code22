print('\nOutput for challenge day 5\n')
import re

with open('days/5/input.txt') as file:
    lines = file.readlines()[10:]

stacks = [
        ["G", "W", "L", "J", "B", "R", "T", "D"],
        ["C", "T", "Z", "R"],
        ["V", "P", "S", "H", "C", "T", "D"],
        ["Z", "D", "L", "T", "P", "G"],
        ["D", "C", "Q", "J", "Z", "R", "B", "F"],
        ["R", "T", "F", "M", "J", "D", "B", "S"],
        ["M", "V", "T", "B", "R", "H", "L"],
        ["V", "S", "D", "P", "Q"]
    ]

for line in lines:
    line = line.strip()
    numeric_filter = filter(str.isdigit, line)
    numeric_string = "".join(numeric_filter)
    line.replace("move ", "")

    if len(numeric_string) == 3:
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

    place_of_extractionv = vars(place_of_extraction)
    place_of_insertion = vars(place_of_insertion)

    place_of_extraction.append(S)

