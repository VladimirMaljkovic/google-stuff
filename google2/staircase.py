from timeit import default_timer as timer


def count(height, left):
    # all the bricks have been used
    if left == 0:
        return 1

    # not enough bricks to build a new stair
    if left < height:
        return 0

    # either build a new stair now or try the next height (height + 1)
    return count(height + 1, left - height) + count(height + 1, left)


def bottom_up(n):
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    m[0][0] = 1  # base case

    for last in range(1, n + 1):
        for left in range(0, n + 1):
            m[last][left] = m[last - 1][left]
            if left >= last:
                m[last][left] += m[last - 1][left - last]

    print(m[n][n] - 1)


if __name__ == '__main__':
    n = 500
    start = timer()
    # print(count(1, n) - 1)
    bottom_up(n)

    end = timer()
    print(f'execution lasted {end - start} seconds')
