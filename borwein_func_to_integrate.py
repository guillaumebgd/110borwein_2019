# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## borwein_func_to_integrate.py
##

from math import sin
from error_handling.error_handler import error_handler

def borwein_func_to_integrate(n: int, x: float):
    function_result = 1

    if x == 0:
        return 1
    try:
        k = 0
        while k <= n:
            top_borwein = sin(x / ((2 * k) + 1))
            bottom_borwein = x / ((2 * k) + 1)
            function_result *= top_borwein / bottom_borwein
            k += 1
    except ZeroDivisionError:
        print("/!\ Error report /!\\\n "
            "-> Division by zero occured during the calculation of the function to be integrated\n")
        error_handler()
    return function_result