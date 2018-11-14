import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        self.rect = get.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.direction = direction
           # self.strength = 1
           # self.speed = 1
            #bullet((hero.centerx, hero.centery))
    def update(self):
        if (self.direction == "left"):
            self.rect.centerx -= 10
        elif ((self.direction == "right"):
            self.rect.centerx += 10
                
                
            
