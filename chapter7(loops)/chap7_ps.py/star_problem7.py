'''
for n = 3
  *
 ***
*****

'''
n = int(input("enter the number : "))

for i in range (1, n+1):
    print(" "*(n-i),end="")        # this is for blank space
    print("*" * (2*i-1),end ="" )  # this will print *
    print("")                      # this is for another line
   
#    end = "" means don't switch line 
'''
for n = 5
    *
   ***
  *****
 *******
*********
'''