# print_arguments/main.py
#triger ?
import argparse


def print_arguments(arguments: list[str]):
    for argument in arguments:
        print(argument)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    with open("C:\\Thomas\\CheckHook\\ThomasHookTest.txt", "w") as file:
        file.write("Succes, Now need to find the location")
        file.write(i for i in args.filenames)
    print_arguments(args.filenames)


if __name__ == "__main__":
    main()
