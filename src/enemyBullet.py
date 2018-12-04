import pygame

class enemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, img, speed, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(),(30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.type = type
        self.speed = speed

    def update(self):
        """
        moves the bullet in the correct direction depending on its type
        args: None
        return: None
        """
        if (self.type == "up"):
            self.rect.y += -self.speed
        if (self.type == "down"):
            self.rect.y += self.speed
        if (self.type == "reg"):
            pass
        self.rect.x += -self.speed
