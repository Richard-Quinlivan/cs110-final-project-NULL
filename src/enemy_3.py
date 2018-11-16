import pygame
from enemybullet import enemyBullet
import math

class enemy_3(pygame.sprite.Sprite):
	def __init__(self, position, strength, speed, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.strength = strength
		self.speed = speed
		self.health = health
		self.yCoord = 0

	def update(self):
		self.rect.y += speed * math.sin(self.yCoord)
		self.rect.x += speed
		self.ycoord += 10

	def fire(self):
		enemybullet.enemyBullet(self.position, self.speed * 2, "up")
		enemybullet.enemyBullet(self.position, self.speed * 2, "reg")
		enemybullet.enemyBullet(self.position, self.speed * 2, "down")


	def take_damage(self):
		self.health += -1
