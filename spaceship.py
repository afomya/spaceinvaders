# # Import the Pygame library so we can use it
import pygame

# let's import the laser
from laser import Laser


# Define a new class called Spaceship that is a type of sprite
class Spaceship(pygame.sprite.Sprite):
  # This is the initializer method for our Spaceship class
  def __init__(self, screen_width, screen_height):
    # Call the initializer of the parent class
    super().__init__()
    # Store the screen width and height in an attribute
    self.screen_width = screen_width
    self.screen_height = screen_height
    # Load the spaceship image from the file
    self.image = pygame.image.load("Image/spaceship.png")
    # Get the rectangle for the image and set its position
    self.rect = self.image.get_rect(midbottom=(self.screen_width / 2,
                                               screen_height))
    # Set the speed of the spaceship
    self.speed = 6
    # add the laser
    self.lasers_group = pygame.sprite.Group()
    # indicating that the spaceship is alive
    self.laser_ready = True
    # shows the laser is ready to fire
    self.laser_time = 0
    # controls time delay between lasers
    self.laser_delay = 300


# new method for handling spaceship movement based on user input
def get_user_input(self):
  # get a list of all the keys that are currently pressed
  keys = pygame.key.get_pressed()

  # check if the right arrow key is pressed
  # the code here does not mean the spaceship will move right
  # when we click the right arrow key live on here
  # if we wanted to do that, we would need add two methods
  # then we would need to call them in the game loop
  '''
  def move_right(self):
    if self.rect.right < self.screen_width:
      self.rect.x += self.speed

  def move_left(self):
    if self.rect.left > 0:
      self.rect.x -= self.speed
  '''
  if keys[pygame.K_RIGHT] and self.rect.right:
    # self.rect.x = self.rect.x + self.speed
    self.rect.x += self.speed
  # check if the left arrow key is pressed
  if keys[pygame.K_LEFT]:
    # self.rect.x = self.rect.x - self.speed
    self.rect.x -= self.speed
  # note that since we only want it to move left and right, we
  # don't need to check if the up or down arrow keys are pressed
  # therefore, we don't need to add any code for that here

  if keys[pygame.K_SPACE] and self.laser.ready:
    self.laser_ready = False
    laser = Laser(self.rect.center, 5, self.screen_height)
    self.lasers_group.add(laser)
    self.laser_time = pygame.time.get_ticks()

# checking if the laser works in real time 
def shoot_laser(self):
  laser = Laser(self.rect.center, 5, self.screen_height)
  self.laser_group.add(laser)


# new method for updating different methods in this class
# the first one being the spaceship's movement
def update(self):
  self.get_user_input()
  self.contraint_movement()
  self.lasers_group.update()
  self.recharge_laser()

def contraint_movement(self):
  if self.rect.right > self.screen_width:
    self.rect.right = self.screen_width
  if self.rect.left < 0:
    self.rect.left = 0

def recharge_laser(self):
  if not self.laser_ready:
    current_time = pygame.time.get_ticks()
    if current_time - self.laser_time >= self.laser_delay:
      self.laser_ready = Tru