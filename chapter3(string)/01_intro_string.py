name ="ayush"

name ='''ayush
               man'''

name = 'ayush'

print (name)

#string is a datatype of python
# string is a sequence of charater enclosed in quotes



# indexing in string 

nameshort = len(name)   #used for to know lenght of string
print(nameshort)




# string slicing


# a string in python can be sliced for getting a part of the string


nameshort = name[0:3]   
print(nameshort)
print(name[-4:-1])     # convert negative index to positive index ***** 
print(name[1:4])



character1 = name[1]
print("character1 is =" , character1)

#name[ind_start : ind_end] 
#start form index 0 all the way till 3 (excluding3)


# you can move entire line using alt + arrow

# clockwise counting starts form 0 and anticlock from -1 

# string is an immutable , we cann't change a exixting string.*** 

print(name[:4])    # it is same as print(name[0:4])
#if the first end is blank it means it is 0 

print(name[2:])   # its same as print(name[2:5])
#if nothing written in end then write it's length 




# skip value 

word = "amazine"
print(word[1 : 6 : 2])
# output will be "mzn" . 2 is skip value 