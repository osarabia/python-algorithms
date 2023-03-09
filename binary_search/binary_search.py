import unittest

def binarySearch(array, target):
    low, high = 0, len(array) -1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        #arrage
        array = [0,1,2,3,4,5]
        table = [{
            "array": array,
            "target": 0,
            "expected": 0
        },{
            "array": array,
            "target": 1,
            "expected":1
        },{
            "array": array,
            "target": 2,
            "expected":2
        },{
            "array": array,
            "target": 3,
            "expected": 3
        },{
            "array": array,
            "target": 4,
            "expected": 4
        },{
            "array":array,
            "target": 5,
            "expected": 5
        }]

        #action
        for tableCase in table:
            arr,target, expected = tableCase["array"],tableCase["target"],tableCase["expected"] 
            result = binarySearch(arr, target)
            #assert
            assert result == expected, "expecting {}, got {}".format(expected,result)

if __name__ == "__main__":
    unittest.main()
