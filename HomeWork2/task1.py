from HomeWork2.tex_module_src.tex_module import (
    save_code_in_tex_file,
    generate_tex_file_in_str,
    generate_table_content,
)
import sys
import os

ARTIFACT_RELATIVE_PATH = "/artifacts/task1/"


def read_table_from_command_line() -> list[list[str]]:
    """
    Reads lines from stdin writes them to array
    """
    table = []
    print("print rows count")
    try:
        rows_count = int(input())
    except Exception:
        raise Exception(f"Can not parse input to int")
    try:
        for i in range(0, rows_count + 1):
            input_row = input().split(" ")
            table.append(input_row)
    except Exception as e:
        message = e.__str__()
        raise Exception(f"Can not parse input to table, exception: {message}")

    return table


def create_table_from_args(input_table: str) -> list[list[str]]:
    """
    Creates table from input in args
    """
    try:
        result_table = []
        if input_table.startswith('"[[') and input_table.endswith("]]"):
            input_table = input_table[2:-2]
        else:
            raise Exception("Wrong format of table")
        input_table = input_table.split("], [")
        for row in input_table:
            result_table.append(row.split(", "))
        return result_table
    except Exception as e:
        message = e.__str__()
        raise Exception(f"Can not greate table from args, exception: {message}")


def main():
    args = sys.argv[1:]
    tex_code = ""
    table = []
    try:
        if len(args) == 0:
            table = read_table_from_command_line()
        else:
            table = create_table_from_args(args[0])
    except Exception as e:
        print(e)
        return

    try:
        tex_code = generate_tex_file_in_str(generate_table_content(table))
    except Exception as e:
        print(e)
        return

    print("Do you want save tex code to file? Print yes/no")
    answer = input()
    if answer == "yes":
        print("Print filename in format {filename.tex}")
        file_name = input()
        abs_path_for_saving_file = (
            os.path.abspath(os.getcwd()) + ARTIFACT_RELATIVE_PATH + file_name
        )
        save_code_in_tex_file(tex_code, abs_path_for_saving_file)


if __name__ == "__main__":
    main()
