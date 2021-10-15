import numpy as np
import matplotlib.pyplot as plt

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

world = World()

a = Node(np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
b = Node(np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
ligne = Beam(a, b, 10, 0.3, 1)

world.add_object(ligne)
world.add_object(a)
world.add_object(b)

for i in range(50):

    world.step(1)
    print(a.position, b.position, ligne.force)
    #print(a.position)
    print()
    plt.plot(i, a.position[0], "bo")
    plt.plot(i, b.position[0], "r+")

plt.show()