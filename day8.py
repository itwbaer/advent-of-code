"""
You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?
"""


REGISTER = 0
MODIFIER = 1
AMOUNT = 2
COMPARISON = 4
OPERATOR = 5
CONDITION = 6


def read_instructions(input_file):
    instructions = list()
    with open(input_file) as file:
        for file_row in file:

            instructions.append(file_row.split())
    return instructions


def test_condition(registers, instruction):

    if instruction[OPERATOR] == "<=":
        return registers[instruction[COMPARISON]] <= int(instruction[CONDITION])
    elif instruction[OPERATOR] == ">=":
        return registers[instruction[COMPARISON]] >= int(instruction[CONDITION])
    elif instruction[OPERATOR] == "<":
        return registers[instruction[COMPARISON]] < int(instruction[CONDITION])
    elif instruction[OPERATOR] == ">":
        return registers[instruction[COMPARISON]] > int(instruction[CONDITION])
    elif instruction[OPERATOR] == "==":
        return registers[instruction[COMPARISON]] == int(instruction[CONDITION])
    elif instruction[OPERATOR] == "!=":
        return registers[instruction[COMPARISON]] != int(instruction[CONDITION])

def registers_part_1(input_file):

    instructions = read_instructions(input_file)

    registers = dict()


    # go through instructions
    for instruction in instructions:

        # if we haven't seen a register or comparison yet, add as a zero
        if instruction[REGISTER] not in registers:
            registers[instruction[REGISTER]] = 0
        if instruction[COMPARISON] not in registers:
            registers[instruction[COMPARISON]] = 0

        # check the condition
        condition = test_condition(registers, instruction)

        if condition:
            modifier = 1 if instruction[MODIFIER] == "inc" else -1

            registers[instruction[REGISTER]] += (int(instruction[AMOUNT]) * modifier)


    # search for largest
    largest_value = 0
    for key in registers:
        largest_value = registers[key] if registers[key] > largest_value else largest_value

    return largest_value

print(registers_part_1("day8_input.txt"))


"""
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).
"""


def registers_part_2(input_file):

    instructions = read_instructions(input_file)

    registers = dict()

    largest_value = 0
    # go through instructions
    for instruction in instructions:

        # if we haven't seen a register or comparison yet, add as a zero
        if instruction[REGISTER] not in registers:
            registers[instruction[REGISTER]] = 0
        if instruction[COMPARISON] not in registers:
            registers[instruction[COMPARISON]] = 0

        # check the condition
        condition = test_condition(registers, instruction)

        if condition:
            modifier = 1 if instruction[MODIFIER] == "inc" else -1

            registers[instruction[REGISTER]] += (int(instruction[AMOUNT]) * modifier)

            largest_value = registers[instruction[REGISTER]] if registers[instruction[REGISTER]] > largest_value else largest_value
    print(registers)
    return largest_value

print(registers_part_2("day8_input.txt"))
