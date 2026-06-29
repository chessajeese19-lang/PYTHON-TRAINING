#function with the same name in a  class
class demo:
    #def add(self,a):
        #print(a)
    #def add(self,a,b):
        #print(a+b)
    def add(self,*numbers):
        print(sum(numbers))
obj=demo()
obj.add(10)
obj.add(8,9,9,0)
obj=add(10,20)
