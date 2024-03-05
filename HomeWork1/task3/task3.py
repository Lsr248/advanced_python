from wc_executor import *


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        wc_command_from_stdin()
    else:
        try:
            wc_command_from_file(args)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
