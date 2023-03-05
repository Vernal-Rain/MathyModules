from fractions import Fraction


def frac(a):
    return Fraction(str(a)).limit_denominator(1000)


class Point(object):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '('+ str(frac(self.x)) +', '+ str(frac(self.y)) +', '+ str(frac(self.z)) +')'


class Vector(Point):
    def __str__(self):
        return '<'+ str(frac(self.x)) +', '+ str(frac(self.y)) +', '+ str(frac(self.z)) +'>'

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, o):
        return Vector(self.x+o.x, self.y+o.y, self.z+o.z)

    def __sub__(self, o):
        return Vector(self.x-o.x, self.y-o.y, self.z-o.x)

    def __mul__(self, c: float):
        return Vector(c*self.x, c*self.y, c*self.z)

    def __truediv__(self, c: float):
        c = 1/c
        return Vector(c*self.x, c*self.y, c*self.z)

    def unit(self):
        mag = abs(self)
        return Vector(self.x/mag, self.y/mag, self.z/mag)


def dot(v: Vector, w: Vector):
        return v.x*w.x + v.y*w.y + v.z*w.x


def cross(v: Vector, w: Vector):
        c = Vector(v.y*w.z-v.z*w.y, -1*(v.x*w.z-v.z*w.x), v.x*w.y-v.y*w.x)
        return abs(c) if (v.z == 0 and w.z == 0) else c


def grad_at(f, pt: Point):
    d = 0.0001
    a = pt.x
    b = pt.y
    c = pt.z
    da = (f(a+d, b, c)-f(a, b, c))/d
    db = (f(a, b+d, c)-f(a, b, c))/d
    dc =(f(a, b, c+d)-f(a, b, c))/d
    return Vector(da, db, dc)


def dir_deriv(f, v: Vector, pt: Point):
    return dot(grad_at(f, pt), v.unit())


class VectorField(Vector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def value_at(self, a = 0, b = 0, c = 0):
        return Vector(self.x(a, b, c), self.y(a, b, c), self.z(a, b, c))




