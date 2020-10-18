class Player:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.n_jump = 0
        self.on_platform = 0
        self.can_sprint = False
        self.can_double_jump = True
        self.last_wound = 0
        self.life = 3
        self.n_keys = 0
        self.is_alive = True
        self.wins = False
       
        
    def jump(self):
        if self.n_jump > 0:
            self.n_jump -= 3
            self.i -= 3
