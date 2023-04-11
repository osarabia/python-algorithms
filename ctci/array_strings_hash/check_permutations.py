import unittest


def check_permutation(first_string, second_string):
    """
    Check permutation
    """
    if len(first_string) != len(second_string):
        return False
    counter = {}
    for character in first_string:
        counter[character] = 1 + counter.get(character, 0)

    for character in second_string:
        count = counter.get(character, 0)
        if count == 0:
            # find the invalid case
            return False
        counter[character] -= 1
    return True


class TestCheckPermutation(unittest.TestCase):
    """
    Test check permutations
    """
    def test_valid_case(self):
        """
        test a valid permutation
        """
        # arrange
        first_string = "dog"
        second_string = "god"
        expecting = True

        # action
        result = check_permutation(first_string, second_string)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_invalid_case(self):
        """
        Test invalid case
        """
        # arrange
        first_string = "2354"
        second_string = "1234"
        expecting = False

        # action
        result = check_permutation(first_string, second_string)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
