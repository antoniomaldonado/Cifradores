import math
import sys
import utils.utils as utils


def get_text_blocks(blocks_int, msg_size, block_size):
    txt = []
    for block_int in blocks_int:
        block_txt = []
        for i in reversed(range(block_size)):
            if len(txt) + i < msg_size:
                index = block_int // (len(utils.allowed_chars()) ** i)
                block_int = block_int % (len(utils.allowed_chars()) ** i)
                block_txt.insert(0, utils.allowed_chars()[index])
        txt.extend(block_txt)
    return ''.join(txt)


def get_decrypted_blocks(encrypted_blocks, msg_size, key, block_size):
    decrypted_blocks = []
    n, d = key
    for block in encrypted_blocks:
        decrypted_blocks.append(pow(block, d, n))  # text ^ dec mod num
    return get_text_blocks(decrypted_blocks, msg_size, block_size)


def decrypt(message_filename, key_filename):

    key_size, num, dec = utils.read_key_file(key_filename)
    content = utils.read_file(message_filename)
    msg_size, block_size, msg = content.split('|')
    msg_size = int(msg_size)
    block_size = int(block_size)

    if not (math.log(2 ** key_size, len(utils.allowed_chars())) >= block_size):
        sys.exit('Wrong block size. Encryption aborted.')

    blocks = []
    for block in msg.split(','):
        blocks.append(int(block))

    return get_decrypted_blocks(blocks, msg_size, (num, dec), block_size)


def main():
    print('1. Introduce the file name with the message to decrypt:')
    input_file_name = input()
    print('2. Introduce the file name containing the private key:')
    priv_key_file_name = input()
    print('The message is : ')
    print(decrypt(input_file_name, priv_key_file_name))


if __name__ == '__main__':
    main()
