# check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list = [x for x in some_list if some_list.count(x) > 1]
new_list = list(set(new_list))

print(new_list)
