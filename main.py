from world import World
from beams import Beam
from nodes import Node
from utils import BALL_SIZE

import numpy as np
import pyglet
from pyglet import shapes

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

X_DRAW_FACTOR, Y_DRAW_FACTOR = 1, 1
X_DRAW_OFFSET, Y_DRAW_OFFSET = 50, 50

world = World()
line = shapes.Line(x=150, y=150, x2=150, y2=150, width=5, color = (255, 255, 255), batch = batch)
line2 = shapes.Line(x=150, y=150, x2=150, y2=150, width=5, color = (255, 255, 255), batch = batch)
line3 = shapes.Line(x=150, y=150, x2=150, y2=150, width=5, color = (255, 255, 255), batch = batch)
circle_a = pyglet.shapes.Circle(x=150, y=150, radius=BALL_SIZE, color=(255, 0, 0), batch=batch)
circle_b = pyglet.shapes.Circle(x=150, y=150, radius=BALL_SIZE, color=(0, 255, 0), batch=batch)
circle_c = pyglet.shapes.Circle(x=150, y=150, radius=BALL_SIZE, color=(0, 0, 255), batch=batch)

a = Node(np.array([270.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
b = Node(np.array([180.0, 330.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
c = Node(np.array([250.0, 300.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 10)
ligne = Beam(a, b, 1, 160.0, 0.5)
ligne2 = Beam(b, c, 1, 160.0, 0.5)
ligne3 = Beam(a, c, 1, 160.0, 0.5)

world.add_object(ligne)
world.add_object(ligne2)
world.add_object(ligne3)
world.add_object(a)
world.add_object(b)
world.add_object(c)

def update(interval=1):
    world.step(1)

    line.x, line.y = X_DRAW_FACTOR*a.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*a.y + Y_DRAW_OFFSET
    line.x2, line.y2 = X_DRAW_FACTOR*b.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*b.y + Y_DRAW_OFFSET

    line2.x, line2.y = X_DRAW_FACTOR*b.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*b.y + Y_DRAW_OFFSET
    line2.x2, line2.y2 = X_DRAW_FACTOR*c.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*c.y + Y_DRAW_OFFSET

    line3.x, line3.y = X_DRAW_FACTOR*a.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*a.y + Y_DRAW_OFFSET
    line3.x2, line3.y2 = X_DRAW_FACTOR*c.x + X_DRAW_OFFSET, Y_DRAW_FACTOR*c.y + Y_DRAW_OFFSET

    circle_a.x = X_DRAW_FACTOR*a.x + X_DRAW_OFFSET
    circle_a.y = Y_DRAW_FACTOR*a.y + Y_DRAW_OFFSET

    circle_b.x = X_DRAW_FACTOR*b.x + X_DRAW_OFFSET
    circle_b.y = Y_DRAW_FACTOR*b.y + Y_DRAW_OFFSET

    circle_c.x = X_DRAW_FACTOR*c.x + X_DRAW_OFFSET
    circle_c.y = Y_DRAW_FACTOR*c.y + Y_DRAW_OFFSET

    

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.clock.schedule_interval(update, 1/200.0)

pyglet.app.run()