def print_ayushman():
    # Define letter patterns as 2D binary arrays (1 = star, 0 = space)
    letters = {
        'A': [
            [0,0,1,0,0],
            [0,1,0,1,0],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ],
        'Y': [
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
        ],
        'U': [
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]
        ],
        'S': [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]
        ],
        'H': [
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ],
        'M': [
            [1,0,0,0,1],
            [1,1,0,1,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ],
        'N': [
            [1,0,0,0,1],
            [1,1,0,0,1],
            [1,0,1,0,1],
            [1,0,0,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ]
    }
    
    name = "AYUSHMAN"
    
    # Loop through each row (7 rows for letter height)
    for row in range(7):
        # Loop through each letter in the name
        for letter in name:
            # Get the pattern for this letter
            pattern = letters[letter]
            
            # Loop through each column in the current row
            for col in range(5):
                if pattern[row][col] == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            
            # Add space between letters
            print("  ", end="")
        
        # Move to next line after completing a row
        print()

# Print the pattern
print_ayushman()