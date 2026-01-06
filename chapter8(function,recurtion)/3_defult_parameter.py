# we are giveing a default value for a parameter 

def goodDay(name,ending="thank you"):
    print(f"good day,{name}")
    print(ending)

goodDay(input("enter your name :"))
goodDay(input("enter your name :"),"thanks")
