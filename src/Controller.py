import sys
import pygame
import random
import time
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

        self.enemies1 = pygame.sprite.Group()
        num_enemies = random.randrange(3,5)
        for i in range(num_enemies):
            y = random.randrange(80, 400)
            x = random.randrange(550, 600)
            self.enemies1.add(enemy_1.enemy_1(x, y, 3, 'assets/enemy.png' ))
        self.heroBullet = pygame.sprite.Group()
        # self.heroBullet.add(heroBullet.heroBullet(50, 50, 3, 'assets/herobullet.png'))
        self.enemyBullet = pygame.sprite.Group()
        # self.enemyBullet.add(enemyBullet.enemyBullet(50, 50, 'assets/enemybullet.png', 2, "reg"))
        self.hero = (Hero.hero("phil", 3, 80, 3, "assets/hero.png"))
        self.all_sprites = pygame.sprite.Group(self.hero,self.enemies1,self.enemyBullet,self.heroBullet)
        self.state = "START"

    def mainLoop(self):
        while True:
            if(self.state == "START"):
                self.startLoop()
            elif(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    def startLoop(self):
        pygame.key.set_repeat(1,50)
        while self.state == "START":
            self.screen.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            font = pygame.font.SysFont("arial", 40, True)
            title = font.render('Welcome to Galaxy Shooter!', True, (0,0,0))
            self.screen.blit(title, (100,100))
            font = pygame.font.SysFont("arial", 20, True)
            instruct1 = font.render('Move with the UP/DOWN/LEFT/RIGHT keys', True, (0,0,0))
            instruct2 = font.render('Shoot with SPACE', True, (0,0,0))
            instruct3 = font.render('Good Luck!~', True, (0,0,0))
            self.screen.blit(instruct1, (150,165))
            self.screen.blit(instruct2, (230,205))
            self.screen.blit(instruct3, (255,245))
            pygame.draw.rect(self.screen, (80,208,255), (50,400,150,50)) #instruct
            pygame.draw.rect(self.screen, (0,192,0), (440,400,150,50)) #plat
            font = pygame.font.SysFont("arial", 25, True)
            start_button = font.render('PLAY', True, (0,0,0))
            self.screen.blit(start_button, (490,410))
            font = pygame.font.SysFont("arial", 25, True)
            start_button = font.render('QUIT', True, (0,0,0))
            self.screen.blit(start_button, (100,410))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #tuple postition
            #print(click)
            if click[0] == 1 and mouse[0] in range(440,590) and mouse[1] in range(400,450):
                self.state = "GAME"
            if click[0] == 1 and mouse[0] in range(50,200) and mouse[1] in range(400,450):
                sys.exit()
            pygame.display.flip()

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        time_elapsed = 0
        clock = pygame.time.Clock()
        while self.state == "GAME":
            new_time = clock.tick()
            time_elapsed += new_time
            if time_elapsed > 1000:
                enemies = self.enemies1.sprites()
                if len(enemies) > 1:
                    fire = random.randrange(0, len(enemies))
                    self.enemy_1 = enemies[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_1.rect.x, self.enemy_1.rect.y, 'assets/enemybullet.png', 2, "reg"))
                    self.all_sprites = pygame.sprite.Group(self.hero,self.enemies1,self.enemyBullet,self.heroBullet)
                    time_elapsed = 0
            self.background.fill((250, 250, 250)) #white
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move("up")
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move("down")
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move("left")
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move("right")
                    elif(event.key == pygame.K_SPACE):
                        self.heroBullet.add(heroBullet.heroBullet(self.hero.rect.x + 50, self.hero.rect.y + 20, 3, 'assets/herobullet.png'))
                        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemyBullet)+tuple(self.heroBullet))
            #check for collisions with enemy
            fights = pygame.sprite.groupcollide(self.heroBullet, self.enemies1, True, True)


            #check for collisions with hero
            collide = pygame.sprite.spritecollide(self.hero, self.enemyBullet, True) != []
            if collide:
                self.hero.health -= 1
                print(self.hero.health)

            #redraw the entire screen
            self.all_sprites.update()
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"

            #display the text
            font = pygame.font.SysFont("arial", 18, True)
            lives = font.render('Health: ' + str(self.hero.health), True, (250,0,0))
            self.screen.blit(lives, (570,450))
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
