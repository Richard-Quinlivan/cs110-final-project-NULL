import pygame

class Hero(pygame.sprite.Sprite):
        def __init__(self, name, pos, image):
            pygame.sprite.Sprite.__init__(self)
            self.name = name
            self.image = pygame.image.load(image)
            self.rect = get.image.get_rect()
            self.rect.x = pos[0] #don't need if start at origin
            self.rect.y = pos[1] #don't need if start at origin
            self.strength = 1
            self.speed = 1
            
        def move(self, direction):
            if (direction.lower() == "down"):   
                self.rect.y -= self.speed
            if (direction.lower() == "up"):
                self.rect.y += self.speed
            if (direction.lower() == "left"):
                self.rect.x -= self.speed
            if (direction.lower() == "right"):
                self.rect.x += self.speed
        def fight(self, other):
            if (other.strength > self.strength):
                return random.choice([True, Flase])
            
            #fight is being called through controller


