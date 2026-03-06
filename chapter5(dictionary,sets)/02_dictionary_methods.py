marks = {
    "ayush": 80,
    "tanisha": 100,
    "rohan": 20,
    0 : "ayushi"
}
print(marks.items())  # gives all items including keys and values in dictionary in term of tuple

print(f"the keys of disctionary are{marks.keys()}")  #gives only keys indise dictionary

print(marks.values())    #gives only value  inside dictionary

marks.update({"ayush":100 , "ghora":25})   #it's add or change key and values
print ("new dict is ", marks)


print(marks.get("ghora"))   #returns none
print (marks.get("ayush"))    # to get values
#print(marks["ayush1"])   #returns an error

print(marks.pop("rohan"))
print(len(marks))
