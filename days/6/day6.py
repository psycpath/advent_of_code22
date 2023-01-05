print('\nOutput for challenge day 2\n')

with open('days/6/input.txt') as file:
    lines = file.readlines()


for char in lines:

    for i in range(0, 4095):

        packet = str()

        packet += (char[i])
        packet += (char[i+1])
        packet += (char[i+2])
        packet += (char[i+3])

        if len(set(packet)) == len(packet):
            print("The first marker appears at:", char.index(packet)+4)
            break