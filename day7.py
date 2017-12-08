"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?
"""


class ProgramNode:

    def __init__(self, name, weight):

        self.id = name
        self.weight = weight



def generate_tree(input_file):
    appearance_count = dict()
    with open(input_file) as file:
        for file_row in file:
            # seperate by tabs, add to spreadsheet
            new_row = file_row.strip().split('\t')
            # convert to ints
            new_row = list(map(int, new_row))
            spreadsheet.append(new_row)

    return spreadsheet