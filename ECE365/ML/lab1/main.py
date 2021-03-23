import numpy as np


class Lab1(object):
    def solver(self, A, b):
        return None

    def fitting(self, x, y):
        coeff = np.zeros(2)
        return coeff

    def naive5(self, X, A, Y):
        # Calculate the matrix with $(i,j$)-th entry as  $\mathbf{x}_i^\top A \mathbf{y}_j$ by looping over the rows of $X,Y$.
        return None

    def matrix5(self, X, A, Y):
        # Repeat part (a), but using only matrix operations (no loops!).
        return None

    def naive6(self, X, A):
        # Calculate a vector with $i$-th component $\mathbf{x}_i^\top A \mathbf{x}_i$ by looping over the rows of $X$.
        return None

    def matrix6(self, X, A):
        # Repeat part (a) using matrix operations (no loops!).
        return None
