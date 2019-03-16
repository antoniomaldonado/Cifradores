import utils.dictUtils


def is_english(message, word_percentage=20, letter_percentage=80):

    if word_percentage > 100:
        word_percentage = 100
    elif word_percentage < 10:
        word_percentage = 10

    letters_percent_in_msg = \
        float(len(remove_non_alpha(message))) / len(message) * 100
    return get_valid_words_count(message) * 100 >= word_percentage \
        and letters_percent_in_msg >= letter_percentage


def remove_non_alpha(message):
    letters_only = []
    for symbol in message:
        if symbol in utils.dictUtils.ALPHABET_UP_LO_BLANK:
            letters_only.append(symbol)
    return ''.join(letters_only)


def get_valid_words_count(message):

    words = remove_non_alpha(message.upper()).split()

    if words == []:
        return 0.0

    matches = 0
    for word in words:
        if word in DICTIONARY:
            matches += 1

    return float(matches) / len(words)


DICTIONARY = utils.dictUtils.load_dictionary('dictionary.txt')
