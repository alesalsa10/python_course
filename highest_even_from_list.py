# print the highest even number from a list
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def highest_even(li):
    evens = [x for x in li if x % 2 == 0]
    return max(evens)


print(f'The highest even number on your list is {highest_even(some_list)}')
