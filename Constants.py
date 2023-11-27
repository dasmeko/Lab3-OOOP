import math
import pygame

WIDTH = 600
ROWS = 3
TILE_SIZE = WIDTH // ROWS

GAP = math.floor(0.95 * TILE_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
X_IMAGE = pygame.transform.scale(pygame.image.load("cross.png"), (GAP, GAP))
O_IMAGE = pygame.transform.scale(pygame.image.load("circle.png"), (GAP, GAP))

MESSAGES = {
    0: "Goodbye!",
    1: "X player wins!",
    2: "O player wins!",
    3: "It's a draw!"
}
