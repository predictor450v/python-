file = open("my_file.txt", "r")
for line in file: # Efficient for large files
    print(line.strip()) # Remove newline characters
file.close()