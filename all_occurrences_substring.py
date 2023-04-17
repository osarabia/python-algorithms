import unittest


def find_all_ocurrences(long_string, short_string):
    """
    return all ocurrences where short_string start inside long_string
    """
    indexes = []
    on_going_index = -1
    
    for index, character in enumerate(long_string):
        if index > 0:
            if character == short_string[on_going_index+1]:
                on_going_index += 1
            elif character == short_string[0]:
                on_going_index = 0
            else:
                on_going_index = -1
        else:
            if character == short_string[on_going_index+1]:
                on_going_index += 1
            else:
                on_going_index = -1
        if on_going_index == len(short_string) - 1:
            indexes.append(index - (len(short_string)-1))
            on_going_index = -1
    return indexes


class TestAllOcurrences(unittest.TestCase):
    """
    Test Find All Ocurrences
    """

    def test_at_the_beginning(self):
        """
        Test at the beginning
        """
        # arrange
        long_string = "abracadabra"
        short_string = "abra"
        expected = [0, 7]

        # action
        result = find_all_ocurrences(long_string, short_string)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_duplicate_character(self):
        """
        test duplicate characters
        """
        # arrange
        long_string = "aabracadaabra"
        short_string = "abra"
        expecting = [1, 9]

        # action
        result = find_all_ocurrences(long_string, short_string)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
