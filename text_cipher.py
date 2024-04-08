import sys
import os

def create_dictionary_file(file_path: str, dictionary: list):
    """
    Funkcja tworząca plik słownika.

    Args:
        file_path (str): Ścieżka do pliku słownika.
        dictionary (list): Lista elementów słownika.
        """
    with open(file_path, 'w') as file:

        dictionary = list(set(dictionary))
        file.write(','.join(dictionary))


def get_dictionary_file(file_path: str):
    """
    Funkcja odczytująca zawartość pliku słownika.

    Args:
        file_path (str): Ścieżka do pliku słownika.

    Returns:
        str: Zawartość pliku słownika.

    Raises:
        FileNotFoundError: Jeśli plik słownika nie istnieje.
    """
    try:

        with open(file_path, 'r') as file:
            return file.read()
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


def get_dictionary(dictionary: str):
    """
    Funkcja przetwarzająca zawartość słownika.

    Args:
        dictionary (str): Zawartość słownika.

    Returns:
        list: Lista elementów słownika.

    Raises:
        ValueError: Jeśli słownik ma nieparzystą liczbę elementów.
        ValueError: Jeśli słownik jest pusty.
        ValueError: Jeśli słownik zawiera zduplikowane elementy.
        ValueError: Jeśli format słownika jest niepoprawny.
    """
    try:
        dictionary = dictionary.split(',')

        if len(dictionary) % 2 != 0:
            raise ValueError("Error: Słownik musi mieć parzystą liczbę elementów, spróbuj dodać jeden więcej element do słownika.")
        
        elif len(dictionary) == 0:
            raise ValueError("Error: Słownik jest pusty")

        elif len(dictionary) != len(set(dictionary)):
            raise ValueError("Error: Słownik zawiera zduplikowane elementy, proszę usunąć duplikaty i spróbować ponownie.")

        return dictionary
    
    except:
        raise ValueError("Error: Niepoprawny format słownika, proszę sprawdzić format i spróbować ponownie. [wartość1, wartość2, wartość3, wartość4, ...]")


def encrypt_text(dictionary: list, text: str):
    """
    Funkcja szyfrująca tekst.

    Args:
        dictionary (list): Lista elementów słownika.
        text (str): Tekst do zaszyfrowania.

    Returns:
        str: Zaszyfrowany tekst.

    Raises:
        ValueError: Jeśli niektóre znaki w tekście nie znajdują się w słowniku.
    """
    encrypted_text = ""

    for letter in text:

        if letter.lower() in dictionary:

            index = dictionary.index(letter.lower())
            
            if (index + 1) % 2 == 0:

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
                raise ValueError("Error: Niektóre znaki w tekście nie znajdują się w słowniku, proszę sprawdzić zawartość tekstu lub słownika i spróbować ponownie.")

            encrypted_text += letter

    return encrypted_text

            
def decrypt_text(dictionary: list, text: str):
    """
    Funkcja deszyfrująca tekst.

    Args:
        dictionary (list): Lista elementów słownika.
        text (str): Tekst do odszyfrowania.

    Returns:
        str: Odszyfrowany tekst.

    Raises:
        ValueError: Jeśli niektóre znaki w tekście nie znajdują się w słowniku.
    """
    decrypted_text = ""

    for letter in text:

        if letter.lower() in dictionary:

            index = dictionary.index(letter.lower())
            
            if (index + 1) % 2 == 0:

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
                raise ValueError("Error: Niektóre znaki w tekście nie znajdują się w słowniku, proszę sprawdzić zawartość tekstu lub słownika i spróbować ponownie.")
            
            decrypted_text += letter

    return decrypted_text


def main():
    """
    Główna funkcja programu, która obsługuje szyfrowanie i deszyfrowanie tekstu.
    """
    args = {
        'usage': None,
        'dictionary': None,
        'text': None,
    }

    try:
        args['usage'] = sys.argv[1]
    
    except:
        print("Error: Brak podanego użycia, proszę podać -e dla szyfrowania lub -d dla deszyfrowania.")
        sys.exit(1)

    if args['usage'] == '-e':

        try:
            
            if os.path.exists(sys.argv[2]):
                
                dictionary = get_dictionary_file(sys.argv[2])
                args['text'] = sys.argv[3]

            else:

                args['text'] = sys.argv[3]
                create_dictionary_file(sys.argv[2], args['text'])
                dictionary = get_dictionary_file(sys.argv[2])
                print(f"Utworzono plik slownika o ściece: {sys.argv[2]}")

            args['text'] = sys.argv[3]
            args['dictionary'] = get_dictionary(dictionary)
            print(f'Zaszyfrowany tekst: {encrypt_text(args["dictionary"], args["text"])}')

        except:
            print("Usage: python text_cipher.py <-e or -d> <path to dictionary file> 'tekst do zaszyfrowania/odszyfrowania' ")
            sys.exit(1)

    elif args['usage'] == '-d':

        try:
            
            dictionary = get_dictionary_file(sys.argv[2])
            args['dictionary'] = get_dictionary(dictionary)
            args['text'] = sys.argv[3]
            print(f'Odszyfrowany tekst: {decrypt_text(args["dictionary"], args["text"])}')

        except:
            print("Usage: python text_cipher.py <-e or -d> dictionary.txt 'tekst do zaszyfrowania/odszyfrowania' ")
            sys.exit(1)


    args['dictionary'] = get_dictionary(dictionary)

if __name__ == "__main__":
    main()