def rotate_matrix_90_degrees(matrix):
    """ Method to rotate a matrix 90 degrees clockwise. """
    n = len(matrix)
    m = len(matrix[0])
    rotated_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n - i - 1] = matrix[i][j]
    return rotated_matrix
