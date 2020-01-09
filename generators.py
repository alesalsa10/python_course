def generator_function(num):
    for i in range(num):
        yield i


# yield only keeps the most recent data in memory, unlike lists which store all items
# this makes it a lot faster

for item in generator_function(1000):
    print(item)


def gen2(num):
    for i in range(num):
        yield i * 2


# yield pauses the function and comes back when next is called


g = gen2(100)
print(next(g))  # this returns 0, it runs 0 * 2 and that is it. List run all range

h = gen2(100)
next(h)  # 0*2=0
next(h)  # 1*2=2
print(next(h))  # 2*2=4
