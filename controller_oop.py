class Controller:
    def __init__(self):
        self.torque_out = 0.0

    def step(self, step_size, angle, angle_setpoint):

        self.torque_out = 0.0  # replace this with controller logic
