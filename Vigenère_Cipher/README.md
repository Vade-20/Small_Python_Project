# Vigenère Cipher 

## Overview

This Python script implements the Vigenère cipher, a polyalphabetic substitution cipher that provides a more secure encryption compared to simple substitution ciphers. The Vigenère cipher uses a keyword to shift letters in the plaintext, creating a complex pattern of substitutions.

## Requirements

To run this script, ensure that you have the following dependencies installed:

- [pyperclip](https://pypi.org/project/pyperclip/): Used for copying the encrypted or decrypted text to the clipboard.

You can install the required package using the following command:

```bash
pip install pyperclip
```

## How to Use

1. Run the script in a Python environment.

   ```bash
   python vigenere_cipher.py
   ```

2. The script will prompt you to choose between encryption and decryption by entering 'e' or 'd', respectively.

3. Enter the key to be used for encryption or decryption. The key should be a word or any combination of letters without spaces.

4. Input the message you want to encrypt or decrypt.

5. The result will be displayed on the console, and the full text will be copied to the clipboard for easy sharing.

## Example

```plaintext
Vigenère Cipher
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.

Do you want to (e)ncrypt or (d)ecrypt?
> e

Please specify the key to use.
It can be a word or any combination of letters withouse spaces:
> key

Enter the message to encrypt.
> HelloWorld

Encrypted message:
RijvsUyvjn
```

## Notes

- Ensure that the key provided is alphabets only. 
- The encrypted or decrypted text is automatically copied to the clipboard for your convenience.

