# Loop through 6 rows
for row in range(6):
    # Loop through 7 columns
    for col in range(7):
        # Apply mathematical conditions to form boundaries
        if (row == 0 and col % 3 != 0) or \
           (row == 1 and col % 3 == 0) or \
           (row - col == 2) or \
           (row + col == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # Move to the next line after completing a row
    print()
