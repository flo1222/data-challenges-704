# pylint: disable=missing-docstring

def factorial(number):
    '''function that returns a factorial of a number'''
    result = 1
    for i in range(1, number):
        result += result * i
    return result

def count_possibilities(n_toss, n_heads):
    '''TO DO: return the number of possibilities to get n_heads when flipping the coin n_toss times
        Ex: count_possibilities(4, 4)  = 1'''
    return factorial(n_toss)/(factorial(n_heads)*factorial(n_toss - n_heads))

def count_total_possibilities(n_toss):
    '''TO DO: return the total amount of differentt combinations
        when flipping the coins n_toss times
        Ex: count_total_possibilities(3) = 8'''
    result = 1
    for _ in range(n_toss):
        result = result * 2
    return result

def probability(n_toss):
    '''return a dictionnary. `play_n_game` The keys will be the
        possible number of heads of each game, the values for each of those
        keys will correspond to the probability of a game ending with that result.'''
    dict_proba = {}
    for i in range (n_toss + 1):
        dict_proba[i] = count_possibilities(n_toss, i)/count_total_possibilities(n_toss)
    return dict_proba
