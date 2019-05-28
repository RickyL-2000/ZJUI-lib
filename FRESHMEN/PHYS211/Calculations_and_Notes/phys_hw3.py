# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:31:36 2019

@author: RickyLi
"""

def Homework3():
    m_e = 5.9742e24
    r_e = 6.3781e6
    m_m = 7.36e22
    r_m = 1.7374e6
    d = 3.844e8
    G = 6.67428e-11
    
    v = 5534
    a = -(m_e/r_e + m_m/(d-r_e))
    b = m_e*d/r_e + m_e + m_m*d/(d-r_e) - m_m
    c = -m_e*d + 0.5*v*v/G
    delta = b*b - 4*a*c
    
    x_1 = 0.5*(-b + delta**0.5)/a
    x_2 = 0.5*(-b - delta**0.5)/a
    
    print(x_1, x_2)
    
Homework3()