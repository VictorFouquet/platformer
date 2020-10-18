from math import cos, sin



ROTATION_STEPS = [3.14 * i * 0.02 for i in range(100)]


class Plateform:
    def __init__(self, attrs):
        self.coord     = [attrs[0], attrs[1]]
        self.width     = attrs[2]
        self.direction = attrs[3]
        self.min       = attrs[4]
        self.max       = attrs[5]
        self.player_j  = None
    
    def holds_player(self, player):
        for j in range(self.coord[1], self.coord[1] + self.width):
            if [self.coord[0] - 1, j] == [player.i, player.j] \
            or [self.coord[0], j] == [player.i, player.j]:
                self.player_j = j
                
                return True
        return False
    

class VerticalMover(Plateform):
    def __init__(self, attrs):
        super().__init__(attrs)
    
    def move(self):
        if not self.min <= self.coord[0] + self.direction <= self.max:
            self.direction *= -1
        self.coord[0] += self.direction


class HorizontalMover(Plateform):
    def __init__(self, attrs):
        super().__init__(attrs)

    def move(self):
        if not self.min <= self.coord[1] + self.direction <= self.max:
            self.direction *= -1
        self.coord[1] += self.direction


class CircularMover(Plateform):
    def __init__(self, attrs, ray, rate):
        super().__init__(attrs)
        self.steps = [
            (
                round(ray * sin(step) * attrs[3] + attrs[0]),
                round(ray * cos(step) * 1.2 * attrs[3] * 2 + attrs[1])
            )
            for step in ROTATION_STEPS
        ]
        self.mid_line = attrs[0]
        self.rate = rate
        self.n = 0
        self.n_steps = len(ROTATION_STEPS) - 1
        self.current_step = 0

    def move(self):
        self.n += 1
        if self.n % self.rate == 0:
            if self.current_step == self.n_steps:
                self.current_step = 0
            else:
                self.current_step += 1
            self.coord = self.steps[self.current_step]

        
        

if __name__ == '__main__':
    from player import Player
    player = Player(4,6)
    horiz_plateform = HorizontalMover([5,3,3,1,0,10])
    vert_plateform = VerticalMover([5,3,3,1,0,10])
    print(horiz_plateform.holds_player(player))
    print(vert_plateform.holds_player(player))
    horiz_plateform.move()
    vert_plateform.move()
    print(horiz_plateform.holds_player(player))
    print(vert_plateform.holds_player(player))
