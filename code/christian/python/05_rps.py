# Let's play rock-paper-scissors with the computer. 
# You may want to try using these emojis πΏπβοΈβββ

# The computer will ask the user for their choice (rock, paper, scissors)
# The computer will randomly choose rock, paper or scissors
# Determine who won and tell the user
# Let's list all the cases:

# rock vs rock (tie)
# rock vs paper
# rock vs scissors
# paper vs rock
# paper vs paper (tie)
# paper vs scissors
# scissors vs rock
# scissors vs paper
# scissors vs scissors (tie)

import random
moves = ['πΏ', 'π', 'βοΈ']
robo_choice = []
robo_choice = random.choice(moves)

print("Welcome to:\n\nROCK...\n\tPAPER...\n\t\tSCISSORS!!!\n")
player_move = input("CHOOSE.YOUR.WEAPON > πΏ - π - βοΈ : ")
if player_move == "πΏ" and robo_choice == 'πΏ':
    winner = 'NONE... ITS A TIE!'
elif player_move == "πΏ" and robo_choice == 'π':
    winner = 'COMPUTER'
elif player_move == "πΏ" and robo_choice == 'βοΈ':
    winner = 'YOU'
elif player_move == "π" and robo_choice == 'πΏ':
    winner = 'YOU'
elif player_move == "π" and robo_choice == 'π':
    winner = 'NONE... ITS A TIE'
elif player_move == "π" and robo_choice == 'βοΈ':
    winner = 'COMPUTER'
elif player_move == "βοΈ" and robo_choice == 'πΏ':
    winner = 'COMPUTER'
elif player_move == "βοΈ" and robo_choice == 'π':
    winner = 'YOU'
elif player_move == "βοΈ" and robo_choice == 'βοΈ':
    winner = 'NONE... ITS A TIE'

print(f"\nPlayers weapon: {player_move}\nRobots weapon:  {robo_choice}\n")
print(f"WINNER: {winner}!!!")

# Version 2 (optional)
# After playing, ask them if they'd like to play again. 
# If they say yes, restart the game, otherwise exit.

# Version 3 (optional)
# Rock, paper, scissors, lizard, Spock! 
# https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/