'''
Title: Handling exceptions in Python
Desc: Program that accepts user inputs and
    handles common exceptions, such as division
    by zero and invalid input
'''

#Task 1 - Using ZeroDivision
#Divides numbers, gives an error if divided by 0
def divide_nums():
    try:
        num1 = int(input("Enter a number for the first value: "))
        num2 = int(input("Enter a number for the second value: "))

        result = num1 / num2
        print(f"The result is: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

divide_nums()

#Task 2
#converts age to int, gives an error if a string is entered

def age_to_int():
    try:
        age = int(input("Enter your age: "))
        return age
    except ValueError:
        print("Error: Invalid input")

age = age_to_int()
print(f"Your age is: {age}")

#Task 3
#Opens a file, shows error if file is not there

def open_file():
    try:
        file_name = input("Enter filename: ")
        with open(file_name, "r" ) as open_file:
            file = open_file.read()
            print("The file contents are: ")
            print(file)
    except FileNotFoundError:
        print("Error: File does not exist")

open_file()
