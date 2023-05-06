weight = int(input("Your Weight: "))
unit = input("Is that (K)g or (L)bs: ")

if unit.upper() == "K":
    print("Weight in lbs would be: ", weight*2.205)
else:
    print("Weight in Kg would be: ", weight*0.453 )

