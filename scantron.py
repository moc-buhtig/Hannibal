import random
import sys

import pyautogui
import pyperclip
import time
pyautogui.PAUSE = 0
def get_board():
    t = time.time()
    pyautogui.moveTo(1342, 193)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    coldic = {'red': 'RE', 'lightblue': 'LB', 'purple': 'PU', 'green': 'GR', 'pink': 'PN', 'orange': 'OG', 'maroon': 'MR', 'teal': 'TL', 'yellow': 'YL', 'brown': 'BR', 'blue': 'BL', 'purpleblue': 'PB', '': ''}
    html = pyperclip.paste()
    lines = []
    current_line = []
    html = html[:html.find('</tbody>')]
    if 'alert center' in html:
        return '', True
    for i, item in enumerate(html):
        if html[i:].startswith('<td class'):
            add = False
            indx = html[i:].find('</td>')
            scanned = html[i:indx+i]
            number = scanned[scanned.find(">")+1:]
            if '<' in number:
                number = number[:number.find('<')]
            if number != '':
                number = int(number.replace("%", ""))
            else:
                number = 0
            name = ''
            for q in scanned:
                if q == '"':
                    add = not add
                    if add:
                        continue
                    else:
                        break
                if add:
                    name += q
            namelm = name.split(' ')
            namel = []
            owner = ''
            for thing in namelm:
                if thing != 'attackable':
                    namel.append(thing)
            if namel[-1] in ['large', 'small', 'tiny']:
                namel = namel[:-1]
            if namel == ['mountain']:
                name = 'MTN'
            if 'neutral' in namel[1:]:
                name = 'n'
                owner = coldic[namel[0]]
            if 'city' in namel[1:]:
                name = 'c'
                owner = coldic[namel[0]]
            if namel == ['fog']:
                name = '?'
            if namel == ['fog', 'obstacle']:
                name = 'M?'
            if 'general' in namel:
                name = 'g'
                owner = coldic[namel[0]]
            if namel == ['']:
                name = '_'
            current_line.append([owner, name, number])
        if html[i:].startswith('</tr>'):
            lines.append(current_line)
            current_line = []
    return lines, False
def move_space(startx, starty, direction, board, g_c):
    for a, l in enumerate(board):
        for b, m in enumerate(l):
            if m[0] == 'RE' and m[1] == 'g':
                board_general = (b, a)
                break
    general_coords = g_c
    pyautogui.click(1, 1)
    assert direction in ['up', 'left', 'right', 'down']
    pyautogui.click(general_coords)
    xmove = startx - board_general[0]
    ymove = starty - board_general[1]
    wait = 0.1
    with pyautogui.hold('shift'):
        if xmove < 0:
            for _ in range(abs(xmove)):
                pyautogui.press('left')
                time.sleep(wait)
        else:
            for _ in range(abs(xmove)):
                pyautogui.press('right')
                time.sleep(wait)
        if ymove > 0:
            for _ in range(abs(ymove)):
                pyautogui.press('down')
                time.sleep(wait)
        else:
            for _ in range(abs(ymove)):
                pyautogui.press('up')
                time.sleep(wait)
    pyautogui.press(direction)



