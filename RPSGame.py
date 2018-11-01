from random import randint

player_lives = 5
computer_lives = 5

#available weapons
choices = ["Rock", "Paper", "Scissors"]
player = False

#make the computer pick one item at random
computer = choices[randint(0, 2)]

#show the computer's choices in the terminal window
print("computer chooses: ", computer)

while player is False:
    print("==============================")
    print("Player Lives:", player_lives, "/5")
    print("AI Lives:", computer_lives, "/5")
    print("==============================")
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("player choose:", player)

    #check to see if you picked the same thing
    if (player == computer):
        print("Tie!Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            #computer won
            player_lives -= 1
            print("You lose", computer, "covers", player, "\n")
        else:
            print("You win!", player, "smashes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            #computer won
            player_lives -= 1
            print("You lose!", computer, "cuts", player, "\n")
        else:
            print("You win!", player, "covers", computer, "\n")
            computer_lives -= 1

    elif player == "Scissors":
        if computer == "Rock":
            #computer won
            player_lives -= 1
            print("You lose!", computer, "smashes", player, "\n")
        else:
            print("You win!", player, "cuts", computer, "\n")
            computer_lives -= 1

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    player = False
    computer = choices[randint(0, 2)]
