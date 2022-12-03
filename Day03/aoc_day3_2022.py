#!/usr/bin/env python3
"""
Advent of Code Day 3
Ryan Bartelme
"""

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
        Returns a list of lists from the file parsing to analyze.
    """
    with open(elf_text) as f_l:
        lines = f_l.readlines()
        lst_lst_lines = [i.split() for i in lines]
    return lst_lst_lines

# function to split a file line list into a set
def splt_lst_to_set(lst_str_in : str):
    """
    Parameters
    ----------
    lst_str_in : str
        Takes a str as an input list-ifies it and splits the list in half.

    Returns
    -------
    u_of_s : str
        The union of the two split lists as sets.
    """
    lst_in = []
    lst_in = [z for z in lst_str_in]
    half = len(lst_in)//2
    lsta = lst_in[half:]
    lstb = lst_in[:half]
    bw_union = set(lsta) & set(lstb)
    return bw_union

smol_letters = list(map(chr, range(97, 123)))
big_letters = list(map(chr, range(65, 91)))
lst_of_letters = smol_letters + big_letters
letter_vals = list(range(1, 53))

letter_pts_map = dict(zip(lst_of_letters, letter_vals))

ELF_PACKING_LIST = r"./day3_input.txt"

ln_lst = parse_elf_guide(elf_text = ELF_PACKING_LIST)

un_letters  = [splt_lst_to_set(ii) for ii in ln_lst]

print(un_letters[2])
