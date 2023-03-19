import unittest


def max_substring(s):
    """
    return max length of substring w/o repetion characters
    """
    seen = set()
    left = 0
    max_length = 0

    for right, character in enumerate(s):
        while character in seen:
            seen.remove(s[left])
            left += 1
        seen.add(character)
        calculated_length = right - left + 1
        max_length = max(max_length, calculated_length)

    return max_length

class TestMaxSubstring(unittest.TestCase):
    """
    Test Cases for Max Substring non repetitive
    """
    def test_example_1(self):
        """
        Test Example 1
        """
        # arrange
        astring = "abcabcbb"
        expected = 3

        # action
        length = max_substring(astring)

        # assert
        assert length == expected, f"expecting {expected}, got {length}"

    def test_example_2(self):
        """
        Test Example 2
        """
        # arrange
        astring = "bbbbb"
        expected = 1

        # action
        length = max_substring(astring)

        # assert
        assert length == expected, f"expecting {expected}, got {length}"

    def test_example_3(self):
        """
        Test Example 3
        """
        # arrange
        astring = "pwwkew"
        expected = 3

        # action
        length = max_substring(astring)

        # assert
        assert length == expected, f"expecting {expected}, got {length}"


if __name__ == "__main__":
    unittest.main()