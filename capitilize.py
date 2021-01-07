# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:20:21 2020

@author: leosh
"""

def upper(line):
  words = line.split(" ")
  res =''
  for w in words:
    if w[0].isalpha():
      res = res + " " + w[:1].upper() +w[1:]
  return res

print(upper("the brown fox"))