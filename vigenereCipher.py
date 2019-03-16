import utils.dictUtils


def encrypt_msg(key, message):
    return translate_msg(key, message, 'encrypt')


def decrypt_msg(key, message):
    return translate_msg(key, message, '')


def translate_msg(key, message, mode):
    translated = []

    key = key.upper()
    key_index = 0
    is_encrypt = mode == 'encrypt'

    for symbol in message:
        offset = get_alphabet().find(symbol.upper())
        if exist_symbol(offset):
            offset = get_alphabet_offset(is_encrypt, key, key_index, offset)
            if symbol.isupper():
                translated.append(get_alphabet()[offset])
            elif symbol.islower():
                translated.append(get_alphabet()[offset].lower())
            key_index = key_iter(key, key_index)
        else:
            translated.append(symbol)

    return ''.join(translated)


def exist_symbol(offset):
    return offset != -1


def get_alphabet():
    return utils.dictUtils.ALPHABET_UPPER


def get_alphabet_offset(is_encript, key, key_index, offset):
    if is_encript:
        offset += get_alphabet().find(key[key_index])
    else:
        offset -= get_alphabet().find(key[key_index])
    offset %= len(get_alphabet())
    return offset


def key_iter(key, key_index):
    key_index += 1
    if key_index == len(key):
        key_index = 0
    return key_index


def main():

    print('1. Introduce a message: ')
    message = input()
    print('2. Introduce the key: ')
    key = input()
    print('3. Introduce the word "encrypt" to encrypt the message or push '
          'Enter to decrypt: ')
    mode = input().lower()

    if mode == 'encrypt':
        translated = encrypt_msg(key, message)
    else:
        translated = decrypt_msg(key, message)

    print('%sed message:' % (mode.title()))
    print(translated)


if __name__ == '__main__':
    main()
