import turtle

w = 1000
h = 1000

# Size of cage
vw = w // 2
vh = h // 2
turtle.Screen().setup(w, h)

# Upper bounds for movements on a given timestep
max_mag = 5  # So we move 1% of full map at most
#max_angle = 36  # So we move 10% of a full rotation at most
max_angle = 360 # Since this empirically is very small


class Body(turtle.Turtle):
    def __init__(self, animate=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # todo add support for this?
        self.animate = animate

        # Add cage display to the canvas
        turtle.getcanvas().create_rectangle(-vw // 2, vh // 2, vw // 2, -vh // 2, width=3, outline="red")
        turtle.tracer(15, 0)
        # self.ht() # hide body

        self.speed = 1

    def us_dist(self, *args, **kwargs):
        # returns the distance measured from the Ultra Sonic sensor,
        # i.e. range in front of it to the nearest object
        # takes the PIN as argument, ofc we don't need that
        # returns distance (in cm) of the object
        return -1
        pass

    def exit(self):
        if not self.animate:
            turtle.update()

    def normalize(self, angle, mag):
        """
        We have chosen our max angle and magnitude values at initialization, so we normalize
            left and right to ensure they fit those ranges
            max(angle) = 512 (255 - (-255))
            max(mag) = 512 (255 + 255)

        Note: if 255 ends up being not the max, this needs to change

        So to get normalized values:
            angle* = (angle/max(angle))*max_angle
            mag* = (mag/max(mag))*max_mag


        :param angle: [0,512]
        :param mag: [0,512]
        :return: [normalized_angle in range [0, max_angle], normalized_mag in range [0, max_mag]
        """
        return (angle / 512.) * max_angle, (mag / 512.) * max_mag

    def move(self, left, right):
        """
        Given neuron firings for force to apply to left muscles and right muscles,
            compute the normalized angle and magnitude to move the nematode body
            and move it. Return normalized angle and magnitude.

        Each movement is a vector, in that it has angle and magnitude.
        Given left, right, both in ranges [-255,255]:
            angle = max(left,right) - min(left,right)
            mag = left + right

        With both left/right and forward/backward being determined by whichever is largest.


        :param left: [-255, 255] accumulated left muscle neuron values
        :param right: [-255, 255] accumulated right muscle neuron values
        :return: (angle, mag) indicating the vector we moved
            (normalized for our maximum allowed angle and magnitude)
        """

        # Get raw angles and normalize
        angle = max(left, right) - min(left, right)
        mag = left + right
        angle, mag = self.normalize(angle, mag)

        # Rotate first
        if left >= right:
            # More power in the left, so we turn right
            self.right(angle)
        else:
            # More power in the right, so we turn left
            self.left(angle)

        # Move next
        if mag >= 0:
            self.forward(mag)
        else:
            self.backward(-mag)

        return angle, mag
