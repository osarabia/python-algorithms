import unittest


def is_unique(astring):
    """
    use of extra memory O(n)
    time complexity O(n)
    """
    hash_set = set()
    for character in astring:
        if character in hash_set:
            return False
        hash_set.add(character)
    return True


class TestIsUnique(unittest.TestCase):
    """
    Test Cases For Is Unique
    """

    def test_all_uniques(self):
        """
        all unique characters
        """
        # arrange
        astring = "helo"
        expecting = True

        # action
        result = is_unique(astring)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_non_unique_characters(self):
        """
        non unique chars
        """
        # arrange
        astring = "hello world"
        expecting = False

        # action
        result = is_unique(astring)

        # assert
        assert expecting == result, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()