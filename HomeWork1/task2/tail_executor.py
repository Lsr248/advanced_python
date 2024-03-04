import sys
import os

def tail_command_from_stdin():
    """
       Reads lines from stdin writes them to standard output
    """
    k_number_to_output = 17
    try:
        str_number = 1
        while True:
            input_line = input()
            result = "".join(["\t", str(str_number), " ", input_line])
            print(result)
            str_number = str_number + 1
    except EOFError:
        pass


def tail_command_from_file(file_names: list[str]):
    """
       Reads lines from the given files and writes them to standard output

       Parameters:
           file_names: list of file names to process
    """
    k_number_to_output = 10
    is_output_name_needed = len(file_names) > 1

    for file_name in file_names:
        try:
            file = open(file_name, 'rb')
        except OSError:
            print("Could not open/read file:", file_name)
            sys.exit()
        with file:
            if is_output_name_needed:
                print(" ".join(["==>", file_name, "<=="]))
            lines = file.readlines()
            if len(lines) < k_number_to_output:
                print("".join(lines))
                continue
            print("".join(lines[len(lines) - k_number_to_output + 1:]))