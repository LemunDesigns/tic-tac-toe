##tic-tac-toe by lemundesgins

from random import randint
from sys import exit


wins = {
    'X': 0,
    'O': 0
}

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

in_corrs = {
    'TL': [0, 0], 'TM': [0, 1], 'TR': [0, 2],
    'ML': [1, 0], 'MM': [1, 1], 'MR': [1, 2],
    'LL': [2, 0], 'LM': [2, 1], 'LR': [2, 2]
}

def convert_input(i, i_type):

    if i_type == 'string':

        if i == 'help':
            show_help()
            return [3,3]

        if i == 'exit':
            print()
            exit(0)

        for key, value in in_corrs.items():
            if i == key:
                return value

        return [3, 3]

    elif i_type == 'list':

        for key, value in in_corrs.items():
            if i == value:
                return key

def print_board(board):
    print('  ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print(' ---+---+---')
    print('  ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print(' ---+---+---')
    print('  ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def show_help():
    print()
    print(' Type the correspondent cell to move on that space:')
    print()
    print('  TL | TM | TR ')
    print(' ----+----+----')
    print('  ML | MM | MR ')
    print(' ----+----+----')
    print('  LL | LM | LR ')

def compute_ai(board):

    for x in range(3):
        if board[x][0] == 'O' and board[x][1] == 'O' and board[x][2] == ' ':
            return [x, 2]
        if board[x][0] == 'O' and board[x][1] == ' ' and board[x][2] == 'O':
            return [x, 1]
        if board[x][0] == ' ' and board[x][1] == 'O' and board[x][2] == 'O':
            return [x, 0]
    for y in range(3):
        if board[0][y] == 'O' and board[1][y] == 'O' and board[2][y] == ' ':
            return [2, y]
        if board[0][y] == 'O' and board[1][y] == ' ' and board[2][y] == 'O':
            return [1, y]
        if board[0][y] == ' ' and board[1][y] == 'O' and board[2][y] == 'O':
            return [0, y]
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == ' ':
        return [2, 2]
    if board[0][0] == 'O' and board[1][1] == ' ' and board[2][2] == 'O':
        return [1, 1]
    if board[0][0] == ' ' and board[1][1] == 'O' and board[2][2] == 'O':
        return [0, 0]
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == ' ':
        return [2, 0]
    if board[0][2] == 'O' and board[1][1] == ' ' and board[2][0] == 'O':
        return [1, 1]
    if board[0][2] == ' ' and board[1][1] == 'O' and board[2][0] == 'O':
        return [0, 2]

    for x in range(3):
        if board[x][0] == 'X' and board[x][1] == 'X' and board[x][2] == ' ':
            return [x, 2]
        if board[x][0] == 'X' and board[x][1] == ' ' and board[x][2] == 'X':
            return [x, 1]
        if board[x][0] == ' ' and board[x][1] == 'X' and board[x][2] == 'X':
            return [x, 0]
    for y in range(3):
        if board[0][y] == 'X' and board[1][y] == 'X' and board[2][y] == ' ':
            return [2, y]
        if board[0][y] == 'X' and board[1][y] == ' ' and board[2][y] == 'X':
            return [1, y]
        if board[0][y] == ' ' and board[1][y] == 'X' and board[2][y] == 'X':
            return [0, y]
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == ' ':
        return [2, 2]
    if board[0][0] == 'X' and board[1][1] == ' ' and board[2][2] == 'X':
        return [1, 1]
    if board[0][0] == ' ' and board[1][1] == 'X' and board[2][2] == 'X':
        return [0, 0]
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == ' ':
        return [2, 0]
    if board[0][2] == 'X' and board[1][1] == ' ' and board[2][0] == 'X':
        return [1, 1]
    if board[0][2] == ' ' and board[1][1] == 'X' and board[2][0] == 'X':
        return [0, 2]

    if board[1][1] == ' ' and randint(1,2) == 1:
        return [1, 1]

    r = randint(1,8)
    if r == 1:
        if board[0][0] == ' ':
            return [0, 0]
        if board[0][2] == ' ':
            return [0, 2]
        if board[2][2] == ' ':
            return [2, 2]
        if board[2][0] == ' ':
            return [2, 0]
    elif r == 2:
        if board[0][2] == ' ':
            return [0, 2]
        if board[2][2] == ' ':
            return [2, 2]
        if board[2][0] == ' ':
            return [2, 0]
        if board[0][0] == ' ':
            return [0, 0]
    elif r == 3:
        if board[2][2] == ' ':
            return [2, 2]
        if board[2][0] == ' ':
            return [2, 0]
        if board[0][0] == ' ':
            return [0, 0]
        if board[0][2] == ' ':
            return [0, 2]
    elif r == 4:
        if board[2][0] == ' ':
            return [2, 0]
        if board[0][0] == ' ':
            return [0, 0]
        if board[0][2] == ' ':
            return [0, 2]
        if board[2][2] == ' ':
            return [2, 2]

    r = randint(1,4)
    if r == 1:
        if board[0][1] == ' ':
            return [0, 1]
        if board[1][2] == ' ':
            return [1, 2]
        if board[2][1] == ' ':
            return [2, 1]
        if board[1][0] == ' ':
            return [1, 0]
    elif r == 2:
        if board[1][2] == ' ':
            return [1, 2]
        if board[2][1] == ' ':
            return [2, 1]
        if board[1][0] == ' ':
            return [1, 0]
        if board[0][1] == ' ':
            return [0, 1]
    elif r == 3:
        if board[2][1] == ' ':
            return [2, 1]
        if board[1][0] == ' ':
            return [1, 0]
        if board[0][1] == ' ':
            return [0, 1]
        if board[1][2] == ' ':
            return [1, 2]
    elif r == 4:
        if board[1][0] == ' ':
            return [1, 0]
        if board[0][1] == ' ':
            return [0, 1]
        if board[1][2] == ' ':
            return [1, 2]
        if board[2][1] == ' ':
            return [2, 1]

def has_won(board):

    victory = False

    for x in range(3):
        if board[x][0] != ' ':
            if board[x][0] == board[x][1] and board[x][1] == board[x][2]:
                victory = True

    for y in range(3):
        if board[0][y] != ' ':
            if board[0][y] == board[1][y] and board[1][y] == board[2][y]:
                victory = True

    if board[1][1] != ' ':
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            victory = True
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            victory = True

    return victory

def board_is_complete(board):
    board_complete = True
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                board_complete = False
    return board_complete

def ai_turn(board):

    x, y = compute_ai(board)
    board[x][y] = 'O'

    print()
    print(' AI moved on ' + convert_input([x, y], 'list'))

    if has_won(board):
        victor = 'O'
        return [board, 'break', victor]

    if board_is_complete(board):
        return [board, 'break', '']

    return [board, '', '']

def player_turn(board):

    print()
    print_board(board)
    print()

    print(' Player: move on which space? (\'help\' to see moves, \'exit\' to ' +
        'exit)')
    print()
    move = input(' > ')

    x, y = convert_input(move, 'string')

    try:
        if board[x][y] == ' ':
            board[x][y] = 'X'
        else:
            return [board, 'continue', '']
    except IndexError:
        return [board, 'continue', '']

    if has_won(board):
        victor = 'X'
        return [board, 'break', victor]

    if board_is_complete(board):
        return [board, 'break', '']

    return [board, '', '']

def game(board):
    print()
    print(' You play X, AI plays O. Rolling dice to decide who begins...')
    begin = 'X' if randint(1,2) == 1 else 'O'
    print()
    print(' ' + begin + ' begins!')

    if begin == 'O':
        board, state, victor = ai_turn(board)

    while True:

        board, state, victor = player_turn(board)
        if state == 'continue':
            continue
        elif state == 'break':
            break

        board, state, victor = ai_turn(board)
        if state == 'break':
            break

    print()
    print_board(board)
    print()
    if victor == '':
        print(' It\'s a draw!')
    else:
        wins[victor] += 1
        print(' ' + victor + ' wins!')
    print()
    print(' Player has won ' + str(wins['X']) + ' time(s), AI has won ' + str(wins['O']) + ' time(s)')

def reset_board(board):
    for x in range(3):
        for y in range(3):
            board[x][y] = ' '


print()
print(' ------ TIC TAC TOE ------')
print()
print(' A simple game by lemundesigns')
print()
print(' Code available at: https://github.com/lemundesigns/tic-tac-toe')

while True:

    game(board)

    choice = ''
    while choice != 'y' and choice != 'n':
        print()
        print(' Do you want to play again? (y/n)')
        print()
        choice = input(' > ')
    if choice == 'y':
        reset_board(board)
        continue
    else:
        print()
        exit(0)
