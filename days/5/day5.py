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
    line.replace("move ", "")
    line.replace("from", " ")
    line.replace("to", " ")
    print(line)
