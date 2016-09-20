__author__ = "Dor Rondel"
__session__ = "9:30am"

#1.a
#A function is a named sequence of statements that performs a computation
#It can return a value but does not have to
#A function's components are its name, arguments (if any), and return type (if exists).

#1.b
int(9.8)
float(8)
str(56)

#1.c
#A module is a file that contains a collection of related functions

import math
from math import *

#1.d
#local variables are variables that exist within a limited function scope
#void functions are functions that return None (in pythonic terms)

#1.e
#output would be  '2.0'

# PART 2

#A
def min_to_milis(minutes):
    return minutes * 60000.0  # 1 min is 6x10^4 ms

#B
def square_based_pyramid_volume(side, height):
    return side**2 * (height/3)

#C
def avg_2_scores(scr1, scr2):
    return (scr1+scr2) / 2.0

#D
from math import sqrt
def quadratic_formula(a,b,c):
    return [
    (-b + sqrt(b**2 - 4*a*c))/(2*a), # positive root
    (-b - sqrt(b**2 - 4*a*c))/(2*a) # negative root
    ]

#E
def avg_speed(sp1, t1, sp2, t2):
    first_d = sp1*t1
    second_d = sp2*t2
    total_d = first_d + second_d
    return total_d / (t1+t2) # returns km/hr

def kph_to_ms(kph):
    return (kph * 1000) / 3600.0

print("Avg speed: {} ".format(kph_to_ms(avg_speed(40.0, 2.0, 60.0, 3.0))) + "m/s")

#F
def k_to_r(kelv):
    return (kelv - 273.15) * (4.0/5)

def r_to_c(ream):
    return ream * (5.0/4)

def k_to_c(kelv):
    r = k_to_r(kelv)
    return r_to_c(r)

#print(k_to_c(10000))

#G
def cube_in_rect(a):
    rect_vol = a*(8*a)*(9*a)
    cub_vol = (2*a)**3.0
    return rect_vol / cub_vol

print("{} cubes fit into the rectangular prism".format(cube_in_rect(199)))
## Answer is 9.0 regardless of input, so 9a times

# H
from math import pi
def marble_in_cube(n):
    cube_vol = n**3
    sphere_vol = (4.0/3)*pi*(n/4)**3
    return cube_vol / sphere_vol

print("{} marbles fit in the cube".format(marble_in_cube(4)))  # 4 randomly chosen, can try with different n

# I
top_line = "^ - ^ - ^"*4
cube = """i        i        i        i        i
i        i        i        i        i
i        i        i        i        i
i        i        i        i        i
{}
"""

def print_board(tile, top):
    print(top_line+"^")
    print(tile.format(top)*4)

print_board(cube, top_line)
