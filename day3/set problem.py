#if duplicate numbers present then print false or else true
numbers=list(map(int,input("enter the number:").split()))
if len(numbers)==len(set(numbers)):
    print(False)
else:
    print(True)

#length of list is compared with length of set
#duplicates can be there in list but not in set
#number="1 2 1 2 3"
#mapped to integers  in list[ 1 2 1 2 3] 
#set [1,2,3]
#5!=3 so false

