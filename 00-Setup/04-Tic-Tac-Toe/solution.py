def display_board(board, width):
    counter = 0
    dash_count = width * 3 + width - 1
    dashstring = ''
    for i in range (dash_count):
        dashstring += '-'
    string = ''
    number_rows = int(len(board)/width)
    for i in range (number_rows - 1):
        for j in range (width - 1):
            string = string + ' '+ board[counter]+' |'
            counter += 1
        string = string + ' '+ board[counter]+' \n'+ dashstring + '\n'
        counter += 1
    for k in range (width - 1):
        string = string + ' '+ board[counter]+' |'
        counter += 1
    string = string + ' '+ board[counter] + ' '
    return string
    
    