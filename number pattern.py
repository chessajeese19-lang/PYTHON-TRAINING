n=int(input("enter the no of rows"))
m=int(input("enter the no of columns"))
num=1
for i in range(1,n+1,1):
    for j in range(1,m+1,1):
        if(i>=j):
            print(num,end=" ")
            num=num+1
        else:
            print(" ",end=" ")
    print()