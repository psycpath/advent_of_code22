print('\nOutput for challenge day 2\n')

with open('days/6/input.txt') as file:
    lines = file.readlines()


for char in lines:

    for i in range(0, 4095):

        packet = str()

        for n in range(0, 14):
            packet += (char[i+n])

        if len(set(packet)) == len(packet):
            print("The first marker appears at:", char.index(packet) + 14)
            break
