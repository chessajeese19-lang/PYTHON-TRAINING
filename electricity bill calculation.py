# first 100 units-->1.50/units
# above 100 units-->2.50/units
# above 200 units-->4/units
# calculate the bill
N=(int(input("enter the no of units consumed")))
if N>0 and N<=100:
    a1=N*1.50
elif N>100 and N<=200:
    a1=(100*1.5)+((N-100)*2.50)
else:
    a1=(100*1.5)+(100*2.5)+((N-200)*4)
print(a1)


