# import numpy as np
import math


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    g = 9.81  # gravity
    theta_rad = math.radians(incline)  # converting angle to radians

    # Potential energy at top
    potential_energy = mass * g * height

    # Work done by friction
    normal_force = mass * g * math.cos(theta_rad)
    friction_force = friction * normal_force
    work_friction = friction_force * length

    # Effective energy for translation
    effective_energy = potential_energy - work_friction

    if effective_energy < 0:
        # Not enough energy to overcome friction
        return 0.0

    # Total kinetic energy:
    # I = (1/2) * m * r²
    # 0.5 * I * ω² = 0.25 * m * v²
    total_mass_factor = mass + 0.5 * mass  # m + I/r²
    final_speed = math.sqrt(2 * effective_energy / total_mass_factor)

    return final_speed


def test_disk():
    v1 = final_disk_speed(height=2.0, length=3.0, incline=40.0, mass=1.0, friction=0.0, radius=0.1)
    print(f"Test 1 Speed: {v1:.3f} m/s")

    v2 = final_disk_speed(height=1.0, length=5.0, incline=20.0, mass=2.0, friction=0.2, radius=0.2)
    print(f"Test 2 Speed: {v2:.3f} m/s")

test_disk()
