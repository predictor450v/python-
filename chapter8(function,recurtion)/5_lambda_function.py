# Lambda functions are anonymous, inline functions.

print("hello world")
a = 20
b = int(input("enter value of b "))
c = a+b

# Lambda function
check = lambda x: 'okay!' if x >= 50 else 'notokay!'

print(check(c))


# List of students with grades
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade using lambda
sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)
# Output: [{'name': 'Charlie', 'grade': 78}, {'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

'''
# Python discards the keys and returns only the original items
result = [student3, student1, student2]
# Which is:
# [
#     {'name': 'Charlie', 'grade': 78},
#     {'name': 'Alice', 'grade': 85},
#     {'name': 'Bob', 'grade': 92}
# ]
```

---

## **Visual Flow Diagram**
```
Input: students list
         ↓
    [Alice:85, Bob:92, Charlie:78]
         ↓
    Apply key function (lambda)
         ↓
    Extract grades: [85, 92, 78]
         ↓
    Create pairs: [(Alice,85), (Bob,92), (Charlie,78)]
         ↓
    Sort by grade: [(Charlie,78), (Alice,85), (Bob,92)]
         ↓
    Remove grades: [Charlie, Alice, Bob]
         ↓
Output: sorted list
'''
#  
