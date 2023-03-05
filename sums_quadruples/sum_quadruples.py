import unittest

def sumQuadruples(array, targetSum):
    pairsSum = {}
    quadruples = []
    for i in range(1, len(array)-1):
        # calculate diff to evaluate agains sum of pairs
        for j in range(i+1, len(array)):
            sumValue = array[i] + array[j]
            diff = targetSum - sumValue
            if diff in pairsSum:
                quadruples.append(pairsSum[diff] + [array[i], array[j]])

        #group by total sum of pairs
        for k in range(0, i):
            sumValue = array[k] + array [i]
            if sumValue not in pairsSum:
                pairsSum[sumValue] = [array[k], array[i]]
            else:
                pairsSum[sumValue].append([array[k], array[i]])

    return quadruples


class TestSumQuadruples(unittest.TestCase):

    def test_quadruples_simple(self):
        array = [7,6,4,-1,2, 1]
        target = 16
        expecting =  [[7,6,4,-1],[7,6,2,1]] 

        quadruples = sumQuadruples(array, target)

        assert expecting == quadruples, "expecting {} got {}".format(expecting, quadruples)

    def test_quadruples_four_numbers(self):
        array = [7,6,2,1]
        target = 16
        expecting = [[7,6,2,1]]
        quadruples = sumQuadruples(array, target)

        assert expecting == quadruples, "expecting {} got {}".format(expecting, quadruples)

    def test_quadruples_empty(self):
        array = [7,5,2,1]
        target = 16
        expecting = []
        quadruples = sumQuadruples(array, target)

        assert expecting == quadruples, "expecting {} got {}".format(expecting, quadruples)


if __name__ == "__main__":
    unittest.main()
