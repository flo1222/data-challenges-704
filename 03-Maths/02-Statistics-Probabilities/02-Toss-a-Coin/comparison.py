# pylint: disable=missing-docstring

from flip_coin_factorial import probability
from simulate_reality import play_n_game

def mean_squared_error(n_games, n_toss):
    '''TO DO: return the squared error between theorical and "actual"
    results (get through simulation)'''
    play = play_n_game(n_games, n_toss)
    prob = probability(n_toss)
    newdict = {}
    for j in range(n_toss+1):
        newdict[j] = 0
    # print(prob)
    for k in range(n_toss+1):
        if k in play.keys():
            newdict[k] = play[k]
    # print(newdict)
    mse = 0
    for i in range(n_toss+1):
        mse += (prob[i] - newdict[i])**2
        # print(mse)
    return mse/n_toss
print(mean_squared_error(3, 100))
