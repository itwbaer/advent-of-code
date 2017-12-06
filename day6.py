"""
 debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next-highest-indexed memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.


Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?
"""


def create_memory_banks(input_file):

    with open(input_file) as file:
        for list in file:
            block_list = list.strip().split('\t')

    memory_banks = dict()

    i = 0
    for block in block_list:
        memory_banks[i] = int(block)
        i += 1


    return memory_banks


def get_hash(memory_banks):

    hash_ = ""
    for key in memory_banks:
        hash_ += str(key) + ":" + str(memory_banks[key])

    return hash_


# automatically loops and skips current
def next_redist_i(memory_banks, current_i, skip_i):
    test_i = current_i + 1
    #test_i += 1 if current_i == skip_i else 0
    return test_i if test_i < len(memory_banks) else 0


VALUE = 1
INDEX = 0


def memory_reallocation_part_1(input_file):

    memory_banks = create_memory_banks(input_file)

    seen_states = dict()
    cycles = 0

    # current largest index and corresponding value
    current_largest = [0, 0]

    # find first largest value
    for key in memory_banks:
        # use > because we want to take lower index if tie
        if memory_banks[key] > current_largest[VALUE]:
            current_largest[INDEX] = key
            current_largest[VALUE] = memory_banks[key]

    # put first state in the seen
    seen_states[get_hash(memory_banks)] = 1

    all_unique = True

    while all_unique:

        block_redist_count = current_largest[VALUE]
        memory_banks[current_largest[INDEX]] = 0

        current_i = next_redist_i(memory_banks, current_largest[INDEX], current_largest[INDEX])

        new_largest = [0, 0]
        new_largest[VALUE] = 0
        # doing this so we for sure pick up a lower index
        new_largest[INDEX] = len(memory_banks) + 1

        while block_redist_count > 0:

            # add one to next i
            memory_banks[current_i] = memory_banks[current_i] + 1

            block_redist_count += -1

            #check if that is now the largest
            if memory_banks[current_i] >= new_largest[VALUE] and current_i < new_largest[INDEX]:
                new_largest[INDEX] = current_i
                new_largest[VALUE] = memory_banks[current_i]

            # get next i
            current_i = next_redist_i(memory_banks, current_i, current_largest[INDEX])


        current_largest = new_largest

        # increment cycles
        cycles += 1

        # if we have seen this state, exit loop, else add to see
        if get_hash(memory_banks) in seen_states:
            all_unique = False
        else:
            seen_states[get_hash(memory_banks)] = 1

    return cycles



print(memory_reallocation_part_1("day6_input.txt"))

# 385, 562, 761 too low
# not taking lowest index right?