products=input("enter the list of product IDs:").split()
all_IDs=set(products)
duplicates=set()
#find duplicates
for id in products:
    if products.count(id)>1:
        duplicates.add(id)
lost_IDs=all_IDs-duplicates
print("lost product IDs:",lost_IDs)
