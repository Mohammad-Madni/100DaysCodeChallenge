from art import logo
print(logo)
print(("Welcome to the secret auction program."))
key_value = {}
result = {}
should_run = True
while should_run:
    user_name = input("What is your name?: ").lower()
    user_bid = input("What's your bid?: ").lower()
    key_value[user_name] = user_bid
    user_choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if user_choice == "yes":
        print("\n" * 20)
    elif user_choice == "no":
        print(f"the winner is {result}")
    else :
        print("wrong input !")
