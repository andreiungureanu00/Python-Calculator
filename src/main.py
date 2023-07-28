"""Main Module to run the program"""

import logging
import sys

from utils.parsers import arg_parser, input_parser
from utils.calculator import Calculator


def main():
    """Function to trigger the main module"""

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = arg_parser()
    numbers, delimiter = input_parser(args.input)

    calculator = Calculator(numbers, delimiter)

    try:
        result = calculator.add()
        print(f"Result = {result}")

    except ValueError as value_error:
        logging.info(value_error)
        sys.exit()
    except Exception as error:
        logging.error(error)
        sys.exit()


if __name__ == "__main__":
    main()
