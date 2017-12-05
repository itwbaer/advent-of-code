"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""


def read_passwords(input_file):
    passwords = list()
    with open(input_file) as file:
        for file_row in file:
            passwords.append(file_row.strip('\n'))

    return passwords


def passphrase_validity_part_1(input_file):
    passwords = read_passwords(input_file)
    valid_sum = 0

    for password in passwords:
        # need a dictionary to store already used words
        used = dict()
        # process the password into list to make it easier to read
        password = password.split()

        # validate password, can't be duplicate
        valid = True
        for word in password:
            if word in used:
                valid = False
            else:
                used[word] = 1

        valid_sum += 1 if valid else 0

    return valid_sum


print(passphrase_validity_part_1("day4_input.txt"))

"""
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
"""


def passphrase_validity_part_2(input_file):
    passwords = read_passwords(input_file)
    valid_sum = 0

    for password in passwords:
        # need a dictionary to store already used words
        used = dict()
        # process the password into list to make it easier to read
        password = password.split()

        # validate password, can't be duplicate, can't be anagram
        valid = True
        for word in password:

            # instead of just checking word, check the sorted word
            word = list(word)
            word.sort()
            word = ''.join(word)

            if word in used:
                valid = False
            else:
                used[word] = 1

        valid_sum += 1 if valid else 0

    return valid_sum


print(passphrase_validity_part_2("day4_input.txt"))
