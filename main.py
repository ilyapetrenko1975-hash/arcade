import pygame
import random 
pygame.init()
BLACK = (0,0,0)
YELLOW = (255,255,0)
BACK = (200,255,255)
DARK_BLUE = (0,0,100)

class Area:
    def __init__(self, x, y, width = 300, height = 150, color = DARK_BLUE):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def draw(self):
        pygame.draw.rect(mv, self.fill_color, self.rect)
class TextArea(Area):
    def set_text(self, text, fsize = 55, color=BLACK):
        self.image = pygame.font.Font(None, fsize).render(text, True, color)
    def draw(self, shift_x = 0, shift_y = 0):
        super().draw()
        mv.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))

class Label(TextArea):
    def __init__(self, x, y, width=300, height=150, color=DARK_BLUE):
        super().__init__(x + 20, y + 20, width - 40, height - 40, color=YELLOW)
        self.frame = pygame.rect.Rect(x,y, width, height)
        self.frame_color = color
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mv, self.frame_color, self.frame)
        return super().draw(shift_x, shift_y)
mv = pygame.display.set_mode((1500, 760))
mv.fill(BACK)
game = True
FPS = 40
wait = 0
WAIT = FPS / 2
areas = []
for x in [200,1000]:
    for y in [500,100]:
        areas.append(Label(x,y))

clock = pygame.time.Clock()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if wait == 0:
        cards = random.randint(0, len(areas) - 1)
        wait = WAIT
    else:
        wait -= 1
    for i,box in enumerate(areas):
        if i == cards:
            box.set_text('CLICK!')
        else:
            box.set_text('')
        box.draw(55,35)


    pygame.display.update()
    clock.tick(FPS)