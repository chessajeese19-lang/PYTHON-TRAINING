#two wheeler vehicles=130
#four wheeler vehicles=70
V=int(input("enter the no of vehicles"))
W=int(input("enter the no of wheels"))
four_wheelers=(W-2*V)//2
two_wheelers=V-four_wheelers
if W%2!=0 or two_wheelers<0 or four_wheelers<0:
    print("invalid")
else:
    print("No of four_wheelers=",four_wheelers)
    print("No of two_wheelers=",two_wheelers)
 



