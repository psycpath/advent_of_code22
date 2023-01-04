print('\nOutput for challenge day 5\n')
import re

with open('days/5/input.txt') as file:
    lines = file.readlines()[10:]

stacks = [
        ["G", "W", "L", "J", "B", "R", "T", "D"],
        ["C", "W", "S",],
        ["M", "T", "C", "R"],
        ["V", "P", "S", "H", "C", "T", "D"],
        ["Z", "D", "L", "T", "P", "G"],
        ["D", "C", "Q", "J", "Z", "R", "B", "F"],
        ["R", "T", "F", "M", "J", "D", "B", "S"],
        ["M", "V", "T", "B", "R", "H", "L"],
        ["V", "S", "D", "P", "Q"]
    ]

for line in lines:
    line = line.replace("move","")
    line = line.replace("from", " ")
    line = line.replace("to", " ")

    amount_of_crates = int(line[:3])
    place_of_extraction = int(line[3:7])
    place_of_insertion = int(line[7:])



    for _ in range(amount_of_crates):
        removed_element = ((stacks[place_of_extraction - 1]).pop(0))
        stacks[place_of_insertion-1].insert(0, removed_element)
