class dog:
    def sound(self):
        print("bow bow")
    def eat(self):
        print("dog is eating")
class cat(dog):
    def sound(self):
        print("meow meow")
d=cat()
d.eat()
d.sound()