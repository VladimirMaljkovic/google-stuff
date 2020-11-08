def bottom_up(n):
    matrix = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # i have n+1 lists made of n+1 0's
    matrix[0][0] = 1

    for current in range(1, n + 1):
        for remaining in range(0, n + 1):
            matrix[current][remaining] = matrix[current - 1][remaining]
            if remaining >= current:
                matrix[current][remaining] += matrix[current - 1][remaining - current]

    return matrix[n][n] - 1
    # submitted like this
