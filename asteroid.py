from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(
                screen,
                "white",
                self.position,
                self.radius,
                LINE_WIDTH
            )    
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid split")
        angle= random.uniform(20,50)
        ang1 = self.velocity.rotate(angle)
        ang2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteriod1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteriod2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteriod1.velocity = ang1 *1.2
        asteriod2.velocity = ang2 *1.2
        