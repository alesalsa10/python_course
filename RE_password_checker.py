# at least 8 char long
#contain any letters, numbers, $%#@
#ends in a number

import re


pattern = re.compile(r'[a-zA-Z0-9@#$%]{8,}\d')
password = 'hhh2@#455'

check = pattern.fullmatch(password)
if check:
    print('Your password is valid')
else:
    print('This is not a valid password')


