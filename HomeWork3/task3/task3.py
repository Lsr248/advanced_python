from matrix import Matrix


def main():
    a = Matrix([[6, 7], [2, 7]])
    b = Matrix([[4, 5, 2], [9, 10, 4]])

    c = Matrix([[14, 7], [4, 4]])
    d = Matrix([[4, 5, 2], [9, 10, 4]])
    assert hash(a) == hash(c)
    assert b == d
    a_b = a @ b
    c_d = c @ d
    assert a_b != c_d

    with open("../artifacts/task3/AB.txt", "w") as file:
        file.write(str(a_b))
        file.close()

    with open("../artifacts/task3/CD.txt", "w") as file:
        file.write(str(c_d))

    with open("../artifacts/task3/hash.txt", "w") as file:
        a_b_hash = hash(a_b)
        file.write(f"hash of AB: {a_b_hash} \n")
        c_d_hash = hash(c_d)
        file.write(f"hash of CD: {c_d_hash} \n")


if __name__ == "__main__":
    main()
