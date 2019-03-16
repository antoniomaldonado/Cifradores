import utils.dictUtils
import secrets
import vigenereCipher


def get_key(size):
    key = ''
    for i in range(size):
        key += secrets.choice(utils.dictUtils.ALPHABET_UPPER)
    return key


def main():
    print('1. Introduce the message to encrypt: ')
    message = input()
    key = get_key(len(message))
    print('Your encryption key is', key, 'Save it!')
    print('Your encrypted message is:',
          vigenereCipher.encrypt_msg(key, message))


if __name__ == '__main__':
    main()
