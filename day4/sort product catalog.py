N=eval(input("enter"))
sortby=input("enter sort")
def price(item):
    return item[1]
def alphabet(item):
    return item[0]
if sortby=="price":
    N1=sorted(N,key=price)
elif sortby=="alphabet":
    N1=sorted(N,key=alphabet)
print(N1)
#sorting by key sorted()
#sorting by value item()