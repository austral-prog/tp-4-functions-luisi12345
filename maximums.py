# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x>y:
        return x
    elif x==y:
        return x
    else:
        return y
max_of_two(5,2)

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
    elif x==y and x>z:
        return x
    elif x==z and z>y:
        return x
    else:
        return y
max_of_three(5,2,3)

