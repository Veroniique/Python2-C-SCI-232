'''
This program calculates the sum of a list of
integers using recursion. A test function
will verify the recursive implementation works.
If nothing is in the list, it will return 0.
'''

#gets sum of list of integers
def recursive_sum(list):
    if not list:
        return 0
    else:
        return list[0] + recursive_sum(list[1:])

num_list = [3, 5, 8, 10, 15]
print(recursive_sum(num_list))