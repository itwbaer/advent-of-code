"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?
"""



class ProgramNode:

    def __init__(self, name, weight, children_ids):

        self.id = name
        self.weight = weight
        self.parent = None
        self.children = list()
        self.children_ids = children_ids


NAME = 0
WEIGHT = 1
CHILDREN_INDICATOR = 2
CHILDREN_START = 3


def read_node_input(input_file):
    nodes = dict()
    with open(input_file) as file:
        for file_row in file:

            processed_row = file_row.split()
            processed_row[WEIGHT] = processed_row[WEIGHT].replace("(", "")
            processed_row[WEIGHT] = processed_row[WEIGHT].replace(")", "")

            children_ids = list()
            if len(processed_row) - 1 >= CHILDREN_INDICATOR:
                for i in range(CHILDREN_START, len(processed_row)):

                    processed_row[i] = processed_row[i].replace(",", "")
                    children_ids.append(processed_row[i])

            node = (ProgramNode(processed_row[NAME], int(processed_row[WEIGHT]), children_ids))
            nodes[node.id] = node

    return nodes


def recursive_circus_part_1(input_file):

    node_input = read_node_input(input_file)

    # for every node, go through and assign all of the children's parent
    for node_key in node_input:
        node = node_input[node_key]
        for child_id in node.children_ids:
            node_input[child_id].parent = node


    for node_key in node_input:
        node = node_input[node_key]
        if node.parent is None:
            return node.id


print(recursive_circus_part_1("day7_input.txt"))