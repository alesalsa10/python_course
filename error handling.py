# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        10 / age
        # raise ValueError('hey cut it out')   (rarely used)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    finally:
        print('ok, I am finally done')  # runs regardless at the end of everything


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('please enter numbers')


print(sum('1', 2))
