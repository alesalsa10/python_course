# list that starts with 0, 1 adds them to get 1, then 1+1=2, 1+2=3 [0,1,1,2,3,5, etc]
def fib(number):
    a = 0  # starting numbers
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(5):
    print(x)


def fib2(number):
    a = 0  # starting numbers
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(6))
