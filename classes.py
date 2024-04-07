'''
Assignment: Classes
Creating class 'person' with
attributes and methods.
'''

#creating a class
class Person:
    #defining attributes and methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #string printer with name
    def string_print(self):
        print(f"Hello, my name is {self.name}")

#instance with person details
person1 = Person("Nik", 25)
person2 = Person("Taylor", 28)
person3 = Person("Simon", 32)

#calling string_print method on all instances
person1.string_print()
person2.string_print()
person3.string_print()



