#console game of rock, scissors and paper. 


import random
import sys

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer. Good luck!")

#the user enters their choice in the console.
#the computer will randomly select a choice and the winner will be displayed in the console.
#the game will continue until the user decides to quit.
#the user will be warned if they enter an invalid choice.

while True:
    print("Please enter your choice: ")
    print("Enter rock, paper, scissors or quit to quit the game.")
    choice = input()
    choice = choice.lower()
    print("Your choice is: " + choice)

    if choice == "quit":
        sys.exit()
    
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print("The computer's choice is: " + computer_choice)

    if choice == computer_choice:
        print("It's a tie!")
    elif choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid choice, please try again.")
