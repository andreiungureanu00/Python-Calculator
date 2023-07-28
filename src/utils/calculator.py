"""Module to store the calculator class"""

import re


class Calculator:
    """Class representing the calculator which has a numbers string and a delimiter to split"""

    def __init__(self, numbers, delimiter):
        self.numbers = numbers
        self.delimiter = delimiter

    def add(self):
        """Function to add the numbers passed in the input after splitting the delimiters"""

        if not self.numbers:
            return 0

        # replacing the newlines with delimiters
        nums = self.numbers.replace("\\n", self.delimiter)

        # creating the numbers list after splitting with delimiters and ignoring
        # numbers bigger than 1000
        try:
            nums = [
                int(num)
                for num in re.split(self.delimiter, nums)
                if num and int(num) <= 1000
            ]
        except ValueError as value_error:
            raise ValueError("Invalid Input") from value_error

        # check negatives and raising error if there are any
        negative_nums = [num for num in nums if num < 0]
        if negative_nums:
            raise ValueError(
                "Negatives not allowed: " + ", ".join(str(num) for num in negative_nums)
            )

        return sum(nums)
