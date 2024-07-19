from enum import Enum
import pygame
from constants import BLOCK_SIZE, GRID_HEIGHT, GRID_WIDTH

class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Snake:
  def __init__(self) -> None:
    self.body = [pygame.Vector2(0, 0), pygame.Vector2(1, 0), pygame.Vector2(2, 0)]
    self.direction = pygame.Vector2(1, 0)
    self.counter = 0;
    self.speed = 40
    self.current_direction = Direction.RIGHT
    
  def draw(self, screen):
    for pos in self.body:
      pygame.draw.rect(screen, "green", pygame.Rect(pos.x * BLOCK_SIZE + 1, pos.y * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

  def move(self):
    self.counter += 1
    if (self.counter % (50-self.speed) != 0):
      return
    
    # Get the last added segment of the snake
    head = self.body[-1]
    
    # Work out where the new segment of the snake will be
    new_head = pygame.Vector2((head[0] + self.direction.x + GRID_WIDTH) % GRID_WIDTH, 
                (head[1] + self.direction.y + GRID_HEIGHT) % GRID_HEIGHT)
    
    # add the new segment to the snake
    self.body.append(new_head)
    
    # remove the oldest segment of the snake
    self.body.pop(0)
    
  def change_direction(self, direction: Direction):
    if direction == Direction.UP and self.current_direction != Direction.DOWN:
      self.direction = pygame.Vector2(0, -1)
    if direction == Direction.DOWN and self.current_direction != Direction.UP:
      self.direction = pygame.Vector2(0, 1)
    if direction == Direction.LEFT and self.current_direction != Direction.RIGHT:
      self.direction = pygame.Vector2(-1, 0)
    if direction == Direction.RIGHT and self.current_direction != Direction.LEFT:
      self.direction = pygame.Vector2(1, 0)
      
    self.current_direction = direction
  
  # Check if the snake head has collided with itself
  def does_self_collide(self):
    head = self.body[-1]
    return head in self.body[:-1]
  
  def does_collide_with_food(self, food):
    return self.body[-1] == food.pos
  
  def grow(self):
    self.body.insert(0, self.body[0])
