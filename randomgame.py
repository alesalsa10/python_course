# generate a number 1-10
# get input from user
# check that input is a number 1-10
# check if number is the right guess
# ask again

from random import randint
import sys

name = input('What is your name? ')
number = randint(int(sys.argv[1]), int(sys.argv[2]))
guesses_taken = 0
print(f'Well, {name}, I am thinking of a number between 1 and 10')

while True:
    guess = input('Guess a number from 1 to 10. Type exit to finish ')
    guesses_taken += 1
    if guess == 'exit':
        break

    elif int(guess) == number:
        print(f'Congratulations, you got the number and it took you {guesses_taken} tries')
        break

    elif int(guess) > number:
        print('Too high')
    elif int(guess) < number:
        print('Too low')
