import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
     # --- groups ---
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()


  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # cap to 60 FPS and get delta time in seconds
        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over!")
                pygame.quit()
                return
        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
