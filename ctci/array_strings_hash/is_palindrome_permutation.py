import unittest

def is_palindrome_permutation(frase):
    """
    Is palindrome permutation by count
    """
    lower_limit = ord('a')
    upper_limit = ord('z')
    counter_map = [0] * 26
    # letters counter
    for character in frase:
        lower_case = character.lower()
        lower_case_value = ord(lower_case)
        if lower_case_value >= lower_limit and lower_case_value <= upper_limit:
            index = lower_case_value - lower_limit
            counter_map[index] += 1

    odd_count = 0
    for count in counter_map:
        if count > 0 and count % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False

    return True

class TestIsPalindromePermutation(unittest.TestCase):
    """
    Test is palindrome permutation
    """
    def test_valid(self):
        """
        Test valid case
        """
        # arrange
        astring = "aba"
        expecting = True

        # action
        result = is_palindrome_permutation(astring)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"
    
    def test_invalid_case(self):
        """
        Test invalid case
        """
        # arrange
        astring = "Random Words"
        expecting = False

        # action
        result = is_palindrome_permutation(astring)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_another_valid(self):
        """
        Test another valid
        """
        # arrange
        astring = "no x in nixon"
        expecting = True    

        # action
        result = is_palindrome_permutation(astring)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
