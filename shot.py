import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, direct):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = PLAYER_SHOOT_SPEED
        self.direct = direct

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                            color="white",
                            center=self.position,
                            radius=self.radius,
                            width=2)

    def update(self, dt):
        self.position += (self.direct * self.velocity * dt)

