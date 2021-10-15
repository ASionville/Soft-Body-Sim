import numpy as np
from utils import GRAVITY

class Node():

    def __init__(self, position, velocity, force, mass):
        self.position = position
        self.velocity = velocity
        self.force = force
        self.mass = mass

    def step(self, delta_time):
        print(self.force)
        self.force += (self.mass * GRAVITY)

        self.velocity += (self.force / self.mass) * delta_time
        self.position += self.velocity * delta_time

        
        self.force = np.array([0.0, 0.0, 0.0])