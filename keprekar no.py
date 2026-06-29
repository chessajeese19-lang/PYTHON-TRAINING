#n=45
#n^2=2025
#split the square no 20+25 =45 hence a keprekar number
n=int(input("enter the no"))
a=n*n
digit=len(str(n))
right=a%(10**digit)
left=a//(10**digit)
if left+right==n:
    print("keprekar")
else:
    print("not keprekar")
    

