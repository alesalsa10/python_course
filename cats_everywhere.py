# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('cat1', 3)
cat2 = Cat('cat2', 4)
cat3 = Cat('cat3', 7)
cats_list = [cat1, cat1, cat3]


# 2 Create a function that finds the oldest cat
def oldest_cat():
    return max(cat1.age, cat2.age, cat3.age)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat()} years old')
