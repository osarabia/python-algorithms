import unittest


def top_k_frequent_elements(array, k):
    """
    Received an array and k value to retrieve k times most frequent elements
    """

    counter = {}
    frequency = []
    for _ in range(0, len(array)+1):
        frequency.append([])
    for element in array:
        counter[element] = counter.get(element, 0) + 1
    for number, freq in counter.items():
        frequency[freq].append(number)

    resp = []
    index = len(frequency) - 1
    while index > 0:
        if len(frequency[index]) > 0:
            for number in frequency[index]:
                if len(resp) < k:
                    resp.append(number)
            if len(resp) == k:
                return resp
        index = index - 1


class TestKFrequentElements(unittest.TestCase):
    """
    Test more frequent elements
    """
    def test_most_frequent(self):
        """
        Test more frequent at beginning
        """
        # arrange
        array = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]

        # action
        resp = top_k_frequent_elements(array, k)

        # assert
        assert resp == expected, f"expecting {expected}, got {resp}"

    def test_frequent_at_tail(self):
        """
        Test more frequent at end part of array
        """
        # arrange
        array = [3, 2, 2, 1, 1, 1]
        k = 2
        expected = [1, 2]

        # action
        resp = top_k_frequent_elements(array, k)

        # assert
        assert resp == expected, f"expecting {expected}, got {resp}"


if __name__ == "__main__":
    unittest.main()
