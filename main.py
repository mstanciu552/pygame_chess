import pygame

from Board import Board
from piece_definitions import draw

# TODO Make check_valid_move function

pygame.init()

WIDTH, HEIGHT = 800, 800

BLACK = (0, 0, 0)

win = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

board = Board(100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    win.fill(BLACK)

    board.draw(win)
    draw(win, board)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
