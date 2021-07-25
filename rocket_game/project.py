import pygame
from random import randint

main_display = pygame.display.set_mode((1200, 800))

fon = pygame.image.load('back.jpg')
rocket = pygame.image.load('rocket.png')
meteorite = pygame.image.load('meteorite.png')
heart = pygame.image.load('heart.png')
bullet = pygame.image.load('bullet.png')

fon = pygame.transform.scale(fon, (1200, 800))
rocket = pygame.transform.scale(rocket, (120, 150))
meteorite = pygame.transform.scale(meteorite, (130, 130))
heart = pygame.transform.scale(heart, (100, 100))
heart3 = heart2 = heart1 = heart
#bullet = pygame.transform.scale(bullet, (50, 50))

rocket_rect = rocket.get_rect(x = 0, bottom = 800)
meteorite_rect = meteorite.get_rect(x = 300, y = 0)
heart_rect3 = heart.get_rect(x = 900, bottom = 800)
heart_rect2 = heart.get_rect(x = 1000, bottom = 800)
heart_rect1 = heart.get_rect(x = 1100, bottom = 800)

score = 0
game = True
lives = 3

while game:

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] == True:
        rocket_rect.x -= 2

    if keys[pygame.K_RIGHT] == True:
        rocket_rect.x += 2


    if meteorite_rect.colliderect(rocket_rect):
        if lives == 3:
            heart3 = pygame.transform.scale(heart3, (0, 0))
        elif lives == 2:
            heart2 = pygame.transform.scale(heart2, (0, 0))
        else:
            heart1 = pygame.transform.scale(heart1, (0, 0))

        lives -= 1
        print(f'Oh no, a collision! Lives left: {lives}')

        meteorite_rect.y = -100
        meteorite_rect.x = randint(100, 1100)

    if lives == 0:
        print('Game over')
        game = False
    if rocket_rect.x < -15:
        rocket_rect.x = -15

    if rocket_rect.x > 1095:
        rocket_rect.x = 1095

    main_display.blit(fon, (0, 0))
    main_display.blit(rocket, rocket_rect)
    main_display.blit(meteorite, meteorite_rect)
    main_display.blit(heart1, heart_rect1)
    main_display.blit(heart2, heart_rect2)
    main_display.blit(heart3, heart_rect3)
    #main_display.blit(bullet, bullet_rect)

    meteorite_rect.y += 5

    if meteorite_rect.y > 800:
        meteorite_rect.y = -100
        meteorite_rect.x = randint(-30, 1100)
        score += 1
        print(f'Total score: {score}')

    pygame.display.update()