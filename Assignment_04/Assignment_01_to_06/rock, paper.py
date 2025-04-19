import random

list = ['rock', 'paper', 'scissor']

bot = random.choice(list)
user = None

while user not in list:
    user = input("Rock, Paper or Scissor ?: ")

    if user.lower() not in list:
        print("\n\twrong input!\n")    
    else:
        print("\nComputer: "+bot.capitalize()+"\nYou: "+user.capitalize())
        if bot.lower() == user.lower():
            print("\n\tdraw\n")
        elif bot.lower() == "rock" and user.lower() == "scissor" or bot.lower() == "scissor" and user.lower() == "paper" or bot.lower() == "paper" and user.lower() == "rock":
            print("\n\tComputer Wins\n")
            break
        else:
            print("\n\tYou Win\n")
            break
