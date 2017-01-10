from wpilib.command.subsystem import Subsystem

from wpilib.joystick import Joystick

import robotmap

class OperatorInput(Subsystem):

    def __init__(self):
        super().__init__('Operator Input')

        self.joystick = Joystick(robotmap.portsList.stickID)
