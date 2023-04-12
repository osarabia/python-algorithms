import unittest

def urlify(astring, true_length):
    """
    urlify
    """

    # run it backwards
    new_string = [""] * true_length
    last_index = len(astring) - 1
    backward_index = last_index
    # move backward index until we find a character
    while backward_index >= 0:
        char = astring[backward_index]
        if char != " ":
            break
        backward_index -= 1

    # continue moving backward , but after finding first character
    while backward_index >= 0:
        char = astring[backward_index]
        if char == " ":
            new_string[last_index] = "0"
            new_string[last_index-1] = "2"
            new_string[last_index-2] = "%"
            last_index -= 3
        else:
            new_string[last_index] = char
            last_index -= 1
        backward_index -= 1
    return "".join(new_string)


class TestUrlIfy(unittest.TestCase):
    """
    Test urlify
    """
    def test_first(self):
        """
        testing "test test" frase
        """
        # arrange
        frase = "test test  "
        expecting = "test%20test"

        # action
        result = urlify(frase, len(frase))

        # assert
        assert expecting == result, f"expecting {expecting}, got {result}"
    
    def test_second(self):
        """
        test "Mr John Smith" frase
        """
        # arrange
        frase = "Mr John Smith    "
        expecting = "Mr%20John%20Smith"

        # action
        result = urlify(frase, len(frase))

        # assert
        assert expecting == result, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
    #astring = "test test  "
    #astring = "Mr John Smith    "
    #urlify(astring, len(astring))