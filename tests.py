from vector import *


v = Vector(1, 0, 0)
print(dir_deriv(lambda x, y, z:x**2+y, v, Point(0, 5, 0)))