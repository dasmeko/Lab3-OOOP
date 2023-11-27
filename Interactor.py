import sys
import pygame
from Renderer import Renderer
from Board import Board
from Constants import WIDTH

pygame.init()

window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")
renderer = Renderer(window)

running = True
    
while running:
    board = Board()
    done = False
    player = 0
    
    renderer.render(board)
       
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                moved = board.move(player, pygame.mouse.get_pos())
                if moved:
                    player = (player + 1) % 2
                renderer.render(board)
                done, result = board.win_check()
            if event.type == pygame.QUIT:
                done = True
                running = False
                result = 0
        
    renderer.display_message(result)

pygame.display.quit()
pygame.quit()
sys.exit()
