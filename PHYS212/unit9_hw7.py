from scipy.optimize import fsolve
import numpy as np

R1 = 100
R2 = 200
R3 = 30
R4 = 400
V1 = 4
V2 = 12

# ! x[I1, I2, I3, I4]


def f(x):
    return np.array(
        [
            x[0] * R1 + x[2] * R3 - V1,
            x[0] * R1 + x[1] * R2 - V2 - V1,
            x[3] * R4 + V2,
            x[0] - x[1] - x[2],
        ]
    )


x = fsolve(f, [0, 0, 0, 0])
print(x)
