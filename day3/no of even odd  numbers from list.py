s=list(map(int,input("enter the numbers").split()))
counte=0
counto=0
for i in range(len(s)):
    if s[i]%2==0:
         counte=counte+1
    else:
         counto=counto+1
print(counte)
print(counto)