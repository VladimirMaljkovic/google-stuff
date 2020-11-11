from timeit import default_timer as timer

# u svakoj generaciji se bombe repliciraju, tj
# ako imam 5 f bombi, dobijem jos 5 M bombi, i obrnuto
# zanima me brjo ciklusa da dobijem trazen broj bombi ako trecem od 1 M 1 F bombe


def attempt1(mm, ff):
    m = int(mm)
    f = int(ff)
    counter = 0
    solved = False

    if m == f == 1:
        return 0

    if (m % 2 == 0 and f % 2 == 0) or (m == f):
        return 'impossible'

    while solved is not True:
        if m == 1 and f == 1:
            solved = True
        if m > f:
            m = m - f
            counter += 1
        if f > m:
            f = f - m
            counter += 1
    return str(counter)


def attempt2(x, y):
    x, y = int(x), int(y)
    cycles = 0
    while x != 1 and y != 1:
        if x % y == 0:
            return "impossible"
        else:
            # FOR EXAMPLE FOR 7/3 : 2 CYCLES ARE CONSUMED
            cycles = cycles+int(max(x, y)/min(x, y))
            x, y = max(x, y) % min(x, y), min(x, y)
    return str(cycles+max(x, y)-1)


def solution(x, y):
    m, f = int(x), int(y)

    generations = 0

    # as long as at least one is not 1
    while m != 1 and f != 1:
        if m % f == 0:
            return 'impossible'
        else:
            generations = generations + int(max(m, f) / min(m, f))
            m, f = max(m, f) % min(m, f), min(m, f)
    return str(generations + max(m, f) - 1)


if __name__ == '__main__':
    start = timer()
    # print(attempt1('12', '13'))
    print(solution('4578346587236589723465789324567', '63457632475863429578'))
    end = timer()
    print(f'execution laster {end - start} seconds')
