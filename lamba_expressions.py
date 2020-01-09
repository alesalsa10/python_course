# lambda expressions are one time expressions, that do not need to be reused later on, so they dont
# stay in memory once completed
from functools import reduce
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item * 2, my_list)))


# same as above, but using lambda, it is not stored in memory, so once done, it can't be reused


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))  # same as only_odd, but with lambda

print(reduce(lambda  acc, item: acc + item, my_list))