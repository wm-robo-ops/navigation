# proof of concept navigation tracking using robot wheel turns
from math import pi as PI

class Navigation(object):

    def __init__(self, wheel_circumference, position={ 'x': 0, 'y': 0, 'direction': 0 }):
        self.circ = wheel_circumference
        self.x = position['x']
        self.y = position['y']
        self.direction = position['direction']

    def move(self, n):
        """ move all wheels n rotations
        Args:
            n: number of wheel rotations
                (positive for forward and negative for backwards)
        """
        pass

    def rotate(self, d):
        """
        Args:
            d: rotate some degrees
                (positive for left and negative for right)
        """
        pass



class Position(object):

    """
    Attributes:
        x: x coordinate
        y: y coordinate
        direction: direction the robot is currently facing.
            A number between 0 and 2*PI.
    """
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.d = direction


if __name__ == '__main__':
    nav = Navigation(3)

