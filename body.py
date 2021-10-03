import turtle

class Body(turtle.Turtle):
    def __init__(self, animate=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animate = animate

        if not self.animate:
            turtle.tracer(15,0)
            #turtle.delay(0) # remove delay
            #self.ht() # hide body

        self.speed = 1

    def fwd(self, *args, **kwargs):
        # go fwd by distance, else keep going fwd
        #print("\tFORWARD")
        self.forward(1)
        pass

    def bwd(self, *args, **kwargs):
        # go bwd by distance, else keep going bwd
        #print("\tBACKWARD")
        self.backward(1)
        pass

    def left_rot(self, *args, **kwargs):
        # turn left without changing position
        #print("\tLEFT ROTATE")
        self.left(10)
        pass
        pass

    def right_rot(self, *args, **kwargs):
        # turn right without changing position
        #print("\tRIGHT ROTATE")
        self.right(10)
        pass

    def stop(self, *args, **kwargs):
        # stop movin
        # not currently relevant, could be implemented if we have turtle running in a separate thread, the "reality" thread
        print("\tSTOP")
        pass

    def set_speed(self, *args, **kwargs):
        # sets both left and right motors to this speed, range [0, 255]
        #print("\tSPEED CHANGE")
        pass

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