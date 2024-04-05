import numpy as np
from matrix import Matrix, generate_matrix_from_ndarray


def main():
    first_matrix = generate_matrix_from_ndarray(np.random.randint(0, 10, (10, 10)))
    second_matrix = generate_matrix_from_ndarray(np.random.randint(0, 10, (10, 10)))
    add_result_matrix = first_matrix + second_matrix
    mul_result_matrix = first_matrix * second_matrix
    mat_mul_result_matrix = first_matrix @ second_matrix
    with open("../artifacts/task2/matrix+.txt", "w") as file:
        file.write("first_matrix:\n")
        file.write(str(first_matrix))
        file.write("\n\nsecond_matrix:\n")
        file.write(str(second_matrix))
        file.write("\n\nadd operation result:\n")
        file.write(str(add_result_matrix))
        file.close()

    with open("../artifacts/task2/matrix*.txt", "w") as file:
        file.write("first_matrix:\n")
        file.write(str(first_matrix))
        file.write("\n\nsecond_matrix:\n")
        file.write(str(second_matrix))
        file.write("\n\nmul operation result:\n")
        file.write(str(mul_result_matrix))
        file.close()

    with open("../artifacts/task2/matrix@.txt", "w") as file:
        file.write("first_matrix:\n")
        file.write(str(first_matrix))
        file.write("\n\nsecond_matrix:\n")
        file.write(str(second_matrix))
        file.write("\n\nmat_mul operation result:\n")
        file.write(str(mat_mul_result_matrix))
        file.close()


if __name__ == "__main__":
    main()
