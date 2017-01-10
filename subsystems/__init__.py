from .drivetrain import DriveTrain
from .operatorinput import OperatorInput

drivetrain = None
operatorinput = None


def init():

    global drivetrain, operatorinput

    drivetrain = DriveTrain()
    operatorinput = OperatorInput()
