# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## is_integer.py
##

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()