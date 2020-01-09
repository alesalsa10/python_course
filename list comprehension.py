# works on list, set, dictionaries
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

my_list = [char for char in 'hello']  # same as above, for char in hello, add char to list

# list 2 creates a list with numbers ranging from 0 to 99
my_list2 = [num for num in range(0, 100)]  # for number in range 0 to 100, add num to my_list2
print(my_list2)

# multiplies all numbers from 0 to 100 times 2
my_list3 = [num * 2 for num in range(0, 100)]
print(my_list3)

# return only the even numbers
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)
