import unittest

def largestRange(array):
    biggestRange = []
    longestDistance = 0
    nums = {}
    #mark numbers as not evaluated
    for num in array:
        nums[num] = True
    for n in array:
        #number already evaluated
        if not nums[n]:
            continue
        nums[n] = False
        currentDistance = 0
        left = num - 1
        right = num + 1
        #evaluate current number to left side
        while left in nums:
            nums[left] = False
            currentDistance += 1
            left -= 1
        #evaluate current number to right side
        while right in nums:
            nums[right] = False
            currentDistance += 1
            right += 1
        if currentDistance > longestDistance:
            longestDistance = currentDistance
            biggestRange = [left + 1, right - 1]
        return biggestRange


class TestLargetRange(unittest.TestCase):
    def test_a_largest_aray(self):
        #arrange
        arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
        expected = [0,7]

        #action
        result = largestRange(arr)

        #assert
        assert result == expected, "expecting {}, got {}".format(expected, result)

    def test_a_short_array(self):
        #arrange
        arr =  [4, 2, 1, 3]
        expected = [1,4]

        #action
        result = largestRange(arr)

        #assert
        assert result == expected, "expecting {}, got {}".format(expected, result)





if __name__ == "__main__":
    #arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    #arr = [4, 2, 1, 3]
    #print(largestRange(arr))
    unittest.main()
