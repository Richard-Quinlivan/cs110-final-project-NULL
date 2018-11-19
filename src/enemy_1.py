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
		self.rect.x += self.speed

	def fire(self):
		enemybullet.enemyBullet(self.position, self.speed * 2, "reg")

	def take_damage(self):
		self.health += -1
