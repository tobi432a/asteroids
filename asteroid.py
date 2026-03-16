import pygame
from constants import *
from circleshape import CircleShape # type: ignore
import random
from logger import log_event # type: ignore

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS * 2:
            return []
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            vel_asteroid1 = self.velocity.rotate(random_angle)
            vel_asteroid2 = self.velocity.rotate(-random_angle)
            rad_asteroid1 = self.radius / 2
            rad_asteroid2 = self.radius / 2
            ast1 = Asteroid(self.position.x, self.position.y, rad_asteroid1)
            ast2 = Asteroid(self.position.x, self.position.y, rad_asteroid2)
            ast1.velocity = vel_asteroid1 * random.uniform(1, 1.4)
            ast2.velocity = vel_asteroid2 * random.uniform(1, 1.4)
            return [ast1, ast2]
            


