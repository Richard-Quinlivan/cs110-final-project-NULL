import pygame
from src import enemyBullet
import math

class enemy_3(pygame.sprite.Sprite):
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
		creates 3 enemyBullet's. 1 that goes straight, and 2 that go diagonal
		args: none
		return: none
		"""
		enemyBullet.enemyBullet(self.position, self.speed * 2, "up")
		enemyBullet.enemyBullet(self.position, self.speed * 2, "reg")
		enemyBullet.enemyBullet(self.position, self.speed * 2, "down")
