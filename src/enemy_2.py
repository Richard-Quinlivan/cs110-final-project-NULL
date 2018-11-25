import pygame
from src import enemyBullet
import math

class enemy_2(pygame.sprite.Sprite):
	def __init__(self, x, y, strength, speed, health, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.strength = strength
		self.speed = speed
		self.health = health
		self.yCoord = 0

	def update(self):
		self.rect.y += speed * math.sin(self.yCoord)
		self.rect.x += speed
		self.ycoord += 10

	def fire(self):
		enemyBullet.enemyBullet(self.position, self.speed * 2, "reg")



	def take_damage(self):
		self.health += -1
