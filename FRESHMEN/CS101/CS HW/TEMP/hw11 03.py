# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:30:21 2018

@author: RickyLi
"""

guess_dist   = 0    # m
guess_angle  = 0    # deg
guess_m_prop = 0.05 # kg

max_dist = 0.0

# change angle iteratively until improvement stops
old_guess_dist = guess_dist - 1
while guess_dist >= old_guess_dist:
    old_guess_dist = guess_dist
    guess_angle += 1
    guess_dist = dist( guess_angle,guess_m_prop )
    max_angle = guess_angle

# then change m_prop iteratively until improvement stops
old_guess_dist = guess_dist - 1
while (guess_dist >= old_guess_dist) and (guess_m_prop <= 0.12):
    old_guess_dist = guess_dist
    guess_m_prop += 0.001
    guess_dist = dist(max_angle,guess_m_prop)
    max_m_prop = guess_m_prop    
          # similar to the above but in guess_m_prop
          # do not change the angle at all here; just use max_angle

# now you should know max_dist, max_angle, max_m_prop