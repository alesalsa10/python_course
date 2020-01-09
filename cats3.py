class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat Object with 3 cats
cat1 = Cat('Garfield', 4)
cat2 = Cat('Solly', 6)
cat3 = Cat('Tom', 7)

cats_ages = [cat1.age, cat2.age, cat3.age]

oldest_age = max(cats_ages)
print(f'The oldest cat is {oldest_age} years old')
# create a function that finds the oldest cat


'''def get_oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old')'''

'''def oldest_age(*args):
    old_list = []
    for item in args:
        old_list.append(item)
    return max(old_list)


def oldest_name():
    if oldest_age(cat1.age, cat2.age, cat3.age) == cat3.age:
        return cat3.name


print(f'The oldest cat is {oldest_age(cat1.age, cat2.age, cat3.age)} years old and his name is {oldest_name()}')'''
