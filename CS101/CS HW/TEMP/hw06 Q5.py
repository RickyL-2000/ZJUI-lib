# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:44:42 2018

@author: RickyLi
"""

my_file = open('C:\\Users\\RickyLi\\Desktop\\batting_test.csv','r')
lines = my_file.readlines()
del lines[0]
career_rbis = {}
for linestr in lines:
    line = linestr.split(',')
    if line[12].isdigit():
       if line[0] in career_rbis.keys():
           career_rbis[line[0]] += int(line[12]) #the data in the sheet may not be digit.
       else:                                     #It can be a string.
           career_rbis[line[0]] = int(line[12])
items = list(career_rbis.items())
items.sort(key = lambda x:x[1])
max_player = items[-1][0]
max_rbis = items[-1][1]

print(max_player,max_rbis)