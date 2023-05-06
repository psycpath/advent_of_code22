x =  int(input("Alter des Hundes in Jahren [1...20]:"))

if x <= 2:
    print("Alter des Hundes ausgedrückt in Menschenjahren: ", x*10.5)
else:
    print("Alter des Hundes ausgedrückt in Menschenjahren: ", 2*10.5 + 4*(x-2))
