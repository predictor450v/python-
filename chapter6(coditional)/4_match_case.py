a=int(input("enter a number b/w 1 to 10 \n"))
match (a):
    case 5:
        print("you won")
    case 2:
        print("you won but no gift")
    case _:
        print("better luck next time")
