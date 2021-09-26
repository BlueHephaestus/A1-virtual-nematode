# Handle movement logic
# everything is in radians always

from base import *
from config import *


class Bot():
    def __init__(self):
        self.x = CANVAS_WIDTH // 2
        self.y = CANVAS_HEIGHT // 2
        self.theta = 0

    def update(self, left, right):
        # Given the radian rotation to rotate the (simulated) left wheel and right wheel on our simulated 2-wheel robot,
        # Update our robot's x and y values as well as direction it's facing (theta)
        # left = left wheel rotation
        # right = right wheel rotation

        # the inputs are what the robot's mind outputs.
        # Our outputs are the environmental wrapper around converting those to how it's body moves. It's like the muscles tensing at the command of the brain.

        ####################################
        # Part 1 - Simultaneous Motor Movement
        ####################################
        # Possible cases for this Part

        case_1a = (left == 0 or right == 0)
        case_1b = (left >= 0 and right <= 0)
        case_1c = (left <= 0 and right >= 0)
        case_1d = (left >= 0 and right >= 0)
        case_1e = (left <= 0 and right <= 0)

        # Amount wheels rotate is amount they are both moving
        # AKA however long it takes one of them to reach 0
        wheel_rotation = min(abs(left), abs(right))

        # Take this amount from our left and right rotations to bring them closer to 0
        left -= np.sign(left) * wheel_rotation
        right -= np.sign(right) * wheel_rotation

        if case_1a:
            # Skip to part 2
            pass

        elif case_1b or case_1c:
            # Wheels are both turning in opposite directions, so we rotate in place.
            # So we update only our direction(theta) based on the amount of movement.

            # Obtain bot rotation from wheel rotation
            bot_rotation = wheel_rotation * WHEEL_RADIUS / BOT_RADIUS

            # 1b) Positive change to theta (clockwise)
            if case_1b:
                self.theta += bot_rotation

            # 1c) Negative change to theta (counter-clockwise)
            elif case_1c:
                self.theta -= bot_rotation

        # Case 1d->1e
        elif case_1d or case_1e:
            # Wheels turn in same directions, so we move without rotating.
            # We only update x and y based on amount of movement
            bot_movement = wheel_rotation * WHEEL_RADIUS

            # Using our current theta and the bot movement as our radius
            # for polar calculations, get x and y deltas
            x_delta, y_delta = polar_to_cartesian(bot_movement, self.theta)

            # We either move forward or backward using these deltas depending on the case.
            # (regardless we still face the same direction)

            # Move forward
            if case_1d:
                self.x += x_delta * CANVAS_SCALE
                self.y += y_delta * CANVAS_SCALE

            # Move backward
            elif case_1e:
                self.x -= x_delta * CANVAS_SCALE
                self.y -= y_delta * CANVAS_SCALE

        ####################################
        # Part 2 - Individual Motor Movement
        ####################################
        case_2a = (left == 0 and right == 0)
        case_2b = left != 0
        case_2c = right != 0

        if case_2a:
            # Skip to end
            pass

        elif case_2b or case_2c:

            if case_2b:
                # Clockwise
                sign = 1

                # Get theta delta from left wheel's movement
                theta_delta = left * WHEEL_RADIUS / BOT_DIAMETER

            elif case_2c:
                # Counter-Clockwise
                sign = -1

                # Get theta delta from right wheel's movement
                theta_delta = right * WHEEL_RADIUS / BOT_DIAMETER

            # Compute the actual distance traversed using this and our bot diameter
            bot_movement = BOT_DIAMETER * np.sin(theta_delta / 2)

            # Compute the angle to move x and y along - not the angle we're facing,
            # just the angle we move along to get our x and y deltas
            navigation_theta = self.theta + sign * theta_delta / 2

            # Use this along with theta to get our x and y deltas
            x_delta, y_delta = polar_to_cartesian(bot_movement, navigation_theta)

            # Now we can update our theta
            self.theta = self.theta + sign * theta_delta

            # And we update our x and y's with our deltas scaled accordingly
            self.x += x_delta * CANVAS_SCALE
            self.y += y_delta * CANVAS_SCALE

        # Keep our theta in it's bounds; THETA_MIN <= self.theta <= THETA_MAX
        self.theta = bounded_clip(self.theta, THETA_MIN, THETA_MAX, THETA_RANGE)

        # print("X:{} Y:{} THETA:{}".format(self.x, self.y, self.theta))
