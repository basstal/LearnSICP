from interval_bounds import *

def make_interval(x, y):
    return {'x' : x, 'y' : y}

def sub_interval(x, y):
    return make_interval(lower_bound(x) - lower_bound(y), upper_bound(x) - upper_bound(y))
    