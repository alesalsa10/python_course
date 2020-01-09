# given the same input, it will always return the same output
# produces no side effects (does not touch anything on the outside world. It is contained in the function
from functools import reduce

'''def multiply_by2(li):
    new_list = []  # empty list must be inside of the function, no print in it, only outside
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))'''

my_list = [1, 2, 3]
your_list = [10, 20, 10]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):  # 10 takes initial value of acc, so it is 10+1=11, 11+2=13, 13+3=16
    return acc + item  # 1,2,3 because those are the list values, final number is 16


print(list(map(multiply_by2, [1, 2, 3])))  # same as first function(MAP makes this possible)
print(list(filter(only_odd, my_list)))  # FILTER, returns true if item % 2 !=0, it True, gets added to list
print(list(zip(my_list, your_list)))  # Joins 2 lists
print(reduce(accumulator, my_list, 10))
