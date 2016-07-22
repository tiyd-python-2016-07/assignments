import math
from vector import Vector, ShapeError
from nose.tools import raises


def are_equal(x, y, tolerance=0.001):
    """Helper function to compare floats, which are often not quite equal."""
    return abs(x - y) <= tolerance


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]


def test_shape_vectors():
    """shape takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert Vector([1]).shape() == (1,)
    assert Vector(m).shape() == (2,)
    assert Vector(v).shape() == (3,)


def test_vector_add():
    """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    """
    assert Vector(v) + Vector(w) == Vector([1, 5, 4])
    assert Vector(u) + Vector(y) == Vector([11, 21, 31])
    assert Vector(u) + Vector(z) == Vector(u)


def test_vector_add_is_commutative():
    assert Vector(w) + Vector(y) == Vector(y) + Vector(w)


@raises(ShapeError)
def test_vector_add_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    Vector(m) + Vector(v)


def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]
    Matrix + Matrix = Matrix
    """
    assert Vector(v) - Vector(w) == Vector([1, 1, -4])
    assert Vector(w) - Vector(v) == Vector([-1, -1, 4])
    assert Vector(y) - Vector(z) == Vector(y)
    assert Vector(w) - Vector(u) == Vector(z) - (Vector(u) - Vector(w))


@raises(ShapeError)
def test_vector_sub_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    Vector(m) - Vector(v)


def test_vector_sum():
    """vector_sum can take any number of vectors and add them together."""
    assert Vector.sum(v, w, u, y, z) == Vector([12, 26, 35])


@raises(ShapeError)
def test_vector_sum_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    Vector.sum(v, w, m, y)


def test_dot():
    """
    dot([a b], [c d])   = a * c + b * d
    dot(Vector, Vector) = Scalar
    """
    assert Vector(w).dot(Vector(y)) == 160
    assert Vector(m).dot(Vector(n)) == 15
    assert Vector(u).dot(Vector(z)) == 0


@raises(ShapeError)
def test_dot_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    Vector(v).dot(Vector(m))


def test_vector_multiply():
    """
    [a b]  *  Z     = [a*Z b*Z]
    Vector * Scalar = Vector
    """
    assert Vector(v) * 0.5 == [0.5, 1.5, 0]
    assert Vector(m) * 2 == [6, 8]


def test_vector_mean():
    """
    mean([a b], [c d]) = [mean(a, c) mean(b, d)]
    mean(Vector)       = Vector
    """
    assert Vector.mean(m, n) == [4, 2]
    assert Vector.mean(v, w) == [0.5, 2.5, 2]
    assert are_equal(Vector.mean(v, w, u)[0], 2 / 3)
    assert are_equal(Vector.mean(v, w, u)[1], 2)
    assert are_equal(Vector.mean(v, w, u)[2], 5 / 3)


def test_magnitude():
    """
    magnitude([a b])  = sqrt(a^2 + b^2)
    magnitude(Vector) = Scalar
    """
    assert Vector(m).magnitude() == 5
    assert Vector(v).magnitude() == math.sqrt(10)
    assert Vector(y).magnitude() == math.sqrt(1400)
    assert Vector(z).magnitude() == 0
