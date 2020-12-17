# import pygame
# start drawing

# lines 8 - 21 displays pygame window
import pygame
import sys

BOARD_SIZE = WIDTH, HEIGHT = 640, 480
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 0, 255, 255


class LifeGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)

    # ball = pygame.image.load('intro_ball.gif')      //are images, but going to draw//
    # ballrect = ball.get_rect()
    def run(self):

        circle_rect = pygame.draw.circle(self.screen, ALIVE_COLOR, (50, 50), 5, width=0)
        print(type(circle_rect))
        print(circle_rect)
        # screen.blit(ball, ballrect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.screen.fill(DEAD_COLOR)

            # screen.blit(ball, ballrect) # is where I'm going to put my rectangles
            pygame.display.flip()  ## blit to draw and flip to push it into memory


if __name__ == '__main__':
    game = LifeGame()
    game.run()

