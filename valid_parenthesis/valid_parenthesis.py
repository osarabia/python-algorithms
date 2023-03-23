import unittest


def is_valid(astring):
    """
    Check if string is valid
    strings contains open parenthesis open squarebrackes and open curly
    brackets
    """
    stack = []
    open_chars = ["(", "[", "{"]
    close_chars = {")": "(", "]": "[", "}": "{"}
    for character in astring:
        if character in open_chars:
            stack.append(character)
        else:
            if len(stack) > 0:
                if close_chars[character] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    return len(stack) == 0


class TestIsValidParenthesis(unittest.TestCase):
    """
    Test Cases to Validate if Parenthesis are valid
    """

    def test_example_1(self):
        """
        input = "()"
        """
        # arrange
        astring = "()"

        # action
        result = is_valid(astring)

        # assert
        assert result, "expecting True"

    def test_example_2(self):
        """
        input = "()[]{}"
        """
        # arrange
        astring = "()[]{}"

        # action
        result = is_valid(astring)

        # assert
        assert result, "expecting True"

    def test_example_3(self):
        """
        input = "(]"
        """
        # arrange
        astring = "(]"

        # action
        result = is_valid(astring)

        # assert
        assert not result, "expecting False"

    def test_example_4(self):
        """
        input = "((())))"
        """
        # arrange
        astring = "((())))"

        # action
        result = is_valid(astring)

        # assert
        assert not result, "expecting False"

    def test_example_5(self):
        """
        input = "["
        """
        # arrange
        astring = "["

        # action
        result = is_valid(astring)

        # assert
        assert not result, "expecting False"


if __name__ == "__main__":
    unittest.main()
