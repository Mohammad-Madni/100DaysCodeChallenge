from art import logo,vs
import random
from game_data import data

def formated_data(account):
    """format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}.")
#generate a random account from game_data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b.random.choice(data)

print(logo)

print(f"Compare A: {formated_data(account=account_a)}")

#print art between 1st and 2nd data
print(vs)

print(f"Compare B: {formated_data(account=account_b)}")




#ask the user to guess

#check the user is correct
##get follower count of each account
##user if statement to check if user is correct

#give user the feedback for there guess

#score keeping

#make the game repeatable

#making account at position b to a if user guess's it right

#clear screen between rounds


