

# Using Object Oriented Programming, write a program that implements a dice game. The game should have two players, and each player should have a name and a score. The game should have a method called play that takes two players as arguments and simulates the game. The game should be played as follows:

#     Each player rolls a die.
#     The player with the highest roll wins the round.
#     The winner gets one point added to their score.
#     The game ends when one player has 5 points.
#     The player with the most points at the end of the game wins.
#     The program should print out the winner's name and score.
#     If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.

import random
class DiceGame():
    dice = [1,2,3,4,5,6]
    
    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player1_score = 0
        self.player2 = player2
        self.player2_score = 0
        
    def play(self):
        player1_roll = random.choice(dice) 
        player2_roll = random.choice(dice)
        