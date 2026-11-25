import pygame
from apps.fast_clicker import Label,clicker
from apps.config import mv,FPS
pygame.init()
BLACK = (0,0,0)
BACK = (200,255,255)

clicker_game = Label(100,100)
clicker_game.set_text('Fast clicker', fsize=53)

game = True
name_game = 0
clock = pygame.time.Clock()


while game:
    pygame.display.update()
    clock.tick(FPS)
    mv.fill(BACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if clicker_game.choose(event.pos):
               clicker_game.draw()
               name_game = 1 
            pygame.time.wait(1000)
    if name_game == 0:
        clicker_game.draw()
    if name_game == 1:
        name_game = clicker(game)

