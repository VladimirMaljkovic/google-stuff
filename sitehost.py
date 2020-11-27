from timeit import default_timer as timer


def foo():
    for x in range(1, 1001):
        if x % 15 == 0:
            print('SiteHost')
            continue
        elif x % 3 == 0:
            print('Site')
            continue
        elif x % 5 == 0:
            print('Host')
            continue
        else:
            print(x)


def foo2():
    [print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i) for i in range(1, 1001)]


if __name__ == '__main__':
    start1 = timer()
    foo()
    end1 = timer()
    print()
    print()

    start2 = timer()
    foo2()
    end2 = timer()
    print(f'foo lasted {end1-start1}')
    print(f'foo2 lasted {end2-start2}')