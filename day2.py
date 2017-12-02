"""
The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
"""


def generate_spreadsheet(input_file):
    spreadsheet = list()
    with open(input_file) as file:
        for file_row in file:
            # seperate by tabs, add to spreadsheet
            new_row = file_row.strip().split('\t')
            # convert to ints
            new_row = list(map(int, new_row))
            spreadsheet.append(new_row)

    return spreadsheet


def spreadsheet_checksum_part_1(input_file):

    # read in input
    spreadsheet = generate_spreadsheet(input_file)
    checksum = 0

    for row in spreadsheet:
        # for every row, keep a largest and smallest value, check all others against current
        # assume first element
        smallest = row[0]
        largest = row[0]
        for column in row:
            smallest = column if column < smallest else smallest
            largest = column if column > largest else largest

        checksum += largest - smallest

    return checksum


print(spreadsheet_checksum_part_1("day2_input.txt"))

"""
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.
"""


def spreadsheet_checksum_part_2(input_file):

    spreadsheet = generate_spreadsheet(input_file)
    checksum = 0

    # brute force answer is n^2 loop over each row
    # if we sort the rows, we can reduce to n log n because we dont have to see if a bigger value divides smaller one
    for row in spreadsheet:
        row.sort(reverse=True)

        # assume only 1 division works?
        i = 0
        while i < len(row):
            current = row[i]
            j = i + 1
            while j < len(row):
                if current % row[j] == 0:
                    checksum += int(current / row[j])
                j += 1
            i += 1

    return checksum


print(spreadsheet_checksum_part_2("day2_input.txt"))