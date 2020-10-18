class Enemy:
    def __init__(self, attrs):
        self.coord = [attrs[0], attrs[1]]
        self.direction = attrs[2]
        self.symbols = attrs[3]
        self.alts = attrs[4]
        self.current = attrs[5]
        self.min = attrs[6]
        self.max = attrs[7] 
        
    def move(self):
        if self.coord[1] + self.direction > self.max or \
            self.coord[1] + self.direction < self.min:
                self.direction *= -1
                [self.symbols, self.alts] = [self.alts, self.symbols]
        self.coord[1] += self.direction
        if self.current >= len(self.symbols) - 1:
            self.current = 0
        else:
            self.current += 1
        