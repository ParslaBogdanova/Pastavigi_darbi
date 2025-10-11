import math

c = 3*10**8
v = 1*10**8
m = 0.14
gamma = 1 / math.sqrt(1 - (v**2 / c**2))
p = m * v * gamma

print(p)
