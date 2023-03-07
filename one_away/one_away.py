import unittest

def oneAway(firstString, secondString):
    if abs(len(firstString) - len(secondString)) > 1:
        return False

    i,j = 0,0

    justOneEdition = False

    while i < len(firstString) and j < len(secondString):
        if firstString[i] == secondString[j]:
            i += 1
            j += 1

        else:
            if justOneEdition:
                return False

            justOneEdition = True
            if len(firstString) > len(secondString):
                i += 1
            elif len(secondString) > len(firstString):
                j += 1
            else:
                i += 1
                j += 1

    return True

class TestOneAway(unittest.TestCase):
    def test_diff_lengths_one_char(self):
        #arrange
        input1 = "pale"
        input2 = "ple"

        #action
        result = oneAway(input1, input2)

        assert result == True,"should be true"

    def test_diff_length_the_other_way_one_char(self):
        #arrange
        input1 = "ple"
        input2 = "pale"

        #action
        result = oneAway(input1, input2)

        assert result == True, "shold be true"

    def test_dff_lenth_more_than_one_char(self):
        input1 = "ppale"
        input2 = "ppa"

        result = oneAway(input1, input2)

        assert result == False, "should be false"

    def test_dff_lenth_more_than_one_char_mid_diff(self):
        input1 = "ppale"
        input2 = "pple"

        result = oneAway(input1, input2)

        assert result == True, "should be false"



if __name__ == "__main__":
    unittest.main()
