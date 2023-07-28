"""Module to provide the input parsers needed for Calculator class"""

import argparse
import re


def arg_parser():
    """Function to read the input arguments"""

    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument("input", type=str, help="Input arguments")
    args = parser.parse_args()

    return args


def input_parser(numbers):
    """Function to extract the delimiter based on the input"""

    delimiter = re.match(r"//(.+?)\\n", numbers)

    if delimiter:
        end_pos = delimiter.end()
        delimiter = delimiter.group(1)

        delimiters = re.findall(r"\[(.*?)\]", delimiter)
        if delimiters:
            delimiter = "|".join(re.escape(x) for x in delimiters)
            delimiter = rf"{delimiter}"

        numbers = numbers[end_pos:]

    else:
        delimiter = ","

    return numbers, delimiter
