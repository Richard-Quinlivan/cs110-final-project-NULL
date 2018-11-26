import pygame
from src import enemyBullet
import math

class enemy_1(pygame.sprite.Sprite):
	def __init__(self, x, y, speed, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img).convert_alpha()
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
		self.rect.x += self.speed

	def fire(self):
		"""
		Has the emeny ship fire a enemyBullet
		args: None
		return: enemyBullet
		"""
		enemyBullet.enemyBullet(self.position, self.speed * 2, "reg")
