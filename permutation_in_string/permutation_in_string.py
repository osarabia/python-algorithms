import unittest

def permutation_in_string(s1, s2):
    """
    return true if s1 is a permutation inside s2
    """
    if len(s1) > len(s2):
        return False
    
    counter_s1 = [0] * 26
    counter_s2 = [0] * 26

    left, matches = 0, 0
    for i in range(0, len(s1)):
        counter_s1[ord(s1[i]) - ord('a')] += 1
        counter_s2[ord(s2[i]) - ord('a')] += 1
    
    for i in range(0, 26):
        if counter_s1[i] == counter_s2[i]:
            matches += 1
    
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        index = ord(s2[right]) - ord('a')
        counter_s2[index] += 1
        if counter_s1[index] == counter_s2[index]:
            matches += 1
        elif counter_s1[index] + 1 == counter_s2[index]:
            matches -= 1
        
        index = ord(s2[left]) - ord('a')
        counter_s2[index] -= 1
        if counter_s1[index] == counter_s2[index]:
            matches += 1
        elif counter_s1[index] - 1 == counter_s2[index]:
            matches -= 1
        left += 1
    return matches == 26


class TestPermutationString(unittest.TestCase):
    """
    Test Cases for permutation string
    """

    def test_anagram_match(self):
        """Anagram match"""
        # arrange
        s1 = "ab"
        s2 = "eidbaooo"

        # action
        result = permutation_in_string(s1, s2)

        # assert
        assert result, "expecting True"

    def test_no_match(self):
        """no match"""
        # arrange
        s1 = "ab"
        s2 = "eidboaoo"

        # action
        result = permutation_in_string(s1, s2)

        # assert
        assert not result, "expecting False"

    def test_match_at_tail_of_s2(self):
        """tail match"""
        # arrange
        s1 = "abc"
        s2 = "bbbca"

        # action
        result = permutation_in_string(s1, s2)

        # assert
        assert result, "expecting True"


if __name__ == "__main__":
    unittest.main()
