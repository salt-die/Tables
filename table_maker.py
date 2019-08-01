#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def table_maker(my_lists=[['John Smith', '356 Grove Rd', '123-4567'],\
                          ['Mary Sue', '311 Penny Lane', '555-2451'],\
                          ['A Rolling Stone', 'N/A', 'N/A']],\
                headers=['Name', 'Address', 'Phone Number']):
    """
    Takes a list of lists, my_lists, and a list, headers, and prints an
    aligned table with columns labeled by items in headers and with each row as
    a sublist of my_lists.

    Each sublist of my_lists should have the same length as headers.

    Default output looks like:
    ┌─────────────────┬────────────────┬──────────────┐
    │ Name            │ Address        │ Phone Number │
    ├─────────────────┼────────────────┼──────────────┤
    │ John Smith      │ 356 Grove Rd   │ 123-4567     │
    │ Mary Sue        │ 311 Penny Lane │ 555-2451     │
    │ A Rolling Stone │ N/A            │ N/A          │
    └─────────────────┴────────────────┴──────────────┘
    """
    number_of_columns = len(headers)

    #Check that sizes match up
    for my_list in my_lists:
        if len(my_list) != number_of_columns:
            return "Number of items in rows don't match number of headers."

    my_lists.insert(0, headers) #Combine headers and my_lists
    table = zip(*my_lists) #Transpose my_lists to iterate over columns
    lengths = [] #Used later in box_drawing() to find correct number of '─''s
    for i, column in enumerate(table):
        max_length = max([len(item) for item in column])
        lengths.append(max_length)
        #Pad the length of items in each column
        for j, item in enumerate(column):
            my_lists[j][i] += " " * (max_length - len(item))

    #Construct table
    table = "\n".join("│ " + " │ ".join(row) + " │" for row in my_lists) + "\n"
    #Use row_length to insert the second box_drawing line in the correct place
    row_length = sum(lengths) + number_of_columns * 3 + 2

    def box_drawing(i):
        """
        Returns the box-line seperators.
        """
        left, mid, right = [("┌", "┬", "┐"),\
                            ("├", "┼", "┤"),\
                            ("└", "┴", "┘")][i]
        return left + mid.join("─" * (length + 2)\
                               for length in lengths) + right

    table = box_drawing(0) + "\n" +\
            table[:row_length] +\
            box_drawing(1) + "\n" +\
            table[row_length:] +\
            box_drawing(2)

    print(table)
    #return table #Alternatively use this line to save the table as a string
