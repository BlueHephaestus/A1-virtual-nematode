from turtle import *

begin_fill()

def fwd(*args, **kwargs):
    # go fwd by distance, else keep going fwd
    forward(20)
    pass

def bwd(*args, **kwargs):
    # go bwd by distance, else keep going bwd
    backward(20)
    pass

def left_rot(*args, **kwargs):
    # turn left without changing position
    pass

def right_rot(*args, **kwargs):
    # turn right without changing position
    pass

def stop(*args, **kwargs):
    # stop movin
    pass

def set_speed(*args, **kwargs):
    # sets both left and right motors to this speed, range [0, 255]
    pass

def us_dist(*args, **kwargs):
    # returns the distance measured from the Ultra Sonic sensor,
    # i.e. range in front of it to the nearest object
    # takes the PIN as argument, ofc we don't need that
    # returns distance (in cm) of the object
    return -1
    pass