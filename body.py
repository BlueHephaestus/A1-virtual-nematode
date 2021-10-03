import turtle

w = 1000
h = 1000

# Size of cage
vw = w // 2
vh = h // 2
turtle.Screen().setup(w, h)

# Upper bounds for movements on a given timestep
max_magnitude = 5  # So we move 1% of full map at most
max_angle = 36  # So we move 10% of a full rotation at most


class Body(turtle.Turtle):
    def __init__(self, animate=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # todo add support for this?
        self.animate = animate

        # Add cage display to the canvas
        turtle.getcanvas().create_rectangle(-vw // 2, vh // 2, vw // 2, -vh // 2, width=3,
                                            outline="red")
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

    def normalize(self, angle, magnitude):
        """
        We have chosen our max angle and magnitude values at initialization, so we normalize
            left and right to ensure they fit those ranges
            max(angle) = 512 (255 - (-255))
            max(magnitude) = 512 (255 + 255)

        Note: if 255 ends up being not the max, this needs to change

        So to get normalized values:
            angle* = (angle/max(angle))*max_angle
            magnitude* = (magnitude/max(magnitude))*max_magnitude


        :param angle: [0,512]
        :param magnitude: [0,512]
        :return: [normalized_angle in range [0, max_angle], normalized_magnitude in range [0, max_magnitude]
        """
        return (angle / 512.) * max_angle, (magnitude / 512.) * max_magnitude

    def move(self, left, right):
        """
        # they were using speed to control how much it moved forward and backward, since
        # apparently the gpg interface doesn't allow actual #s forward and back,

        but I am a little confused, wouldn't this mean that a hard right turn would also result
        in it moving a lot to the right in addition to turning that way? How could it then turn on
            it's axis without moving?

            we could have forward/backward amount = left + right, so that
                -255 + 255 = no translation, but maximum rotation
                0 + 255 = medium translation, medium rotation
                255 + 255 = max translation, no rotation

            This makes sense to me, b/c with their model it'd be:
                -255 + 255 = max translation, max rotation
                0 + 255 = medium translation, medium rotation
                255 + 255 = max translation, max rotation
                    it's data lost.
                    so im going with the method that ensures maximum connection of brain-> body

        Each movement is a vector, in that it has angle and magnitude.
        Given left, right, both in ranges [-255,255]:
            angle = max(left,right) - min(left,right)
            magnitude = left + right


        with both left/right and forward/backward being determined by whichever is largest.


        :param left: [-255, 255] accumulated left muscle neuron values
        :param right: [-255, 255] accumulated right muscle neuron values
        :return: (angle, magnitude) indicating the vector we moved
            (normalized for our maximum allowed angle and magnitude)
        """

        # Get raw angles and normalize
        angle = max(left, right) - min(left, right)
        magnitude = left + right
        angle, magnitude = self.normalize(angle, magnitude)

        # Rotate first
        if left >= right:
            # More power in the left, so we turn right
            self.right_rot(angle)
        else:
            # More power in the right, so we turn left
            self.left_rot(angle)

        # Move next
        if magnitude >= 0:
            self.forward(magnitude)
        else:
            self.backward(-magnitude)

        return angle, magnitude
