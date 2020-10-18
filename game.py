from time import time

from player import Player


class Game:
    def __init__(self, levels):
        self.player = Player(30,1)
        self.keypressed = None
        self.level = 0
        self.levels = levels[:-2]
        self.loose_screen = levels[-2]
        self.win_screen = levels[-1]
        self.last_level = self.level
        
    def apply_gravity(self):
        i = self.player.i + 1
        j = self.player.j
        if self.levels[self.level].content[i][j] != '#':
            if self.levels[self.level].content[i][j] == '^':
                if time() - self.player.last_wound > .5:
                    self.player.life -= 1
                    self.player.last_wound = time()
            else:
                self.player.i += 1
        else:
            self.player.can_double_jump = True
    
    def can_jump(self):
        i = self.player.i + 1
        j = self.player.j
        if self.player.can_double_jump or self.levels[self.level].content[i][j] == '^' \
            or self.levels[self.level].content[i][j] == '#' \
                and self.player.n_jump == 0 \
                    or self.player.on_platform:
            self.player.n_jump += 9
            if self.player.can_double_jump:
                self.player.can_double_jump = False
            
    def move_player(self):
        if self.player.j != None:
            dist = 2 if self.player.can_sprint else 1
            if self.keypressed == 'left':                    
                self.player.j -= dist
            elif self.keypressed == 'right':
                self.player.j += dist   
        if self.levels[self.level].content[self.player.i-1][self.player.j] == '#':
            self.player.n_jump = 0
        elif self.levels[self.level].content[self.player.i][self.player.j] == '#':
            self.player.n_jump = 0
        self.player.jump()
    
    def replace_player(self):
        self.player.is_alive = False
        self.player.i = 30
        if self.level < self.last_level:
            self.player.j = len(self.levels[self.level].content[0]) - 3
        else:
            self.player.j = 3
        
    def player_in_screen(self):
        if self.player.j != None:
            if self.player.j < 1:
                if self.level > 0:
                    self.last_level = self.level
                    self.level -= 1
                    self.player.j = len(self.levels[self.level].content[0]) - 4
                else:
                    self.player.j = 1
            elif self.player.j >= len(self.levels[self.level].content[0]) - 2:
                if self.level < len(self.levels) - 1:
                    self.last_level = self.level
                    self.level += 1
                    self.player.j = 2
                else:
                    self.player.j =  len(self.levels[self.level].content[0]) - 3
        if self.player.i < 0:
            self.player.i = 1
            self.player.n_jump = 0
        elif self.player.i >= len(self.levels[self.level].content) - 1:
            self.replace_player()