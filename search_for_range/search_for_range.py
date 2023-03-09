import unittest

def searchForRange(array, target):
    notContained = [-1, -1] 
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > target:
            high = mid -1
        elif array[mid] < target:
            low = mid + 1
        else:
            rangeOutput = [mid, mid]
            while rangeOutput[0]-1 >=0 and array[rangeOutput[0]-1] == target:
                rangeOutput[0] = rangeOutput[0] - 1
            while rangeOutput[1] + 1 < len(array) and array[rangeOutput[1] +1] == target:
                rangeOutput[1] = rangeOutput[1] + 1
            return rangeOutput
    return notContained

class TestSearchForRange(unittest.TestCase):
    def test_at_beginning(self):
        #arrange
        array = [20,20,20,20,21,22,23,24,100,200,201]
        expected = [0,3]
        #action
        result = searchForRange(array, 20)

        #assert
        assert result == expected, "expecting {}, got {}".format(expected, result)

    def test_at_middle(self):
        #arrange
        array = [21,22,23,200,200,200,200,501,555,556,557]
        expected = [3,6]
        #action
        result = searchForRange(array, 200)

        #assert
        assert result == expected,"expecting {}, got {}".format(expected, result)

    def test_at_tail(self):
        #arrange
        array = [20,21,22,23,24,25,26,26,26,26,26,26]
        expected = [6,11]

        #action
        result = searchForRange(array, 26)

        #assert
        assert result == expected, "expecting {}, got {}".format(expected, result)

    def test_not_in_place(self):
        #arrange
        array = [1,2,3,4,5,6,7,8,9]
        target = 10
        expected = [-1,-1]
        #action
        result = searchForRange(array, 10)

        #assert
        assert result == expected, "expecting {},got {}".format(expected, result)

if __name__ == "__main__":
    unittest.main()
