def normalize(path):
    length = len(path)
    new_length = length + 2

    new_path = [[None for i in range(new_length)] for j in range(new_length)]
    new_path1 = [[None] * new_length] * new_length

    # print('empty new_path:')
    # for i in range(new_length):
    #     for j in range(new_length):
    #         print(f'{new_path[i][j]} ', end='')
    #     print()
    # print()
    #
    # print('empty new_path1:')
    # for i in range(new_length):
    #     for j in range(new_length):
    #         print(f'{new_path1[i][j]} ', end='')
    #     print()
    # print()

    # print(f'type(new_path): {type(new_path)}')
    # print(f'type(new_path1): {type(new_path1)}')
    # print(f'type(new_path[0]): {type(new_path[0])}')
    # print(f'type(new_path1[0]): {type(new_path1[0])}')
    # print(f'type(new_path[0][0]): {type(new_path[0][0])}')
    # print(f'type(new_path1[0][0]): {type(new_path1[0][0])}')
    # print()

    for i in range(length):
        for j in range(length):
            new_path[i + 1][j + 1] = path[i][j]
            new_path1[i + 1][j + 1] = path[i][j]

    print('filled new_path:')
    for i in range(new_length):
        for j in range(new_length):
            print(f'{new_path[i][j]} ', end='')
        print()
    print()

    print('filled new_path1:')
    for i in range(new_length):
        for j in range(new_length):
            print(f'{new_path1[i][j]} ', end='')
        print()
    print()


if __name__ == '__main__':
    path = [
        [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
    ]

    normalize(path)
