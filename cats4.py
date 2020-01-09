class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# add another cat

class Garfield(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# instantiate the cat object with the cats
Simon = Simon('Simon', 3)
Sally = Sally('Sally', 6)
Garfield = Garfield('Garfield', 8)

# create a list of all the pets (create 3 cat instances from the above)
my_cats = [Simon, Sally, Garfield]

# instantiate the Pets class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# output all of the cats walking using my_pets instance
my_pets.walk()
