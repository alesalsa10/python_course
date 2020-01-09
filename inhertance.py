# users can be wizards or archers, etc. So the different types must have access to the user class

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):  # this gives the wizard class access to the user class
    def __init__(self, name, power, email):
        # User.__init__(self, email)  # calls the user email
        super().__init__(email)  # same as above
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking  with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows} ')


wizard1 = Wizard('Merlin', 40, 'fdjfhdsj@hotmail.com')
archer1 = Archer('robin', 100)
wizard1.attack()

print(isinstance(wizard1, User))  # returns true if wizard1 is an instance of User, which it is here
