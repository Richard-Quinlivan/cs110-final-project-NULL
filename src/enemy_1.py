import pygame
from enemybullet import enemyBullet
import math

class enemy_1(pygame.sprite.Sprite):
	def __init__(self, position, strength, speed, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.strength = strength
		self.speed = speed
		self.health = health

	def update(self):
		self.rect.x += speed

	def fire(self):
		enemybullet.enemyBullet(self.position, self.speed * 2, "reg")

	def take_damage(self):
		self.health += -1
