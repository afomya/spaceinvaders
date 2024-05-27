import sys

import pygame

# importing the spaceship from the class
from spaceship import Spaceship

# importing the laser class
# from laser import Laser

pygame.init()  # initialize pygame

# we specfify the width and height of the display surface
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
# we create a display surface
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)
"""
# we pick a color and add it to the display in the game loop later
GRAY = (128, 128, 128)

# creating the display surface, the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# here we name our game
pygame.display.set_caption("Python Space Invadors")

# here we load the background image
clock = pygame.time.Clock()

# here we initialize the spaceship, if we didn't do this, the
# spaceship wouldn't move and
# it wouldn't be part of the game. we are telling the computer to # create a spaceship object.
spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
# lets initialize the laser
# laser = Laser((100,100),6, SCREEN_HEIGHT)
# laser2 = Laser((100,200),6,SCREEN_HEIGHT)
# time to make the Sprite
spaceship_group = pygame.sprite.GroupSingle()

# adding spaceship to the sprite
spaceship_group.add(spaceship)

# we do this cause there are multiple lasers we are going to shoot
# that is why we have multiple lasers in the top
# laser_group = pygame.sprite.Group()
# adding the lasers to the sprite group
# laser_group.add(laser, laser2)

# setting up the game loop
while True:

    for event in pygame.event.get():
        # defining a way to exit the game when the user want to
        # otherwise the game will keep running forever
        '''
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spaceship.move_right()
            elif event.key == pygame.K_LEFT:
                spaceship.move_left()
        '''
        # updates everything in that method for all the items in                 # the sprite group
        spaceship_group.update()

        # updates everything in that method for all the items in          # the sprite group
        # laser_group.update()

        # adding color to the display
        screen.fill(GRAY)

        #adds the spaceship to the display from the sprite group
        spaceship_group.draw(screen)

        # add the laser to the display
        # laser_group.draw(screen)

        # another way to add the laser to the display
        spaceship_group.sprite.lasers_group.draw(screen)

        # we have to tell the clock object how fast to go
        # otherwise the game will run as fast as our computer can
        # handle, so it will be different on different devices
        pygame.display.update()
        clock.tick(60)
