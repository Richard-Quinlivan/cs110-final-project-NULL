import pygame

class enemyBullet(pygame.sprite.Sprite):
	def __init__(self, position, speed, direction):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = position[0]
		self.rect.centery = position[1]
		#if (self.direction == "right"):
		#	self.image = pygame		not finished. will flip the image of the bullet if the hero is turned around

	def update(self):
		# if (self.direction == "right"):
		# 	self.rect.centerx += speed
		 if (self.direction == "left"):
		 	self.rect.centerx += -speed
