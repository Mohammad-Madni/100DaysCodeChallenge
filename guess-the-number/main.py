#Number Guessing Game Objectives:
from art import logo
import random
chosen = random.randint(1,100)
def check(a):
    global chosen
    if a == chosen:
        return (f"You've Got it! The Answer was {chosen}.")
    if a > chosen:
        return ("Too High")
    else:
        return ("Too low")
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_life = 0
user_dif = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
if user_dif == "easy":
    user_life = 10
elif user_dif == "hard":
    user_life = 5
while user_life > 0:
    print(f"You have {user_life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    print(check(guess))
    user_life = user_life - 1
    if guess == chosen:
        user_life = 0
    if user_life == 0 and guess != chosen:
        print(f"You Lose! Actual answer is {chosen}")
