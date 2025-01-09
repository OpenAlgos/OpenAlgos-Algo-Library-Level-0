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

 