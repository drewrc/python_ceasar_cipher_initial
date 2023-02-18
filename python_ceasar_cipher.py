import string

alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase

def encrypt(user_text, c):
    # shift lowercase and uppercase characters by c
    shift_lower = alphabet_lowercase[c:] + alphabet_lowercase[:c]
    shift_upper = alphabet_uppercase[c:] + alphabet_uppercase[:c]

    # set encryption up to empty array that we can append
    # the value of letter to 
    encryption = []

    for e in user_text:
        if e.islower():
            letter = shift_lower[alphabet_lowercase.find(e)]
            encryption.append(letter)
        elif e.isupper():
            letter = shift_upper[alphabet_uppercase.find(e)]
            encryption.append(letter)
        else:
            encryption.append(e)

    return ''.join(encryption)

def decrypt(encrypted_text, c):
    # shift lowercase and uppercase characters by c
    shift_lower = alphabet_lowercase[c:] + alphabet_lowercase[:c]
    shift_upper = alphabet_uppercase[c:] + alphabet_uppercase[:c]

    # set decryption up to empty array that we can append
    decryption = []

    for e in encrypted_text:
        if e.islower():
            letter = alphabet_lowercase[shift_lower.find(e)]
            decryption.append(letter)
        elif e.isupper():
            letter = alphabet_uppercase[shift_upper.find(e)]
            decryption.append(letter)
        else:
            decryption.append(e)

    return ''.join(decryption)
#'c' sets the value that we want to shift the new alphabet by 


def main():
    #c = shifted amount
    c = 3

    user_text = input('Hello, user, please enter your text here: ')

    # get the encryption or decryption choice from the user
    choice = input('Do you want to encrypt or decrypt the text? (Choose: e/d?) ')

    # perform the encryption or decryption based on the user's choice
    if choice == 'e':
        result = encrypt(user_text, c)
    elif choice == 'd':
        result = decrypt(user_text, c)
    else:
        print('Please enter e or d.')

    # print the result
    print('Result:', result)

if __name__ == '__main__':
    main()