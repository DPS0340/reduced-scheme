from interpreter import Interpreter
import interpreter


def main():
    interpreter = Interpreter()
    while True:
        line = input("RScheme>> ")
        print("Output>>", interpreter.eval(line).value)


if __name__ == "__main__":
    main()
