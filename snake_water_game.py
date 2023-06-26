import random
l=['s','p','k']
chance=3
no_of_chance=0
computer_point=0
player_point=0
print("\t\t\tStone, Paper, Scissor Game\n")
print("s for Stone\np for Paper\nk for Scissor\n")
while no_of_chance<chance:
    _input=input("Stone,Paper,Scissor:")
    _random=random.choice(l)
    
    if _input==_random:
        print("Tie both 0 points to each")
        
    elif _input=="s" and _random=="p":
        computer_point=computer_point+1
        print(f"player guess {_input} and computer guess {_random}")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and player point is {player_point}")
        
    elif _input=="s" and _random=="k":
        player_point=player_point+1
        print(f"player guess {_input} and computer guess {_random}")
        print("player wins 1 point")
        print(f"computer point is {computer_point} and player point is {player_point}")
        
    elif _input=="p" and _random=="k":
        computer_point=computer_point+1
        print(f"player guess {_input} and computer guess {_random}")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and player point is {player_point}")
        
    elif _input=="p" and _random=="s":
        player_point=player_point+1
        print(f"player guess {_input} and computer guess {_random}")
        print("player wins 1 point")
        print(f"computer point is {computer_point} and player point is {player_point}")
        
    elif _input=="k" and _random=="s":
        computer_point=computer_point+1
        print(f"player guess {_input} and computer guess {_random}")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and player point is {player_point}")
        
    elif _input=="k" and _random=="p":
        player_point=player_point+1
        print(f"player guess {_input} and computer guess {_random}")
        print("player wins 1 point")
        print(f"computer point is {computer_point} and player point is {player_point}")
        
    else:
        print("You have input wrong")
        
    no_of_chance=no_of_chance+1
    print(f"{chance - no_of_chance} is left of {chance}\n")
        
print("Game over")

if computer_point==player_point:
    print("Tie")
elif computer_point>player_point:
    print("computer wins and player loose")
else:
    print("player wins and computer loose")
    
print(f"player point is {player_point} and computer point is {computer_point}")
