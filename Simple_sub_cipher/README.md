# Simple Substitution Cipher

## Overview

The Simple Substitution Cipher is a Python script that implements a basic substitution cipher for encrypting and decrypting messages. This cipher replaces each letter in the plaintext with a corresponding letter in the ciphertext based on a user-defined key. The script allows you to either enter your own key or generate a random key for encryption.

## How to Use

1. Run the script in your Python environment.

2. You'll be prompted to choose between encryption (e) or decryption (d) by entering 'e' or 'd'.

3. If you choose encryption:
   - Enter your encryption key or type 'RANDOM' to generate a random key.
   - A random key will be displayed, make sure to keep it secret.

4. If you choose decryption:
   - Enter the decryption key you used for encryption.

5. You'll be asked to enter the message you want to encrypt or decrypt.

6. The script will process the message and provide the result, either encrypted or decrypted.

7. The result will be copied to your clipboard for easy access.

## Important Notes

- If you generate a random key, it's crucial to keep it safe because it's needed for decryption.

- The substitution is a one-to-one mapping of characters from the plaintext to the ciphertext based on the key.

## Example Usage

### For Encryption
```Command line
Simple Substitution Cipher

A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.

Do you want to (e)ncrypt or (d)ecrypt : e
Please specify the key to use.
Or enter RANDOM to have one generated for you.
KEY: RANDOM

The key is XBVHPJKFRGLZDYTSOAMUWEQCIN. KEEP THIS SECRET!
Enter the message to encrypted : Hello World !!!
The encrypted message is: Fpzzt Qtazh !!!

Full encrypted text copied to clipboard.
```

### For Decryption
```Command line
Simple Substitution Cipher

A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.

Do you want to (e)ncrypt or (d)ecrypt : d
Please specify the key to use.
KEY: LRYJPFXOKGZQMHABVESNTIWUDC 


Enter the message to decrypted : Opqqa Waeqj
The decrypted message is:Hello World

Full decrypted text copied to clipboard.
```