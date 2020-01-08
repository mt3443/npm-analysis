from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import groupby
from common_typos import common_typos

common_typos = {
        '@': ['2', 'a', '1', 'q', 'w', 'e', '3'],
        '1': ['2', 'w', 'q', 'i', 'l'],
        '2': ['1', 'q', 'w', 'e', '3'],
        '3': ['2', 'w', 'e', 'r', '4'],
        '4': ['3', 'e', 'r', 't', '5', 'a'],
        '5': ['4', 'r', 't', 'y', '6', 's'],
        '6': ['5', 't', 'y', 'u', '7'],
        '7': ['6', 'y', 'u', 'i', '8'],
        '8': ['7', 'u', 'i', 'o', '9'],
        '9': ['8', 'i', 'o', 'p', '0'],
        '0': ['9', 'o', 'p', '-', '_'],
        '-': ['_', '0', 'p', '.'],
        '_': ['-', '0', 'p', '.'],
        'q': ['1', '2', 'w', 's', 'a'],
        'w': ['1', '2', '3', 'e', 'd', 's', 'a', 'q', 'vv'],
        'e': ['2', '3', '4', 'r', 'f', 'd', 's', 'w'],
        'r': ['3', '4', '5', 't', 'g', 'f', 'd', 'e'],
        't': ['4', '5', '6', 'y', 'h', 'g', 'f', 'r'],
        'y': ['5', '6', '7', 'u', 'j', 'h', 'g', 't', 'i'],
        'u': ['6', '7', '8', 'i', 'k', 'j', 'h', 'y'],
        'i': ['1', '7', '8', '9', 'o', 'l', 'k', 'j', 'u', 'y'],
        'o': ['8', '9', '0', 'p', 'l', 'k', 'i'],
        'p': ['9', '0', '-', '_', 'l', 'o'],
        'a': ['q', 'w', 's', 'x', 'z'],
        's': ['q', 'w', 'e', 'd', 'c', 'x', 'z', 'a', '5'],
        'd': ['w', 'e', 'r', 'f', 'v', 'c', 'x', 's'],
        'f': ['e', 'r', 't', 'g', 'b', 'v', 'c', 'd'],
        'g': ['r', 't', 'y', 'h', 'n', 'b', 'v', 'f'],
        'h': ['t', 'y', 'u', 'j', 'm', 'n', 'b', 'g'],
        'j': ['y', 'u', 'i', 'k', 'm', 'n', 'h'],
        'k': ['u', 'i', 'o', 'l', 'm', 'j'],
        'l': ['i', 'o', 'p', 'k', '1'],
        'z': ['a', 's', 'x'],
        'x': ['z', 'a', 's', 'd', 'c'],
        'c': ['x', 's', 'd', 'f', 'v'],
        'v': ['c', 'd', 'f', 'g', 'b'],
        'b': ['v', 'f', 'g', 'h', 'n'],
        'n': ['b', 'g', 'h', 'j', 'm'],
        'm': ['n', 'h', 'j', 'k', 'rn'],
        '.': ['-', '_'],
        '/': ['1', 'l', 'i']
        }

def repeated_characters(str1, str2):

    # remove consecutive duplicates
    # example: 'aabbbcabbcca' becomes 'abcabca'
    s1_chars = [i[0] for i in groupby(str1)]
    s2_chars = [i[0] for i in groupby(str2)]

    return s1_chars == s2_chars

def omitted_characters(str1, str2):

    if len(str1) == len(str2):
        return False

    s1_chars = list(str1)
    s2_chars = list(str2)

    if len(s1_chars) < len(s2_chars):
        long_word = s2_chars
        short_word = s1_chars
    else:
        long_word = s1_chars
        short_word = s2_chars

    long_iterator = 0
    short_iterator = 0
    long_word_length = len(long_word)
    short_word_length = len(short_word)
    n_omitted = 0

    while long_iterator < long_word_length and short_iterator < short_word_length:
        if n_omitted == 3:
            break

        if long_word[long_iterator] == short_word[short_iterator]:
            long_iterator += 1
            short_iterator += 1
        else:
            del long_word[long_iterator]
            long_word_length -= 1
            n_omitted += 1

    return long_word == short_word

def rearranged_characters(str1, str2):
    return sorted(str1) == sorted(str2) 

def swapped_characters(str1, str2):
    if len(str1) != len(str2):
        return False

    if not rearranged_characters(str1, str2):
        return False

    s1_chars = list(str1)
    s2_chars = list(str2)

    for i in range(len(s1_chars)):
        if s1_chars[i] != s2_chars[i]:
            s1_chars[i], s1_chars[i + 1] = s1_chars[i + 1], s1_chars[i]
            return s1_chars == s2_chars

    return False

def swapped_words(str1, str2):
    return fuzz.token_sort_ratio(str1, str2) == 100

def detect_typos(testing_package, popular_package):
    # testing_package: name of the package we're testing for malicious replacements
    # popular package: benign, popular package name

    for i in range(len(testing_package)):
        for replacement in common_typos[testing_package[i]]:
            if testing_package.replace(testing_package[i], replacement, 1) == popular_package:
                return True

    return False

def highest_ratio(package_name, choices):
    return process.extractOne(package_name, choices, scorer=fuzz.ratio)
