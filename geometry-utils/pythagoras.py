'''
Pythagorean Theorem: Step-by-Step solver
13 April, 2020
'''

import math


def solve_hypotenuse(a, b):
    solution = "a^2 + b^2 = c^2\nc^2 = a^2 + b^2\nc^2 = {}^2 + {}^2\n".format(
        a, b)

    a, b = a ** 2, b ** 2
    solution += "c^2 = {} + {}\n".format(a, b)

    c = a + b
    solution += "c^2 = {}\n".format(c)

    c = math.sqrt(c)
    solution += "c = {}".format(c)
    return solution


def solve_leg(a, c):
    solution = "a^2 + b^2 = c^2\nb^2 = c^2 - b^2\nc^2 = {}^2 - {}^2\n".format(
        c, a)

    a, c = a ** 2, c ** 2
    solution += "b^2 = {} - {}\n".format(c, a)

    b = c - a
    solution += "b^2 = {}\n".format(b)

    b = math.sqrt(b)
    solution += "b = {}".format(b)
    return solution


print('For triangle ABC with C == 90deg, input sides\n"a b c" replacing the unknown value with ?\nex. 3 ? 5')
dim = input('\n(! to quit)  > ').strip().split()

while dim[0] != '!':
    if dim[0] == '?':
        ta = int(dim[1])
        tc = int(dim[2])
        print(solve_leg(ta, tc))

    elif dim[1] == '?':
        ta = int(dim[0])
        tc = int(dim[2])
        print(solve_leg(ta, tc))

    else:
        ta = int(dim[0])
        tb = int(dim[1])
        print(solve_hypotenuse(ta, tb))

    dim = input('\n(! to quit)  > ').strip().split()
