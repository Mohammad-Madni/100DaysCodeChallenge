# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


#new_list = [new_item for item in list if test]
#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonethic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#new_dict = {key:value for (key, value) in dict if test}
##we put .itterrows() for the ittration through row
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

should_continue = True
while should_continue:
    try:
        word = input("Enter a Word :").upper()
        output_list = [phonethic_dict[letter] for letter in word]
        should_continue = False
    except KeyError:
        print("Sorry only letter's in the Alphabet please.")
    else:
        print(output_list)
