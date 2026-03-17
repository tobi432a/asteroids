from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SPEED, PLAYER_TURN_SPEED,PLAYER_SHOOT_SPEED # type: ignore
import pygame # type: ignore
from circleshape import CircleShape # type: ignore 
from shot import Shot # type: ignore 

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0.0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "light blue", self.triangle(), width=LINE_WIDTH)
    
    def rotate(self, dt):
        keys = pygame.key.get_pressed()
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)  
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  
    
    def shoot(self):
        if self.cooldown_timer > 0:
            return
        else:
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = forward * PLAYER_SHOOT_SPEED