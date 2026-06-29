# valid palindrome
# malayalam / race car 
#remove the blank spaces and then check whether palindrome
s=input("enter the sentence")
cleaned=""
for ch in s:
    if ch.isalnum():
       cleaned+=ch.lower()
if cleaned==cleaned[::-1]:
        print(True)
else:
        print(False)    