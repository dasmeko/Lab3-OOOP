import sys
import pygame
from Renderer import Renderer
from Board import Board
from Constants import WIDTH

pygame.init()

window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

running = True
    
while running:
    board = Board()
    done = False
    player = 0

    renderer = Renderer(window)
    renderer.render(board)
    
