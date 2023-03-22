import unittest

def minimum_substring_window(s, t):
    """
    minimum substring window of t in s
    """
    if len(s) < len(t):
            return ""
    min_length, min_range = 0, {}
    need = 0
    counter_t  = {}
    for c in t:
        if c in counter_t:
            counter_t[c] += 1
        else:
            # even if we need duplicates just count as 1
            need += 1
            counter_t[c] = 1

    have = 0
    counter_w = {}
    left = 0
    for right in range(0, len(s)):
        c = s[right]
        counter_w[c] = 1 + counter_w.get(c, 0)

        if counter_t.get(c, 0) > 0 and counter_w[c] == counter_t[c]:
            have += 1
        if have < need:
            continue
        # after meet have and need count
        while have == need:
            distance = right - left + 1
            if distance < min_length or min_length == 0:
                min_length = distance
                min_range['left'] = left
                min_range['right'] = right
            l = s[left]
            counter_w[l] -= 1
            if counter_t.get(l, 0) > 0 and counter_w[l] + 1 == counter_t[l]:
                have -= 1
            left += 1
    if min_length > 0:
        left,right = min_range['left'],min_range['right']
        return s[left:right+1]
    return ""

class TestMinWindow(unittest.TestCase):
    """
    Test Min Window
    """

    def test_s_greater_than_t(self):
        """
        Test s greater than t
        """
        # arrange
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"

        # action
        result = minimum_substring_window(s, t)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_t_duplicates_chars(self):
        """
        Test Duplicate Chars
        """
        # arrange
        s = "acbbaca"
        t = "aba"
        expected = "baca"

        # action
        result = minimum_substring_window(s, t)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
