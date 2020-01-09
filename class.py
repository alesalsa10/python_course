class PlayerCharater:
    membership = True  # Class Object Attribute, exits for all objects

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name
            self.age = age
            # self._image = age, the - means it is private and should not be changed

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy', num1 + num2)

    def shout(self):
        print(f'My name is {self.name}')  # self is used because it was first passed into the function

    @staticmethod
    def stc_method(param1, param2):
        pass  # cannot take the class like @classmethod does


player1 = PlayerCharater('Alex', 21)
player2 = PlayerCharater('Tom', 45)
player2.attack = 50  # added only to player 2
player3 = PlayerCharater.adding_things(2, 3)  # gets player teddy age 5

print(player1.shout())
print(player2.shout())
