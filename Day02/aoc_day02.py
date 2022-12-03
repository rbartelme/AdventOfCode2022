#!/usr/bin/env python3


# hashmaps for translating char into game strings
opponent_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
your_choices = {"X": "Rock", "Y": "Paper", "C": "Scissors"}
shape_score = {"Rock": "1", "Paper": "2", "Scissors": "3"}
match_score = {"Loss": "0", "Draw": "3", "Win": "6"}


# Match outcome algorithm
def win_lose_draw(opp : str, you : str):
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

# generic parser for the dictionaries
def generic_dict_parser(dct : dict, input_str : str):
    if input_str in list(dct):
        match_val = dct[input_str]
    else:
        raise Exception
    return match_val


def score_input(match : list, opp_choice : dict, your_choice : dict, shape_points : dict, match_points : dict):
    match_tally = 0
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
    match_points = generic_dict_parser(dct = match_points, input_str = match_result)
    # tally score to put into the list output
    final_score = call_pts + match_tally
    return final_score


# main file parser
def parse_elf_guide(foo : str):
    with open(foo) as fl:
        lines = fl.readlines()
        lst_lst_lines = [i.split() for i in lines]
    return lst_lst_lines
        

# calculate the answer procedurally with the glut of hashmaps
elf_guide = r"day2_input.txt"
foo_lst = parse_elf_guide(elf_guide)

print(len(foo_lst))

#print(type(foo_lst[0]))
#print(type(foo_lst[0][0]))
#tmp_dct = {"a": 1, "b": 2, "c": 3}
#tmp_str1 = "a"
#tmp_str2 = "z"

#out_val = generic_dict_parser(dct = tmp_dct, input_str = tmp_str1)
#print(out_val)
#print(foo_lst[0][0])
#print(foo_lst[0][1])
lst_match_scores = [score_input(match = mtch, opp_choice = opponent_choices, your_choice = your_choices, shape_points = shape_score, match_points = match_score) for mtch in foo_lst]
elf_beta = sum(lst_match_scores)
print("Your total score would be: ", elf_beta)


