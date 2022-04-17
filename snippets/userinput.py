# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 09:48:35 2018

@author: th50kn
"""


def inputFloat():
    n = None
    while True:
        n = input("give me a number!:")
        try:
            n = float(n)
            break
        except ValueError:
            print("I want a NUMBER!")
    return n


r = inputFloat()

print("the number is: {0:.2f}".format(r))
