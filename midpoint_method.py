# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## midpoint_method.py
##

from borwein_func_to_integrate import borwein_func_to_integrate

def midpoint_method(n: int):
    a = 0
    b = 5000
    sub_intervals = 10000
    sub_interval_length = (b - a) / sub_intervals
    In = 0.0

    i = 0
    x = sub_interval_length / 2
    while i <= sub_intervals - 1:
        In += sub_interval_length * borwein_func_to_integrate(n, x)
        x += sub_interval_length
        i += 1
    return In