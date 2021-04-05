import random

min = 1
max = 1000
num_of_guesses = 0

num_to_find = random.randint(min, max)

def guess():
    global num_of_guesses
    global num_guessed
    num_guessed = int(input("Enter your guess (between " + str(min) + " and " + str(max) + "): "))
    num_of_guesses += 1

def check_num():
    while(num_guessed != num_to_find):
        if(num_guessed > num_to_find and num_guessed <= max and num_guessed >= min):
            print("Try a lower guess\n")
            guess()
        elif(num_guessed < num_to_find and num_guessed <= max and num_guessed >= min):
            print("Try a higher guess\n")
            guess()
        else:
            print("Invalid number.")
            break

def win():
    if (num_guessed == num_to_find and num_of_guesses == 1):
        print("\nYou found the number in " + str(num_of_guesses) + " guess")
    elif(num_guessed == num_to_find):
        print("\nYou found the number in " + str(num_of_guesses) + " guesses")

guess()
check_num()
win()
