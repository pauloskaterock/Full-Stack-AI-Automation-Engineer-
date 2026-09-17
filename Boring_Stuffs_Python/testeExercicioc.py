
# import re


# 'I have eaten ' + str(99)+ ' burritos.'
# ---------------------------------------------------


# if name == 'Mary':
#   print('Hello Mary')
# if password == 'swordfish':
#   print('Access granted.')
# else:
#   print('Wrong password.')




# --------------------------------------------------------

# name = "Alice"
# age = 10
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')


# -----------------------------------------------------------------------------

# spam = 0
# if spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

# --------------------

# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1




#---------------------

# while True:
#     print('Hello world!')


#
#--------------------------

# import copy

# spam =  ['A', 'B', 'C', 'D']
# cheese = copy.copy(spam)
# cheese[1] = 42
# spam



# import copy
# spam = ['A', 'B', 'C', 'D']
# cheese = copy.copy(spam)
# cheese[1] = 42
# spam
# -------------------------------------------

# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')


#----------------------------------------------------------------

# import pyperclip
# pyperclip.copy('Hello world!')
# pyperclip.paste()


# ------------------------------------------------------

import re


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
