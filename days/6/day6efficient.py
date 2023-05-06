print('\nOutput for challenge day 6\n')

with open('6/input.txt') as file:
    line = file.readline()

first_packet_announced = False

for i in range(len(line)):
    if len(set(line[i:i+4])) == 4 and not first_packet_announced:
        print("The first marker appears at:", i+4)
        first_packet_announced = True

    if len(set(line[i:i+14])) == 14:
        print("The second marker appears at:", i+14)
        print()
        break
