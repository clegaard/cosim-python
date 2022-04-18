import numpy as np


class RobotArm:
    def __init__(self, angle, velocity, interia, gravity, mass, radius):
        self.angle = angle
        self.velocity = velocity
        self.interia = interia
        self.gravity = gravity
        self.mass = mass
        self.radius = radius

    def step(self, step_size, torque_motor):

        torque_gravity = -self.mass * self.gravity * self.radius * np.cos(self.angle)
        acceleration = (torque_motor + torque_gravity) / self.interia
        self.velocity = self.velocity + step_size * acceleration
        self.angle = self.angle + step_size * self.velocity
