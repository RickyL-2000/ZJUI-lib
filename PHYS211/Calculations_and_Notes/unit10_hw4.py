# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:15:44 2019

@author: RickyLi
"""

p1 = [9.2, -2.7, -4.5, 3, -4.2]  #m, x, y, v_x, v_y
p2 = [9.4, -3.7, 3.5, -5, 5.2]
p3 = [7.7, 4.4, -5.6, -6.1, 1.9]
p4 = [7.9, 5.4, 2.6, 4.1, -2.9]

m_sum = p1[0] + p2[0] + p3[0] + p4[0]
CM_x = 0
CM_y = 0
CM_vx = 0
CM_vy = 0
for i in [p1,p2,p3,p4]:
    CM_x += i[0]*i[1]/m_sum
    CM_y += i[0]*i[2]/m_sum
    CM_vx += i[3]*i[0]/m_sum
    CM_vy += i[4]*i[0]/m_sum
    
CM_v = (CM_vx**2 + CM_vy**2)**0.5

print(CM_x)
print(CM_y)
print(CM_v)