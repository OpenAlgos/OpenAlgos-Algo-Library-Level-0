import random

choices = ["rock","paper","scissor"]
user_choice = input("Type whether you are choosing rock,paper or scissor:\n")

computer_choice = random.choice(choices)
print("Computer's choice is", computer_choice,"\nYour choice is",user_choice)
if user_choice == computer_choice:
    print("\nIt's a tie!")

elif user_choice == "rock":
    if computer_choice == "paper":
        print("Computer wins! Paper covers rock.")
    else:
        print("You win! Rock smashes scissors.")

elif user_choice == "paper":
    if computer_choice == "scissor":
        print("Computer wins! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")

elif user_choice == "scissor":
    if computer_choice == "rock":
        print("Computer wins! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
