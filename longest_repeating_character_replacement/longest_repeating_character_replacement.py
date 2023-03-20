import unittest


def max_character_repetition(character_counter):
    """
    Returns max number of character counted
    """
    max_char_repetition = 0
    for _, count in character_counter.items():
        max_char_repetition = max(max_char_repetition, count)
    return max_char_repetition


def longest_repeating_character_replacement(s, k):
    """
    Longest Repeating Character Replacement
    """
    max_length = 0
    left = 0
    counter = {}

    for right, right_char in enumerate(s):
        counter[right_char] = counter.get(right_char, 0) + 1
        distance = right - left + 1
        max_char_repetition = max_character_repetition(counter)
        while left <= right and distance - max_char_repetition > k:
            left_char = s[left]
            counter[left_char] -= 1
            left += 1
            distance = right - left + 1
            max_char_repetition = max_character_repetition(counter)
        max_length = max(max_length, distance)

    return max_length


class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    """
    Testing Longest Repeating Character Replacement
    """

    def test_k_equals_than_full_set_of_chars(self):
        """Test k equals than full set of Chars"""
        # arrange
        astring = "ABAB"
        k = 2
        expected = 4

        # action
        result = longest_repeating_character_replacement(astring, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_k_greater_than_set_of_chars(self):
        """Test k greater than full set of chars"""
        # arrange
        astring = "ABABB"
        k = 2
        expected = 5

        # action
        result = longest_repeating_character_replacement(astring, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_k_less_than_set_of_chars(self):
        """Test k less than full set of chars"""
        # arrange
        astring = "ABABB"
        k = 1
        expected = 4
        # action
        result = longest_repeating_character_replacement(astring, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_k_zero(self):
        """
        Test k  zero substitution
        """
        # arrange
        astring = "ABCDEFG"
        k = 0
        expected = 1

        # action
        result = longest_repeating_character_replacement(astring, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
