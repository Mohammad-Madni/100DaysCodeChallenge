alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesor(plain_text, plain_shift, plain_direction):
    result = ""
    for i in plain_text:
        indexs = alphabet.index(i)
        if plain_direction == "encode":
            no_shifts = indexs + plain_shift
        elif plain_direction == "decode":
            no_shifts = indexs - plain_shift
        else:
            print("Invalid Input !")
        result += alphabet[no_shifts]
    print(f"You Result is = {result}")
caesor(plain_text = text, plain_shift = shift, plain_direction = direction)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.