from tail_executor import *


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        tail_command_from_stdin()
    else:
        try:
            tail_command_from_file(args)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
