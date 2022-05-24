from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

MOVEMENT_PENALTY = 1
CITY_PENALTY = True
PREFER_OWN_TERRITORY = False
PENALTIES = True

move_queue = []  # this should be used for move queue (the program generates moves like a directional list, then adds them here)


def get_move(gc, board):
    return '?'


def get_penalty(square, color):
    if square[1] == 'MTN':
        return 0
    if square[1] == 'c':
        if CITY_PENALTY:
            if PENALTIES:
                return square[2] + 1
            else:
                return MOVEMENT_PENALTY
        else:
            return 0
    if square[1] == 'n':
        if square[0] == color:
            if PREFER_OWN_TERRITORY:
                return 1 / (square[2] - 1)
            else:
                return MOVEMENT_PENALTY
        if square[0] == '':
            return MOVEMENT_PENALTY
        if square[1] not in ['', color]:
            if PENALTIES:
                return square[2] + 1
            else:
                return MOVEMENT_PENALTY
    if square[1] == 'g':
        if square[0] == color:
            if PREFER_OWN_TERRITORY:
                if PENALTIES:
                    return 1 / (square[2] - 1)
                else:
                    return MOVEMENT_PENALTY
            else:
                return MOVEMENT_PENALTY
        else:
            if PENALTIES:
                return square[2] + 1
            else:
                return MOVEMENT_PENALTY


test_board = [[['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0]], [['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0]], [['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'c', 44], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0]], [['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'c', 49], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0]], [['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'c', 42], ['', 'n', 0], ['', 'n', 0], ['', 'c', 43], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'c', 47]], [['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'c', 44], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['LB', 'n', 1]], [['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['RE', 'g', 45], ['RE', 'n', 3], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['RE', 'n', 3], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'c', 49], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['RE', 'n', 3], ['RE', 'n', 17], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['LB', 'n', 2], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['', 'MTN', 0], ['', 'n', 0], ['', 'c', 47], ['', 'n', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['LB', 'n', 2], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'c', 49], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'n', 0], ['', 'n', 0], ['', 'c', 43], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['LB', 'n', 2], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['LB', 'n', 1]], [['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['LB', 'n', 1], ['LB', 'n', 1], ['LB', 'n', 1], ['LB', 'n', 1], ['LB', 'n', 1], ['LB', 'n', 1], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['LB', 'n', 3]], [['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['LB', 'n', 2], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['LB', 'n', 1], ['', 'MTN', 0], ['', 'n', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['LB', 'n', 1], ['LB', 'n', 1], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['LB', 'n', 2], ['', 'MTN', 0]], [['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['LB', 'n', 2], ['LB', 'n', 2], ['LB', 'n', 2], ['LB', 'n', 2], ['LB', 'n', 36], ['LB', 'n', 1], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['LB', 'n', 1], ['LB', 'g', 7], ['LB', 'n', 2], ['LB', 'n', 2], ['LB', 'n', 2], ['', 'n', 0]], [['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0]], [['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'MTN', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'n', 0], ['', 'MTN', 0], ['', 'n', 0]]]


def convert_pathfinder_to_directional(pat):
    print(pat)
    lst = []
    last_coords = pat[0]
    for item in pat[1:]:
        if item[0] == last_coords[0]:
            if item[1] > last_coords[1]:
                # move down
                direction = 'down'
            else:
                # move up
                direction = 'up'
        else:
            if item[0] > last_coords[0]:
                # move right
                direction = 'right'
            else:
                # move left
                direction = 'left'
        lst.append([last_coords, direction])
        last_coords = item
    return lst


def move_square(start_coords, end_coords, board, color):
    matrix = []
    for ln in board:
        line = []
        for square in ln:
            line.append(get_penalty(square, color))
        matrix.append(line)
    grid = Grid(matrix=matrix)
    start = grid.node(start_coords[0], start_coords[1])
    end = grid.node(end_coords[0], end_coords[1])
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    return path


directions = move_square((6, 7), (18, 16), test_board, 'RE')
print(convert_pathfinder_to_directional(directions))
