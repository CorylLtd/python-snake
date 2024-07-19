import pygame
from pygame.locals import *

from constants import HEIGHT, WIDTH
from food import Food
from snake import Direction, Snake


class App:
    def __init__(self):
      self._running = True
      self._display_surf = None
      self.size = self.weight, self.height = WIDTH, HEIGHT
      self._snake = Snake()
      self._food = Food.createRandomFood(self._snake)

    def on_init(self):
      pygame.init()
      self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
      pygame.display.set_caption('Python Snake')
      self._running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
        
            if event.key == pygame.K_w:
                self._snake.change_direction(Direction.UP)
            if event.key == pygame.K_s:
                self._snake.change_direction(Direction.DOWN)
            if event.key == pygame.K_a:
                self._snake.change_direction(Direction.LEFT)
            if event.key == pygame.K_d:
                self._snake.change_direction(Direction.RIGHT)

    def on_loop(self):
        self._snake.move()
        
        # collided with ourselves?
        if self._snake.does_self_collide():
            self._running = False
            
        # have we eaten the food?
        if self._snake.does_collide_with_food(self._food):
            self._snake.grow()
            self._food = Food.createRandomFood(self._snake)
         
    def display_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {len(self._snake.body) - 3}", True, "white")
        self._display_surf.blit(text, (10, 10))
         
    def on_render(self):
      # fill the screen with a color to wipe away anything from last frame
      self._display_surf.fill("black")
      self._food.draw(self._display_surf)
      self._snake.draw(self._display_surf)
      self.display_score()
        
    def on_cleanup(self):
      pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
        clock = pygame.time.Clock()
       
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.flip()
            clock.tick(10)

        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
