from wpilib.command import Command

import subsystems

import robotmap

class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')
        self.requires(subsystems.drivetrain)

    def execute(self):
        subsystems.drivetrain.set(subsystems.operatorinput.joystick.getRawAxis(robotmap.buttonsList.yAxis), subsystems.operatorinput.joystick.getRawAxis(robotmap.buttonsList.xAxis))

    def isFinished(self):
        super().isFinished()
