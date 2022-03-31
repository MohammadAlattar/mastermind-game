import os
import random
import string

print("-----------------------------------------")
print("\t\tMenu")
print("-----------------------------------------")
print("Enter code using characters.")
print("You should constant of 4 characters from A to F ")
print("EXAMPLE : ABCD")
print("If you don't know how to play the game, read the file README")
print("-----------------------------------------")
result_str = []
attempts= 0 
def get_random_string():
    letters = string.ascii_uppercase
    for i in range(4):
        rand_str= ''.join(random.choice('ABCDEF'))
        result_str.append(rand_str)
    
    return result_str


def create_game():
    global attempts 
    attempts +=1
    right_position = 0 
    wrong_position = 0 
    # print(result_str)    
    input_str = input("Your guess : ")
    guess = []
    for count_str in range(4):
        guess.append(input_str[count_str].upper())  
    
    for guess_str_w in range(4):
        for check in range(4):
            if guess[guess_str_w] == result_str[check]:
                wrong_position +=1  
    for guess_str in range(4):    
        if guess[guess_str] == result_str[guess_str]: 
            right_position +=1                    
    print("Right Position is : ", right_position)    
    print("wrong Position is : ", wrong_position)    

    if right_position == 4 :
        print("congratulations you win after ".upper(),attempts)
        
    else : 
        create_game()   



get_random_string()
create_game()
