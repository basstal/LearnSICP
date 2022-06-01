from turtle import xcor, ycor


def make_vect(x, y):
    return (x, y)


def xcor_vect(v):
    return v[0]


def ycor_vect(v):
    return v[1]


def add_vect(v1, v2):
    return (xcor_vect(v1) + xcor_vect(v2), ycor_vect(v1) + ycor_vect(v2))


def sub_vect(v1, v2):
    return (xcor_vect(v1) - xcor_vect(v2), ycor_vect(v1) - ycor_vect(v2))


def scale_vect(s, v):
    return (s * xcor_vect(v), s * ycor_vect(v))
