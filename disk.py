import numpy as np


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
