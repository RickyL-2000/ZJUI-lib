# %%
import numpy as np
import scipy.stats as st

# %%
p = 1./7
T = 30
T_LS = 10
X, L, S, C = [], [], [], []
while True:
    temp = []
    for i in range(T):
        temp.append(st.bernoulli.rvs(p))
    if sum(temp) >= T_LS:
        X = temp
        break
X_arr = np.array(X)
S = (np.argwhere(X_arr > 0).squeeze() + 1).tolist()[:10]
L = [S[0]] + [S[i] - S[i-1] for i in range(1, 10)]
C = [X[0]]
for i in range(1, len(X)):
    C.append(C[i-1] + X[i])
print(X)
print(L)
print(S)
print(C)

# %%
L = st.geom.rvs(p)
print(L)

# %%
a = np.zeros(10)
a[[1, 2, 3, 4]] = 1
# print(a)

# %%
T = 30
p = 1./7
L = [st.geom.rvs(p) for _ in range(T)]
# S = [L[0]] + [L[i-1] + L[i] for i in range(1, len(L))]
S = [L[0]]
for i in range(1, len(L)):
    S.append(S[i-1] + L[i])
X = np.zeros(S[-1], dtype=int)
print(len(X))
print(L)
print(S)

# %%
X[np.array(S) - 1] = 1
X = X.tolist()
C = [X[0]]
for i in range(1, len(X)):
    C.append(C[i-1] + X[i])

print("L: ", L)
print("X: ", X)
print("S: ", S)
print("C: ", C)
