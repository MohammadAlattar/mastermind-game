import random
import collections
import termcolor
import pyfiglet

length = 4
random_string = [random.choice("ABCDEF") for rand_str in range(length)]
# print(*random_string)
count = collections.Counter(random_string)

def rule():
    print(termcolor.colored(pyfiglet.figlet_format("MASTERMIND"), color="red"))
    print("-----------------------------------------")
    print("\t\tMenu")
    print("-----------------------------------------")
    print("Enter code using characters.")
    print("you should constant of 4 characters from A to F ")
    print("EXAMPLE : ABCD")
    print("If you don't know how to play the game, read the file README\n")
    print("You have 8 attempts")

def create_game():
    guess = input('Your guess ?: ').upper() 
    guess_count = collections.Counter(guess)
    wrong_position = sum(min(count[key], guess_count[key]) for key in count)
    right_position = sum(a==b for a,b in zip(random_string, guess))
    wrong_position -= right_position
    print(f'Right Position is : {right_position} Wrong Position is : {wrong_position}')
    return right_position != length

def result():
    for attempts in range(8):
        if not create_game(): 
            print('You Win !')
            break
        else:
            print('Your remaining attempts is :', 8 - 1- attempts)
    else:
        print('You Lost . The secret was {}.'.format(''.join(random_string)))

rule()
print("-----------------------------------------")
create_game()
result()
