# write factorial of given number
# 5! = 1x 2 x 3 x 4 x 5

n  = int(input("enter your number "))

product = 1
for i in range ( 1, n+1):    # cause range goes n-1 and we need full range
    product = product * i

print(f"the factorial of {n} is {product}")
