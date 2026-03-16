import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT # type: ignore
from logger import log_state # type: ignore

 

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: "+ str(SCREEN_WIDTH))
    print("Screen height: "+ str(SCREEN_HEIGHT))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
