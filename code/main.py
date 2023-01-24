import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # General setup
        # Initialize the pygame library
        pygame.init()
        # Set the screen size
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Set the window title
        pygame.display.set_caption('Zelda')
        # Create a clock object to control the game's frame rate
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        # Start the game loop
        while True:
            # Checkfor QUIT event (e.g. when the window is closed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Clear the screen to black
            self.screen.fill('black')
            self.level.run()
            # Update the display
            pygame.display.update()
            # Limit the frame rate
            self.clock.tick(FPS)

# Create and instance of the game and start the game loop
if __name__ == '__main__':
    game = Game()
    game.run()