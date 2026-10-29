import pygame 
pygame.init()
BLACK = (0,0,0)
YELLOW = (255,255,0)
BACK = (200,255,255)

class Area:
    def __init__(self, x, y, width = 300, height = 150, color = YELLOW):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def draw(self):
        pygame.draw.rect(mv, self.fill_color, self.rect)

mv = pygame.display.set_mode((1500, 760))
mv.fill(BACK)
game = True
FPS = 40
areas = [Area(300,500), Area(1000,500), Area(100,600)]


clock = pygame.time.Clock()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    for area in areas:
        area.draw()


    pygame.display.update()
    clock.tick(FPS)