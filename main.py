# this allows us to use code from
# the open-source pygame library
# throughout this file :D
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        

        #limit the framerate to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()