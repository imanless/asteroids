from circleshape import CircleShape
import random
from constants import *
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = int(random.uniform(20,51))          
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_1.velocity = vector1*1.2
            ast_2.velocity = vector2*1.2
