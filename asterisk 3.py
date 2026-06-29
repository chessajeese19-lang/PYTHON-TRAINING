n=int(input("enter the no of rows"))
m=int(input("enter the no of columns"))
for i in range(n,0,-1):
    for j in range(m,0,-1):
        if(i>=j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()