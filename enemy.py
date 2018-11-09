import pygame
from enemybullet import enemyBullet
import math

class enemy(pygame.sprite.Sprite):
	def __init__(self, position, strength, speed, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.strength = strength
		self.speed = speed
		self.health = health

	def move(self):
		yCoord = 0
		while self.health > 0:
			self.rect.y = sin(yCoord)
			ycoord += 10

	def take_damage(self):
		self.health += -1

	def die(self):
		if self.health == 0:
			#make disapear
