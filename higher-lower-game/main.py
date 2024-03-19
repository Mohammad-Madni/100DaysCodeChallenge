from art import logo
import random
from game_data import data
print(logo)
chose = random.choice(data)
follower = chose["follower_count"]
def sorting():
    country = chose["country"]
    description = chose["description"]
    name = chose["name"]
    print(f"{name}, a {description}, from {country}.")
print(sorting())
def compare(count1, count2):
    if count1 > count2:
        print(f"{count1} Win")

print(chose)

#compare() with return user's point
#