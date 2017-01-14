import wpilib

from wpilib.command.subsystem import Subsystem

from commands.followjoystick import FollowJoystick

import robotmap

class DriveTrain(Subsystem):

    def __init__(self):
        super().__init__('DriveTrain')

        self.leftMotors = wpilib.Talon(robotmap.portsList.leftMotorID)
        # self.leftMotors.setInverted(True)
        self.rightMotors = wpilib.Talon(robotmap.portsList.rightMotorID)

        # self.leftMotorsEncoder = wpilib.Encoder(robotmap.portsList.leftMotorsEncoderChannelAID, robotmap.portsList.leftMotorsEncoderChannelBID)
        # self.rightMotorsEncoder = wpilib.Encoder(robotmap.portsList.rightMotorsEncoderChannelAID, robotmap.portsList.rightMotorsEncoderChannelBID)

        self.robotDrive = wpilib.RobotDrive(self.leftMotors, self.rightMotors)
        self.robotDrive.setInvertedMotor(wpilib.RobotDrive.MotorType.kRearLeft, True)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())

    def set(self, yAxis, xAxis):
        self.robotDrive.arcadeDrive(yAxis, xAxis)
