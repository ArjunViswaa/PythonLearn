import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(original_text, shift_amount) : 
#     cipher_text = ""
#     for letter in original_text : 
#         shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
#         cipher_text += alphabet[shifted_position]
    
#     print(f"Here is the encoded result : {cipher_text}")

# def decrypt(encrypted_text, shift_amount) : 
#     original_text = ""
#     for letter in encrypted_text : 
#         shifted_position = (alphabet.index(letter) - shift_amount)
#         original_text += alphabet[shifted_position]
    
#     print(f"Here is the decoded text : {original_text}")


def caesar(original_text, shift_amount, encode_or_decode) : 
    output_text = ""

    if encode_or_decode == "decode" : 
        shift_amount *= -1

    for letter in original_text : 
        if letter not in alphabet : 
            output_text += letter
        else : 
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d text : {output_text}")

shouldContinue = True
while shouldContinue : 
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() == "no" : 
        shouldContinue = False
        print("Goodbye!!!")