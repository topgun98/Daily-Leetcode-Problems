# -*- coding: utf-8 -*-
"""Maximum Score After Splitting a String

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixGhog27v83jMAJQn1zNkmTGQlFvafaO
"""

class Solution:
    def maxScore(self, s: str) -> int:
        t=0
        for i in range(len(s)-1):
            l=s[:i+1]
            r=s[i+1:]
            if l.count("0")+r.count("1")>t:
                t=l.count("0")+r.count("1")
        return t

