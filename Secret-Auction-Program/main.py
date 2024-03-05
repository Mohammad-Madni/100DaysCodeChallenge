from art import logo
print(logo)
print(("Welcome to the secret auction program."))

user_name = input("What is your name?: ").lower()
user_bid = input("What's your bid?: ").lower()

user_choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
if user_choice == "yes":
    print("\n")
