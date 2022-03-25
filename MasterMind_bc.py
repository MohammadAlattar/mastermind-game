# first create random numbers 
import random
numbers = []
efforts = 0 
def RandomNumbers(): 
 for i in range(4):
     r=random.randrange(0,9)
     if r not in numbers: 
       numbers.append(r)
     else:
       numbers.clear
       RandomNumbers()  
     
 

# create game 
def play():
  global efforts 
  efforts +=1 
  bulls = 0 
  cows=0
  print(numbers)
  inputNum = input("enter 4 digit numbers")
  gus=[]

# input 4 digit number to gus and check if the numbers bulls or not   
  for bu in range(4):
    gus.append(int(inputNum[bu])) 
  for i in range(4):
     if gus[i] == numbers[i]:
      bulls+=1

# check the cows : if the number in gus[cw] is exist in numbers[i] at any index of list 
  for cw in range(4):
    for i in range(4):
     if gus[cw] == numbers[i]:
      cows += 1
  print(f"A{bulls}{cows}B")
  if bulls == 4 : 
    print(f"you win after :{efforts} efforts")
  else:
    play()

RandomNumbers()
play()
