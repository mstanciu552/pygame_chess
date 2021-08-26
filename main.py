import pygame

from Board import Board
from Game import Game

# TODO Complete board array
# TODO Make move function on piece
# TODO Make check_valid_move function

pygame.init()

WIDTH, HEIGHT = 800, 800

BLACK = (0, 0, 0)

win = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

game = Game(win)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    win.fill(BLACK)

    game.update()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
