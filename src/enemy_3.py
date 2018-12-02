import pygame
from src import enemyBullet
import math

class enemy_3(pygame.sprite.Sprite):
	def __init__(self, x, y, speed, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(),(60, 60))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = speed
		self.yCoord = 0

	def update(self):
		"""
		moves the ship in a sin curve to the left
		args: none
		return: self.rect.x, self.rect.y, self.yCoord
		"""
		self.rect.y += self.speed * math.sin(math.radians(self.yCoord))
		self.rect.x -= self.speed
		self.yCoord += 10

	def fire(self):
		"""
		creates 3 enemyBullet's. 1 that goes straight, and 2 that go diagonal
		args: none
		return: none
		"""
		enemyBullet.enemyBullet(self.position, self.speed * 2, "up")
		enemyBullet.enemyBullet(self.position, self.speed * 2, "reg")
		enemyBullet.enemyBullet(self.position, self.speed * 2, "down")
