from world import World
from beams import Beam
from nodes import Node

import numpy as np
import pyglet
from pyglet import shapes

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

X_DRAW_FACTOR, Y_DRAW_FACTOR = 1, 1
X_DRAW_OFFSET, Y_DRAW_OFFSET = 50, 50

world = World()
line = shapes.Line(x=150, y=150, x2=150, y2=150, width=5, color = (255, 255, 255), batch = batch)
circle_a = pyglet.shapes.Circle(x=150, y=150, radius=10, color=(255, 0, 0), batch=batch)
circle_b = pyglet.shapes.Circle(x=150, y=150, radius=10, color=(0, 255, 0), batch=batch)


a = Node(np.array([270.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
b = Node(np.array([180.0, 330.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
ligne = Beam(a, b, 1, 160.0, 0.5)

world.add_object(ligne)
world.add_object(a)
world.add_object(b)

def update(interval=1):
    world.step(1)

    line.x, line.y = X_DRAW_FACTOR*a.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*a.y + Y_DRAW_OFFSET
    line.x2, line.y2 = X_DRAW_FACTOR*b.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*b.y + Y_DRAW_OFFSET

    circle_a.x = X_DRAW_FACTOR*a.x + X_DRAW_OFFSET
    circle_a.y = Y_DRAW_FACTOR*a.y + Y_DRAW_OFFSET

    circle_b.x = X_DRAW_FACTOR*b.x + X_DRAW_OFFSET
    circle_b.y = Y_DRAW_FACTOR*b.y + Y_DRAW_OFFSET


@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.clock.schedule_interval(update, 1/200.0)

pyglet.app.run()