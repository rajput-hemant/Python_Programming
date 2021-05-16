# Rock Paper Scissor Game
import random

comp_choice = ['Rock', 'Paper', 'Scissor']
rounds, user_wins, comp_wins = 10, 0, 0
print("1:Rock  2:Paper  3:Scissor")
while rounds > 0:
    user = int(input("Enter your Choice="))
    if 4 > user > 0:
        comp = random.choice(comp_choice)
        print("Computer's choice=", comp)
        if (user == 1 and comp == 'Rock') or (user == 2 and comp == 'Paper') or (user == 3 and comp == 'Scissor'):
            print("It's tie")
        elif user == 1 and comp == 'Paper':
            comp_wins += 1
            print("Paper wraps the Rock, Computer Won")
        elif user == 2 and comp == 'Rock':
            user_wins += 1
            print("Paper wraps the Rock, User Won")
        elif user == 1 and comp == 'Scissor':
            user_wins += 1
            print("Rock breaks the Scissor, User Won")
        elif user == 3 and comp == 'Rock':
            comp_wins += 1
            print("Rock breaks the Scissor, Computer Won")
        elif user == 2 and comp == 'Scissor':
            comp_wins += 1
            print("Scissor cuts the Paper, Computer Wins")
        elif user == 3 and comp == 'Paper':
            user_wins += 1
            print("Scissor cuts the Paper, User Wins")
        rounds -= 1
        print(f"Rounds Left '{rounds}'")
    else:
        print(" Invalid Choice, Please choose again")
if user_wins > comp_wins:
    print("Congratulations! You have Won")
elif comp_wins > user_wins:
    print("GAME OVER!You Lose")
elif user_wins == comp_wins:
    print("It's a tie ")
