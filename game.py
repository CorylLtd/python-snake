# Example file showing a circle moving on screen
import pygame
from pygame.locals import *

class App:
    def __init__(self):
      self._running = True
      self._display_surf = None
      self.size = self.weight, self.height = 640, 400
      self._player_pos = None

    def on_init(self):
      pygame.init()
      self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
      self._running = True
      self._player_pos = pygame.Vector2(self._display_surf.get_width() / 2, self._display_surf.get_height() / 2)
    
    def on_event(self, event, dt):
      if event.type == pygame.QUIT:
          self._running = False

      if event.type == pygame.VIDEORESIZE:
          self.size = self.weight, self.height = event.size
          self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
          self._player_pos = pygame.Vector2(self._display_surf.get_width() / 2, self._display_surf.get_height() / 2)

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              self._running = False
      
      '''
          if event.key == pygame.K_w:
              self._player_pos.y -= 300 * dt
          if event.key == pygame.K_s:
              self._player_pos.y += 300 * dt
          if event.key == pygame.K_a:
              self._player_pos.x -= 300 * dt
          if event.key == pygame.K_d:
              self._player_pos.x += 300 * dt
      '''


    def on_loop(self, dt):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
          self._player_pos.y -= 300 * dt
      if keys[pygame.K_s]:
          self._player_pos.y += 300 * dt
      if keys[pygame.K_a]:
          self._player_pos.x -= 300 * dt
      if keys[pygame.K_d]:
          self._player_pos.x += 300 * dt

      
    def on_render(self):
      # fill the screen with a color to wipe away anything from last frame
      self._display_surf.fill("black")

      # draw a square at the player's position
      pygame.draw.rect(self._display_surf, "blue", pygame.Rect(self._player_pos.x - 20, self._player_pos.y - 20, 40, 40))

      # draw a circle at the player's position
      # pygame.draw.circle(screen, "red", player_pos, 40)
        
    def on_cleanup(self):
      pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
        clock = pygame.time.Clock()
        dt = 0;

 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event, dt)
            self.on_loop(dt)
            self.on_render()
            pygame.display.flip()
            dt = clock.tick(60) / 1000

        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
