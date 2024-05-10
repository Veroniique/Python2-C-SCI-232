"""
Fibonacci sequence creator. Add the
number of calculations you want.
"""
def fibonacci(v1, v2, run_cnt):
    print(f'{v1} + {v2} = {v1+v2}')

    if run_cnt <= 1:  # Base case:
                      # Ran for user's number of steps
        pass  # Do nothing
    else:             # Recursive case
        fibonacci(v2, v1+v2, run_cnt-1)

print ('This program outputs the\n'
       'Fibonacci sequence step-by-step,\n'
       'starting after the first 0 and 1.\n')

run_for = int(input('How many steps would you like? '))

fibonacci(0, 1, run_for)