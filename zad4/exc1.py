import numpy as np

print(np.zeros(10))

print(np.ones(10))

a = np.empty(10)
a.fill(5)
print(a)

b = np.arange(10, 51, 1)
print(b)

c = np.arange(10, 51, 2)
print(c)

d = np.arange(0, 9, 1).reshape(3, 3)
print(d)

e = np.identity(3)
print(e)

f = np.random.rand(25)
print(f)

g = np.arange(0.01, 1.01, 0.01).reshape(10,10)
print(g)

h = np.linspace(0, 1, 20)
print(h)

