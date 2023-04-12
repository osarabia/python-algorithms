import unittest


def string_compression(astring):
    """
    String compression
    """
    compressed_string = []
    on_going_count = 0
    index = 0
    while index < len(astring):
        if index == 0:
            on_going_count += 1
        else:
            # compare agains previous character
            if astring[index-1] != astring[index]:
                # push to the array
                compressed_string.append(astring[index-1])
                compressed_string.append(f"{on_going_count}")
                # re-set on_going_count
                on_going_count = 1
            else:
                on_going_count += 1
        index += 1

    compressed_string.append(astring[-1])
    compressed_string.append(f"{on_going_count}")
    if len(compressed_string) > len(astring):
        return astring
    return "".join(compressed_string)


class TestStringCompression(unittest.TestCase):
    """
    Test String Compression
    """
    def test_compression(self):
        """
        Test Compression
        """
        # arrange
        astring = "aabccccaaa"
        expecting = "a2b1c4a3"

        # action
        result = string_compression(astring)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_long_compression(self):
        """
        test long compression
        """
        # arrange
        astring = "abcdef"

        # action
        result = string_compression(astring)

        # assert
        assert result == astring, f"expecting {astring}, got {result}"


if __name__ == "__main__":
    unittest.main()
