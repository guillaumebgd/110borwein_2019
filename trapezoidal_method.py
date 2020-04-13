# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## trapezoidal_method.py
##

from borwein_func_to_integrate import borwein_func_to_integrate

def trapezoidal_method(n: int):
    a = 0
    b = 5000
    sub_intervals = 10000
    h = (b - a) / sub_intervals
    In = 0.0

    i = 1
    while i <= sub_intervals - 1:
        x = i * h
        In += borwein_func_to_integrate(n, x)
        i += 1
    In = ((In * 2) + 1 + borwein_func_to_integrate(n, b))
    In *= h / 2
    return In