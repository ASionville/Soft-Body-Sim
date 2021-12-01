import numpy as np
from utils import GRAVITY, BALL_SIZE

class Node():

    def __init__(self, position, velocity, force, mass):
        self.position = position
        self.velocity = velocity
        self.force = force
        self.mass = mass

        self.x, self.y, self.z = self.position
        self.vx, self.vy, self.vz = self.velocity

    def step(self, delta_time):
        self.previous_position = self.position.copy()

        self.force += (self.mass * GRAVITY)

        #Force de frottement
        air_drag_force = self.velocity * -0.5
        self.force += air_drag_force
        print(air_drag_force, self.force)

        self.velocity += (self.force / self.mass) * delta_time
        self.position += self.velocity * delta_time

        
        self.force = np.array([0.0, 0.0, 0.0])
        self.x, self.y, self.z = self.position
        self.vx, self.vy, self.vz = self.velocity