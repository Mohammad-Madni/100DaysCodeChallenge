from art import logo,vs
import random
from game_data import data
score = 0
def formated_data(account):
    """format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}.")
def check_answer(guess, a_follower, b_follower):
    """Takes the account data and user guess returns if they are right """
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"
#generate a random account from game_data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b.random.choice(data)

print(logo)

print(f"Compare A: {formated_data(account=account_a)}")

#print art between 1st and 2nd data
print(vs)

print(f"Against B: {formated_data(account=account_b)}")




#ask the user to guess
guess = input("Who has more follower's ? Type 'A' or 'B': ").lower()
#check the user is correct
##get follower count of each account
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
is_correct = check_answer(guess,a_follower_count,b_follower_count)

if is_correct == True:
    score +=1
    print(f"You're right. Current score: {score}")
else:
    print(f"Sorry, that's wrong. Final score: {score}")
##use if statement to check if user is correct
if a_follower_count > b_follower_count:
    if guess == "a":
        print("You' guessed it right")
#give user the feedback for there guess

#score keeping

#make the game repeatable

#making account at position b to a if user guess's it right

#clear screen between rounds


