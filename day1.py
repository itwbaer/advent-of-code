"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
What is the solution to your captcha?
"""


def captcha_solver_part_1(input_file):
    sum_ = 0
    digits = list()
    # read in file and go character by character to create list
    with open(input_file) as file:
        for line in file:
            for c in line:
                digits.append(int(c))
    i = 0
    for i in range(len(digits)):
        # account for circular, if at last index, check 0 not i + 1
        wrap = 0 if i + 1 >= len(digits) else 1

        sum_ = (sum_ + digits[i]) if digits[i] == digits[(i + 1)*wrap] else sum_

    return sum_


print(captcha_solver_part_1("day1_input.txt"))


"""
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
"""


def captcha_solver_part_2(input_file):
    sum_ = 0
    digits = list()
    # read in file and go character by character to create list
    with open(input_file) as file:
        for line in file:
            for c in line:
                digits.append(int(c))

    # now there is a step term
    # can assume even input per problem
    step = int(len(digits) / 2)

    #still going through whole list
    i = 0
    for i in range(len(digits)):

        # now check if digit at i + step is equal
        # is i + step >= length then wrap around
        wrap = 1 if i + step >= len(digits) else 0

        sum_ = (sum_ + digits[i]) if digits[i] == digits[(i + step) - len(digits) * wrap] else sum_

    return sum_


print(captcha_solver_part_2("day1_input.txt"))

