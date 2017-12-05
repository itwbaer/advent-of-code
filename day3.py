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

"""
Build graph??

Order: E, NE, N, NW, W, SW, S, SE
"""


class SpiralNode:
    # directions N, S, E, W, NE, NW, SE, SW
    # connections to other nodes, with direction as key

    value = 0

    connections = dict()

    def add_connection(self, node, direction):
        self.connections[direction] = node

    def add_connection(self, direction):
        self.connections[direction]

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __init__(self, parent, direction):
        self.parent = parent
        self.add_connection(parent, direction)

    # connect with parent nodes in reach




def spiral_memory_part_2(input):
    # create the first node, 1
    genesis_node = SpiralNode()
    genesis_node.set_value(1)
