#!/usr/bin/env python3


# hashmaps for translating char into game strings
opponent_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
your_choices = {"X": "Rock", "Y": "Paper", "C": "Scissors"}
shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
match_score = {"Loss": 0, "Draw": 3, "Win": 6}


# scoring algorithms

def win_lose_draw(opp : str, your_choice : str):
    if opp == your_choice:
        outcome = "Draw"
    elif your_choice == "Scissors":
        if opp == "Paper":
            outcome = "Win"
        else:
            outcome = "Loss"
    elif your_choice == "Paper":
        if opp == "Rock":
            outcome = "Win"
        else:
            outcome = "Loss"
    elif your_choice == "Rock":
        if opp == "Scissors":
            outcome = "Win"
        else:
            outcome = "Loss"
    else:
        print("Well that ain't right, this just terminates the logic.")

    return outcome

def score_input(match : list, opp_choice : dict, your_choice : dict, shape_points : dict, match_points : dict):
    opponent_raw_value = match[0]
    your_raw_value = match[1]
    # parse opponent dict
    # parse your dict
    return None




# main file parser
def parse_elf_guide(foo : str):
    with open(foo) as fl:
        lines = fl.readlines()
        lst_lst_lines = [i.split() for i in lines]
    return lst_lst_lines
        

# print outputs of parser
elf_guide = r"day2_input.txt"
foo_lst = parse_elf_guide(elf_guide)
print(foo_lst[0])

