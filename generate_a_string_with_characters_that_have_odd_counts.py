# -*- coding: utf-8 -*-
"""Generate a String With Characters That Have Odd Counts

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixGhog27v83jMAJQn1zNkmTGQlFvafaO
"""

class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a'*n if (n%2)!=0 else 'a'*(n-1) + 'b'

