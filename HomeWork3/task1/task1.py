import numpy as np
from matrix import Matrix


def generate_matrix() -> Matrix:
    raw_matrix = list(np.random.randint(0, 10, (10, 10)))
    result_matrix = []
    for row in raw_matrix:
        result_matrix.append(row.tolist())
    print(result_matrix)
    return Matrix(result_matrix)


def get_pretty_str_from_matrix(matrix) -> str:
    return "\n".join(["\t".join(map(str, row)) for row in matrix])


def main():
    first_matrix = generate_matrix()
    second_matrix = generate_matrix()
    add_result_matrix = first_matrix + second_matrix
    mul_result_matrix = first_matrix * second_matrix
    mat_mul_result_matrix = first_matrix @ second_matrix

    with open("../artifacts/task1/matrix+.txt", "w") as file:
        file.write("first_matrix:\n")
        file.write(get_pretty_str_from_matrix(first_matrix.matrix))
        file.write("\n\nsecond_matrix:\n")
        file.write(get_pretty_str_from_matrix(second_matrix.matrix))
        file.write("\n\nadd operation result:\n")
        file.write(get_pretty_str_from_matrix(add_result_matrix.matrix))
        file.close()

    with open("../artifacts/task1/matrix*.txt", "w") as file:
        file.write("first_matrix:\n")
        file.write(get_pretty_str_from_matrix(first_matrix.matrix))
        file.write("\n\nsecond_matrix:\n")
        file.write(get_pretty_str_from_matrix(second_matrix.matrix))
        file.write("\n\nmul operation result:\n")
        file.write(get_pretty_str_from_matrix(mul_result_matrix.matrix))
        file.close()

    with open("../artifacts/task1/matrix@.txt", "w") as file:
        file.write("first_matrix:\n")
        file.write(get_pretty_str_from_matrix(first_matrix.matrix))
        file.write("\n\nsecond_matrix:\n")
        file.write(get_pretty_str_from_matrix(second_matrix.matrix))
        file.write("\n\nmat_mul operation result:\n")
        file.write(get_pretty_str_from_matrix(mat_mul_result_matrix.matrix))
        file.close()


if __name__ == "__main__":
    main()
