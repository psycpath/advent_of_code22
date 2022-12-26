print('\nOutput for challenge day 2\n')

with open('days/3/input.txt') as file:
    lines = file.readlines()

# To loop through lines, we can instead use an increasing index to access the lines
for i in range(0, len(lines)):
    line = lines[i]
    print(line)

# The range() functon has a third parameter, which is the step size.
# If we want to jump two lines at a time instead of 1, we can do this:
for i in range(0, len(lines), 2):
    oddLine = lines[i]
    evenLine = lines[i+1]
    print(oddLine)
    print(evenLine)
