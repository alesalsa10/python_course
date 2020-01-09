is_magician = False
is_expert = True

# check if magician and expert: 'you are a master magician'
if is_magician and is_expert:
    print('You are a master magician')

# check if magician but not expert: 'at least you're getting there'
if is_magician and not is_expert:
    print('At least you are getting there')

# if you're not a magician: You need magic powers

if not is_magician:
    print('You need magic powers ')
