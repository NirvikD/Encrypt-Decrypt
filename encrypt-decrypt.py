import string
#first we make a list of all alphabets
alphabet = list(string.ascii_letters)

#Encrypted function
def encrypt(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position= (position +shift_key)%52
            cipher_text+=alphabet[new_position]
        else:#this is to include the spaces in sentence
            cipher_text+= char
    print(f"The encrypted message is:{cipher_text}")

#Decrypted function
def decrypt(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position= (position-shift_key)%52
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char

    print(f"The decrypted message is:{plain_text}")

end=False
#user input
while not end:
    text = input("Enter your message: ")
    key = int(input("Enter the key: "))
    option = int(input("1.Encrypt 2.Decrypt\n"))
    if option==1:
        encrypt(text,key)
    elif option==2:
        decrypt(text,key)
    play_again=int(input("You want to continue 1.Yes 2.No\n"))
    if play_again==2:
        end=True
        print("EXITING>>>")







