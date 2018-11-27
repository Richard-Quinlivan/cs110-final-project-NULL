import pygame
from src import heroBullet

class hero(pygame.sprite.Sprite):
	def __init__(self, name, health, x, y, image):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(),(60, 60))
		self.rect = self.image.get_rect()
		self.rect.x = x #don't need if start at origin
		self.rect.y = y #don't need if start at origin
		self.strength = 1
		self.speed = 1
		self.health = health

	def move(self, direction):
		"""
		allows the hero to move when keys are pressed
		args: direction
		return: self.rect.x, self.rect.y
		"""
		if (direction.lower() == "down"):
			self.rect.y -= self.speed
			if (direction.lower() == "up"):
				self.rect.y += self.speed
			if (direction.lower() == "left"):
				self.rect.x -= self.speed
			if (direction.lower() == "right"):
				self.rect.x += self.speed
	# def fire(self):
	# 	"""
	# 	creates a heroBullet object
	# 	args: none
	# 	return: heroBullet
	# 	"""
	# 	heroBullet.heroBullet(self.x, self.y, 5)
	#

	def take_damage(self):
		"""
		removes one health from the hero
		args: none
		return: self.hero.health
		"""
		self.health += -1

			#fight is being called through controller
