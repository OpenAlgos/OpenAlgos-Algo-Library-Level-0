def banking_algo():
    print("You selected the Banking Algorithm.")
    #this is a banking algorithm 
    #this is a basic version, all the updates will be patched soon
    #debit,credit
    #check pull
    balance = 1000
    print("Welcome to the OpenAlgos banking algorithm")
    print("Your model bank balance is 1000 points")
    print("Press 1 for crediting point and press 2 for debiting points:")

    operation = int(input())

    if (operation != 1 and operation != 2):
        print("error:Choose between 1 or 2")
    
    elif(operation == 1):
        credit_amount = int(input("Type the amount to be credit:\n"))
        balance += credit_amount
        print("Your current balance is",balance)
    
    elif (operation == 2):
        debit_amount = int(input("Type the amount to be debited:\n"))
    
        if(balance < debit_amount):
            print("insufficient balance")
        
        balance -= debit_amount
        print("Your current balance is",balance)
        


def stone_paper_scissors():
    print("You selected Stone Paper Scissors.")
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

    
def unique_guess_the_number():
    print("You selected the Unique Guess The Number game.")
    import random
    points = 0
    point_setter = int(input("Set how many points match you want to play:\n"))
    rounds_wanna_play = int(input("Set how many inputs you have to limit:\n"))
    rounds = 0

    while points < point_setter and rounds_wanna_play > rounds:  
        x = int(input("\nPick a number from 1 to 10:\n"))

        choices = tuple(int(i) for i in range(1, 11))

        y = random.choice(choices)

        print("Computers choice :",y)
    
    

        if(x == y):
            print("You got 10 points")
            points += 10
            print("Your points are", points)
            rounds += 1
            print("Your have", rounds_wanna_play - rounds ,"rounds left")
        
        elif(y - 2 < x and x < y + 2):
            print("You got 5 points")
            points += 5
            print("Your points are", points)
            rounds += 1
            print("Your have", rounds_wanna_play - rounds ,"rounds left")
        
        elif(y - 4 < x and x < y + 4):
            print("You got 3 points")
            points += 3
            print("Your points are", points)
            rounds += 1
            print("Your have", rounds_wanna_play - rounds ,"rounds left")
        
        elif(y - 6 < x and x < y + 6):
            print("You got 1 point")
            points += 1
            print("Your points are", points)
            rounds += 1
            print("Your have", rounds_wanna_play - rounds ,"rounds left")
        
        else:
            print("You got no point")
            print("Your points are", points)
            rounds += 1
            print("Your have", rounds_wanna_play - rounds ,"rounds left")

    if points >= point_setter:  
        print("Congratulations! You've reached the point target and won!")
    else:
        print("\nGame over! You didn't reach the point target within the allowed rounds.")
        print("Your final points are:", points)

 

def main():
    while True:
        print("\n--- OpenAlgos ---")
        print("Select an algorithm to run:")
        print("1. Banking Algorithm")
        print("2. Stone Paper Scissors")
        print("3. Unique Guess The Number Game")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            banking_algo()
        elif choice == '2':
            stone_paper_scissors()
        elif choice == '3':
            unique_guess_the_number()
        elif choice == '4':
            print("Exiting OpenAlgos. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
