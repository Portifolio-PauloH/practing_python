# Project of the day (day 04) - Rock, Paper and Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choises = [rock, paper, scissors]
play = random.randint(0, 2)

player = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if player >= 3 or player < 0:
    print("This number is out of range, please choise 0 or 1 or 2.")
else:
    print(f"Your choise: {choises[player]}")
    print(f"CPU choise: {choises[play]}")

    if player == 0 and play == 2:
        print("You win!")
    elif play == 0 and player == 2:
        print("You lose.")
    elif play > player:
        print("You lose.")
    elif player > play:
        print("You win!")
    elif player == play:
        print("It's draw.")
