import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    updatables= pygame.sprite.Group()
    drawables= pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids ,updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(x,y)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                     return
        
        updatables.update(dt)
        for stones in asteroids:
            if stones.check_collision(player):
                print("Game Over")       
                sys.exit()
            for shot in shots:
                 if stones.check_collision(shot):
                      shot.kill()
                      stones.split()       
        screen.fill("black")
        for items in drawables: 
            items.draw(screen)
        pygame.display.flip()
        dt = time.tick(60)/1000
        

if __name__== "__main__":
    main()