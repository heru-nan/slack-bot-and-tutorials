
def get_min(params):
    i = params[0]
    for j in params:
        if j < i: i = j
    return i

