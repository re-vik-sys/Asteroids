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

        if self.asteroid <= ASTEROID_MIN_RADIUS:
            return

        else:
            log_event("asteroid_split")
            random.uniform(20, 50)
            self.asteroid.rotate(self.velocity)
            self.asteroid.rotate()
