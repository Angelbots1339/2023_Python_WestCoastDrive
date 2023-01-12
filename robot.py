from re import I
from wpilib import XboxController
from wpilib import Talon

# Create objects for the Xbox controller and the Spark motor controllers
controller = XboxController(0)
front_left_motor = Talon(0)
front_right_motor = Talon(1)
rear_left_motor = Talon(2)
rear_right_motor = Talon(3)
center_left_motor = Talon(4)
center_right_motor = Talon(5)


def teleopPeriodic():
    # Get the joystick values from the Xbox controller
    x = controller.getleftX()
    y = controller.getleftY()

    # Apply the motor speeds to the motor controllers
    if(x> 0.1 or y> 0.1):
        front_left_motor.set(-y + x)
        center_left_motor.set(-y + x)
        rear_left_motor.set(-y + x)
        
        front_right_motor.set(-y - x)
        center_right_motor.set(-y - x)
        rear_right_motor.set(-y - x)
    else:
        front_left_motor.set(0)
        center_left_motor.set(0)
        rear_left_motor.set(0)
        
        front_right_motor.set(0)
        center_right_motor.set(0)
        rear_right_motor.set(0)