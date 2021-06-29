import pygame
from time import *
from random import *


def flappy_bird():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("flappy bird")
    obs_x = 400
    obs_y = randrange(120,550)
    bird = pygame.image.load('flap.png')
    def car(x,y):
        screen.blit(bird, (x,y))

    def obstacle(obs_x, obs_y):
        pygame.draw.rect(screen, (0, 255, 0), (obs_x,obs_y, 20, 500))
        pygame.draw.rect(screen, (0, 255, 0), (obs_x,obs_y-600, 20, 500))
    x=100
    y=100
    vel=0
    accel = 0.1
    live = True
    run=True
    score = 0
    while run:

        if x == obs_x and live == True:
            score+=1
        screen.fill((91, 188, 228))
        obstacle(obs_x, obs_y)
        if live == True and score < 2:
            obs_x-=1
        if live == True and score > 22:
            obs_x-=3
        if live == True and score > 2:
            obs_x-=2
    #hit box for lower block
        if (x+20)==obs_x and y >= obs_y:
            live = False
        if (y+20) >= obs_y and x>=obs_x and x<(obs_x+20):
            live = False
    #hit box for upper block
        if (x+20)==obs_x and y <= (obs_y -100):
            live = False
        if y <= (obs_y-100) and x>=obs_x and x<=(obs_x+20):
            live = False
        if obs_x <=-50:
            obs_x = 400
            obs_y = randrange(100,350)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and live == True:
            vel = -2
        elif keys[pygame.K_r] and live == False:
            flappy_bird()
        for event in pygame.event.get(12):
            if event.type == pygame.QUIT:
                run = False
        y+= vel
        vel += accel
        r = randrange(1,14)
        b = randrange(1,254)
        g = randrange(1,254)
        pygame.draw.rect(screen, (r, b, g), (x,y, 20, 20))
        car(x,y)
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 800, 10))
        pygame.draw.rect(screen, (255, 0, 0), (0,550, 800, 460))
        if y <= 10 or y >= 550:
            live = False

            
        pygame.display.update()
        pygame.time.delay(10)
    pygame.quit()
flappy_bird()
