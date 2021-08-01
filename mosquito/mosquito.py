import pygame
from random import randint
import time

main_display = pygame.display.set_mode((800, 600))
bg = pygame.image.load('forest.jpg')
mosquito = pygame.image.load('mosquito.png')

bg = pygame.transform.scale(bg, (800, 600))
mosquito = pygame.transform.scale(mosquito, (150, 150))
mosquito_rect = mosquito.get_rect(x = randint(0, 700), y = randint(0, 500))

game = True

clock = pygame.time.Clock()
FPS = 20
speed_x = 0
speed_y = 0

while game:
    clock.tick(FPS)
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if mosquito_rect.collidepoint(e.pos):
                pygame.draw.circle(bg, 'red', e.pos, 15)
                mosquito = pygame.transform.scale(mosquito, (1, 1))
                mosquito = pygame.transform.scale(mosquito, (150, 150))
                


    mosquito_rect.x += speed_x
    mosquito_rect.y += speed_y
    time.sleep(0.02)
    speed_x += randint(-2, 2)
    speed_y += randint(-2, 2)
    if speed_x > 5:
        speed_x -= randint(1, 3)
    if speed_y > 5:
        speed_y -= randint(1, 3)

    if mosquito_rect.x > 650 or mosquito_rect.x < 0:
        speed_x *= -1

    if mosquito_rect.y > 450 or mosquito_rect.y < 0:
        speed_y *= -1



    main_display.blit(bg, (0, 0))
    main_display.blit(mosquito, mosquito_rect)

    pygame.display.update()
