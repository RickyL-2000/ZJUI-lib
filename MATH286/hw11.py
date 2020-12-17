# %%
import numpy as np

# %%
m1 = np.mat([[0, 1, 9, 0, 1, 19],
             [-1, 0, -23, 0, 0, -46],
             [0, 0, -6, 0, 0, -12],
             [-6, 1, 9, 6, 1, 19],
             [1, 0, -1, 0, 0, -2],
             [0, 0, 6, 0, 0, 12]])
m2 = m1 * m1
print(m2)
w1 = np.array([[0, 1, 0, 0, 0, 0]]).T
print(m1 * m1 * m1 * w1)

# %%
def rsmat(arbmat):
    """ Convert an arbitrary matrix to a simplest matrix """
    arbmat = arbmat.astype(float)
    row_number, column_number = arbmat.shape
    if row_number == 1:
        if arbmat[0, 0] != 0:
            return (arbmat / arbmat[0, 0])
        else:
            return arbmat
    else:
        rc_number = min(row_number, column_number)
        anarbmat = arbmat.copy()
        r = 0
        for n in range(rc_number):
            s_row = -1
            for i in arbmat[r:row_number, n]:
                s_row += 1
                if abs(i) > 1e-10:
                    anarbmat[r, :] = arbmat[s_row + r, :]
                    for j in range(r, row_number):
                        if j < s_row + r:
                            anarbmat[j + 1, :] = arbmat[j, :]
                    arbmat = anarbmat.copy()
            if abs(anarbmat[r, n]) > 1e-10:
                anarbmat[r, :] = anarbmat[r, :] / anarbmat[r, n]
                for i in range(row_number):
                    if i != r:
                        anarbmat[i, :] -= \
                            anarbmat[i, n] * anarbmat[r, :]
            arbmat = anarbmat.copy()
            if abs(arbmat[r, n]) < 1e-10:
                r = r
            else:
                r = r + 1
        for m in range(column_number):
            if abs(arbmat[-1, m]) > 1e-10:
                arbmat[-1, :] = arbmat[-1, :] / arbmat[-1, m]
                for i in range(row_number - 1):
                    arbmat[i, :] -= \
                        arbmat[i, m] * arbmat[-1, :]
                break

        return arbmat


# %%
m = np.mat([[3, 1, -2, -1, 2],
            [5, 1, -3, -2, 3],
            [14, 3, -9, -5, 9],
            [13, 3, -8, -5, 8],
            [16, 3, -10, -6, 10]])
m2 = m * m
print(m2)
m2_ge = rsmat(m2)
print(m2_ge)
m3 = m * m * m
print(m3)

# %%
w1 = np.array([[0, 1, 0, 0, 0]]).T
print(m * w1)
print(m * m * w1)
print(m * m * m * w1)

# %%
B = np.mat([[0, 1, -2, -1, 2],
            [5, -2, -3, -2, 3],
            [14, 3, -12, -5, 9],
            [13, 3, -8, -8, 8],
            [16, 3, -10, -6, 7]])
lamb, v = np.linalg.eig(B)
print(lamb)
print(v)

# %%
B2 = B * B
print(B2)

# %%
v1 = np.array([[1], [0], [0], [0], [0]])
v2 = np.array([[0], [1], [0], [0], [0]])
v3 = np.array([[0], [0], [1], [0], [0]])
v4 = np.array([[0], [0], [0], [1], [0]])
v5 = np.array([[0], [0], [0], [0],[1]])
# print(v1)
print(B * v1)


# %%
B = np.mat([[0, 1, -2, -1, 2],
            [5, -2, -3, -2, 3],
            [14, 3, -12, -5, 9],
            [13, 3, -8, -8, 8],
            [16, 3, -10, -6, 7]])
S = np.mat([[1, 0, 0, 0, 0],
            [-5, 1, 3, 2, -3],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]])
S1 = np.mat([[0, 1, 0, 0, 0],
             [1, -5, 3, 2, -3],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1]])
print(S1.I * B * S1)
