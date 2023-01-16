import wpilib
import wpilib.drive

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):

        self.lstick = wpilib.Joystick(0)
        self.rstick = wpilib.Joystick(1)

        self.front_left = wpilib.Jaguar(1)
        self.mid_left = wpilib.Jaguar(2)
        self.rear_left = wpilib.Jaguar(3)
        self.left = wpilib.MotorControllerGroup(self.front_left, self.mid_left, self.rear_left)

        self.front_right = wpilib.Jaguar(4)
        self.mid_right = wpilib.Jaguar(5)
        self.rear_right = wpilib.Jaguar(6)
        self.right = wpilib.MotorControllerGroup(self.front_right, self.mid_right, self.rear_right)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""

        self.drive.arcadeDrive(-self.lstick.getY(), self.lstick.getX())

        # Move a motor with a Joystick
        y = self.rstick.getY()

        # stop movement backwards when 1 is on
        if self.limit1.get():
            y = max(0, y)

        # stop movement forwards when 2 is on
        if self.limit2.get():
            y = min(0, y)

        self.motor.set(y)


if __name__ == "__main__":
    wpilib.run(MyRobot)