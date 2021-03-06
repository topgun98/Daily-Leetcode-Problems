# -*- coding: utf-8 -*-
"""longest-substring-without-repeating-characters

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixGhog27v83jMAJQn1zNkmTGQlFvafaO
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub={}
        cur_sub_start=0
        cur_len=0
        longest=0
        
        for i,letter in enumerate(s):
            if letter in sub and sub[letter] >= cur_sub_start:
                cur_sub_start = sub[letter] + 1
                cur_len = i - sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                cur_len = cur_len + 1
                if cur_len>longest:
                    longest=cur_len
                    
        return longest