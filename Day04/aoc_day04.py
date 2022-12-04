#!/usr/bin/env python3

# read in file and strip chr convert to list of ints
ELF_WORK = r"day4_input.txt"

# convert items in list to int
def lst_int_conv(my_lst : list):
    """
    Parameters
    ----------
    my_lst : list
        A list of ints that are currently encoded as str.
    Returns
    -------
    my_ints : list
        A list of integers from input str encodings.
    """
    my_ints = [int(my_i) for my_i in my_lst]
    return my_ints

# main file parser
def parse_elf_guide(elf_text : str):
    """
    Parameters
    ----------
    elf_txt : str
        Takes a string with a file path to parse using with open.
    Returns
    -------
    lst_ints : list
        Returns a list of lists of ints from the file parsing.
    """
    with open(elf_text) as f_l:
        # read in file as a list of each line as a str
        lines = f_l.readlines()
        # get rid of the new line statements
        lst_str = [line.rstrip('\r\n') for line in lines]
        # prep work for eval into a list of ints encoded as characters
        lst_lst_lines = [(n.replace(",", "','").replace("-", "','"))\
                         for n in lst_str]
        # encapsulate the string with list text
        lst_lst_lines = ["['" + m + "']" for m in lst_lst_lines]
        # evaluate our strings that are now actually python code
        lst_range_lines = [eval(z) for z in lst_lst_lines]
        # convert our ints that are str back to ints now that there's a list
        lst_ints = [lst_int_conv(nn) for nn in lst_range_lines]
        return lst_ints

# test parser and char list output
test_elf = parse_elf_guide(elf_text = ELF_WORK)

# print test out
print(type(test_elf[0]))
print(test_elf[0])
#print(type(eval(test_elf[0])))
