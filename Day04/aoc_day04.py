#!/usr/bin/env python3

# read in file and strip chr convert to list of ints
ELF_WORK = r"day4_input.txt"


# convert items in list to int
def lst_int_conv(my_lst: list):
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
def parse_elf_guide(elf_text: str):
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

# Define Function to take two lists and see if they are subsets of each other
def is_lst_sbset(m: list, n: list):
    """
    Parameters
    ----------
    m: list
        A list to be compared to n
    n: list
        A list to be compared to m
    Returns
    -------
    z: int
        An integer of 1 or 0 where 1 = is_subset and 0 = not_subset
    """
    m_set = set(m)
    n_set = set(n)
    if n_set.issubset(m_set) or m_set.issubset(n_set):
        z = 1
    else:
        z = 0
    return z

# Define function to take a list of len 4 and create ranges from the 4 ints
def lst_to_range(x: list):
    """
    Parameters
    ----------
    x: list
        List of integers of length 4.
    Returns
    -------
    yn: int
        Integer of either 0 or 1. To be tallied at the end.
    """
    assert len(x) == 4
    x_0 = int(x[0])
    x_1_1 = int(x[1]) + 1
    x_2 = int(x[2])
    x_3_1 = int(x[3]) + 1
    f_range_lst = list(range(x_0, x_1_1))
    r_range_lst = list(range(x_2, x_3_1))
    # find whether the two lists are subsets
    yn = is_lst_sbset(m = f_range_lst, n = r_range_lst)
    return yn


# Parse text file into list of list of int
test_elf = parse_elf_guide(elf_text = ELF_WORK)

# print test out
# print(type(test_elf[0]))
# print(test_elf[0])
# print(type(eval(test_elf[0])))
#Parse each list of int to find whether the ranges overlap
elf_yn = [lst_to_range(x = elf) for elf in test_elf]

#Total the yn from the subset comparison of the ranges
finelf = sum(elf_yn)

# print the answer
print("The total number of overlapping elf tasks is: ", finelf)
