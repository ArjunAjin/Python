# # same method but different implementation

# class Animal:
#     def move(self):
#         print("Animal Walks")

# class Frog(Animal):
#     def move(self):
#         print("Frog jump")

# forg = Frog()
# forg.move()



class Animal():
    def sound(self):
        print("Animal making sound")

class Cat():
    def sound(self):
        print("Meow")

class Dog():
    def sound(self):
        print("Woof")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


#*******************************************************************************
print("************************************************************************")

class Vehicle():
    def start(self):
        print("vehicle Starting")

class Car(Vehicle):
    def start(self):
        print("car starting using by key")

class Electric_bike(Vehicle):
    def  start(self):
        print("Bike starting using by the remote")

car = Car()
electric_bike = Electric_bike()

car.start()
electric_bike.start()