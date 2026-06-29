n=input()
p=1
for i in range(len(n)):
   ld=int(n[i])%10
   p=p*ld
   n=int(n[i])//10
   len(n)==len(n)-1
print(p)



