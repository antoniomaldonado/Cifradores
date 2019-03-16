import vigenereCipher
from utils import language, dictUtils


def hack_vigenere_dictionary(ciphertext, accuracy):

    words = dictUtils.load_dictionary('dictionary.txt')

    print('List of decripted messages:')
    for word in words:
        word = word.strip()
        decrypted_text = vigenereCipher.decrypt_msg(word, ciphertext)
        if language.is_english(decrypted_text, word_percentage=accuracy):
            print('For key ' + str(word) + '| Decription msg -> "'
                  + decrypted_text[:100] + '"')


def main():

    print('1. Introduce the message to decrypt with the dictionary attack:')
    msg = input()
    print('2. Introduce percent of words in the msg matching the dictionary:')
    accuracy = int(input())

    hack_vigenere_dictionary(msg, accuracy)


if __name__ == '__main__':
    main()
