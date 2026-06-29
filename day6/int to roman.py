class conversion():
    def int_to_roman(self,num):
        roman=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        integers=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romanEqual=""
        for i in range(len(integers)):
            while num>=integers[i]:
                romanEqual+= roman[i]
                num-=integers[i]
        return(romanEqual)
num=int(input("enter the number:"))
obj=conversion()
print(obj.int_to_roman(num))

