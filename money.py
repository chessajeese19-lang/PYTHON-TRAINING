ticket=int(input("enter the no of tickets"))
price=int(input("enter the price of a ticket"))
amount=price*ticket
print("amount=",amount)
category=int(input("enter the category"))
if ticket>=15 and category==1:
    print("normal discount and student discount applicable")
    discount=(amount)*25/100;
elif ticket<15 and category!=1:
    print("No discount")
elif ticket==15 and category==2:
    print("normal discount applicable")
    discount=(amount)*20/100;
else:
    print("student discount applicable")
    discount=(amount)*5/100;
print(discount)
 