import random


def computers_choice():
    lst = ["rock", "paper", "scissors"]
    choice = random.choice(lst)
    return choice


print("**************** WELCOME TO ROCK-PAPER-SCISSORS GAME *****************")
print("How many games do you want to play?")
number = int(input())
games_won = 0
i = 0
while i < number:
    print("Enter your choice -- Rock,Paper,Scissors")
    players_choice = input().lower()
    choice1 = computers_choice()
    if players_choice == "rock" and choice1 == "paper":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("Paper beats Rock,You Lost")
        i += 1
        continue
    elif players_choice == "rock" and choice1 == "scissors":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("Rock beats Scissors,You Won")
        games_won += 1
        i += 1
        continue
    elif players_choice == "rock" and choice1 == "rock":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("It is a Draw by repetition")
        i += 1
        continue
    elif players_choice == "paper" and choice1 == "paper":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("It is a Draw by repetition")
        i += 1
        continue
    elif players_choice == "paper" and choice1 == "scissors":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("Scissors beats Paper,You Lost")
        i += 1
        continue
    elif players_choice == "paper" and choice1 == "rock":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("Paper beats Rock,You Won")
        i += 1
        games_won += 1
        continue
    elif players_choice == "scissors" and choice1 == "paper":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("Scissors beats Paper,You Won")
        i += 1
        games_won += 1
        continue
    elif players_choice == "scissors" and choice1 == "scissors":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("It is a Draw by repetition")
        i += 1
        continue
    elif players_choice == "scissors" and choice1 == "rock":
        print("Your choice is", players_choice, "and", "Computers choice is", choice1)
        print("Rock beats Scissors,You Lost")
        i += 1
        continue
    else:
        print("Enter Valid Choice!")
print("\n")

print("Total Games Won :", games_won)
print("Total Games Played :", number)
