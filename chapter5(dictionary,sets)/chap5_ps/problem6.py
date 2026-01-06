# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.


d ={}

name = input("enter friends name :")
lang = input("enter lang name:")
d.update ({name: lang})

name = input("enter friends name :")
lang = input("enter lang name:")
d.update ({name: lang})

name = input("enter friends name :")
lang = input("enter lang name:")
d.update ({name: lang})

name = input("enter friends name :")
lang = input("enter lang name:")
d.update ({name: lang})

print(d)


# by chat gpt using for loop
# Create an empty dictionary
favorite_languages = {}

# Allow 4 friends to input their names and favorite languages
for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    language = input(f"Enter {name}'s favorite programming language: ")
    favorite_languages[name] = language

# Print the dictionary
print(favorite_languages)



