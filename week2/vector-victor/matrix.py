from vector import Vector, ShapeError


class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def shape(self):
        rows = len(self.rows)
        try:
            columns = len(self.rows[0])
            return (rows, columns)
        except:
            return (rows,)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row = key[0]
            col = key[1]
            if row is None:
                return [row[col] for row in self.rows]
            else:
                return [r[col] for i, r in enumerate(self.rows) if i == row]
        else:
            return self.rows[key]

    def __eq__(self, other):
        return self.rows == other.rows

    def __add__(self, other):
        Matrix.ensure_same_shape(self, other)
        return Matrix([(Vector(a) + Vector(b)).values for a, b in zip(self.rows, other.rows)])

    def __sub__(self, other):
        Matrix.ensure_same_shape(self, other)
        return Matrix([(Vector(a) - Vector(b)).values for a, b in zip(self.rows, other.rows)])

    def __mul__(self, scalar):
        if isinstance(scalar, Matrix):
            rows, cols = scalar.shape()
            return Matrix([[Vector(row).dot(Vector(scalar[None, col])) for col in range(cols)] for row in self.rows])
        if isinstance(scalar, Vector):
            return Vector([Vector(row).dot(scalar) for row in self.rows])
        else:
            return Matrix([Vector(row) * scalar for row in self.rows])

    def ensure_same_shape(*matrices):
        if len({matrix.shape() for matrix in matrices}) != 1:
            raise ShapeError
