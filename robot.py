import wpilib

from commandbased import CommandBasedRobot

import subsystems
from commands.followjoystick import FollowJoystick

class Robot(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        self.followJoystick = FollowJoystick()

    def teleopInit(self):
        self.followJoystick.start()

if __name__ == '__main__':
    wpilib.run(Robot)
