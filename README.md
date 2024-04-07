
# Text Cipher

This program allows you to encrypt and decrypt text using a dictionary-based cipher.

## Usage

To encrypt text, use the following command:
```
python text_cipher.py -e <path to dictionary file> 'text to encrypt'
```

To decrypt text, use the following command:
```
python text_cipher.py -d <path to dictionary file> 'text to decrypt'
```

Make sure to replace `<path to dictionary file>` with the path to your dictionary file, and `'text to encrypt'` or `'text to decrypt'` with the actual text you want to encrypt or decrypt.

## Dictionary Format

The dictionary file should contain a comma-separated list of letters without duplicated. All the letters in dictionary should be placed in the same order and content to ensure proper decryption. While encrypting, all letters used in plain text should be placed in dictionary file.

''' 
a,b,c,d,e,f,g
```

The dictionary must have an even number of elements, and each plaintext word should be unique.

## Error Handling

The program will raise a `ValueError` if any of the following conditions are met:
- The dictionary has an odd number of elements.
- The dictionary is empty.
- The dictionary contains duplicate elements.
- The text contains characters that are not in the dictionary.

