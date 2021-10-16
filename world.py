import numpy as np

from nodes import Node
from beams import Beam

class World():

    def __init__(self):

        self.beams, self.nodes = [], []
        self.gravity = np.array([0.0, -9.81, 0.0])

    def add_object(self, object):
        if isinstance(object, Beam):
            self.beams.append(object)
        elif isinstance(object, Node):
            self.nodes.append(object)
    
    def remove_object(self, object):
        if isinstance(object, Beam):
            self.beams.remove(object)
        elif isinstance(object, Node):
            self.nodes.remove(object)

    def step(self, delta_time):
        for obj in self.beams:
            obj.step(delta_time)
        for obj in self.nodes:
            obj.step(delta_time)
