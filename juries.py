from collections import namedtuple
import random

Juries = namedtuple("Juries", ["Anna", "John", "Xander"])

x_random = random.randint(0, 10)
y_random = random.randint(0, 10)
z_random = random.randint(0, 10)

p = Juries(x_random, y_random, z_random)

print(p)
print(p.Anna)
print(p.John)
print(p.Xander)
