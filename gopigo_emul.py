import turtle
from turtle import *
turtle.delay(0)
speed = 1

def fwd(*args, **kwargs):
    # go fwd by distance, else keep going fwd
    #print("\tFORWARD")
    forward(1)
    pass

def bwd(*args, **kwargs):
    # go bwd by distance, else keep going bwd
    #print("\tBACKWARD")
    backward(1)
    pass

def left_rot(*args, **kwargs):
    # turn left without changing position
    #print("\tLEFT ROTATE")
    left(10)
    pass

def right_rot(*args, **kwargs):
    # turn right without changing position
    #print("\tRIGHT ROTATE")
    right(10)
    pass

def stop(*args, **kwargs):
    # stop movin
    # not currently relevant, could be implemented if we have turtle running in a separate thread, the "reality" thread
    print("\tSTOP")
    pass

def set_speed(*args, **kwargs):
    # sets both left and right motors to this speed, range [0, 255]
    #print("\tSPEED CHANGE")
    pass

def us_dist(*args, **kwargs):
    # returns the distance measured from the Ultra Sonic sensor,
    # i.e. range in front of it to the nearest object
    # takes the PIN as argument, ofc we don't need that
    # returns distance (in cm) of the object
    return -1
    pass