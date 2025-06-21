import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable, )
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    running = True

    while running:
        
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")


        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                running = False
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
