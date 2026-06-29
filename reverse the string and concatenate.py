s=input("enter the string")
mid=len(s)//2
#name[start:end]
first_part=s[:mid]
second_part=s[mid:]
rev1=first_part[::-1]
rev2=second_part[::-1]
result=rev1+rev2
print(result)