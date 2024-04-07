import sys

def get_dictionary_file(file_path: str):

    try:
        with open(file_path, 'r') as file:
            return file.read()
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


def get_dictionary(dictionary: str):

    try:

        dictionary = dictionary.split(',')

        if len(dictionary) %2 != 0:
            print("Error: Dcitionary needs to have an even number of elements, try adding one more element to the dictionary.")
            sys.exit(1)
        
        elif len(dictionary) == 0:
            print("Error: Dictionary is empty")
            sys.exit(1)

        elif len(dictionary) != len(set(dictionary)):
            print("Error: Dictionary has duplicate elements, please remove the duplicates and try again.")
            sys.exit(1)

        return dictionary
    
    except:

        print("Error: Dictionary format is incorrect, please check the format and try again. [value1,value2,value3,value4,...]")
        sys.exit(1)


def encrypt_text(dictionary: list, text: str):

    encrypted_text = ""

    for letter in text:

        if letter.lower() in dictionary:

            index = dictionary.index(letter.lower())
            
            if (index + 1) %2 == 0:

                if letter.isupper():
                    encrypted_text += dictionary[(index-1) % len(dictionary)].upper()

                else:
                    encrypted_text += dictionary[(index-1) % len(dictionary)]
            
            else:

                if letter.isupper():
                    encrypted_text += dictionary[(index+1) % len(dictionary)].upper()

                else:
                    encrypted_text += dictionary[(index+1) % len(dictionary)]
    
        else:

            if letter.isalpha():
                
                print("Error: Some characters in the text are not in the dictionary, please check the text or dictionary content and try again.")
                sys.exit(1)

            encrypted_text += letter

    return encrypted_text

            
def decrypt_text(dictionary: list, text: str):

    decrypted_text = ""

    for letter in text:

        if letter.lower() in dictionary:

            index = dictionary.index(letter.lower())
            
            if (index + 1) %2 == 0:

                if letter.isupper():
                    decrypted_text += dictionary[(index-1) % len(dictionary)].upper()

                else:
                    decrypted_text += dictionary[(index-1) % len(dictionary)]
            
            else:

                if letter.isupper():
                    decrypted_text += dictionary[(index+1) % len(dictionary)].upper()

                else:
                    decrypted_text += dictionary[(index+1) % len(dictionary)]
    
        else:

            if letter.isalpha():

                print("Error: Some characters in the text are not in the dictionary, please check the text or dictionary content and try again.")
                sys.exit(1)
            
            decrypted_text += letter

    return decrypted_text


def main():

    args = {
        'usage': None,
        'dictionary': None,
        'text': None,
    }

    try:
        args['usage'] = sys.argv[1]
    
    except:
        print("Error: Usage is missing, please provide the usage -e for encryption or -d for decryption.")
        sys.exit(1)

    if args['usage'] == '-e':

        try:
            
            dictionary = get_dictionary_file(sys.argv[2])
            args['dictionary'] = get_dictionary(dictionary)
            args['text'] = sys.argv[3]
            print(f'Encrypted text: {encrypt_text(args["dictionary"], args["text"])}')

        except:
            print("Usage: python text_cipher.py <-e or -d> dictionary.txt 'text to encrypt/decrypt' ")
            sys.exit(1)

    elif args['usage'] == '-d':

        try:
            
            dictionary = get_dictionary_file(sys.argv[2])
            args['dictionary'] = get_dictionary(dictionary)
            args['text'] = sys.argv[3]
            print(f'Decrypted text: {decrypt_text(args["dictionary"], args["text"])}')

        except:
            print("Usage: python text_cipher.py <-e or -d> dictionary.txt 'text to encrypt/decrypt' ")
            sys.exit(1)


    args['dictionary'] = get_dictionary(dictionary)



if __name__ == "__main__":
    main()