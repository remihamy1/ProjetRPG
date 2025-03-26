class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def deplacer(self, direction):
        if direction == "N":
            self.y -= 1
        elif direction == "S":
            self.y += 1
        elif direction == "E":
            self.x += 1
        elif direction == "O":
            self.x -= 1
