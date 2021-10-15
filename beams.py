import numpy as np

class Beam():

	def __init__(self, A, B, stiffness, rest_length, damping_factor):
		self.a = A
		self.b = B
		self.stiffness = stiffness
		self.rest_length = rest_length
		self.damping_factor = damping_factor
		
		self.x = np.linalg.norm(self.b.position - self.a.position) - self.rest_length
		self.force = np.array([0.0, 0.0, 0.0])

	def step(self, delta_time):
		self.x = np.linalg.norm(self.b.position - self.a.position) - self.rest_length
		
		self.spring_force = self.stiffness * self.x
		self.damping_force = np.dot(((self.b.position - self.a.position) / np.linalg.norm(self.b.position - self.a.position)),
									(self.b.velocity) - self.a.velocity) * self.damping_factor
		self.force = self.spring_force + self.damping_force

		self.a.force = np.dot(self.force, ((self.b.position - self.a.position) / np.linalg.norm(self.b.position - self.a.position)))
		self.b.force = np.dot(self.force, ((self.a.position - self.b.position) / np.linalg.norm(self.a.position - self.b.position)))
