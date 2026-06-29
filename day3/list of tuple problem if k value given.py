tuple_list=eval(input("Enter the list of tuple"))
k=int(input("enter the column"))
product =1
for tup in tuple_list:
    product=product*tup[k]
    print(f"product of values:{k}:{product}")
#list=[(1,2,3),(4,5,6),(7,8,9)]
#k=1
#product=80 (product of elements in column no 1)