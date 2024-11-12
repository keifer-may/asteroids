import pygame
from constants import *
from player import Player

def main():
    ## Init pygame
    pygame.init()

    ## Create groups for our game objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    ## All player objects must be updateable & drawable
    Player.containers = (updateable, drawable)

    ## Create time clock and dt
    timer = pygame.time.Clock()
    dt = 0
    
    ## Create screen & player object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        ## FPS calcs
        time = timer.tick(60)
        dt = time/1000

        ## Ensures closing window ends game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ## Update all updateable objects (players only for now)
        for each in updateable:
            each.update(dt)

        ## Fill screen black
        screen.fill("black")

        ## Draw all drawable objects (players only for now)
        for each in drawable:
            each.draw(screen)

        pygame.display.flip()

 ##   print("Starting asteroids!")
 ##   print(f"Screen width: {SCREEN_WIDTH}")
 ##   print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

