import pygame
from Constants import WIDTH, TILE_SIZE, GAP, WHITE, BLACK, GRAY, MESSAGES, X_IMAGE, O_IMAGE

class Renderer:
    def __init__(self, window):
        self.window = window
        self.messages = MESSAGES

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.window, GRAY, (x, 0), (x, WIDTH), 3)
            pygame.draw.line(self.window, GRAY, (0, x), (WIDTH, x), 3)

    def display_message(self, result):
        content = self.messages[result]
        pygame.time.delay(300)
        self.window.fill(WHITE)
        font = pygame.font.SysFont('courier', 40)
        end_text = font.render(content, 1, BLACK)
        self.window.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.delay(1000)

    def render(self, board):
        self.window.fill(WHITE)
        self.draw_grid()

        for tile in board.tiles:
            if tile.value:
                x = tile.x
                y = tile.y
                if tile.value == 1:
                    image = X_IMAGE
                else:
                    image = O_IMAGE
                self.window.blit(image, (x - image.get_width() // 2, y - image.get_height() // 2))

        pygame.display.update()

