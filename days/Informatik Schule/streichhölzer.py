from random import randint

x = randint(12,20)

print("Nimm Spiel")
print("")
print("Wer das letzte Streichholz nehmen muss, hat verloren!")
print("Anzahl Streichhölzer:", x)

spielzug = int(input("Wie viele Streichhölzer nehmen Sie? [1,2,3] "))
if x = 1:
    print("Spieler hat Gewonnen")
print("Anzahl Streichhölzchen: ", x - spielzug)

x -= spielzug


computerspielzug = (x-1)%4

print("Computer nimmt", computerspielzug)
x -= computerspielzug
print("Anzahl Streichhölzer:", x)
