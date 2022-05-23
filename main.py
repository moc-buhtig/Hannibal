import scantron
import pyautogui
import importlib
import sys
import time
def del_line(number):
    for _ in range(number):
        sys.stdout.write("\033[F")  # back to previous line
        sys.stdout.write("\033[K")  # clear line
print("Hello!")
gs = float(input("Enter gamespeed: "))
dl = 0.5/gs
input("Please start the game, and then hover over your general. Press enter when this is done.")
pos = pyautogui.position()
gc = (pos.x, pos.y)
FILENAME_AI = 'basicai'
ai = importlib.import_module(FILENAME_AI, False)
print("Beginning game...")
tick = 1
failstreak = 0
while True:
    print("-"*25)
    print("Beginning tick "+str(tick))
    t = time.time()
    print("Retrieving board ... ", end='')
    board_d = scantron.get_board()
    print('done')
    board = board_d[0]
    if board_d[1] is True:
        print("Game Over!")
        sys.exit(0)
    print("Getting move ... ", end='')
    move = ai.get_move(gc, board)
    if move != '':
        print("done")
        print("Moving ... ", end='')
        scantron.move_space(move[0], move[1], move[2], board, gc)
        print('done')
        failstreak = 0
    else:
        print("failed")
        failstreak += 1
        if failstreak > 50:
            print("No moves / quitsig")
            sys.exit(0)
    elapsed = time.time()-t
    if dl-elapsed > 0:
        print("Ahead of schedule by", dl-elapsed)
        time.sleep(dl-elapsed)
    else:
        print("Behind schedule by", abs(dl-elapsed))
    del_line(6)
    tick += 1
print("-"*25)
print("Game completed.")
