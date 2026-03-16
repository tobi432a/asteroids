import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT # type: ignore
from logger import log_state, log_event # type: ignore
from player import Player # type: ignore
from asteroid import Asteroid # type: ignore
from asteroidfield import AsteroidField # type: ignore



 

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: "+ str(SCREEN_WIDTH))
    print("Screen height: "+ str(SCREEN_HEIGHT))
    pygame.init()
    Player.containers = pygame.sprite.Group()  # type: ignore
    updatable = pygame.sprite.Group()  # type: ignore
    drawable = pygame.sprite.Group()  # type: ignore
    asteroids = pygame.sprite.Group()  # type: ignore
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        if pygame.key.get_pressed()[pygame.K_w]:
            player.move(dt)
        if pygame.key.get_pressed()[pygame.K_s]:
            player.move(-dt)
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0

if __name__ == "__main__":
    main()
