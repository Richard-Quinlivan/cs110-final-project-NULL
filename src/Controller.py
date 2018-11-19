import sys
import pygame
import random
from src import Hero
from src import enemy_1
from src import enemy_2
from src import enemy_3
from src import heroBullet
from src import enemyBullet

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()

        """Load the sprites that we need"""

        self.enemy_1 = pygame.sprite.Group()
        num_enemies = random.randrange(1,5)
        for i in range(num_enemies):
            y = random.randrange(80, 400)
            self.enemy_1.add(enemy_1.enemy_1((580,y), 1, 2, 3, 'assets/enemy.png' ))
        self.heroBullet = pygame.sprite.Group()
       # self.heroBullet.add(heroBullet.heroBullet(self.hero.x, self.hero.y 'assets/herobullet.png' ))
        self.enemyBullet = pygame.sprite.Group()
      #  self.heroBullet.add(heroBullet.heroBullet(self.enemy.x, self.enemy.y 'assets/enemybullet.png' ))
        self.hero = hero.Hero(self.hero.name, (50,80), "assets/hero.png")
        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemy_1)+tuple(self.enemybullet)+tuple(self.herobullet))
       # self.state = "START"
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
        #    elif(self.state == "START"):
         #       self.startLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
##    def startLoop(self):
##        while self.state == "START":
##            name = (input("Please enter a name: "))
##            press 1 to look at instructions
##            for event in pygame.event.get():
##                    if event.type == pygame.QUIT:
##                        sys.exit()
##                    if event.type == pygame.KEYDOWN:
##                        if(event.key == pygame.K_1):
##                            self.screen.blit(self.background, (0, 0))
##                            myfont = pygame.font.SysFont(None, 30)
##                            message = myfont.render('Move with Up/Down/Left/Right keys. Shoot enemy space ships but be careful, do not let them pass you or lose a life!', False, (0,0,0))
##                            self.screen.blit(message, (self.width/2,self.height/2))
##                            pygame.display.flip()
##            if play button pressed
##                self.state = "GAME"

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while self.state == "GAME":
            self.background.fill((0, 0, 0)) #black
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move(up)
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move(down)
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move(left)
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move(right)
                    elif(event.key == pygame.K_SPACE):
                        self.hero.fight() #NOT WRITTEN YET//shoots


            #check for collisions with enemy
            fights = pygame.sprite.spritecollide(self.heroBullet, self.enemy_1, True)
            if fights:
                for enemy_1 in fights:
                    if self.hero.fight(enemy_1): #if returns true or false?
                        self.enemy_1.take_damage()
                    else:
                        pass #if hero bullet misses, do nothing

            #check for collisions with hero
            collide = pygame.sprite.spritecollide(self.enemyBullet, self.Hero, True)
            if collide:
                for enemy_1 in collide:
                    if self.enemy_1.fire(hero): #?_?
                        self.hero.take_damage()
                    else:
                        pass #if enemy bullet misses, do nothing (if bullet passes the screen)

            #redraw the entire screen
            self.enemy_1.update()
##            self.enemy_2.update()
##            self.enemy_3.update()
            self.heroBullet.update()
            self.enemyBullet.update()
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"

            #display the text
            font = pygame.font.SysFont(None, 30, True)
            hero_sur = font.render('Remaining Health:'+ str(self.hero.health), False, (250,0,0))
            self.screen.blit(hero_sur, (10,50))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def gameOver(self):
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0,0,0))
        self.screen.blit(message, (self.width/2,self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
