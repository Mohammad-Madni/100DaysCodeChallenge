from art import logo
import random
from game_data import data
print(logo)
chose = random.choice(data)
print(chose)
follower = chose["follower_count"]
def sorting():
    country = chose["country"]
    description = chose["description"]
    name = chose["name"]
    print(f"{name}, a {description}, from {country}.")

#compare() with return user's point
#