import random

def min_and_max():
    global min
    global max

    min = int(input("Enter the minimum number: "))
    max = int(input("Enter the maximum number: "))

def check_min_and_max():
    global min
    global max

    if (min < 0 or max < 0):
        print("The minimum and the maximum numbers need to be positive")
        min_and_max()
    elif (min > max):
        print("The maximum number needs to be greater than minimum number")
        min_and_max()
        
def number():
    global min
    global max
    global random_number

    min_and_max()
    check_min_and_max()

    random_number =  random.randint(min, max)

number()
print("Your random number is " + str(random_number))


