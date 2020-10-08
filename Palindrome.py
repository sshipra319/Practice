# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:40:09 2020

@author: Shipra
"""

text = "abcda"

class Solution:
    def palindrome(self, text):
        s = ""
        for i in text:
            s = i + s
        if s == text:
            return True
        else:
            return False          
               
sol = Solution()
print(sol.palindrome(text))