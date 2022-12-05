#!/usr/bin/env python3
"""
Advent of Code Day 5:
    Find the most efficient algorithm to move the boxes around Santa's Queue

"""
# define parser to split the stacks from the moves
# and produce transformed lists of stacks of boxes
# and move instructions
def in_stacks_moves(in_file: str):
    """
    Parameters
    ----------
    in_file: str
        The input file path to split into stacks and moves
    Returns
    -------
    stacks: list
        List of the items in the stack.
    moves: list
        List of moves to make between the stacks.
    """
    with open(in_file) as i_f:
        stks, movs = [s.split('\n') for s in i_f.read().split('\n\n')]
    stacks = [[x for x in st if x!=' '][::-1] for st in map(list,zip(*[*stks])) if st[-1]!=' ']
    moves = [[int(y) for y in m if y.isdigit()] for m in movs]
    return stacks, moves
