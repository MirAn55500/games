import pygame
class Snake():
    def __init__(self):
        self.head = pygame.Surface((20, 20))
        self.head.fill('blue')
        self.rect = self.head.get_rect(x = 280, y = 300)
        self.body = [self.head.get_rect(x = 260, y = 300), self.head.get_rect(x = 240, y = 300), self.head.get_rect(x = 220, y = 300)]
        self.speed_x = 20
        self.speed_y = 0

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    if self.speed_y != 20:
                        self.speed_x = 0
                        self.speed_y = - 20

                elif e.key == pygame.K_DOWN:
                    if self.speed_y != -20:
                        self.speed_x = 0
                        self.speed_y = 20

                elif e.key == pygame.K_RIGHT:
                    if self.speed_x != -20:
                        self.speed_x = 20
                        self.speed_y = 0

                elif e.key == pygame.K_LEFT:
                    if self.speed_x != 20:
                        self.speed_x = -20
                        self.speed_y = 0
                events.clear()

        self.body.insert(0, self.rect.copy())

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left >= 800:
            self.rect.left = 0
        if self.rect.right <= 0:
            self.rect.right = 800
        if self.rect.top >= 600:
            self.rect.top = 0
        if self.rect.bottom <= 0:
            self.rect.bottom = 600

    def draw(self, main_display):
        main_display.blit(self.head, self.rect)
        for body_blocks in self.body:
            main_display.blit(self.head, body_blocks)

    def body_pop(self):
        self.body.pop()

    def bump(self):
        for body_block in self.body:
            if body_block.colliderect(self.rect):
                return False
        return True

if __name__ == '__main__':
    print("Опять запустила КЛАСС!!!")