import pygame
import random

from pygame.transform import rotate
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                            color="white",
                            center=self.position,
                            radius=self.radius,
                            width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        degrees = random.uniform(20, 50)

        angle = self.velocity.copy()
        radius_copy = self.radius

        pos_angle = (angle.rotate(degrees))
        neg_angle = (angle.rotate(-degrees))

        new_radius = radius_copy - ASTEROID_MIN_RADIUS

        new_ast_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_two = Asteroid(self.position.x, self.position.y, new_radius)

        new_ast_one.velocity = pos_angle * 1.2
        new_ast_two.velocity = neg_angle * 1.2
