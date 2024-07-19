from random import randint
import pygame
from constants import BLOCK_SIZE, GRID_WIDTH, GRID_HEIGHT
from snake import Snake

class Food:
    def __init__(self, pos: pygame.Vector2) -> None:
        self.pos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow",  
                           (self.pos.x * BLOCK_SIZE + (1 + BLOCK_SIZE/2), 
                            self.pos.y * BLOCK_SIZE + (1 + BLOCK_SIZE/2)), 
                           (BLOCK_SIZE - 4)/2)                       
      
    @staticmethod  
    def createRandomFood(snake: Snake):
      while True:
        food = Food(pygame.Vector2(randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1)))
        if food.pos not in snake.body:
          return food
      
    