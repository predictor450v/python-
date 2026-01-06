name ="ayush"
print(len(name))        #it will give length of string 

print(name.endswith("ush"))   # it will give end letters of string in case of "true" and "flase"

print(name.startswith("ayu")) # it will give start letter of string in case of true or flase

print(name.capitalize())   # it will capital the first letter in string

print(name)   # it will print the original string

x = "ayushman is very good boy"
replaced_string = x.replace("good","bad")   # for replace and string 
print(replaced_string)

"hello".upper()  # Output: 'HELLO'

"HELLO".lower()  # Output: 'hello'

"hello world".title()  # Output: 'Hello World'

"  hello  ".strip()  # Output: 'hello'   Removes leading and trailing spaces or specified characters.

"hello world".split()  # Output: ['hello', 'world']

"-".join(['hello', 'world'])  # Output: 'hello-world'

"hello".find("l")  # Output: 2       Returns the lowest index where the substring is found, or -1 if not found.

"hello".count("l")  # Output: 2     Returns the number of non-overlapping occurrences of a substring.

"123".isdigit()  # Output: True     Checks if all characters in the string are digits.

"hello".isalpha()  # Output: True   Checks if all characters in the string are alphabetic.

