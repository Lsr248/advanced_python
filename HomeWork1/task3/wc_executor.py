import sys


class Statistic:
    def __init__(self, number_of_lines, number_of_words, number_of_bytes, file_name):
        self.number_of_lines = number_of_lines
        self.number_of_words = number_of_words
        self.number_of_bytes = number_of_bytes
        self.file_name = file_name

    def print_for_command_line_input(self):
        print(f"      {self.number_of_lines}       {self.number_of_words}      {self.number_of_bytes}")

    def print_for_file(self):
        print(f" {self.number_of_lines} {self.number_of_words} {self.number_of_bytes} {self.file_name}")


def split_to_words(lines: list[str]):
    words = []
    for line in lines:
        words += line.split()
    return words


def count_numer_of_bytes(words: list[str]):
    bytes_in_words = 0
    for word in words:
        bytes_in_word = word.encode('utf-8')
        bytes_in_words += len(bytes_in_word) + 1

    return bytes_in_words


def count_number_of_lines(lines: list[str]):
    number_of_lines = 0
    for line in lines:
        number_of_lines += line.count('\n')

    return number_of_lines


def count_common_statistics(lines: list[str], file_name: str = None):
    number_of_lines = count_number_of_lines(lines)
    words = split_to_words(lines)
    number_of_words = len(words)
    number_of_bytes = count_numer_of_bytes(words)
    if number_of_lines != len(lines):
        number_of_bytes -= 1
    # to count empty strings in file like empty.txt
    if number_of_lines > 0 and number_of_words == 0:
        number_of_bytes = number_of_lines
    return Statistic(number_of_lines, number_of_words, number_of_bytes, file_name)


def wc_command_from_stdin():
    """
       Counts statistic for input and writes it to standard output
    """

    lines = []
    try:
        while True:
            input_line = input()
            lines.append(input_line + '\n')
    except EOFError:
        statistics = count_common_statistics(lines)
        statistics.print_for_command_line_input()


def wc_command_from_file(file_names: list[str]):
    """
       Counts statistic for file and writes it to standard output

       Parameters:
           file_names: list of file names to process
    """
    is_total_needed = len(file_names) > 1
    file_statistics = []

    for file_name in file_names:
        try:
            file = open(file_name, 'r')
        except OSError:
            print("Could not open/read file:", file_name)
            sys.exit()
        with file:
            lines_in_file = file.readlines()
            file_statistic = count_common_statistics(lines_in_file, file_name)
            file_statistic.print_for_file()
            file_statistics.append(file_statistic)

    if is_total_needed:
        total_number_of_lines = 0
        total_number_of_words = 0
        total_number_of_bytes = 0

        for file_statistic in file_statistics:
            total_number_of_lines += file_statistic.number_of_lines
            total_number_of_words += file_statistic.number_of_words
            total_number_of_bytes += file_statistic.number_of_bytes

        total_statistic = Statistic(total_number_of_lines, total_number_of_words, total_number_of_bytes, "total")
        total_statistic.print_for_file()
