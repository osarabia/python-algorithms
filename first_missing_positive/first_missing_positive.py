import unittest


def first_missing_positive(nums):
    """
    First Missing Positive
    """
    # changes negative value to positive
    for index, number in enumerate(nums):
        if number < 0:
            nums[index] = 0

    # hashSet using  array of numbers, map numbers in range to positions
    # changing to negative number
    for number in nums:
        index = abs(number) - 1
        if index >= 0 and index < len(nums):
            index_current_value = nums[index]
            if index_current_value > 0:
                nums[index] *= -1
            if index_current_value == 0:
                # handling zero case
                # just setting to a value out of looking range
                nums[index] = (len(nums) + 20) * -1
    missing_number = 0
    for number in range(1, len(nums) + 1):
        position = number - 1
        if nums[position] < 0:
            missing_number = number
        else:
            break

    return missing_number + 1


class FirstMissingPositiveTests(unittest.TestCase):
    """
    First missing positive test cases
    """
    def test_all_positives(self):
        """
        Test all positives
        """
        # arrange
        numbers = [1, 2, 0]
        expected = 3
        # action
        result = first_missing_positive(numbers)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_negative_numbers(self):
        """
        Test Negative numbers
        """
        # arrange
        numbers = [3, 4, -1, 1]
        expected = 2

        # action
        result = first_missing_positive(numbers)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_positives_out_of_range(self):
        """Test all positives out of range"""
        # arrange
        nums = [7, 8, 9, 11, 12]
        expecting = 1

        # action
        result = first_missing_positive(nums)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_positives_missing_at_end(self):
        """
        Test all positives missing at the end
        """
        # arrange
        numbers = [1, 2, 6, 3, 5, 4]
        expecting = 7

        # action
        result = first_missing_positive(numbers)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_just_one_negative(self):
        """
        Test just one negative
        """
        # arrange
        numbers = [-5]
        expecting = 1

        # action
        result = first_missing_positive(numbers)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
