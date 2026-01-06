# check input number is a prime or not

n = int(input("ENTER A NUMBER: "))

for i in range(2,n):
    if(n%i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")

# prime number is which can not get devided by any other number expect itself or 1

        