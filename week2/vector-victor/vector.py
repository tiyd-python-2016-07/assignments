class ShapeError(Exception):
    pass


class Vector:
    def __init__(self, values):
        self.values = values

    def shape(self):
        rows = len(self.values)
        return (rows,)

    def __eq__(self, other):
        return self.values == other.values

    def __add__(self, other):
        Vector.ensure_same_shape(self, other)
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        Vector.ensure_same_shape(self, other)
        return Vector([a - b for a, b in zip(self.values, other.values)])

    def dot(self, other):
        Vector.ensure_same_shape(self, other)
        return sum([(a * b) for a, b in zip(self.values, other.values)])

    def __mul__(self, scalar):
        return [value * scalar for value in self.values]

    def magnitude(self):
        return self.dot(self) ** (1 / 2)

    def sum(*vectors):
        Vector.ensure_same_shape(*tuple(Vector(v) for v in vectors))
        return Vector([sum(v) for v in zip(*vectors)])

    def mean(*vectors):
        return Vector.sum(*vectors) * (1 / len(vectors))

    def ensure_same_shape(*vectors):
        if len({vector.shape() for vector in vectors}) != 1:
            raise ShapeError
