import unittest


def sum_all_triples(nums):
    """
    All triples that sum up zero, avoid triples repetition
    """
    output = []
    nums.sort()
    for i in range(0, len(nums)-2):
        # avoid choosing same value
        if i > 0 and nums[i] == nums[i-1]:
            continue

        low, high = i+1, len(nums)-1
        while low < high:
            calculate_sum = nums[i] + nums[low] + nums[high]
            if calculate_sum > 0:
                high -= 1
            elif calculate_sum < 0:
                low += 1
            else:
                output.append([nums[i], nums[low], nums[high]])
                low += 1
                # avoid choosing same value
                while low < len(nums) - 1 and nums[low] == nums[low-1]:
                    low += 1
    return output


class TestSumAllTriples(unittest.TestCase):
    """
    Test Sum All Triples
    """
    def test_duplicates_values(self):
        """
        Test duplicate values
        """
        # arrange
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]

        # action
        result = sum_all_triples(nums)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_no_triples(self):
        """
        Test no triples
        """
        # arrange
        nums = [0, 1, 1]
        expected = []

        # action
        result = sum_all_triples(nums)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_same_values(self):
        """
        Test same values equals nums length to 3
        """
        # arrange
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]

        # action 
        result = sum_all_triples(nums)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_same_values_len_gt_3(self):
        """
        Test same values nums length greater than 3
        """
        # arrange
        nums = [0, 0, 0, 0, 0, 0]
        expected = [[0, 0, 0]]

        # action
        result = sum_all_triples(nums)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

if __name__ == "__main__":
    unittest.main()
