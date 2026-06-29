#a
#ab
#abc
#abcd
n = int(input("enter the no of rows: ")) 

for i in range(1, n + 1): 
    ch = 65  # Reset the starting character to 'A' for each new row
    for j in range(1, i + 1): 
        print(chr(ch), end=" ") 
        ch = ch + 1 
    print()
