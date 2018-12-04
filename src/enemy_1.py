import pygame
from src import enemyBullet

class enemy_1(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(),(60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        """
        Moves the enemy to the left as the screen updates
        args: None
        return: self.rect.x
        """
        self.rect.x -= self.speed

	#FIX POSITION
