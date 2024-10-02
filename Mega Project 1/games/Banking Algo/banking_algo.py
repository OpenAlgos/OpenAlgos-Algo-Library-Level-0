#this is a banking algorithm 
#debit,credit
#this is a basic version, all the updates will be patched soon
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
        
