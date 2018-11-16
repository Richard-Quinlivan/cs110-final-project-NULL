import pygame

class enemyBullet(pygame.sprite.Sprite):
	def __init__(self, position, speed, type):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = position[0]
		self.rect.centery = position[1]
		self.type = type

	def update(self):
		if (self.type = "up"):
			self.rect.y += -speed
		if (self.type = "down"):
			self.rect.y += speed
		if (self.type = "reg"):
			pass
	 	self.rect.x += -speed
