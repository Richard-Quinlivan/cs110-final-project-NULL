import sys
import pygame
import random
import pickle
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
        self.enemy1_freq = 3
        self.enemy2_freq = 2
        self.enemy3_freq = 1

        """Load the sprites that we need"""

        self.enemies1 = pygame.sprite.Group()
        self.enemies2 = pygame.sprite.Group()
        self.enemies3 = pygame.sprite.Group()
        num_enemies = random.randrange(3,5)
        for i in range(num_enemies):
            y = random.randrange(30, 400)
            x = random.randrange(550, 600)
            self.enemies1.add(enemy_1.enemy_1(x, y, 3, 'assets/enemy.png' ))
        self.heroBullet = pygame.sprite.Group()
        self.enemyBullet = pygame.sprite.Group()
        self.hero = (Hero.hero("phil", 3, 80, 3, "assets/hero.png"))
        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
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
        time_elapsed_1 = 0
        time_elapsed_2 = 0
        time_elapsed_3 = 0
        enemy1_accum = 0
        enemy2_accum = 0
        enemy3_accum = 0
        enemy_time = 0
        e1_killcount = 0
        e2_killcount = 0
        e3_killcount = 0
        clock = pygame.time.Clock()
        other_clock = pygame.time.Clock()
        while self.state == "GAME":
            #sets the enemies to fire periodaically
            new_time = clock.tick()
            time_elapsed_1 += new_time
            time_elapsed_2 += new_time
            time_elapsed_3 += new_time
            enemy1_accum += new_time
            enemy2_accum += new_time
            enemy3_accum += new_time
            if (time_elapsed_1 > 1000):
                enemies = self.enemies1.sprites()
                if len(enemies) >= 1:
                    fire = random.randrange(0, len(enemies))
                    self.enemy_1 = enemies[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_1.rect.centerx, self.enemy_1.rect.centery, 'assets/enemybullet.png', 6, "reg"))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    time_elapsed_1 = 0
            if (time_elapsed_2 > 1000):
                enemies_two = self.enemies2.sprites()
                if len(enemies_two) >= 1:
                    fire = random.randrange(0, len(enemies_two))
                    self.enemy_2 = enemies_two[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_2.rect.centerx, self.enemy_2.rect.centery, 'assets/enemybullet.png', 6, "reg"))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    time_elapsed_2 = 0
            if (time_elapsed_3 > 3000):
                enemies_three = self.enemies3.sprites()
                if len(enemies_three) >= 1:
                    fire = random.randrange(0, len(enemies_three))
                    self.enemy_3 = enemies_three[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_3.rect.centerx, self.enemy_3.rect.centery, 'assets/enemybullet.png', 6, "up"))
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_3.rect.centerx, self.enemy_3.rect.centery, 'assets/enemybullet.png', 6, "reg"))
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_3.rect.centerx, self.enemy_3.rect.centery, 'assets/enemybullet.png', 6, "down"))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    time_elapsed_3 = 0

            #creates new enemies periodaically
            if enemy1_accum > 6000:
                for i in range(self.enemy1_freq):
                    y = random.randrange(30, 400)
                    x = random.randrange(550, 600)
                    self.enemies1.add(enemy_1.enemy_1(x, y, 3, 'assets/enemy.png' ))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    enemy1_accum = 0
            if (enemy2_accum >= 10000):     #change to 30000
                enemy2_accum = 0
                enemy_time += 1
                for i in range(self.enemy2_freq):
                    y = random.randrange(30, 400)
                    x = random.randrange(550, 600)
                    self.enemies2.add(enemy_2.enemy_2(x, y, 3, 'assets/enemy2.png' ))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
            if (enemy3_accum >= 15000):     #change to 60000
                enemy3_accum = 0
                enemy_time += 1
                for i in range(self.enemy3_freq):
                    y = random.randrange(30, 400)
                    x = random.randrange(550, 600)
                    self.enemies3.add(enemy_3.enemy_3(x, y, 3, 'assets/enemy3.png' ))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
            self.background.fill((250, 250, 250)) #white
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        if (self.hero.rect.y > 0):
                            self.hero.move("up")
                    elif(event.key == pygame.K_DOWN):
                        if (self.hero.rect.y < 420):
                            self.hero.move("down")
                    elif(event.key == pygame.K_LEFT):
                        if (self.hero.rect.x > 0):
                            self.hero.move("left")
                    elif(event.key == pygame.K_RIGHT):
                        if (self.hero.rect.x < 500):
                            self.hero.move("right")
                    elif(event.key == pygame.K_SPACE):
                        self.heroBullet.add(heroBullet.heroBullet(self.hero.rect.x + 50, self.hero.rect.y + 20, 12, 'assets/herobullet.png'))
                        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
            #check for heroBullet collisions with enemy
            if pygame.sprite.groupcollide(self.heroBullet, self.enemies1, True, True):
                e1_killcount += 1
            if pygame.sprite.groupcollide(self.heroBullet, self.enemies2, True, True):
                e2_killcount += 1
            if pygame.sprite.groupcollide(self.heroBullet, self.enemies3, True, True):
                e3_killcount += 1
            # check for heroship collisions with emeny ships
            ship_collide1 = pygame.sprite.spritecollide(self.hero, self.enemies1, True) != []
            if ship_collide1:
                self.hero.health -= 1
                print(self.hero.health)
                e1_killcount += 1
            ship_collide2 = pygame.sprite.spritecollide(self.hero, self.enemies2, True) != []
            if ship_collide2:
                self.hero.health -= 1
                print(self.hero.health)
                e2_killcount += 1
            ship_collide3 = pygame.sprite.spritecollide(self.hero, self.enemies3, True) != []
            if ship_collide3:
                self.hero.health -= 1
                print(self.hero.health)
                e3_killcount += 1
            #check for enemyBullet collisions with hero
            collide = pygame.sprite.spritecollide(self.hero, self.enemyBullet, True) != []
            if collide:
                self.hero.health -= 1
                print(self.hero.health)
             #saving killcounts into pickle file to load in game over state
            with open('killcounts.pkl', 'wb') as f:
                pickle.dump((e1_killcount, e2_killcount, e3_killcount), f)
            #redraw the entire screen
            self.all_sprites.update()
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health <= 0):
                self.state = "GAMEOVER"

            #display the text
            font = pygame.font.SysFont("arial", 22, True)
            lives = font.render('Health: ' + str(self.hero.health), True, (250,0,0))
            self.screen.blit(lives, (550,450))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def gameOver(self):
        self.hero.kill()
        with open('killcounts.pkl', 'rb') as f:
            e_killcount = pickle.load(f)
        self.screen.fill((220, 220, 220))
        myfont = pygame.font.SysFont("arial", 50, True)
        message = myfont.render('Game Over', False, (250,0,0))
        self.screen.blit(message, (200,50))
        self.end_enemies1 = pygame.sprite.Group()
        self.end_enemies2 = pygame.sprite.Group()
        self.end_enemies3 = pygame.sprite.Group()
        self.end_enemies1.add(enemy_1.enemy_1(200, 145, 0, 'assets/enemy.png' ))
        self.end_enemies2.add(enemy_2.enemy_2(200, 185, 0, 'assets/enemy2.png' ))
        self.end_enemies3.add(enemy_3.enemy_3(200, 225, 0, 'assets/enemy3.png' ))
        self.end_sprites = pygame.sprite.Group(self.end_enemies1, self.end_enemies2, self.end_enemies3)
        myfont = pygame.font.SysFont("arial", 30, True)
        message1 = myfont.render('x     ' + str(e_killcount[0]), False, (0,128,250))
        message2 = myfont.render('x     ' + str(e_killcount[1]), False, (0,128,250))
        message3 = myfont.render('x     ' + str(e_killcount[2]), False, (0,128,250))
        self.screen.blit(message1, (300,160))
        self.screen.blit(message2, (300,200))
        self.screen.blit(message3, (300,240))
        self.end_sprites.draw(self.screen)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
