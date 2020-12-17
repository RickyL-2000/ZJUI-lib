from scipy.optimize import fsolve
import numpy as np

V1 = 18
V2 = 12
R1 = R5 = 79
R2 = R6 = 108
R4 = 68
R3 = 108

# ! x = [I1, I2, I3, I4, I6]
# ! in which, I4, I6 from left to right


def f(x):
    return np.array(
        [
            x[0] * R1 - V1 - x[2] * R3,
            x[1] * R2 + x[2] * R3 + V1 + x[4] * R6 - V2,
            x[3] * (R4 + R5) + V2,
            x[1] - x[0] - x[2],
            x[0] + x[2] - x[4]
        ]
    )


x = fsolve(f, [0, 0, 0, 0, 0])
print(x)

# Q1
V4 = x[3] * R4
print(abs(V4))

# Q2
print(x[2])

# Q3
print(x[1])

# Q4
print(x[0])

# Q5
Vab = x[4] * R6
print(Vab)
