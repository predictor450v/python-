# Write a program to accept marks of 6 students and display them in a sorted manner



marks = []

f1 = int(input("enter marks here :"))
marks.append(f1)
f2 = int(input("enter marks here :"))    #if we write without int it will give us string as output
marks.append(f2)
f3 = int(input("enter marks here :"))
marks.append(f3)
f4 = int(input("enter marks here :"))
marks.append(f4)
f5 = int(input("enter marks here :"))
marks.append(f5)
f6 = int(input("enter marks here :"))
marks.append(f6)

marks.sort()   # it will sort the list
print(marks)