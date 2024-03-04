import sys


def nb_command_from_stdin():
    """
       Reads lines from stdin writes them to standard output
    """
    try:
        str_number = 1
        while True:
            input_line = input()
            result = "".join(["\t", str(str_number), " ", input_line])
            print(result)
            str_number = str_number + 1
    except EOFError:
        pass


def nb_command_from_file(file_names: list[str]):
    """
       Reads lines from the given files and writes them to standard output

       Parameters:
           file_names: list of file names to process
    """
    for file_name in file_names:
        try:
            file = open(file_name, 'r')
        except OSError:
            print("Could not open/read file:", file_name)
            sys.exit()
        with file:
            result = []
            str_number = 1
            lines = file.readlines()
            for line in lines:
                result.append("\t" + str(str_number) + " " + str(line))
                str_number = str_number + 1
            print("\n".join(result))
