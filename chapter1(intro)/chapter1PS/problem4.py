# write a python program to print the contents of a directory useing the os module, search online for the function which does that
# useing chatgpt
import os

path = "/"  # Replace with your directory path

try:
    print('\n'.join(os.listdir(path)))
except FileNotFoundError:
    print(f"Directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")
