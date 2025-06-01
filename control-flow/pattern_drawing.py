# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using while loop for rows
while row < size:
    # Use for loop to print asterisks in a row
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1
