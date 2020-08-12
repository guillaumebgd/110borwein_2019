# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## solve_borwein_integral_for_n.py
##

from math import pi
from src.midpoint_method import midpoint_method
from src.trapezoidal_method import trapezoidal_method
from src.simpson_method import simpson_method

def print_In_and_diff(n: int, In: float):
    diff = abs((pi / 2) - abs(In))

    print("I%d = %.10f" % (n, In))
    print("diff = %.10f" % diff)

def solve_borwein_integral_for_n(n: int):
    In = midpoint_method(n)
    print("Midpoint:")
    print_In_and_diff(n, In)
    In = trapezoidal_method(n)
    print("\nTrapezoidal:")
    print_In_and_diff(n, In)
    In = simpson_method(n)
    print("\nSimpson:")
    print_In_and_diff(n, In)