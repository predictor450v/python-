# how to know type of variable 

a = 31
t = type(a)
print (t)
#output class int

b = 5.67
t = type(b)
print(t)
# output class float

c ="ayush"
t =type(c)
print(t)
# output will be class str means string 

d= "32.3"
t = type(d)
print(t)
# output class str

# now how to convert 32.3 str to float 
f= "32.3"
g = float(f)  # f but the type should be float 
t = type(g)
print (t)
#output class float 

# so we use type function to know type of variable
# and with str float int we can do convertion if the convertion is valid 