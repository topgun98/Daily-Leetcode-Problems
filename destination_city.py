# -*- coding: utf-8 -*-
"""Destination_city

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18WTAPGxLmzWF316S6D2QvDjeP2UmA3bd
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting = []
        destination = []
        for i in range(len(paths)):
            starting.append(paths[i][0])
        for i in range(len(paths)):
            destination.append(paths[i][1])
        s=set(starting)
        d=set(destination)
        k = d.difference(s)
        return k.pop()