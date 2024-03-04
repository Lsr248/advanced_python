import sys


def tail_command_from_stdin():
    """
       Reads lines from stdin and writes last 17 lines to standard output
    """
    k_number_to_output = 17
    result = []
    try:
        while True:
            input_line = input()
            result.append(input_line)
    except EOFError:
        if len(result) < k_number_to_output:
            print("\n".join(result))
        else:
            print("\n".join(result[len(result) - k_number_to_output :]))


def tail_command_from_file(file_names: list[str]):
    """
       Reads lines from the given files and writes last 10 of them to standard output

       Parameters:
           file_names: list of file names to process
    """
    k_number_to_output = 10
    is_output_name_needed = len(file_names) > 1

    for file_name in file_names:
        try:
            file = open(file_name, 'r')
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
            print("".join(lines[len(lines) - k_number_to_output :]))