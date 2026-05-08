# Replace the "ANSWER HERE" for your answer
import math

import math

#________________________________________ROOTS________________________________________

def roots(a, b, c):

    discriminante = (b**2 - 4 * a * c)

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f'{float(raiz1), float(raiz2)}'
    elif discriminante == 0:
        raiz0 = (-b) / (2*a)
        return f'({float(raiz0)})'
    else:
        return f'({" "})'

#________________________________________VALUE Y________________________________________

def value_y(a, b, c, x):
    y = a * x**2 + b * x + c
    return y

#________________________________________TO STRING________________________________________

def to_string(a, b, c):
    A = a
    B = b
    C = c

    if A == 0 and B == 0 and C == 0:
        return "f(x) = 0"

    elif A == 0 and B == 0 and C != 0:
        return f"f(x) = {C}"
    elif A == 0 and B != 0 and C == 0:
        return f"f(x) = {B}"
    elif A != 0 and B == 0 and C == 0:
        return f"f(x) = {A}"

    elif A == 0 and B != 0 and C != 0:
        return f"f(x) = {B} * X + {C}"
    elif A != 0 and B == 0 and C != 0:
        return f"f(x) = {A} * X^2 + {C}"
    elif A != 0 and B != 0 and C == 0:
        return f"f(x) = {A} * X^2 + {B} * X"

    else:
        return f"f(x) = {A} * X^2 + {B} * X + {C}"

#________________________________________DERIVATION________________________________________

def derivation(a, b, c):
    if 2*a == 0:
        return f"f'(x) = {b}"
    elif b==0:
        return f"f'(x) = {2*a} * X"

    return f"f'(x) = {2*a} * X + {b}"