'''
Title: Understanding modules
Desc: Importing modules, using functions and printing results
April 15
'''
#importing modules
import math
import my_module
import datetime

#circumference of circle
def calc_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = 5
circle = calc_circle(radius)
print(f"Circumference of circle with radius of 5: {round(circle)}")

#printing results from my_module
def var_results(my_var):
    print(f"Results are: {my_module.my_var}")
var_results(my_module.my_var)

#printing datetime from module
def print_datetime():
    today_date = datetime.datetime.now()
    print(f"Today's date and time is: {today_date}")
print_datetime()