import pygame
from heroBullet import heroBullet

class mainCharacter(pygame.sprite.Sprite):
	def __init__(self, name, position, strength, speed, health):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.strength = strength
		self.speed = speed
		self.health = health

	def move(self, direction):
		if (direction.lower() == "up"):
			self.rect.y += -self.speed
		if (direction.lower() == "down"):
			self.recte.y += self.speed
		if (direction.lower() == "right"):
			self.rect.x += self.speed
		if (direction.lower() == "left"):
			self.rect.x += -self.speed

	def take_damage(self):
		self.health += -1

	def die(self):
		if self.health == 0:
			# end game, maybe freeze all bullets and emenies, then display game over and return to start screen
