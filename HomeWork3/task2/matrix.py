from numpy.lib.mixins import NDArrayOperatorsMixin


class Matrix(NDArrayOperatorsMixin):
    def __init__(self, matrix: list[list]):
        NDArrayOperatorsMixin.__init__(self)
        if not isinstance(matrix[0], list):
            raise TypeError("Input matrix should be list of list")
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError("Wrong shapes of matrix")
        self.matrix_ = matrix

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    @property
    def matrix(self):
        return self.matrix_

    @matrix.getter
    def matrix(self):
        return self.matrix_

    @matrix.setter
    def matrix(self, new_matrix: list[list]):
        self.matrix_ = new_matrix

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if (
            len(inputs) != 2
            or getattr(inputs[0], "matrix") is None
            or getattr(inputs[1], "matrix") is None
        ):
            raise ValueError("Two Matrix are expected as arguments")

        arr1: Matrix = inputs[0].matrix
        arr2: Matrix = inputs[1].matrix

        result = generate_matrix_from_ndarray(ufunc(arr1, arr2, **kwargs))
        return result


def generate_matrix_from_ndarray(nd_array) -> Matrix:
    raw_matrix = list(nd_array)
    result_matrix = []
    for row in raw_matrix:
        result_matrix.append(row.tolist())
    return Matrix(result_matrix)
