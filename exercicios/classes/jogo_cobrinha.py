class SnakePart:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:

    def __init__(self, x: int, y: int, direction: tuple = (1,0)):
        self.body : list[SnakePart] = [SnakePart(x,y)]
        self.direction = direction

    def move(self):
        pass