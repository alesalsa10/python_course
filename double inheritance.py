class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')


class Hybrid(Wizard, Archer):  # inherits from both classes
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)  # both have to be called here
        Wizard.__init__(self, name, power)


hb1 = Hybrid('borgie', 50, 100)
print(hb1.sign_in())
print(hb1.check_arrows())
