# pylint: disable=missing-docstring

def sudoku_validator(grid):
    """Une fonction qui test si une grille de Sudoku est correcte."""
    #Dans un premier temmps, testons les lignes...
    for i in range(9):
        for j in range(9):
            if j+1 in grid[i]:
                pass
            else:
                print('lignes non ok')
                return False
    print('lignes OK')
    #Dans un deuxième temmps, testons les colonnes...
    for i in range(9):
        column = []
        for j in range(9):
            column.append(grid[j][i])
        for k in range(9):
            if k+1 in column:
                pass
            else:
                print('colonnes non ok')
                return False
    print('colonnes OK')
    #Dans un troisième temmps, testons les carrés...
    for j in range(3):
        for l in range(3):
            carré = []
            for i in range(1, 4, 1):
                for k in range(1, 4, 1):
                    carré.append(grid[i+j*3-1][k+l*3-1])
            for m in range(9):
                if m+1 in carré:
                    pass
                else:
                    return False
    return True
