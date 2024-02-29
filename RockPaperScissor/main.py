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

#Write your code below this line 👇

import random
computer_choice = random.randint(0,2)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissor."))
if choice == 0:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print("It's Draw.")
    elif computer_choice == 1:
        print(paper)
        print("You Lose.")
    elif computer_choice == 2:
        print(scissors)
        print("You Win.")
elif choice == 1:
    print(paper)
    if computer_choice == 0:
        print(rock)
        print("You Win.")
    elif computer_choice == 1:
        print(paper)
        print("It's Draw.")
    elif computer_choice == 2:
        print(scissors)
        print("You Lose.")
elif choice == 2:
    print(scissors)
    if computer_choice == 0:
        print(rock)
        print("You Lose.")
    elif computer_choice == 1:
        print(paper)
        print("You Win.")
    elif computer_choice == 2:
        print(scissors)
        print("It's Draw.")
else:
    print("Invalid Input")

