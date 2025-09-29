#Rock Paper Scissors Game

'''
September 29, 2025

Project # 1
'''

'''
2 players

1st player will be asked to input either rock, paper or scissors
2nd player will be the computer and will randomly choose either rock, paper or scissors
(or you can have 2 human players, but for another time)

3 possible outcomes,
1. Player 1 wins
2. Player 2 wins
3. Draw
'''

import random
import time
import sys
from colorama import init, Fore, Style

init(convert=True, strip=False, autoreset=True)

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # for newline

r, p, s = "rock", "paper", "scissors"
score = 0
comp_score = 0

round = 1

print("\n-----------------------------------")
print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'rock' for rock, 'paper' for paper, 'scissors' for scissors or 'quit' to exit the game")

while True:
    print("\n-----------------------------------")
    print(f"Round {round}\n")

    player = input("P1, Make your move: ")

    if player == "quit":
        print("Thanks for playing!")
        break

    if player != r and player != p and player != s:
        print("Invalid move, try again")
        continue

    computer = random.choice([r, p, s])

    type_text(Fore.CYAN + "Computron is making a move...\n", 0.07)
    time.sleep(2)

    type_text(Fore.YELLOW + "... Computron plays: " + Fore.GREEN + f"{computer}\n", 0.07)

    time.sleep(1)

    if player == r:
        if computer == s:
            print("Rock crushes scissors \nYou Won!\n")
            score += 1

        elif computer == p:
            print("Paper covers rock \nComputron Wins!\n")
            comp_score += 1

        elif computer == r:
            print("Draw, Player and Computron gets 1 point\n")
            score += 1
            comp_score += 1

    elif player == p:
        if computer == r:
            print("Paper covers rock \nYou Won!\n")
            score += 1

        elif computer == s:
            print("Scissors cuts paper \nComputron Wins!\n")
            comp_score += 1

        elif computer == p:
            print("Draw, Player and Computron gets 1 point\n")
            score += 1
            comp_score += 1

    elif player == s:
        if computer == p:
            print("Scissors cuts paper \nYou Won!\n")
            score += 1

        elif computer == r:
            print("Rock crushes scissors \nComputron Wins!\n")
            comp_score += 1

        elif computer == s:
            print("Draw, Player and Computron gets 1 point\n")
            score += 1
            comp_score += 1

    print(f"Your score is: {score}")
    print(f"Computron score is: {comp_score}\n")
    round += 1

    if round > 5:
        if score > comp_score:
            print("You are the winner!\n")

        elif comp_score > score:
            print("You lose! Computron is the winner!\n")

        elif comp_score == score:
            print("It's a tie!\n")
        break

    input("Press Enter to continue...\n")