import numpy as np


def gaussian(A, b):
    n = len(A)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A[i, k] != 0.0:
                lam = A[i, k] / A[k, k]
                A[i, k + 1:n] = A[i, k + 1:n] - lam * A[k, k + 1:n]
                b[i] = b[i] - lam * b[k]
                A[i, k] = 0.0

    b1 = np.reshape(b, (4, 1))
    A_aug = np.append(A, b1, axis=1)
    return A_aug


def back(A, b):
    n = len(A)
    for k in range(n - 1, -1, -1):
        x[k] = (b[k] - np.dot(A[k, k + 1:n], x[k + 1:n])) / A[k, k]
    return x


# main
A = np.arange(1, 17, dtype=np.float64).reshape(4, 4)
A[1, 2] = 88
A[1, 3] = -3
A[2, 3] = -3
print(f'A = \n{A}')

x = np.ones(A.shape[0])
print(f'Original x = {x}')
b = A @ x.T
print(f'Right hand side for testing: b = {b}')

Ae = gaussian(A, b)
print(f'Eliminated augmented matrix:\n {Ae}')
print(f'Eliminated augmented matrix A part:\n {Ae[:,:-1]}')
print(f'Eliminated augmented matrix b part:\n {Ae[:,Ae.shape[1]-1]}')

# Find solution
x = back(Ae[:, :-1], Ae[:, Ae.shape[1] - 1])
print(f'Solution: {x}')
