"""

he message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example, these offset values will be written all on one line, with the current instruction marked in parentheses. The following steps would be taken before an exit is found:

How many steps does it take to reach the exit?
"""


def read_instructions(input_file):

    instructions = list()
    with open(input_file) as file:
        for file_row in file:
            instructions.append(int(file_row.strip('\n')))

    return instructions


def cpu_maze_part_1(input_file):

    instructions = read_instructions(input_file)

    steps = 0
    exited = False
    i = 0
    while not exited:
        # find next i based on current position
        next_i = i + instructions[i]

        # increment current instruction by 1
        instructions[i] += 1

        #if next_i exceeds list, we escaped
        exited = True if next_i >= len(instructions) else False

        # increment steps
        steps += 1

        # move to next i
        i = next_i

    return steps


print(cpu_maze_part_1("day5_input.txt"))


"""
Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""

def cpu_maze_part_2(input_file):

    instructions = read_instructions(input_file)

    steps = 0
    exited = False
    i = 0
    while not exited:
        # find next i based on current position
        next_i = i + instructions[i]

        # if 3 or more, decrease by 1, else increase by 1
        instructions[i] += -1 if instructions[i] >= 3 else 1

        #if next_i exceeds list, we escaped
        exited = True if next_i >= len(instructions) else False

        # increment steps
        steps += 1

        # move to next i
        i = next_i

    return steps


print(cpu_maze_part_2("day5_input.txt"))
