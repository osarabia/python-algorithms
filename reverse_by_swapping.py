import unittest

def reverse_by_swapping(array):
    i = 0
    while i < len(array)/2:
        last_index = len(array) - 1 - i
        first_element = array[i]
        array[i] = array[last_index]
        array[last_index] = first_element
        i = i + 1

    return array


class TestReververBySwapping(unittest.TestCase):
    def test_odd_length(self):
        #arrange
        input_arr = [1,2,3]
        expected_arr = [3,2,1]

        #action
        output = reverse_by_swapping(input_arr)

        #assert
        assert output == expected_arr, "expecting {}, got {}".format(expected_arr, output)

    def test_even_length(self):
        #arrange
        input_arr = [1,2,3,4]
        expected_arr = [4,3,2,1]

        #action
        output = reverse_by_swapping(input_arr)

        #assert
        assert output == expected_arr, "expecting {}, got {}".format(expected_arr, output)


if __name__ == '__main__':
    unittest.main()
