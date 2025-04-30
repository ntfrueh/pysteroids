# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, all_shots)

    

    player_object = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="#000000")
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision_detect(player_object):
                print("Game over!")
                return
            for shot in all_shots:
                if asteroid.collision_detect(shot):
                    asteroid.split()
                    shot.kill()
                
        pygame.display.flip()
        time_passed = game_clock.tick(60)
        dt = time_passed / 1000
        player_object.timer -= dt


if __name__ == "__main__":
    main()