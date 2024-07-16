from interpreter import *


def main():
    if len(sys.argv) < 2:
        print("Usage: mipl\\main.py <filename> [-ri]")
        return

    filename = sys.argv[1]

    interpreter = MIPLInterpreter(filename)

    interpreter.start()


if __name__ == '__main__':
    print(sys.argv)
    main()
