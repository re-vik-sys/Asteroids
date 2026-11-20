import pygame
import random

import circleshape
from circleshape import CircleShape

import logger
from logger import log_event

import constants
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:

        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)

            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            positive_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            positive_asteroid.velocity = vector_1 * 1.2
            negative_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            negative_asteroid.velocity = vector_2 * 1.2
