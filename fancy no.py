#1234 increasing fancy no
#4321 decreasing fancy no
#1567 not a fancy no
n=input()
increasing=True
decreasing=True
for i in range(len(n)-1):
    #is increasing
    if int(n[i+1])!=int(n[i])+1:
        increasing=False
    if int(n[i+1])!=int(n[i])-1 :
        decreasing=False
if increasing:
    print(" increasing fancy no")
elif decreasing:
    print(" increasing fancy no")
else:
    print(" not a fancy number")

    
