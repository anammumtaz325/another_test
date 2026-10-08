import argparse
import datetime


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def current_timestamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_args():
    parser = argparse.ArgumentParser(description="A small demo CLI tool")
    parser.add_argument("--name", default="world", help="Name to greet")
    parser.add_argument(
        "--op",
        choices=["add", "subtract", "multiply", "divide"],
        help="Arithmetic operation to perform on --a and --b",
    )
    parser.add_argument("--a", type=float, default=0, help="First operand")
    parser.add_argument("--b", type=float, default=0, help="Second operand")
    return parser.parse_args()


def main():
    args = parse_args()

    print(greet(args.name))
    print(f"Current time: {current_timestamp()}")

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if args.op:
        result = operations[args.op](args.a, args.b)
        print(f"{args.op}({args.a}, {args.b}) = {result}")


if __name__ == "__main__":
    main()
