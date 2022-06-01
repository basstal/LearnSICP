from vector_operation import *


def make_segment(sx, sy, ex, ey):
    s = make_vect(sx, sy)
    e = make_vect(ex, ey)
    return (s, e)


def start_segment(seg):
    return seg[0]


def end_segment(seg):
    return seg[1]