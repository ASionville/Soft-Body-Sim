import numpy as np
from utils import GRAVITY

class Node():

    def __init__(self, position, velocity, force, mass):
        self.position = position
        self.velocity = velocity
        self.force = force
        self.mass = mass

        self.x, self.y, self.z = self.position

    def step(self, delta_time):
        self.previous_position = self.position.copy()
        self.force += (self.mass * GRAVITY)

        self.velocity += (self.force / self.mass) * delta_time
        self.position += self.velocity * delta_time

        
        self.force = np.array([0.0, 0.0, 0.0])
        self.x, self.y, self.z = self.position