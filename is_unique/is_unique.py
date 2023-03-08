import unittest

def isUnique(string):
    '''
       is unique w/o additional data structure
    '''

    for i in range(0, len(string)-1):
        for j in range(i+1, len(string)):
            if not string[i].isspace() and string[i] == string[j]:
                return False
    return True


class IsUnique(unittest.TestCase):
    def test_is_unique_characters_word_at_side_each_other(self):
        #arrange
        string = "aaround"

        #action
        result = isUnique(string)

        #assert
        assert result is False, "expecting {}, got {}".format(False, result)

    def test_is_not_unique_word_last_character(self):
        #arrange
        string = "arounda"

        #action
        result = isUnique(string)

        #assert
        assert result is False, "expecting {}, got {}".format(False, result)

    def test_is_unique_phrase(self):
        string = "around this"

        #action
        result = isUnique(string)

        #assert
        assert result is True, "expecting {}, got {}".format(True, result)

if __name__ == "__main__":
    unittest.main()
