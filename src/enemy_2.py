import pygame
from src import enemyBullet
import math

class enemy_2(pygame.sprite.Sprite):
	def __init__(self, x, y, strength, speed, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.strength = strength
		self.speed = speed
		self.yCoord = 0

	def update(self):
		"""
		moves the ship in a sin curve to the left
		args: none
		return: self.rect.x, self.rect.y, self.yCoord
		"""
		self.rect.y += speed * math.sin(self.yCoord)
		self.rect.x += speed
		self.ycoord += 10

	def fire(self):
		"""
		creates the enemyBullet object
		args: none
		return enemyBullet
		"""
		enemyBullet.enemyBullet(self.position, self.speed * 2, "reg")
