import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from controller_oop import Controller
from robot_arm_oop import RobotArm

if __name__ == "__main__":
    m = 1.0  # mass of end effector [kg]
    r = 1.0  # length of link [m]
    g = 9.80665  # gravitation acceleration [m/s^2]
    I = (
        m * r**2
    )  # moment of inertia of point mass at the end of massless link [kg*m^3]
    angle_0 = 0.0  # angle at t=0.0 [rad]
    angle_setpoint = np.pi / 2
    velocity_0 = 0.0  # velocity at t=0.0 [rad/s]
    Δt = 0.001  # step size
    t_eval = np.arange(
        0.0, 1.0, Δt
    )  # time instants for which to evaluate the solution y(t)

    # obtain solution to ordinary differential equations using forward Euler integration scheme
    y0 = (angle_0, velocity_0)
    y = [y0]
    y_cur = y0

    controller = Controller()
    robot_arm = RobotArm(angle_0, velocity_0, I, g, m, r)

    for t in t_eval[1:]:
        controller.step(Δt, robot_arm.angle, -angle_setpoint)
        robot_arm.step(Δt, controller.torque_out)
        y.append((robot_arm.angle, robot_arm.velocity))

    y = np.array(y)

    # plotting
    fig, ax = plt.subplots()
    ax.plot(t_eval, y[:, 0], label="angle")
    ax.plot(t_eval, y[:, 1], label="velocity")
    ax.legend()
    ax.set_xlabel("t")
    plt.show()

    # animation
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    (line,) = ax.plot([], [], "o-", lw=2)
    time_template = "time = %.1fs"
    time_text = ax.text(0.05, 0.9, "", transform=ax.transAxes)

    def update(i):
        angle, vel = y[i]
        xx = np.cos(angle) * r
        yy = np.sin(angle) * r
        line.set_data([0.0, xx], [0.0, yy])
        time_text.set_text(time_template % (i * Δt))
        return (line, time_text)

    ani = FuncAnimation(fig, update, frames=range(y.shape[0]), blit=True, interval=Δt)
    plt.show()
