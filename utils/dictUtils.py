import data
import os

BLANK_CHARS = ' \t\n'
NUMBERS = '0123456789'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_LOWER = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UP_LO = ALPHABET_UPPER + ALPHABET_LOWER
ALPHABET_UP_LO_BLANK = ALPHABET_UPPER + ALPHABET_LOWER + BLANK_CHARS
ALLOWED_MSG_CHARS = ALPHABET_UPPER + ALPHABET_LOWER + NUMBERS + ' !?.'


def get_data_file(file_name):
    dir_name = os.path.dirname(data.__file__)
    file_name = os.path.join(dir_name, file_name)
    return open(file_name)


def load_dictionary(file_name):
    dictionary = get_data_file(file_name)
    english_words = {}
    for word in dictionary.read().split('\n'):
        english_words[word] = None
    dictionary.close()
    return english_words
