#Task 1
import random

items = ['shoe', 'glass', 'chair', 'keyboard', 'lamp']

for x in items:
    answer = random.choice(items)
    player_choice = input("What is your pick? (shoe, glass, chair, keyboard, or lamp) ")
    if player_choice == answer:
        print(f"Good job, the correct choice was {answer}")
    else:
        print(f"Oh too bad! You picked {player_choice} but the correct answer is {answer}")