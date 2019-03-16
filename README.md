# Cifradores

Encryption and decryption algorithms.

## Vignere Cipher
The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It is a form of polyalphabetic substitution
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
##### Execution example:
```
1. Introduce the message to encrypt:
If at first you don't succeed, call it version 1.0
2. Introduce the key:
clown
3. Introduce the word "encrypt" to encrypt the message or push Enter to decrypt:
enrypt
Enrypted message:
Gu mx sggex lmj psa'r hggpctp, gnja ux icgembl 1.0

Process finished with exit code 0
```

#### Vigenere Cypher (Dictionary Attack)
Dictionary attack is a form of brute force attack technique for defeating a cipher or authentication mechanism by trying to determine its decryption key or passphrase by trying millions of likely possibilities, such as words in a dictionary.
##### Execution example:
```
1. Introduce the message to decrypt with the dictionary attack:
Kq op skcgp lqf rka'v diypgpr, ynnw wp igcgebp 1.0
2. Introduce percentage of words in the message matching the dictionary:
40
List of decripted messages:
For key CLOWN| Decription msg -> "If at first you don't succeed, call it version 1.0"
For key CROWN| Decription msg -> "Iz at filst yoo don't mucceyd, calf it velsion 1.0"

Process finished with exit code 0
```

## Invulnerable Cypher
The invulnerable Cypher is based in the “Vigenere cipher. It becomes invulnerable to attacks when the key meets the following criteria:
```
* Key is made up of random symbols
* Key is exactly as long as the message
* Key is used only once and never again
```

##### Execution example:
```
1. Introduce the message to encrypt: 
If at first you don't succeed, call it version 1.0
Your encryption key is DLGBNYXXCTJUDAYAIZRGGIVGWAZSILTWOIWLWODWYKXYCMGWKK save it
Your encrypted message is: Lq gu sgopv rxo gol't attikmy, iwlk ab gxngqky 1.0

Process finished with exit code 0
```
Use the Vigener cypher to decrypit it.

## RSA Cypher
#### Asymmetric key generator
Module rsaUtils in utils package will save a public and private key to disk.

##### Execution example:
```
1. Introduce key file name:
myKeyName
Generating keys...
Saving myKeyName pub key in myKeyName_pub.txt...
Saving myKeyName priv key in myKeyName_priv.txt...
Asymmetric keys generation successful.

Process finished with exit code 0
```

#### RSA key generator
rsaKeyGenerator module will generate the public and private keys

##### Execution example:
```
1. Introduce key file name:
MyKeyFileName
Generating keys...
Saving MyKeyFileName pub key in MyKeyFileName_pub.txt...
Saving MyKeyFileName priv key in MyKeyFileName_priv.txt...
Asymmetric keys generation successful.

Process finished with exit code 0
```

#### Encrypt message with public key
Encrypt with RSA key module will encrypt a text file using the public key generated with the RSA key Generator module.

##### Execution example:
```
1. Introduce the file name with the msg to encrypt:
msg.txt
2. Introduce file name containing the public key:
MyKeyFileName_pub.txt
3. Introduce file name to save the encrypted msg:
encrypted.txt
Encrypting...

Process finished with exit code 0

```
#### Decrypt message with private key
Decrypt with RSA key module will decrypt a text file using the private key generated with the RSA key Generator module.

##### Execution example:
```
1. Introduce the file name with the msg to decrypt:
encrypted.txt
2. Introduce the file name containing the private key:
MyKeyFileName_priv.txt
The message is : 
This is the original message.

Process finished with exit code 0

```
## Author

* **Antonio Maldonado**
