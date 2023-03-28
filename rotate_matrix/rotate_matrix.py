

def rotate_matrix(matrix):
    """
    Rotate Matrix 90 degrees O(1) space
    """

    # set boundaries
    # left, right. top , bottom
    left, right = 0, len(matrix) - 1
    while left < right:
        top, bottom = left, right
        # calculate number of iterations to rotate right - left times
        for i in range(right - left):
            # save top-left
            top_left = matrix[top][left + i]

            # move bottom - left to top-left
            matrix[top][left + i] = matrix[bottom-i][left]

            # move bottom-right to bottom-left
            matrix[bottom-i][left] = matrix[bottom][right-i]

            # move top-right to bottom-right
            matrix[bottom][right-i] = matrix[top+i][right]

            # move top-left to to-right
            matrix[top+i][right] = top_left
        left += 1
        right -= 1
    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    new_matrix = rotate_matrix(matrix)
    print(new_matrix)
