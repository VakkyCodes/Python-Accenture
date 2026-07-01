class oop:
    pass #in python we like indendatation so we cant leave blank space
c1=oop();

#constructor
class oop1:
    def __init__(self,name):
        self.name=name
c1=oop1("vakky")
print(c1.name)

#function inside class
class oop2:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def getname(self):
        print("the name of car is ",self.name," and the color is ",self.color)
c1=oop2("vakky","red")
c1.getname()

#this was all about the classes now we can talk about the 4 pillars
      #INHERITANCE
class animal:
    def __init__(self,name):
        self.name=name
    def print(self):
        print(self.name)
class dog(animal):
    def bark(self):
        print(self.name,"is barking")

d=dog("dog");
d.bark();
d.print()
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # calls Animal's __init__
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)   # Output: Buddy Labrador

     #ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # double underscore = private

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # Output: 1500

# print(account.__balance)   ❌ This would give an error — it's privatE


       #POLYMORPHISM
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

class Cow:
    def speak(self):
        print("Moo")

animals = [Cat(), Dog(), Cow()]

for animal in animals:
    animal.speak()

# Output:
# Meow
# Woof
# Moo


   #ABSTRACTION
from abc import ABC, abstractmethod

class Shape(ABC):              # Abstract class
    @abstractmethod
    def area(self):             # Abstract method — no implementation here
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):              # Must implement this
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

c = Circle(5)
s = Square(4)
print(c.area())   # Output: 78.5
print(s.area())   # Output: 16

class Counter:
    count = 0   # class attribute

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):           # cls refers to the class itself
        return cls.count

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.get_count())   # Output: 3