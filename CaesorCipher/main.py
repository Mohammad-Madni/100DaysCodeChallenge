alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
def caesor(plain_text, plain_shift, plain_direction):
    result = ""

    for i in plain_text:
        # TODO-3: What happens if the user enter a number/symbol/space?
        # Can you fix this code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if i in alphabet:
            indexs = alphabet.index(i)
            if plain_direction == "encode":
                no_shifts = indexs + plain_shift
            elif plain_direction == "decode":
                no_shifts = indexs - plain_shift
            else:
                print("Invalid Input !")
            result += alphabet[no_shifts]
        else:
            result += i
    print(f"Your {plain_direction}d message is = {result}")

repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesor(plain_text = text, plain_shift = shift, plain_direction = direction)
    chose = input("Do you want to start Cipher again ? Type 'Yes' or 'No' \n").lower()
    if chose == "no":
        repeat = False
        print("Good Bye !")