print('\nOutput for challenge day 6\n')

with open('days/6/input.txt') as file:
    lines = file.readlines()

first_packet_announced = False

for char in lines:

    for i in range(0, len(char)):

        packet = str()
        packet2 = str()


        for n in range(0, 14):
            packet2 += char[i+n]
            if n <= 4:
                packet += (char[i+n])


        if not first_packet_announced and len(set(packet)) == len(packet):
            print("The first marker appears at:", char.index(packet) + 4)
            first_packet_announced = True

        if len(set(packet2)) == len(packet2):
            print("The second marker appears at:", char.index(packet2) + 14)
            break
