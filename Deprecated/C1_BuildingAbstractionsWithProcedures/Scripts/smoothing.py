import repeated

dx = 0.00001

def smooth(f):
    global dx
    return lambda x : (f(x - dx) + f(x) + f(x + dx)) / 3

def n_fold_smooth(f, n):
    n_smooth = repeated.repeated(smooth, n)
    return n_smooth(f)