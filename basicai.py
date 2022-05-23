import time
import random
def get_move(gc, board):
    t = time.time()
    my_color = 'RE'
    moves = []
    for y, line in enumerate(board):
        for x, square in enumerate(line):
            owner = square[0]
            name = square[1]
            number = square[2]
            if owner == my_color and number > 1: # TODO: number > 1 bug: fix
                lis = []
                try:
                    if y > 0:
                        lis.append(board[y - 1][x])
                except IndexError:
                    print(end='')
                try:
                    lis.append(board[y+1][x])
                except IndexError:
                    print(end='')
                try:
                    lis.append(board[y][x+1])
                except IndexError:
                    print(end='')
                try:
                    if x > 0:
                        lis.append(board[y][x - 1])
                except IndexError:
                    print(end='')
                dire = ['up', 'down', 'right', 'left']
                for l, ite in enumerate(lis):
                    if ite[0] in [''] and ite[1] != 'MTN':
                        moves.append([x, y, dire[l]])
    if len(moves) == 0:
        return ''
    move = moves[random.randint(0, len(moves)-1)]
    return move
