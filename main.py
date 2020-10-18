import os
from time import sleep, time

import curses
from curses import textpad
from pynput import keyboard

from game import Game
import plateform as pf
import level

LEVEL = level.LEVELS[0]
GAME = Game(level.LEVELS)
MARGIN_VERT = 0
MARGIN_HORZ = 0

def on_press(key):
    if key == keyboard.Key.left:
        GAME.keypressed = 'left'
    elif key == keyboard.Key.right:
        GAME.keypressed = 'right'
    elif key == keyboard.Key.up:
        if GAME.level == len(GAME.levels) - 1 and GAME.player.n_keys == 5 and GAME.player.j == 70:
            GAME.player.wins = True
        else:
            GAME.can_jump()
    elif key == keyboard.Key.shift:
        GAME.player.can_sprint = True
    elif key == keyboard.Key.backspace and not GAME.player.is_alive:
        GAME.player.is_alive = True
        GAME.player.life = 3


def on_release(key):
    if key ==  keyboard.Key.left or \
        key == keyboard.Key.right :
        GAME.keypressed = None
    elif key == keyboard.Key.shift:    
        GAME.player.can_sprint = False
        
        
def init_keyboard():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()


def init_screen():
    stdscr = curses.initscr()
    curses.curs_set(0)
    return stdscr
    
    
def main():
    init_keyboard()
    stdscr = init_screen()
    MARGIN_VERT = (stdscr.getmaxyx()[0] - 1 - len(GAME.levels[GAME.level].content)) // 2 
    MARGIN_HORZ = (stdscr.getmaxyx()[1] - 1 - len(GAME.levels[GAME.level].content[0])) // 2 
    print(stdscr.getmaxyx()[0])
    while 1:
        sleep(0.06)
        if GAME.player.is_alive and not GAME.player.wins:
            
            for i, row in enumerate(GAME.levels[GAME.level].content):
                stdscr.addstr(
                    MARGIN_VERT + i,
                    MARGIN_HORZ + 0,
                    ''.join(row)
                )
                
            for item in GAME.levels[GAME.level].items:
                if item.show:
                    stdscr.addstr(
                        MARGIN_VERT + item.coord[0],
                        MARGIN_HORZ + item.coord[1],
                        item.symbols[item.current]
                    )
                    item.move()
                    
                    if [GAME.player.i, GAME.player.j] == item.coord:
                        GAME.player.n_keys += 1
                        item.show = False
                        
                        
            for e in GAME.levels[GAME.level].enemies:
                stdscr.addstr(
                    MARGIN_VERT + e.coord[0],
                    MARGIN_HORZ + e.coord[1],
                    e.symbols[e.current]
                )
                
                if GAME.player.i == e.coord[0] and GAME.player.j in range(
                    e.coord[1],
                    e.coord[1]+len(e.symbols[e.current])
                ):
                    if time() - GAME.player.last_wound > 1:
                        GAME.player.life -= 1
                        GAME.player.last_wound = time()
                        
                e.move()
                
            for p in GAME.levels[GAME.level].plateforms:
                p.move()
                
            if GAME.player.on_platform != 0:
                
                GAME.player.can_double_jump = True
                p = GAME.levels[
                    GAME.level
                ].plateforms[
                    GAME.player.on_platform-1
                ]
                
                if isinstance(p, pf.HorizontalMover):
                    GAME.player.j += p.direction
                elif isinstance(p, pf.CircularMover):
                    if p.current_step == 0:
                        dif = p.steps[0][1] - p.steps[-1][1]
                    else:
                        dif = p.steps[p.current_step][1] - p.steps[p.current_step - 1][1]
                    GAME.player.j += dif
                
                GAME.player.i = p.coord[0] - 1
            
            else:
                GAME.apply_gravity()
                
            GAME.move_player()
            GAME.player_in_screen()
            is_hold = False
            
            for i, p in enumerate(GAME.levels[GAME.level].plateforms):
                stdscr.addstr(
                    MARGIN_VERT + p.coord[0],
                    MARGIN_HORZ + p.coord[1],
                    ''.join(['#' for _ in range(p.width)])
                )
                if (p.holds_player(GAME.player)):
                    is_hold = True
                    stdscr.addstr(
                        MARGIN_VERT + 25,
                        MARGIN_HORZ + 0,
                        str(i+1)
                    )
                    GAME.player.on_platform = i+1
                    p.player_j = GAME.player.j
                    GAME.player.n_jump = 0
                    
            if is_hold == False:
                GAME.player.on_platform = 0
                
            if GAME.player.life <= 0:
                GAME.player.is_alive = False
                GAME.replace_player()
                
            if GAME.player.is_alive:
                stdscr.addstr(
                    MARGIN_VERT + 2,
                    MARGIN_HORZ + 3,
                    f'LIFE : {GAME.player.life}'
                )
                stdscr.addstr(
                    MARGIN_VERT + 3,
                    MARGIN_HORZ + 3,
                    f'KEYS : {GAME.player.n_keys}'
                )
                stdscr.addstr(
                    MARGIN_VERT + GAME.player.i,
                    MARGIN_HORZ + GAME.player.j,
                    "@"
                )
                                
        elif GAME.player.wins:
            for i, row in enumerate(GAME.win_screen.content):
                stdscr.addstr(
                    MARGIN_VERT + i,
                    MARGIN_HORZ + 0,
                    ''.join(row)
                )            
        else:
            for i, row in enumerate(GAME.loose_screen.content):
                stdscr.addstr(
                    MARGIN_VERT + i,
                    MARGIN_HORZ + 0,
                    ''.join(row)
                )
        stdscr.refresh()

if __name__ == '__main__':
    print('Hello')
    main()