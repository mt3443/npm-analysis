from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import groupby
from common_typos import common_typos

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

    while long_iterator < long_word_length and short_iterator < short_word_length:
        if long_word[long_iterator] == short_word[short_iterator]:
            long_iterator += 1
            short_iterator += 1
        else:
            del long_word[long_iterator]
            long_word_length -= 1

    return long_word[:len(short_word)] == short_word

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
