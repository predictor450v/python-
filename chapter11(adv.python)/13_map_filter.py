numbers = [1 ,2,3 ,45,54,21,4]
def squre(x):
    return x*x

new =list(map(squre,numbers))
print(new)

def is_grater_that_9(x):
    if x>9:
        return True
    else:
        return False
    
a = [1,23,12,44,54,6,53,32,12]
new = list(filter(is_grater_that_9,a))
print(new)