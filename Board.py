import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Board:
    def __init__(self, size):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.size = size
        self.board = [['' for _ in range(8)] for _ in range(8)]

    def draw(self, win):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == '':
                    color = WHITE if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0 else BLACK
                    pygame.draw.rect(win,  color, pygame.Rect(x * self.size, y * self.size, self.size, self.size))
                
