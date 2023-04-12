import unittest


def one_away(first_string, second_string):
    """
    One Away
    """
    first_index = 0
    second_index = 0
    insert_remove_replace = 0
    while first_index < len(first_string) and second_index < len(second_string):
        if len(first_string) == len(second_string) + 1:
            if first_string[first_index] != second_string[second_index]:
                insert_remove_replace += 1
            else:
                second_index += 1
            first_index += 1
        elif len(first_string) == len(second_string):
            if first_string[first_index] != second_string[second_index]:
                insert_remove_replace += 1
            second_index += 1
            first_index += 1
        else:
            return False

    if insert_remove_replace > 1:
        return False
    return True


class TestOneAway(unittest.TestCase):
    """
    test one away
    """
    def test_valid(self):
        """
        test valid case
        """
        # arrange
        first_string = "pale"
        second_string = "ple"
        expecting = True

        # action
        result = one_away(first_string, second_string)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_invalid(self):
        """
        test invalid case
        """
        # arrange
        first_string = "pale"
        second_string = "bake"
        expecting = False

        # action
        result = one_away(first_string, second_string)

        # assert
        assert expecting == result, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
