def attempt1(s):
    first_left_going_right = s.find('>')
    print(f'first left going right is on position {first_left_going_right}')
    first_right_going_left = s.rfind('<')
    print(f'first right going left is {first_right_going_left}')
    num_lefts = 0
    num_salutes = 0

    for x in range(first_left_going_right, first_right_going_left + 1):
        print(f'currently on index {x}, char is {s[x]}')
        if s[x] == '>':
            num_lefts += 1
            print(f'increased num of lefts by 1')
        if s[x] == '<':
            num_salutes += num_lefts * 2
            print(f'increased number of salutes, currently on {num_salutes}')
        print('*')
    print(f'total salutes {num_salutes}')


if __name__ == '__main__':
    attempt1('>>><<<><><><>')
