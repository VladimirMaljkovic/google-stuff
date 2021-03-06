from timeit import default_timer as timer


n = 200
mem = [[-1 for j in range(n + 2)] for i in range(n + 2)]
# list of lists that will set -1 n+2 times on n + 2 lists
# first dimension is height, second is how many bricks i have left apparently


def custom_mem(height, left):
    global mem
    if mem[height][left] != -1:
        return mem[height][left]

    if left == 0:
        return 1
    if left < height:
        return 0
    res = custom_mem(height + 1, left - height) + custom_mem(height + 1, left)
    mem[height][left] = res
    return res


if __name__ == '__main__':
    start = timer()
    print(custom_mem(1, n) - 1)

    end = timer()
    print(f'execution lasted {end - start} seconds')


