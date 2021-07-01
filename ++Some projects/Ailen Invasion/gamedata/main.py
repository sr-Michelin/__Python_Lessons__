import sys
import time
import pygame
import random
from pygame import mixer
from math import pow, sqrt

# Ініціація ігри
pygame.init()

# Створення екрану
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # Стабілізація FPS

# Фон
background = pygame.image.load('images/back.jpg')

# Фонова музика
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

# Імя ігри і лого
pygame.display.set_caption('Ailen Invasion')
image_l = pygame.image.load('images/icon.png')
pygame.display.set_icon(image_l)

# дані гравця
player_img = pygame.image.load('images/spaceship.png')
player_x = 370
player_y = 532
player_change = [0, 0]
# швидкість гравця
player_vc = 3.363

# дані ворога
enemy_img = []
enemy_x = []
enemy_y = []
enemy_ch_x = []
enemy_ch_y = []
diff = []

# Швидкість ворога
en_vc_x = 1.758
en_vc_y = 20

# Кількість ворогів
enemy_N = 10

for i in range(enemy_N):
    enemy_img.append(pygame.image.load('images/alien.png'))
    enemy_x.append(random.randint(1, 763))
    enemy_y.append(random.randint(50, 150))
    enemy_ch_x.append(en_vc_x)
    enemy_ch_y.append(en_vc_y)
    diff.append(i * 0)

# дані missle
missle_img = pygame.image.load('images/missile.png')
missle_x = 0
missle_y = player_y + 10
missle_change = [0, 26.108]
missle_state = 'ready'

# Кількість попадань (ігровий рахунок)
score_val = 0
font = pygame.font.Font('freesansbold.ttf', 24)
text_x = 10
text_y = 10

# Кінець ігри
over_font = pygame.font.Font('freesansbold.ttf', 64)


def Show_score(x, y):
    """Описує вивід на екран ігрового рахунку"""
    score = font.render('Kills: ' + str(score_val), True, (225, 225, 225))
    screen.blit(score, (x, y))


def game_over_text():
    """Описує вивід на екран тексту "Ігра завершена" """
    over_text = font.render('GAME OVER', True, (225, 225, 225))
    screen.blit(over_text, (333, 290))


def Show_FPS():
    """Описує вивід на екран FPS"""
    fpc = font.render('FPS: ' + str(int(clock.get_fps())), True, (225, 225, 225))
    screen.blit(fpc, (685, 10))


def player(x, y):
    """Описує вивід на екран зображення гравця"""
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    """Описує вивід на екран зображення ворога"""
    screen.blit(enemy_img[i], (x, y))


def fire_missle(x, y):
    """Описує вивід на екран зображення снаряда"""
    global missle_state
    missle_state = 'fire'
    screen.blit(missle_img, (x + 24, y + 10))


# Відстань від ворогів до снаяряда
def Collision(enemy_x, enemy_y, missle_x, missle_y):
    """Відповідає за визначення відстані від снаряда до ворога - індикатор попадання"""
    distance = sqrt(pow((enemy_x - 10) - missle_x, 2) + pow(enemy_y - missle_y, 2))
    if distance <= 20:
        return True
    else:
        return False


# Ігровий цикл
while True:
    clock.tick(60)
    # print(clock)
    '''Відслідковування 0дій від клавіатури і мишки'''

    # Виклик гами дисплея
    screen.fill((230, 230, 230))

    # Фон поверх гами
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # рекція на нажаті напрямки right і left

        if event.type == pygame.KEYDOWN:
            # Коли клавіші руху зажаті, ракета рухається
            if event.key == pygame.K_LEFT:
                player_change[0] = -player_vc
            elif event.key == pygame.K_RIGHT:
                player_change[0] = player_vc
            elif event.key == pygame.K_UP:
                player_change[1] = -player_vc
            elif event.key == pygame.K_DOWN:
                player_change[1] = player_vc

            elif event.key == pygame.K_SPACE:
                # Реагує на клавішу "SPACE"
                if missle_state == 'ready':
                    missle_sound = mixer.Sound('sounds/laser.wav')
                    missle_sound.set_volume(0.2)
                    missle_sound.play()
                    missle_x = abs(player_x)
                    fire_missle(missle_x, missle_y)

        if event.type == pygame.KEYUP:
            # Коли клавіші руху віджаті, ракета зупиняється
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change[0] = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_change[1] = 0

    # Рух ракети
    player_x += player_change[0]
    player_y += player_change[1]

    # Створюєм фізичні "рамки" для ракети
    if player_x <= 10:
        player_x = 10
    elif player_x >= 732:
        player_x = 732

    elif player_y < 500:  # Реалізація Y поки не відома
        player_y = 500
    elif player_y > 532:
        player_y = 532

    # Рух ворога

    for i in range(enemy_N):
        # Умова кінця гри
        if enemy_y[i] > 516:
            for j in range(enemy_N):
                enemy_y[j] = 2000
                game_over_text()  # Виклик тексту "кінця гри"
            break  # Зупинка створення і відображення ворогів - ігра програна

        enemy_x[i] += enemy_ch_x[i]
        diff[i] = 50 - enemy_y[i]
        _diff_ = abs(max(diff) / 10.)
        print(_diff_)
        # Створюєм фізичні "рамки" для ворога, пересуваючи його вниз
        if enemy_x[i] <= 10:
            enemy_ch_x[i] = en_vc_x + _diff_
            enemy_y[i] += enemy_ch_y[i]

        elif enemy_x[i] >= 767:
            enemy_ch_x[i] = - en_vc_x - _diff_
            enemy_y[i] += enemy_ch_y[i]

        # collision - попадання по мішені, виклик звуку, обліку попадань
        collision = Collision(enemy_x[i], enemy_y[i], missle_x, missle_y)
        if collision == True:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.set_volume(0.8)
            explosion_sound.play()
            missle_y = player_y
            missle_state = 'ready'
            score_val += 1
            # print(f'score: {score_val}') - для дебагу, не рухати

            # Після смерті вороги появляються у рандомній точці екрану - вічна гра
            enemy_x[i] = random.randint(1, 763)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # рух missle - снаряда
    if missle_y <= 0:
        missle_y = player_y + 10
        missle_state = 'ready'

    if missle_state == 'fire':
        fire_missle(missle_x, missle_y)
        missle_y -= missle_change[1]

    # запуск ігрового процесу
    Show_score(text_x, text_y)
    Show_FPS()
    player(player_x, player_y)

    # відображення останього екрану
    pygame.display.update()
