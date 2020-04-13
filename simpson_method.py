# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## simpson_method.py
##

from borwein_func_to_integrate import borwein_func_to_integrate

def simpson_method(n: int):
    a = 0
    b = 5000
    sub_intervals = 10000
    h = (b - a) / sub_intervals
    In = 0.0

    i = 0
    while i <= sub_intervals - 1:
        x = i * h
        if i == 0:
            In += 4 * borwein_func_to_integrate(n, x + (h / 2))
        else:
            In += (2 * borwein_func_to_integrate(n, x) + (4 * borwein_func_to_integrate(n, x + (h / 2))))
        i += 1
    In = (1 + borwein_func_to_integrate(n, b) + In) * h / 6
    return In