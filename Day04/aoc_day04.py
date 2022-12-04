#!/usr/bin/env python3

# read in file and strip chr convert to list of ints
ELF_WORK = r"day4_input.txt"

# main file parser
def parse_elf_guide(elf_text : str):
    """
    Parameters
    ----------
    elf_txt : str
        Takes a string with a file path to parse using with open.
    Returns
    -------
    lst_lst_lines : list
        Returns a list of lists from the file parsing to analyze with the hashmaps.
    """
    with open(elf_text) as f_l:
        lines = f_l.readlines()
        lst_lst_lines = [i.split() for i in lines]
    return lst_lst_lines

# test parser and char list output
test_elf = parse_elf_guide(elf_text = ELF_WORK)

# print test out
print(type(test_elf[0]))
print(test_elf[0])
