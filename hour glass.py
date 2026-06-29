n=int(input("enter the number of rows"))

for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*((2*i)+1))
for i in range(n):
    print(" "*(n-i)+"*"*((2*i)+1))