from random import randint

print("Nimm Spiel")
print("")
print("Wer das letzte Streichholz nehmen muss, hat verloren!")


x = randint(12,20)

while x != 1:

    print("Anzahl Streichhölzer:", x)
    print("")
    spielzug = int(input("Wie viele Streichhölzer nehmen Sie? [1,2,3] "))
    while spielzug >3 or spielzug <0:
        print("0-3 bitte!")
        spielzug = int(input("Wie viele Streichhölzer nehmen Sie? [1,2,3] "))

    x -= spielzug
    if x == 1:
        print("Spieler hat gewonnen")
        break

    print("Anzahl Streichhölzer:", x)
    print("")

    computerspielzug = (x-1)%4
    if (x-1)%4 == 0:
        computerspielzug = randint(1,3)

    print("Computer nimmt", computerspielzug, "Hölzchen")
    x -= computerspielzug
    if x == 1:
        print("Anzahl Streichhölzer:", x)
        print("Computer hat gewonnen")
