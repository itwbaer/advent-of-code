"""

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?
Your puzzle input is 347991
"""

"""
Works but would like to make more elegant later, like topographical map
"""

"""
1x1, then 3x3, then 5x5
pattern is 2s - 1 = height & width where n is the spiral and s = 1 is just the number 1


will need to calculate how big of an s we need based on an input
input is the area or might need a bigger area
sqrt(input) is height/width (take ceiling if not whole number), then calculate s. If s not whole number, then bump h/w up one
denoting height and width as size


by knowing s, we know how many steps we need to take if the input in horizontally or vertically on line with 1, will be s-1
know 1 will be at the center, or at (s-1,s-1)
can create a local spiral where input is located to find out how much it is offset from 1, which will be called weight
"""

import math


def calculate_size(input):
    size = math.ceil(math.sqrt(input))
    return size if (size + 1) % 2 == 0 else (size + 1)


def calculate_aligned_values(size):
    aligned_values = list()
    aligned_values.append(size ** 2 - ((size - 1) / 2))
    aligned_values.append(aligned_values[0] - (size - 1))
    aligned_values.append(aligned_values[1] - (size - 1))
    aligned_values.append(aligned_values[2] - (size - 1))

    return aligned_values


def spiral_memory_part_1(input):
    size = calculate_size(input)
    n_spirals = int((size + 1) / 2)

    # points horizontal and vertical to 1
    aligned_values = calculate_aligned_values(size)

    # compare input to aligned values to calculate a weight from center
    weight = input
    for value in aligned_values:
        weight = abs(value - input) if abs(value - input) < weight else weight

    steps = n_spirals - 1 + weight

    return steps


print(spiral_memory_part_1(347991))

"""
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?
"""


def expand_grid(spiral_grid):
    original_size = len(spiral_grid)
    new_size = original_size + 2
    # insert a top and bottom row of zeroes
    # insert leading and trailing zero
    spiral_grid.insert(0, [0] * original_size)
    spiral_grid.append([0] * original_size)
    for i in range(new_size):
        spiral_grid[i].insert(0, 0)
        spiral_grid[i].append(0)

    return spiral_grid


def calculate_index(spiral_grid, i, j):

    possible_moves = [[0, 1],
                        [0, -1],
                        [1, 0],
                        [-1, 0],
                        [1, 1],
                        [1, -1],
                        [-1, 1],
                        [-1, -1]
                    ]

    sum_ = 0
    # add adjacent indexies if in bounds
    for move in possible_moves:
        move_i = move[0] + i
        move_j = move[1] + j

        y_bound = True if 0 <= move_i and move_i <= len(spiral_grid) - 1 else False
        x_bound = True if 0 <= move_j and move_j <= len(spiral_grid) - 1 else False

        if y_bound and x_bound:
            sum_ += spiral_grid[move_i][move_j]

    return sum_


def calculate_spiral_pattern(spiral_grid):

    pattern = list()
    # always start one up from bottom right
    i = len(spiral_grid) - 2
    j = len(spiral_grid) - 1

    # go up
    while i > 0:
        pattern.append([i, j])
        i += -1

    # go left
    while j > 0:
        pattern.append([i, j])
        j += -1

    # go down
    while i < len(spiral_grid) - 1:
        pattern.append([i, j])
        i += 1

    # go right
    while j <= len(spiral_grid) - 1:
        pattern.append([i, j])
        j += 1

    return pattern


def spiral_memory_part_2(target):

    # starts with just 1
    spiral_grid = [[1]]

    # will need to stop once we've seen our target
    largest_seen = spiral_grid[0][0]

    build_grid = True

    while build_grid:

        # expand grid
        spiral_grid = expand_grid(spiral_grid)


        # fill it out
        pattern = calculate_spiral_pattern(spiral_grid)

        for pair in pattern:
            i = pair[0]
            j = pair[1]
            spiral_grid[i][j] = calculate_index(spiral_grid, i, j)
            largest_seen = spiral_grid[i][j] if spiral_grid[i][j] > largest_seen else largest_seen

            if largest_seen > target:
                build_grid = False
                break



    return largest_seen


print(spiral_memory_part_2(347991))

