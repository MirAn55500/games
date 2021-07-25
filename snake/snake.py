import pygame
from random import randint
from classSnake import *
from classApple import *
score = 0
main_display = pygame.display.set_mode((800, 600))

def results(main_display, snake_result, score):
    pygame.init()
    font1 = pygame.font.SysFont("Arial", 50)
    font2 = pygame.font.SysFont("Times New Roman", 30)
    text1 = font1.render(f"{snake_result} Your total score: {score}", 1, "black")
    text2 = font2.render('If you want to exit game press Escape', 0, 'grey')

    main_display.blit(text1, (100, 200))
    main_display.blit(text2, (200, 500))
    button = True
    while button:
        pygame.display.update()
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE or e.type == pygame.QUIT:
                button = False

def snake_game(main_display):
    global score

    clock = pygame.time.Clock()
    game = True
    snake = Snake()
    apple = Apple()

    while game:
        clock.tick(5)

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                game = False
                return 'Game closed!'

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                game = False
                return 'Game closed!'

        if snake.rect.colliderect(apple.rect):
            apple.rect.centerx = randint(0, 39) * 20 + 10
            apple.rect.centery = randint(0, 29) * 20 + 10
            score += 1
            print(f'Score: {score}')
        else:
            snake.body_pop()

        snake.update(events)
        game = snake.bump()

        main_display.fill('light green')

        apple.draw(main_display)
        snake.draw(main_display)

        pygame.display.update()

        pygame.init()
        font1 = pygame.font.SysFont('Arial', 30, 'red')

    return 'Game over!'

snake_result = snake_game(main_display)
results(main_display, snake_result, score)