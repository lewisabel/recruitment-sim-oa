import numpy as np
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
    incline_rad = np.deg2rad(incline)

    if length <= 0:
      raise Exception("Slope length must be greater than 0.")
    if not math.isclose(height/length, np.tan(incline_rad), abs_tol=0.001):
      raise Exception("Incline angle does not match with height and length of slope.")
    if friction < 0 or friction > 1:
      raise Exception("Friction coefficient must be between 0 and 1.")
    g = 9.81
    initial_COM_height= height + (radius*np.cos(incline_rad))
    final_COM_height = radius
    abs_delta_height = initial_COM_height - final_COM_height
    final_velocity = np.sqrt(g*abs_delta_height*4/3)

    return final_velocity

# test exceptions thrown for bad inputs
def test_exception_1():
  with np.testing.assert_raises_regex(Exception, "Slope length must be greater than 0."):
    final_disk_speed(10, 0, 90, 10, 0.33, 4)
def test_exception_2():
  with np.testing.assert_raises_regex(Exception, "Incline angle does not match with height and length of slope."):
    final_disk_speed(10, 10, 30, 10, 0.33, 4)
def test_exception_3():
  with np.testing.assert_raises_regex(Exception, "Friction coefficient must be between 0 and 1."):
    final_disk_speed(10, 10, 45, 10, 1.33, 4)
def test_exception_4():
  with np.testing.assert_raises_regex(Exception, "Friction coefficient must be between 0 and 1."):
    final_disk_speed(10, 10, 45, 10, -0.33, 4)

# test proper value
def test_value_1():
  assert final_disk_speed(0, 1, 0, 1, 0, 1) == 0.0
def test_value_2():
  assert math.isclose(final_disk_speed(10, 10, 45, 1, 0.33, 1), 11.26805026, abs_tol=0.00001)

def test_all():
    test_exception_1()
    test_exception_2()
    test_exception_3()
    test_exception_4()

    test_value_1()
    test_value_2
