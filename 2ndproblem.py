# Kenneth John Costa
# Assignment #2
# Decryption

print("DECRYPTION".center(45, "="))

# Ask the user to enter the message to decrypt
while True:
    encrypted_message = input("\033[96mPlease enter the message you want to decrypt: ")
    decrypted_message = ""
    
#Substitute the characters by replacing it to corresponding vowels
    for i in range(len(encrypted_message)):

# If the character is *, change to a
        if encrypted_message[i] == "*":
            decrypted_message += "a"

# If the character is &, change to e
        elif encrypted_message[i] == "&":
            decrypted_message += "e"

# If the character is #, change to i
        elif encrypted_message[i] == "#":
            decrypted_message += "i"

# If the character is +, change to o
        elif encrypted_message[i] == "+":
            decrypted_message += "o"

# If the character is !, change to u
        elif encrypted_message[i] == "!":
            decrypted_message += "u"
        else:
            decrypted_message += encrypted_message[i]

# Print the decrypted message
    print("\033[93mThe decrypted message is:", decrypted_message)
    
# Ask the user if he/she wants to decrypt again