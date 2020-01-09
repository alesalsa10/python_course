my_set = {char for char in 'hello'}  # same as lists only with brackets
print(my_set)

# Dictionary comprehension
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value ** 2 for key, value in simple_dict.items()}
print(my_dict)

# item is the key and item * 2 is the value
my_dict1 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict1)