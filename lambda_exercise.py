# print all the value on the list squared
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# list sorting based on seconds value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])  # first x is the tuple, x[1] is the second item in it
print(a)
