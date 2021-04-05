import random

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*|?'

length = input('Enter the length of the password: ')
length = int(length)

number = input('Enter the number of password: ')
number = int(number)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

