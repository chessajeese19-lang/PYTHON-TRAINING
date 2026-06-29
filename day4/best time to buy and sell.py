prices=[7,2,5,3,6,4]
minn=10
maxx=0
profit=0
for i in range(1,len(prices)):
    if prices[i]<minn:
        minn=prices[i]
    else:
        profit=prices[i]-minn
    if profit>maxx:
       maxx=profit
print(maxx)