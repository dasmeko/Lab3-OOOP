from Constants import ROWS, TILE_SIZE

class Tile:
    def __init__(self, n):
        self.x = (2 * (n % ROWS) + 1) * TILE_SIZE // 2
        self.y = (2 * (n // ROWS) + 1) * TILE_SIZE // 2
        self.value = 0
        self.index = n
