import pygame

class heroBullet(pygame.sprite.Sprite):
	def __init__(self, x, y, speed, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = self.image = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(),(30, 30))
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.speed = speed

	def update(self):
		self.rect.centerx += self.speed
