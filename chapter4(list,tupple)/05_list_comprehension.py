# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, range, or string), optionally filtering items with a condition.

squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(evens)


matrix = [[i*j for j in range(3)] for i in range(3)]
# Result: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
print(matrix)

