#!/usr/bin/env python3

"""
Advent of Code Day 02
Ryan Bartelme
"""

# hashmaps for translating char into game strings
opponent_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
your_choices = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
match_score = {"Loss": 0, "Draw": 3, "Win": 6}
rnd2_choice = {"X": "Loss", "Y": "Draw", "Z" : "Win"}


# Match outcome algorithm
def win_lose_draw(opp : str, you : str):
    """
    Parameters
    ----------
    opp : str
        The opponent's choice of rock/paper/scissors as a string.
    you : str
        Your choice of rock/paper/scissors as a string.

    Returns
    -------
    outcome : str
        The outcome of the rock paper scissors match.
    """

    if opp == you:
        outcome = "Draw"
    elif you == "Scissors":
        if opp == "Paper":
            outcome = "Win"
        else:
            outcome = "Loss"
    elif you == "Paper":
        if opp == "Rock":
            outcome = "Win"
        else:
            outcome = "Loss"
    elif you == "Rock":
        if opp == "Scissors":
            outcome = "Win"
        else:
            outcome = "Loss"
    else:
        print("Well that ain't right, this just terminates the logic.")

    return outcome


def find_shape_by_outcome(opp : str, outcome : str):
    """
    Parameters
    ----------
    opp : str
        The opponent's choice of rock/paper/scissors as a string.
    outcome : str
        Whether you won or lost the

    Returns
    -------
    you : str
        Your choice of shape in the rock paper scissors match.
    """
    #initialize you
    you = ""
    if outcome == "Draw":
        you = opp
    elif outcome == "Win" and opp == "Scissors":
        you = "Rock"
    elif outcome == "Win" and opp == "Paper":
        you = "Scissors"
    elif outcome == "Win" and opp == "Rock":
        you = "Paper"
    elif outcome == "Lose" and opp == "Rock":
        you = "Scissors"
    elif outcome == "Lose" and opp == "Paper":
        you = "Rock"
    elif outcome == "Lose" and opp == "Scissors":
        you = "Paper"
    else:
        print("Well that ain't right, this just terminates the logic.")
    return you

# generic parser for the dictionaries
def generic_dict_parser(dct : dict, input_str : str):
    # initialize match_val
    match_val = None
    if input_str in list(dct):
        match_val = dct[input_str]
    else:
        print("String {input_str} not found in keys of {dct}")
    return match_val


def score_input(match : list, opp_choice : dict, your_choice : dict, shape_points : dict, match_points : dict):
    """
    Parameters
    ----------
    match : list
        The inner list from the list of lists generated by the file parser,
    opp_choice : dict
        Dictionary of what the characters translated into rock/paper/scissors are.
    your_choice : dict
        Dictionary of your rock/paper/scissors responses mapped to the provided key.
    shape_points : dict
        Dictionary mapping the shape (rock, paper, or scissors) and the points for choosing it.
    match_points : dict
        Dictionary mapping the points for the outcome of match. Assessed on the results of win_lose_draw()

    Returns
    -------
    final_score : int
        The final score of the match as an integer.

    """
    opponent_raw_value = str(match[0])
    your_raw_value = str(match[1])
    # parse opponent dict
    opp_call = generic_dict_parser(dct = opp_choice, input_str = opponent_raw_value)
    # parse your dict
    your_call = generic_dict_parser(dct = your_choice, input_str = your_raw_value)
    # get points for choice
    call_pts = generic_dict_parser(dct = shape_points, input_str = your_call)
    # determine match outcome
    match_result = win_lose_draw(opp = opp_call, you = your_call)
    # get points for match
    match_tally = generic_dict_parser(dct = match_points, input_str = match_result)
    # tally score to put into the list output
    final_score = call_pts + match_tally
    return final_score

def outcome_to_score(match : list, opp_choice : dict, match_outcome : dict, shape_points : dict, match_points : dict):
    """
    Parameters
    ----------
    match : list
        The inner list from the list of lists generated by the file parser,
    opp_choice : dict
        Dictionary of what the characters translated into rock/paper/scissors are.
    match_outcome : dict
        Key for matchoutcome translation.
    shape_points : dict
        Dictionary mapping the shape (rock, paper, or scissors) and the points for choosing it.
    match_points : dict
        Dictionary mapping the points for the outcome of match. Assessed on the results of win_lose_draw()
    Returns
    -------
    final_score : int
        The final score of the match as an integer.
    """
    opponent_raw_value = str(match[0])
    raw_match_result = str(match[1])
    # parse opponent dict
    opp_call = generic_dict_parser(dct = opp_choice, input_str = opponent_raw_value)
    # parse match result
    match_out = generic_dict_parser(dct = match_outcome, input_str = raw_match_result)
    # find your shape
    shape_called = find_shape_by_outcome(opp = opp_call, outcome = match_out)
    # get points for choice
    call_pts = generic_dict_parser(dct = shape_points, input_str = shape_called)
    # get points for match
    match_tally = generic_dict_parser(dct = match_points, input_str = match_out)
    # tally score to put into the list output
    final_score = call_pts + match_tally
    return final_score


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


# calculate the answer procedurally with the glut of hashmaps
ELF_GUIDE = r"day2_input.txt"
foo_lst = parse_elf_guide(elf_text = ELF_GUIDE)

# part 1
lst_match_scores = [score_input(match = mtch, opp_choice = opponent_choices, \
        your_choice = your_choices, shape_points = shape_score, match_points = match_score) \
        for mtch in foo_lst]
elf_beta = sum(lst_match_scores)
print("Part 1: Your total score would be: ", elf_beta)

# part 2

# parse fileline list to specify the score for each match via rnd2_choice
pt2_adjusted_scores = [outcome_to_score(match = mtch2, \
                                             opp_choice = opponent_choices, \
                                             match_outcome = rnd2_choice, \
                                             shape_points = shape_score, \
                                             match_points = match_score) \
                       for mtch2 in foo_lst]
# sum the list
elf_rnd2 = sum(pt2_adjusted_scores)
print("Part 2: Your total revised score would be: ", elf_rnd2)


