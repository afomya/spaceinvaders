import pygame


# Define a new class called Laser that is a type of sprite
class Laser(pygame.sprite.Sprite):
  def __init__(self,position,speed, screen_height):
    super().__init__()
    self.image = pygame.Surface((5,15))
    self.image.fill((255, 255, 0))
    self.rect = self.image.get_rect(center = position)
    self.speed = speed
    self.screen_height = screen_height

  def update(self):
    # to move the laser up, positive numbers as arguments

    # to move down, negative numbers as arguments
    self.rect.y -= self.speed
    # what if the laser goes off the screen?
    if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
      # print("Dead!")
      self.kill()