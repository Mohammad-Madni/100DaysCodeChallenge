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
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
if computer_choice == 0:
    print("Computer Chose:")
    print(rock)
elif computer_choice == 1:
    print("Computer Chose:")
    print(paper)
elif computer_choice ==2:
    print("Computer Chose:")
    print(scissors)
