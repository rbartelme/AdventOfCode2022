#!/usr/bin/env python3


# hashmaps for translating char into game strings
opponent_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
your_choices = {"X": "Rock", "Y": "Paper", "C": "Scissors"}
shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
match_score = {"Loss": 0, "Draw": 3, "Win": 6}


# scoring algorithms

def win_lose_draw(opp : str, your_choice : str):
    if opp is your_choice:
        outcome = "Draw"
    elif your_choice is "Scissors":
        if opp is "Paper":
            outcome = "Win"
        else:
            outcome = "Loss"
    elif your_choice is "Paper":
        if opp is "Rock":
            outcome = "Win"
        else:
            outcome = "Loss"
    elif your_choice is "Rock":
        if opp is "Scissors":
            outcome = "Win"
        else:
            outcome = "Loss"
    else:
        print("Well that ain't right, this just terminates the logic.")

    return outcome

def score_input(opponent : str, you : str, opp_choice : dict, your_choice : dict, shape_points : dict, match_points : dict):
    # parse opponent dict
    # parse your dict





# main file parser


# print outputs of parser


