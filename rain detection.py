#size of rain drops--> 0-1 no rain
#                      1-5 light rain
#                      5-10moderate rain
#                      10> heavy rain
size_drop=int(input("enter the size of rain drop"))
if 0<=size_drop<1:
    print("no rain") 
elif 1<=size_drop<5:
    print("light rain")
elif 5<=size_drop<10:
    print("moderate rain")
else:
    print("heavy rain")