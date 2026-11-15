import pygame

import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED

import logger
from logger import log_state

import player
from player import Player

import circleshape
from circleshape import CircleShape


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    clock = pygame.time.Clock()
    dt = 0.0 # meaning 'delta'

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))




    while True:
        log_state()

        for event in pygame.event.get(): # refer/acknoledge this as the event queue
            if event.type == pygame.QUIT:
                return


        dt = clock.tick(60) / 1000

        screen.fill("black")
        for i in drawable:
            i.draw(screen)

        updatable.update(dt)

        pygame.display.flip() # be advised to always to call this last as it refreshes the screen





if __name__ == "__main__":
    main()
