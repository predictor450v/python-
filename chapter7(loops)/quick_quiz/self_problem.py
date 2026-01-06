#  show a list by user input 

# creaing blank list
list = []

# takeing how many inputs we want
n = int(input("number of input: "))

# use input number as range

for i in range (n):
    number= input(f"enter number {i+1}: ")    
    list.append(number)             # to add user input in list

# display the list
print ("list is",list)



