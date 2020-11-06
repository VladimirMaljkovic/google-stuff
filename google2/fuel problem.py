def attempt1(s):
    number = int(s)
    actions = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            print(f'number % 2 == 0, dividing by 2')
        elif number % 4 == 1 or number == 3:
            print(f'n % 4 == 1 or num == 3, subtracting 1')
            number -= 1
        else:
            print('adding 1')
            number += 1
        actions += 1
        print('number of actions increased by 1')
    print(f'actions needed: {actions}')
    return actions


if __name__ == '__main__':
    attempt1('15')