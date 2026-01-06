friends = ["apple","orange",5,345.06, False,"aakash", "rohan" ]
print(friends)
# output  ["apple","orange",5,345.06, False,"aakash", "rohan" ]

friends.append("ayush")   #append = at the end plus
print(friends)
# output  ["apple","orange",5,345.06, False,"aakash", "rohan", "ayush"]

l1 = [1,2,34,5,66,34]

l1.sort()      # for sorting 
print (l1)
# output [1, 2, 5, 34, 34, 66]

l1.reverse()   # for reverse 
print(l1)
# output [66, 34, 34, 5, 2, 1]

l1.insert(3,3333)   # insert in list (index,datatype)
print(l1)
# output  [66, 34, 34, 3333, 5, 2, 1]

l1.pop(2)      # for remove anything from index
print(l1)
# output  [66, 34, 3333, 5, 2, 1]

l1.remove(66)     #remove anty data form list 
print(l1)
# output [34, 3333, 5, 2, 1]