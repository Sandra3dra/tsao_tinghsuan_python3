from random import randint

#available weapons
choices = ["Rock", "Paper", "Scissors"]

#make the computer pick one item at random
computer_choice = choices[randint(0, 2)]

#show the computer's choices in the terminal window
print("computer chooses: ", computer_choice)