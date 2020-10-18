class Item:
    def __init__(self, attrs):
        self.coord = [attrs[0], attrs[1]]
        self.current = attrs[2]
        self.symbols = attrs[3]
        self.max = len(attrs[3]) - 1
        self.show = True
        
    def move(self):
        if self.current < self.max:
            self.current += 1
        else:
            self.current = 0