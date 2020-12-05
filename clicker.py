# здесь подключаются модули
import pygame
import sys
import random
pygame.font.init()
#pygame.mixer.init()
#pygame.mixer.music.load('RUDE - Eternal Youth')
#pg.mixer.music.play(-1)

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
circles = 0
c = []
coords = (-100, -100)
m = 0
pressed = False
x = 300#x
y = 150#y
w = 110#x1
h = 25#y1
h2 = 200#y2
h3 = 25#y3
h4 = 250#y4
h5 = 25#y5
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
score = 0
# если надо до цикла отобразить
# какие-то объекты, обновляем экран

pygame.display.update()
counter = 0
#главный цикл

while True:
    sc.fill(BLACK)
    for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                coords = i.pos
                print(i.pos)
                pressed = True
    f10 = pygame.font.Font(None, 36)
    text10 = f10.render('Aimtestik', True,
                      (255, 0, 0))
    f11 = pygame.font.Font(None, 36)
    text11 = f11.render('Играть', True,
                      (0, 180, 0))
    f12 = pygame.font.Font(None, 36)
    text12 = f12.render('Правила', True,
                      (0, 180, 0))
    f13 = pygame.font.Font(None, 36)
    text13 = f13.render('Выход', True,
                      (0, 180, 0))
    sc.blit(text10, (300, 100))
    sc.blit(text11, (300, 150))
    sc.blit(text12, (300, 200))
    sc.blit(text13, (300, 250))
    
    #pygame.draw.rect(sc, WHITE, (x, y, w, h))
    #pygame.draw.rect(sc, WHITE, (x, h2, w, h3))
    #pygame.draw.rect(sc, WHITE, (x, h4, w, h5))
    if (x <= coords[0] <= x + w) and (h4 <= coords[1] <= h4 + h5) and pressed == True:
        sys.exit()
    if (x <= coords[0] <= x + w) and (h2 <= coords[1] <= h2 + h3) and pressed == True:
        sc.fill(BLACK)
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('Правила', True,
                      (255, 0, 0))
        sc.blit(text2, (350, 50))
        f21 = pygame.font.Font(None, 20)
        text21 = f21.render('В игре присутствуют два режима: на время и бесконечный. Как понятно из названия в первом режиме есть', True,
                      (0, 180, 0))
        f22 = pygame.font.Font(None, 20)
        text22 = f22.render('таймер(30 секунд) до истечения которого нужно набрать как можно больше очков. Получить очки', True,
                      (0, 180, 0))
        f23 = pygame.font.Font(None, 20)
        text23 = f23.render('можно за попадание по кругам, которые будут появляться в случайной части экрана, разных размеров. Во', True,
                      (0, 180, 0))
        f24 = pygame.font.Font(None, 20)
        text24 = f24.render('втором режиме ограничений по времени нет, играйте сколько хотите. Но будьте осторожны! Каждый промах', True,
                      (0, 180, 0))
        f25 = pygame.font.Font(None, 20)
        text25 = f25.render('- 1 ошибка, 5 ошибок и вы проиграли. А теперь идите и покажите свой лучший результат! Удачи!!!', True,
                      (0, 180, 0))
        sc.blit(text21, (50, 100))
        sc.blit(text22, (50, 150))
        sc.blit(text23, (50, 200))
        sc.blit(text24, (50, 250))
        sc.blit(text25, (50, 300))
    if (x <= coords[0] <= x + w) and (y <= coords[1] <= y + h) and pressed == True:
        sc.fill(BLACK)
        f3 = pygame.font.Font(None, 36)
        text3 = f3.render('Выберите режим', True,
                      (255, 0, 0))
        sc.blit(text3, (300, 50))
        
    pygame.display.update()
    q = 1
while q == 0:

    # задержка
    clock.tick(FPS)
    counter += 1

    if counter == 30 * FPS or m == 5:
        print(score)
        break
    con = 30 - (counter / 60)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            coords = i.pos
            print(i.pos)
            pressed = True
        #print(i)

    # --------
    # изменение объектов
    # --------

    # обновление экрана
    sc.fill(BLACK)
    pygame.draw.line(sc, WHITE, [600, 0],
                                [600, 400], 3)
    while circles < 5:
        x = random.randint(0, 550)
        y = random.randint(0, 400)
        r = random.randint(10, 50)
        circles += 1
        c.append((x,y,r))
    hit_circle = False
    for elem in c:
        if (coords[0]-elem[0])**2 + (coords[1]-elem[1])**2 <= elem[2]*elem[2]:
            c.remove(elem)
            circles -= 1
            score += 1
            hit_circle = True
    if hit_circle == False and pressed == True:
            m += 1
    pressed = False
    for elem in c:
         pygame.draw.circle(sc, RED, (elem[0], elem[1]), elem[2])
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Счёт: ', True,
                  (0, 180, 0))
     
    f2 = pygame.font.SysFont(None, 36)
    text2 = f2.render(f'{score}', True,
                      (0, 180, 0))
    f3 = pygame.font.Font(None, 36)
    text3 = f3.render('Ошибки: ', True,
                      (255, 0, 0))
     
    f4 = pygame.font.SysFont(None, 36)
    text4 = f4.render(f'{m}', True,
                      (255, 0, 0))
    f5 = pygame.font.Font(None, 36)
    text5 = f5.render('Время: ', True,
                      (225, 225, 0))
     
    f6 = pygame.font.SysFont(None, 36)
    text6 = f6.render(f'{con}', True,
                      (225, 225, 0))
    sc.blit(text1, (620, 10))
    sc.blit(text2, (685, 10))
    sc.blit(text3, (620, 60))
    sc.blit(text4, (730, 60))
    sc.blit(text5, (620, 110))
    sc.blit(text6, (705, 110))
    pygame.display.update()

