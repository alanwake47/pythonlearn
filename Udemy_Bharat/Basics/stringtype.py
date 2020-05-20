# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:55:34 2019

@author: Aman Krishna
"""
s="you are awesome"
print(s)

s1="""You are
the creator
of your destiny""" 
print(s1)

#indexing
print(s[2])

#repetition
print(s*3)

#length
print(len(s1))

#slice
print(s[0:9])
print(s[2:])
print(s[-7:])
print(s[0:9:2])
print(s[::-1])

#strip
s2="   oyu are sawe   "
print(s2.strip())
print(s2.rstrip())

#find
print(s.find("awe",0,11))
print(s.count("a"))
print(s.replace("awesome","Super"))
print(s.upper())
print(s.lower())
print(s.title())

a=10
b=20.54
c=True
d="I am the best"
print(a,b,c,d)