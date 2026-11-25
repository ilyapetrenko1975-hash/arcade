import pygame
import random 
from apps.config import mv,FPS,WAITS
pygame.init()
BLACK = (0,0,0)
YELLOW = (255,255,0)
BACK = (200,255,255)
DARK_BLUE = (0,0,100)
RED = (255,0,0)
GREEN = (0,255,0)

LABEL = 'CLICK!'

SCORES = [5,10,5,10,15,5,10,15,15]

class Area:
    def __init__(self, x, y, width = 300, height = 150, color = BACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def draw(self):
        pygame.draw.rect(mv, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
class TextArea(Area):
    def set_text(self, text, fsize = 55, color=BLACK):
        self.text_color = color
        self.fsize = fsize
        self.text = text
        return self
    def draw(self, shift_x = 0, shift_y = 0):
        super().draw()
        self.image = pygame.font.Font(None, self.fsize).render(self.text, True, self.text_color)
        mv.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))

class Label(TextArea):
    def __init__(self, x, y, width=300, height=150, color=DARK_BLUE):
        super().__init__(x + 20, y + 20, width - 40, height - 40, color=YELLOW)
        self.frame = pygame.rect.Rect(x,y, width, height)
        self.frame_color = color
        self.text = ''
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mv, self.frame_color, self.frame)
        return super().draw(shift_x, shift_y)
    def click(self, position):
        global score
        if self.collidepoint(*position):
            if self.text == LABEL:
                self.fill_color = GREEN
                score += 1 
            else:
                self.fill_color = RED 
                score -= 1
    def choose(self, position):
        if self.collidepoint(*position):
            self.fill_color = GREEN
            return True


    
# mv = pygame.display.set_mode((1500, 760))

# game = True
#FPS = 40


areas = []
for x in [200,1000]:
    for y in [500,100]:
        areas.append(Label(x,y))

clock = pygame.time.Clock()
score_label = TextArea(0,0,300,50)
time_label = TextArea(1200,0,300,50)
level_label = TextArea(600,0,300,50)
game_over_label = TextArea(0,0,1500,760, color=RED)
win_label = TextArea(0,0,1500,760, color=GREEN)
reload = Label(570,450,250,100)
new_level = Label(570,600,250,100)
menu_labels = [TextArea(200,70 * i + 100, height=70).set_text(f'Уровень {i + 1}') for i in range(len(WAITS))]



score = 0

def clicker(game):
    global cards,SCORES,FPS, score
    x,y = 0,0
    score = 0
    level = 0
    WAIT = FPS * WAITS[level]
    time = 0
    menu = True
    wait = 0
    while game:
        pygame.display.update()
        clock.tick(FPS)
        mv.fill(BACK)
        reload.fill_color = YELLOW
        new_level.fill_color = YELLOW
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if menu:
                    for i,label in enumerate(menu_labels):
                        if label.collidepoint(x,y):
                            level = i
                            menu = False
                            label.text_color = RED
                            label.draw()
                            pygame.display.update()
                            pygame.time.wait(1500)

                for box in areas:
                    box.fill_color = YELLOW
                    box.click(event.pos)
                if reload.collidepoint(x,y):
                    score = 0
                    game = True
                    time = 0
                    reload.fill_color = GREEN
                    reload.draw(shift_x=10, shift_y=20)
                    continue
                if new_level.collidepoint(x,y):
                    score = 0 
                    game = True
                    time = 0
                    new_level.fill_color = GREEN
                    new_level.set_text('Next level')
                    new_level.draw(shift_x=10, shift_y=20)
                    level += 1
                    WAIT = FPS * WAITS[level]
                    continue
        if menu:
            for i,label in enumerate(menu_labels, 1):
                # label.set_text(f'Уровень {i}')
                label.draw()
            continue
            

        if score >= SCORES[level]:
            win_label.set_text('YOU \'RE WINNER CHAMPION!', fsize=100)
            win_label.draw(shift_x = 220, shift_y = 320)
            reload.set_text('Play again', fsize=50)
            reload.draw(shift_x = 10, shift_y = 20)
            if level < len(WAITS) - 1:
                new_level.set_text('Next level', fsize=50)
                new_level.draw(shift_x=10, shift_y=20)
            continue
        if time >= 10:
            game_over_label.set_text('Game Over',fsize=100)
            game_over_label.draw(shift_x = 520, shift_y = 320)
            reload.set_text('Play again', fsize=50)
            reload.draw(shift_x = 10, shift_y = 20)
            continue                            
        if wait == 0:
            cards = random.randint(0, len(areas) - 1)
            wait = WAIT
            time += WAITS[level]
        else:
            wait -= 1
        for i,box in enumerate(areas):
            if i == cards:
                box.set_text(LABEL)
            else:
                box.set_text('')
            box.draw(55,35)

        score_label.set_text(f'Cчёт: {score}')
        score_label.draw(shift_x = 5, shift_y = 5)
        time_label.set_text(f'Время: {time} с.')
        time_label.draw(shift_x = 5, shift_y = 5)
        level_label.set_text(f'Уровень: {level + 1}')
        level_label.draw(shift_x = 5, shift_y = 5)
    return 0


        