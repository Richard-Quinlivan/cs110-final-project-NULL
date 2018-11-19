import pygame

class heroBullet(pygame.sprite.Sprite):
	def __init__(self, position, speed):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = position[0]
		self.rect.centery = position[1]

	def update(self):
		self.rect.centerx += speed
