class ShapeError(Exception):
    pass

from functools import reduce


def ensure_same_shape(*values):
    if len({shape(value) for value in values}) != 1:
        raise ShapeError


def shape(value):
    rows = len(value)
    try:
        columns = len(value[0])
        return (rows, columns)
    except:
        return (rows,)


def vector_add(vector_a, vector_b):
    ensure_same_shape(vector_a, vector_b)
    return [a + b for a, b in zip(vector_a, vector_b)]


def vector_sub(vector_a, vector_b):
    ensure_same_shape(vector_a, vector_b)
    return [a - b for a, b in zip(vector_a, vector_b)]


def vector_sum(*vectors):
    ensure_same_shape(*vectors)
    # return [sum(v) for v in zip(*vectors)]
    return reduce(vector_add, vectors)


def dot(vector_a, vector_b):
    ensure_same_shape(vector_a, vector_b)
    return sum([(a * b) for a, b in zip(vector_a, vector_b)])


def vector_multiply(vector, scalar):
    return [value * scalar for value in vector]


def vector_mean(*vectors):
    # return vector_multiply(vector_sum(*vectors), 1 / len(vectors))
    return [sum(vector) / len(vector) for vector in vectors]


def magnitude(vector):
    # return dot(vector, vector) ** (1 / 2)
    return sum([value ** 2 for value in vector]) ** .5


def matrix_row(matrix, row):
    return matrix[row]


def matrix_col(matrix, col):
    return [row[col] for row in matrix]


def matrix_add(matrix_a, matrix_b):
    ensure_same_shape(matrix_a, matrix_b)
    return [vector_add(a, b) for a, b in zip(matrix_a, matrix_b)]


def matrix_sub(matrix_a, matrix_b):
    ensure_same_shape(matrix_a, matrix_b)
    return [vector_sub(a, b) for a, b in zip(matrix_a, matrix_b)]


def matrix_scalar_multiply(matrix, scalar):
    return [vector_multiply(vector, scalar) for vector in matrix]


def matrix_vector_multiply(matrix, vector):
    return [dot(row, vector) for row in matrix]


def matrix_matrix_multiply(a, b):
    rows, cols = shape(b)
    return [[dot(row, matrix_col(b, col)) for col in range(cols)] for row in a]
