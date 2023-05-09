import random
import random
import string

print('Welcome to the PyPassword Generator')
letter = int(input('How many letters would you like in your password?\n'))
symbol = int(input('How many symbols would you like?\n'))
number = int(input('How many numbers would you like?\n'))

passwordRaw = []
# add random letters
for i in range(0, letter):
    passwordRaw.append(random.choice(string.ascii_letters))
# add random symbols
for i in range(0, symbol):
    passwordRaw.append(random.choice(string.punctuation))
# add random numbers
for i in range(0, number):
    passwordRaw.append(random.choice(string.digits))
print(passwordRaw)

password = ''
# random choice from passwordRaw
random.shuffle(passwordRaw)
for i in passwordRaw:
    password += i
print(password)