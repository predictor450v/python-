import random

# Define the set of numbers
numbers = [-1, 0, 1]

# Generate a random number
#random_number = random.choice(numbers)

##computer = -1 #(fixed value for computer so we need to generate random number ranger (-1,1))

computer = random.choice(numbers)
print("write _s_ for snake ,_w_ for water and _g_ for gun")
youstr = input("enter your choice: ")
youDict = {"s":1,"w": -1, "g":0}
reverseDict = {1 : "snake",-1:"water",0:"gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")



if (computer == you):
    print("tie")
else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("you lose")
    else: 
        print ("you win")


""" if (computer == -1 and you == 1):
        print("you win")
    elif (computer ==-1 and you == 0):
        print("you lose")
    elif(computer == 1 and you ==-1):
        print("you lose")
    elif(computer ==1 and you ==0):
        print("you lose")
    elif(computer ==0 and you == -1):
        print("you lose")
    elif(computer ==0 and you ==1):
        print("you win")
    else:
        print("wrong")
        """

   



