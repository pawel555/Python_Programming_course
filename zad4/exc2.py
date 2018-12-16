import numpy as np

mat = np.arange(1, 26).reshape(5, 5)
print(mat)

# a)
a = mat[2:, 1:]
print(a)

# b)
b = mat[3, 4]
print(b)

# c)
c = mat[0:3, 1]
print(c.reshape(3, 1))

# d)
d = mat[4, :]
print(d)

# e
e = mat[3:, :]
print(e)

# Now do the following:

print(np.sum(mat))

print(np.std(mat))

print(np.sum(mat, axis=0))

print(np.median(mat, axis=0))

print(np.average(mat, axis=0))

print(np.median(mat, axis=1))

print(np.average(mat, axis=1))


