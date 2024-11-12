import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        time = timer.tick(60)
        dt = time/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()

 ##   print("Starting asteroids!")
 ##   print(f"Screen width: {SCREEN_WIDTH}")
 ##   print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

