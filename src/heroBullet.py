import pygame

class heroBullet(pygame.sprite.Sprite):
	def __init__(self, x, y, speed, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = self.image = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(),(30, 30))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = speed

	def update(self):
		"""
		moves the heroBullet to the right
		args: None
		return: self.rect.x
		"""
		self.rect.x += self.speed
