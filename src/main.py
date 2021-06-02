from interpreter import Interpreter
import interpreter


def main():
    interpreter = Interpreter()
    print("Reduced Scheme ver 0.1")
    print("Type (exit) to halt.")
    while True:
        line = input("RScheme>> ")
        print("Output>>", interpreter.eval(line).value)


if __name__ == "__main__":
    main()
