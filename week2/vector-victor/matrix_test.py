from matrix import Matrix
from vector import Vector, ShapeError
from nose.tools import raises


A = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
C = [[1, 2],
     [2, 1],
     [1, 2]]
D = [[1, 2, 3],
     [3, 2, 1]]


# ADVANCED MODE TESTS BELOW
# UNCOMMENT THEM FOR ADVANCED MODE!

def test_shape_matrices():
    """shape takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert Matrix(A).shape() == (3, 3)
    assert Matrix(C).shape() == (3, 2)
    assert Matrix(D).shape() == (2, 3)


def test_matrix_row():
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    assert Matrix(A)[0] == [1, 0, 0]
    assert Matrix(B)[1] == [4, 5, 6]
    assert Matrix(C)[2] == [1, 2]


def test_matrix_col():
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    assert Matrix(A)[None, 0] == [1, 0, 0]
    assert Matrix(B)[None, 1] == [2, 5, 8]
    assert Matrix(D)[None, 2] == [3, 1]


def test_matrix_matrix_add():
    assert Matrix(A) + Matrix(B) == Matrix([[2, 2, 3],
                                            [4, 6, 6],
                                            [7, 8, 10]])


@raises(ShapeError)
def test_matrix_add_checks_shapes():
    """Shape rule: the rows and columns of the matrices must be the same size."""
    Matrix(C) + Matrix(D)


def test_matrix_matrix_sub():
    assert Matrix(A) - Matrix(B) == Matrix([[ 0, -2, -3],
                                            [-4, -4, -6],
                                            [-7, -8, -8]])


@raises(ShapeError)
def test_matrix_sub_checks_shapes():
    """Shape rule: the rows and columns of the matrices must be the same size."""
    Matrix(C) - Matrix(D)


def test_matrix_scalar_multiply():
    """
    [[a b]   *  Z   =   [[a*Z b*Z]
     [c d]]              [c*Z d*Z]]

    Matrix * Scalar = Matrix
    """
    assert Matrix(C) * 3 == Matrix([[3, 6],
                                    [6, 3],
                                    [3, 6]])
    assert Matrix(B) * 2 == Matrix([[ 2,  4,  6],
                                    [ 8, 10, 12],
                                    [14, 16, 18]])


def test_matrix_vector_multiply():
    """
    [[a b]   *  [x   =   [a*x+b*y
     [c d]       y]       c*x+d*y
     [e f]                e*x+f*y]

    Matrix * Vector = Vector
    """
    assert Matrix(A) * Vector([2, 5, 4]) == Vector([2, 5, 4])
    assert Matrix(B) * Vector([1, 2, 3]) == Vector([14, 32, 50])
    assert Matrix(C) * Vector([3, 4]) == Vector([11, 10, 11])
    assert Matrix(D) * Vector([0, 1, 2]) == Vector([8, 4])


@raises(ShapeError)
def test_matrix_vector_multiply_checks_shapes():
    """Shape Rule: The number of rows of the vector must equal the number of
    columns of the matrix."""
    Matrix(C) * Vector([1, 2, 3])


def test_matrix_matrix_multiply():
    """
    [[a b]   *  [[w x]   =   [[a*w+b*y a*x+b*z]
     [c d]       [y z]]       [c*w+d*y c*x+d*z]
     [e f]                    [e*w+f*y e*x+f*z]]

    Matrix * Matrix = Matrix
    """
    assert Matrix(A) * Matrix(B) == Matrix(B)
    assert Matrix(B) * Matrix(C) == Matrix([[8, 10],
                                            [20, 25],
                                            [32, 40]])
    assert Matrix(C) * Matrix(D) == Matrix([[7, 6, 5],
                                            [5, 6, 7],
                                            [7, 6, 5]])
    assert Matrix(D) * Matrix(C) == Matrix([[8, 10], [8, 10]])


@raises(ShapeError)
def test_matrix_matrix_multiply_checks_shapes():
    """Shape Rule: The number of columns of the first matrix must equal the
    number of rows of the second matrix."""
    Matrix(A) * Matrix(D)
