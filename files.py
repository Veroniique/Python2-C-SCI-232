''''
Working with files. Performing open, read, write and close functions
25 April 2024
'''
#writing string to my_file.txt
def write_hello():
    with open("my_file.txt", "w") as file:
        file.write("Hello, world!")

#reading string text from my_file.txt
def read_hello():
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)

#adding numbers to numbers.txt file with a loop + new line
def write_nums():
    with open("numbers.txt", "w") as file:
        for i in range (1, 11):
            file.write(str(i) + "\n")

#calculating all numbers in numbers.txt
def calc_sum():
    total = 0
    with open("numbers.txt", "r") as file:
        for line in file:
            total += int(line.strip())
    return total

#reading guest names from guest_list.txt
def guest_list():
    with open("guest_list.txt", "r") as file:
        for line in file:
            print(line.strip())

#calling all functions
write_hello()
read_hello()
write_nums()
total_sum = calc_sum()
print("Sum of numbers: ", total_sum)
guest_list()