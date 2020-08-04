import random

print("Welcome to the Number Guessing Game.")
print("I am Senor Computer. Can you guess my number?")

computerNum = random. randint(0,20)


# state variables
win = False
play = True
tries = 5

while play == True:
  while tries > 0:
    print()
    playerNum = input("Enter a number between 0-20: ")
    playerNum = float(playerNum)

    if (playerNum > 20 or playerNum < 0):
      print("Bad Number")
      break
    else:
      if playerNum > computerNum:
        print("too big")
        tries -= 1
        print("You only have " + str(tries) + " left!")
      elif playerNum < computerNum:
        print("too small")
        tries -= 1 
        print("You only have " + str(tries) + " left!")
      else:
        print("Correct! " + "The number is " + str(computerNum))
        win = True
        break
  if win == True:
    print("Well Done! You won at " + str(6-tries) + " tries")
  else:
    print("No more tries")
    print("The number was: " + str(computerNum))

  answer = input("Do you want to play again? Y or N")

  if answer.upper() == " N":
    print("Okay then! See you later!")
    play = False
  elif answer.upper() == " Y":
    win = False
    tries = 5
    computerNum = random.randint(0,20)
  else:
    win = False
    tries = 5
    computerNum = random.randint(0,20)







    # if (playerNum is greater than 10 or less than 0)
      # print bad Number
      # break
    # else:
      # if greater
        # print too big
        # subtract 1 to tries 
        # print how many tries the user has left
      # elif lesser
        # print too small 
        # subtract 1 to tries
        # print how many tries the user has left
      # else:
        # print correct
        # change win to True
        # break

  
    # Write a conditional to check if the user number is greater or lesser than the number range (less than 0 or greater than 10)
    # else do a nested conditional that will test if the number is greater than computerNum, less than computerNum, or else equal to computerNumb.


# Goal: User has to guess computer numb
# Project planning
# User input
# Condiional to evaluate big or too small
# Loop repeat asking until tries are 0
# Variable for # of tries
# get computer numb