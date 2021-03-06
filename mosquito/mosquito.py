import pygame
from random import randint

main_display = pygame.display.set_mode((800, 600))
bg = pygame.image.load('forest.jpg')
mosquito_raw = pygame.image.load('mosquito.png')

bg = pygame.transform.scale(bg, (800, 600))
mosquito = pygame.transform.scale(mosquito_raw, (150, 150))
mosquito_rect = mosquito.get_rect(x = randint(0, 700), y = randint(0, 500))

game = True

clock = pygame.time.Clock()
FPS = 20
speed_x = 0
speed_y = 0

while game:
    now = 0
    clock.tick(FPS)
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            click_time = pygame.time.get_ticks()

            if mosquito_rect.collidepoint(e.pos):
                pygame.draw.circle(bg, 'red', e.pos, 15)
                mosquito = pygame.transform.scale(mosquito_raw, (1, 1))
                main_display.blit(mosquito, mosquito_rect)
                now = pygame.time.get_ticks()
                while now <= 1000 + click_time:
                    now = pygame.time.get_ticks()
                mosquito = pygame.transform.scale(mosquito_raw, (150, 150))
                main_display.blit(mosquito, mosquito_rect)


    mosquito_rect.x += speed_x
    mosquito_rect.y += speed_y
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