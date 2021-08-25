import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800

BLACK = (0, 0, 0)

win = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(BLACK)

    pygame.display.update()

pygame.quit()
