def prisoners(x, y):
    # 1 <= x, y <= 100
    # return solution as string
    if y == 1:
        bottom_number = (x * (x + 1)) / 2
        print(f'final number: {bottom_number}')
    else:
        bottom_number = ((x + 1) * (x + 2)) / 2
        print(f'bottom number: {bottom_number}')
        final_number = bottom_number - (y - 1)
        print(f'final number: {final_number}')


def solution(x, y):
    if y == 1:
        return str(int((x * (x + 1)) / 2))
    else:
        return str(int((((x + 1) * (x + 2)) / 2) - (y - 1)))


def prepravka(x, y):
    # x moram da pomerim za onoliko koliko y diktira
    donji_broj = ((x + y - 1) * (x + y) / 2)
    print(f'donji broj je {donji_broj}')
    finalni_broj = donji_broj - (y - 1)
    print(f'finalni broj je {finalni_broj}')


def solution2(x, y):
    return str(int(((x + y - 1) * (x + y) / 2) - (y - 1)))


if __name__ == '__main__':
    # print(solution(2, 5))
    # prepravka(3, 6)
    print(solution2(1, 7))
