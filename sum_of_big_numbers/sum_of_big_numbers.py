import unittest


def sum_of_big_numbers(str1, str2):
    """
    Sum of very big numbers as string
    """
    str1 = str1[::-1]
    str2 = str2[::-1]
    remaining = 0
    output = []

    start_index = 0
    while start_index < len(str1) and start_index < len(str2):
        num1 = int(str1[start_index])
        num2 = int(str2[start_index])
        result = num1 + num2 + remaining
        if result > 9:
            remaining = result // 10
            number = result % 10
            output.append(f"{number}")
        else:
            remaining = 0
            output.append(f"{result}")
        start_index += 1

    while start_index < len(str1):
        num1 = int(str1[start_index])
        result = num1 + remaining
        if result > 9:
            remaining = result // 10
            number = result % 10
            output.append(f"{number}")
        else:
            output.append(f"{result}")
        start_index += 1

    while start_index < len(str2):
        num2 = int(str2[start_index])
        result = num2 + remaining
        if result > 9:
            remaining = result // 10
            number = result % 10
            output.append(f"{number}")
        else:
            remaining = 0
            output.append(f"{result}")
        start_index += 1
    if remaining > 0:
        output.append(f"{remaining}")
    return "".join(output[::-1])


class TestSumOfBigNumbers(unittest.TestCase):
    """
    Test to sum two big numbers inputs received as string
    """

    def test_differents_length(self):
        """
        Test input number strings of differentes lengths
        """
        # arrange
        number1 = "123412341234123412341234"
        number2 = "12341234123412341234"
        expected = "123424682468246824682468"

        # action
        result = sum_of_big_numbers(number1, number2)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_remaining(self):
        """
        Test for remaining
        """
        # arrange
        number1 = "99999999999999999999999"
        number2 = "999999999999"
        expected = "100000000000999999999998"

        # action
        result = sum_of_big_numbers(number1, number2)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
