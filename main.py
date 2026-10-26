import pygame
import random
pygame.init()
BLACK = (0,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
DARK_BLUE = (0,0,100)
BLUE = (80,80,255)
class TextArea:
    def __init__(self, x, y, width = 300, height = 150, color = YELLOW):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        self.image = None

    def set_text(self, text, fsize = 25, color = BLACK):
        self.image = pygame.font.Font(None, fsize).render(text, True, color)

    def draw(self, shift_x = 0, shift_y = 0):
        pygame.draw.rect(mv, self.fill_color, self.rect)
        mv.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y) )
mv = pygame.display.set_mode((1500,760))

clock = pygame.time.Clock()
question = TextArea(500,200, color=BLUE)
question.set_text('Вопрос', fsize=35)

answer = TextArea(500,400, color=BLUE)
answer.set_text('Ответ', fsize=35)
questions = ['Где находится Кабо-Верде?', 'Сколько голов забил Мбаппе сегодня ночью?', 'Кто получил травму в матче ПСЖ vs Барса из команды ПСЖ?']
answers = ['Оно находится в атлантическом океане неподалёку с африкой', 'Он забил 2 гола барсе', 'Травму получил Хвича на 6-9 месяцев ребилетации' ]
FPS = 40
game = True
a,q = -1, -1  
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                q = random.randint(0,len(questions)-1)
                question.set_text(questions[q])
            if event.key == pygame.K_a:
                a  = random.randint(0, len(answers)-1)
                answer.set_text(answers[a])

    mv.fill(WHITE)
    question.draw( shift_y=55)
    answer.draw( shift_y=55)
    pygame.display.update()
    clock.tick(FPS)
    
    