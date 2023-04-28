import unittest


def mathematical_operations(astring):
    """
    Given a string consisting of parentheses,
    single digits, and positive and negative signs,
    convert the string into a mathematical expression to obtain the answer.
    """
    stack = []
    # acc to keep negative number together
    acc = ""
    for char in astring:
        if char == " ":
            acc = ""
            continue
        if char != ")":
            if char == "-":
                acc = char
            else:
                if acc == "-":
                    stack.append(f"-{char}")
                    acc = ""
                else:
                    stack.append(char)
        else:
            # when receive ")" go to get numbers out of the stack
            char = stack.pop()
            number1, number2, operation = "", "", ""
            while char != "(":
                # extract from the stack until we received "("
                if char not in ["+", "-"]:
                    if number2 == "":
                        number2 = int(char)
                    else:
                        number1 = int(char)
                else:
                    operation = char
                char = stack.pop()
            # perform the operation
            if operation == "+":
                stack.append(f"{number1 + number2}")
            else:
                stack.append(f"{number1 - number2}")
    #print(stack)
    if len(stack) == 1:
        return stack[0]
    number1, number2, operation = "", "", ""
    while True:
        char = stack.pop()
        if char in ["+", "-"]:
            operation = char
        else:
            if number2 == "":
                number2 = int(char)
            else:
                # perform operation
                number1 = int(char)
                if operation == "+":
                    stack.append(f"{number1 + number2}")
                else:
                    stack.append(f"{number1 - number2}")
                number1, number2, operation = "", "", ""
                if len(stack) < 3:
                    break
    return stack[0]

class TestMathematicalOperations(unittest.TestCase):
    """
    Test Mathematical Operations
    """

    def test_parenthesis(self):
        """
        test parenthesis
        """
        # arrange
        expression = '-1 + (2 + 3)'
        expecting = "4"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_negative_numbers(self):
        """
        test negative numbers
        """
        # arrange
        expression = '-1 + (2 - 3)'
        expecting = "-2"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"
    
    def test_nested_expression(self):
        """
        test nested expression
        """
        # arrange
        expression = "-1 + (2 + (2 - 3))"
        expecting = "0"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_another_nested_expression(self):
        """
        test nested expression
        """
        # arrange
        expression = "2 + (5 + (3 + 1))"
        expecting = "11"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_simple_parenthesis(self):
        """
        test simple parenthesis
        """
        # arrange
        expression = "(2 + 5)"
        expecting = "7"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_no_parenthesis(self):
        """
        test no parenthesis
        """
        # arrange
        expression = "2 + 5"
        expecting = "7"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_simple_negatives(self):
        """
        test simple negatives
        """
        # arrange
        expression = "-1 + -5"
        expecting = "-6"

        # action
        result = mathematical_operations(expression)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    #-mathematical_operations('-1 + (2 + 3)')
    #-mathematical_operations('-1 + (2 - 3)')
    #-mathematical_operations('-1 + (2 + (2 - 3))')
    #-mathematical_operations('1 + (2 + (2 - 3))')
    #-mathematical_operations('2 + (5 + (3 + 1))')
    #-mathematical_operations('(2 + 5)')
    #-mathematical_operations('2 + 5')
    #-mathematical_operations('-1 + -5')
    unittest.main()
