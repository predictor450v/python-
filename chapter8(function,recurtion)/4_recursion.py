
# recursion ( when a function called it self in a program)

'''
factorial(n) = n * factorial(n-1)
'''

def factorial (n):
    # Base case: Define when the recursion should stop
    if(n==1 or n==0):
        return 1
        # Recursive case: n! = n * (n-1)!
    return n * factorial(n-1)

n = int(input("enter a number: "))

 # Recursive case: Call the function with modified parameters
print(f"the factorial of this number is: {factorial(n)}")
