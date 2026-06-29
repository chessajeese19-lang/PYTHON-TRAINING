#remove the articles a,an,the from the string
s="Alias went to goa to buy a packet of milk and butter"
s=s.replace("A"," ")
s=s.replace("a"," ")
s=s.replace("an"," ")
s=s.replace("AN"," ")
s=s.replace("An"," ")
s=s.replace("the"," ")
s=s.replace("The"," ")
s=s.replace("THE"," ")
print(s)


