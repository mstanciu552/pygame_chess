import pygame

class Piece:
    def __init__(self, pos, color, board, surface_path):
        self.pos = pos
        self.color = color
        self.board = board
        self.square_size = self.board.size
        self.surface = pygame.transform.scale(pygame.image.load(surface_path), (self.square_size, self.square_size))
        self.normalize = lambda pos: (pos[0] * self.square_size, pos[1] * self.square_size)
        self.denormalize = lambda pos: (pos[0] / self.square_size, pos[1] / self.square_size)
        self.selected = False

    def draw(self, win):
        win.blit(self.surface, self.normalize(self.pos))

    def set_pos(self, pos):
        self.pos = pos
    
    def check_click(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_bounds = lambda x, y: x * self.square_size <= mouse_x and mouse_x <= (x + 1) * self.square_size and y * self.square_size <= mouse_y and mouse_y <= (y + 1) * self.square_size
            if check_bounds(self.pos[0], self.pos[1]):
                self.selected = True


    def get_dest(self):
        if not self.selected:
            return
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_bounds = lambda x, y: x * self.square_size <= mouse_x and mouse_x <= (x + 1) * self.square_size and y * self.square_size <= mouse_y and mouse_y <= (y + 1) * self.square_size
            for x in range(8):
                for y in range(8):
                    if check_bounds(x, y) and self.selected: 
                        self.set_pos((x, y))
                        break
                        

    def update(self, win):
        self.draw(win)
        self.check_click()
        self.get_dest()
