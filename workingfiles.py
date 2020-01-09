with open('text.txt', mode='r+') as my_file:  # r+ is read and write
    text = my_file.write('hey, it is me!')
    print(text)
