import unittest


def evaluate_notation(tokens):
    """
    evaluate reverse polish notation
    """
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "-":
            number1, number2 = stack.pop(), stack.pop()
            stack.append(number2 - number1)
        elif token == "/":
            number1, number2 = stack.pop(), stack.pop()
            stack.append(int(number2 / number1))
        else:
            stack.append(int(token))
    return stack[0]


class TestEvaluatePolishNotation(unittest.TestCase):
    """
    Test to evaluate polish notation
    """
    def test_example_1(self):
        """
        input = ["2","1","+","3","*"]
        """
        # arrange
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9

        # action
        result = evaluate_notation(tokens)

        # result
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2(self):
        """
        input = ["4","13","5","/","+"]
        """
        # arrange
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6

        # action
        result = evaluate_notation(tokens)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_3(self):
        """
        input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"
        """
        # arrange
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22

        # action
        result = evaluate_notation(tokens)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
