class Matrix:
    def __init__(self, matrix: list[list]):
        if not isinstance(matrix[0], list):
            raise TypeError("Input matrix should be list of list")
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError("Wrong shapes of matrix")

        self.matrix = matrix

    def check_dimensions(self, other: "Matrix") -> bool:
        return len(self.matrix[0]) == len(other.matrix)

    def __add__(self, other: "Matrix") -> "Matrix":
        if not self.check_dimensions(other):
            raise ValueError("Wrong dimensions")
        result = []
        for row_self, row_other in zip(self.matrix, other.matrix):
            result.append([x + y for x, y in zip(row_self, row_other)])
        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if not self.check_dimensions(other):
            raise ValueError("Wrong dimensions")
        result = []
        for row_self, row_other in zip(self.matrix, other.matrix):
            result.append([x * y for x, y in zip(row_self, row_other)])
        return Matrix(result)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        zip_b = zip(*other.matrix)
        # uncomment next line if python 3 :
        zip_b = list(zip_b)
        return Matrix(
            [
                [
                    sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                    for col_b in zip_b
                ]
                for row_a in self.matrix
            ]
        )
