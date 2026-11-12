import pygame

import constants
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

import logger

from logger import log_state

def main():
    pygame.init()

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

        clock.tick(60)
        dt = clock.tick(60) / 1000
                                    # line 32, added a print statement here to test the flucation of CPU speeds



    screen.fill(black)

    display.flip() # be advised to always to call this last as it refreshes the screen


if __name__ == "__main__":
    main()
