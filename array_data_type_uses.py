#This assignment is based on using numpy
import numpy as np

#create 1d array of numbers 0 - 9
num1 = np.arange(10)
print(num1)

#create a 3x3 numpy array of al true's
num2 = np.full((3, 3), True, dtype=bool)
print(num2)

#extract all odd numbers from arr
num3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8,9])
odd_nums = num3[num3 % 2 == 1]
print(odd_nums)

#replace all odd numbers in arr2 with -1
num4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8,9])
num4[num4 % 2 == 1] = -1
print(num4)

#convert 1d array to a d 2d array with 2 rows
num5 = np.arange(10)
num5_2d = num5.reshape(2, -1)
print(num5_2d)

#creating a pattern by using numpy funcs and arary input
num6 = np.array([1, 2, 3])
pattern_func = np.concatenate([np.repeat(num6, 3), np.tile(num6, 3)])
print(pattern_func)

#get common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
common_items = np.intersect1d(a,b)
print(common_items)

#from array c remove all items present in array d
c = np.array([1,2,3,4,5])
d = np.array([5,6,7,8,9])
result = np.setdiff1d(c, d)
print(result)

#get the position where elements of e and f match
e = np.array([1,2,3,2,3,4,3,4,5,6])
f = np.array([7,2,10,2,7,4,9,4,9,8])
result2 = np.where(e == f)
print(result2)

#get all items between 5 and 10 from a
g = np.array([2, 6, 1, 9, 10, 3, 27])
result3 = g[(g >= 5) & (g <= 10)]
print(result3)