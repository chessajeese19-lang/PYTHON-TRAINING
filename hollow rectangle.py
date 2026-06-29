n=4
for i in range(1,n+1,1):
    for j in range(1,n+1):
        if(i==n or j==n or i==1 or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()