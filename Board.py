import math
from Constants import ROWS, TILE_SIZE

class Tile:
    def __init__(self, n):
        self.x = (2 * (n % ROWS) + 1) * TILE_SIZE // 2
        self.y = (2 * (n // ROWS) + 1) * TILE_SIZE // 2
        self.value = 0
        self.index = n

class Board:
    def __init__(self):
        self.tiles = list(Tile(i) for i in range(ROWS**2))
        self.fullness = 0
        
    def move(self, player, pos):
        min_dist = TILE_SIZE
        index = 0
        x, y = pos
        
        for tile in self.tiles:
            dist = math.sqrt((x - tile.x)**2 + (y - tile.y)**2)
            
            if dist < min_dist:
                min_dist = dist
                index = tile.index
                
        if not self.tiles[index].value:
            self.fullness += 1
            self.tiles[index].value = player + 1
            moved = True
        else:
            moved = False
        
        return moved
        
    def win_check(self):
        result = 0
        done = False
        
        for i in range(ROWS):
            pl_ch = self.tiles[i * ROWS].value
            if pl_ch == 0:
                continue
            win = True
            for j in range(ROWS):
                if self.tiles[i * ROWS + j].value != pl_ch:
                    win = False
                    break
            if win:
                return True, pl_ch
        
        for i in range(ROWS):
            pl_ch = self.tiles[i].value
            if pl_ch == 0:
                continue
            win = True
            for j in range(ROWS):
                if self.tiles[i + j * ROWS].value != pl_ch:
                    win = False
                    break
            if win:
                return True, pl_ch
        
        win = True
        for i in range(ROWS):
            pl_ch = self.tiles[0].value
            if pl_ch == 0:
                win = False
                break
            if self.tiles[i + i * ROWS].value != pl_ch:
                win = False
                break
        if win:
            return True, pl_ch
        
        win = True
        for i in range(ROWS):
            pl_ch = self.tiles[ROWS - 1].value
            if pl_ch == 0:
                win = False
                break
            if self.tiles[(ROWS - 1) * (i + 1)].value != pl_ch:
                win = False
                break
        if win:
            return True, pl_ch
        
        if self.fullness == ROWS**2:
            return True, 3
        
        return done, result

