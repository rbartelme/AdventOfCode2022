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
    stks, movs = [s.split('\n') for s in open(in_file).read().split("\n\n")]
    stacks = [[x for x in st if x!=' '][::-1] for st in map(list,zip(*[*stks])) if st[-1]!=' ']
    moves = [[int(y) for y in m if y.isdigit()] for m in movs]
    return stacks, moves


def find_part1(cargo, instructions):
    for moves, a, b in instructions: 
        for _ in range(moves):
            cargo[b-1].append(cargo[a-1].pop())
    return ''.join(map(lambda x: x[-1], cargo))

# solve part1
DAY5_IN = f"day5_input.txt"
stak_z, moo_vez = in_stacks_moves(in_file=DAY5_IN)
print(stak_z[0])
print(moo_vez[10])
part1_answer = find_part1(cargo=stak_z, instructions=moo_vez)
print("The answer to AoC day 5 part 1 is:", part1_answer)