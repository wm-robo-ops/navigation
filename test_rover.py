from navigation import Navigation
from math import sqrt, atan2, pi

# dummy high level vehicle control API
class Robot(object):
    """
    higher level wrapper for robot operation
    supports moving forward and backwards and also rotating in place
    """

    left_wheels = [ ]
    right_wheels = [ ]
    all_wheels = [ ]

    def __init__(self, motor_pins={ 'back_left': 0, 'back_right': 1, 'front_left': 2, 'front_right': 3 }):
        self.pins = {
            'bl': motor_pins['back_left'],
            'br': motor_pins['back_right'],
            'fl': motor_pins['front_left'],
            'fr': motor_pins['front_right']
        }
        self.nav = Navigation(40, { 'x': 0, 'y': 0, 'direction': 0 })

    def move(self, n):
        # Tell the robot to move
        # to do

        # update the position tracking
        self.nav.move(n)

    def rotate(self, d):
        """
        Args:
            d: number of degrees
            example
            self.rotate(PI/2)
            (end facing)
            ^
            |<—
            |   \ PI/2
            |   ^
            |   |
            ------------> (start facing)
        """

        # update the position tracking
        self.nav.rotate(d)

    def rotate_to(self, angle):
        """
        Args:
            angle: angle to face
            Field:
            __________________________
            |(x,0)                   |
            |          PI/2          |
            |           ^            |
            |           |            |
            |           |            |
            |   PI<---(x,y)--->0     |
            |           |            |
            |           |            |
            |           v            |
            |         3*PI/2         |
            | (0, 0)            (0,x)|
            __________________________
        """
        pass

    def go_to(self, x, y):
        # calcualate angle from current position
        dx = x - self.nav.x
        dy = y - self.nav.y

        distance = sqrt( dx**2 + dy**2 )
        angle = atan2(dy, dx)

        # now go
        self.rotate_to(angle)
        self.move(distance)
        pass


if __name__ == '__main__':
    # test
    rover = Robot()
    rover.go_to(-1,-1)
