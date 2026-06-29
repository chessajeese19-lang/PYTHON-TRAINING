n = int(input("Enter the size of the wing (n): "))

# 1. Top Half of the Butterfly
for i in range(1, n + 1):
    # Left wing stars
    for j in range(1, i + 1):
        print("*", end=" ")
    
    # Middle blank spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")
        
    # Right wing stars
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 2. Bottom Half of the Butterfly
for i in range(n, 0, -1):
    # Left wing stars
    for j in range(1, i + 1):
        print("*", end=" ")
    
    # Middle blank spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")
        
    # Right wing stars
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


