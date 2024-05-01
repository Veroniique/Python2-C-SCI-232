'''
29 April 2024
Creating a base class with 2 subclasses.
Learning how attributes and methods work
from classes
'''

#base class - Animal
class Animal:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def speak(self):
        print("I am an animal")

#Dog subclass
class Dog(Animal):
   def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

   def speak(self):
        print("Woof!")

#Cat subclass
class Cat(Animal):
   def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

   def speak(self):
       print("Meow!")

#Creating instance of Dog and Cat
dog_inst = Dog("Annabeth", 3, "Rhodesian Ridgeback")
cat_inst = Cat("Clawdia", 2, "Grey")

print(f"Dog's Name: ", dog_inst.name)
print(f"Dog's Age: ", dog_inst.age)
print(f"Dog's Breed: ", dog_inst.breed)
dog_inst.speak()

#Create empty line
print()

print(f"Cat's Name: ", cat_inst.name)
print(f"Cat's Age: ", cat_inst.age)
print(f"Cat's Color: ", cat_inst.color)
cat_inst.speak()

