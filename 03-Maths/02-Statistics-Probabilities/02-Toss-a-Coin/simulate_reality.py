# pylint: disable=missing-docstring

import random as rand

def play_one_game(n_toss):
    '''returns the number of heads after n_toss'''
    head_counter = 0
    for _ in range(n_toss):
        head_counter += rand.randrange(0, 2, 1)
    return n_toss - head_counter

print(play_one_game(1))

def play_n_game(n_games, n_toss):
    """returns a dictionary where the keys are the possible head counts
    of each game and the values will the probability of a game ending
    with that number of heads.
    """
    results_list = []
    for _ in range(n_games):
        results_list.append(play_one_game(n_toss))
    dict_proba = {}
    for j in range (n_toss + 1):
        if results_list.count(j) != 0:
            dict_proba[j] = results_list.count(j)/n_games
        else:
            continue
    return dict_proba
