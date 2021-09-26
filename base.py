import numpy as np


def polar_to_cartesian(r, theta):
    return r * np.cos(theta), r * np.sin(theta)


def bounded_clip(x, low, high, dist):
    # Given an x expected to be bound within a circular range low <= x <= high,
    # with dist = abs(high-low),
    # Ensure it stays within those bounds.
    if x < low:
        x = high - (abs(low - x) % dist)
    elif x > high:
        x = low + (abs(high - x) % dist)
    return x
