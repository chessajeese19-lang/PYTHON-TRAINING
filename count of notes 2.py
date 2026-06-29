n=int(input("enter the amount"))
sum=0;
a=[500,100,50,20,10,5,2,1];
for i in a:
    c=n//i;
    n=n%i;
    sum=sum+c;
    i=i+1;
print(sum)