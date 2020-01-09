age = input("What is your age?: ")

if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age
def checkDriver():
    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()