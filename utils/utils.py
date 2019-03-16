import math
import utils.dictUtils


def allowed_chars():
    return utils.dictUtils.ALLOWED_MSG_CHARS


def read_file(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def read_key_file(file_name):
    with open(file_name) as f:
        content = f.read()
    return map(int, content.split(','))


def is_valid(key_size, block_size):
    return math.log(2 ** key_size, len(allowed_chars())) >= block_size
