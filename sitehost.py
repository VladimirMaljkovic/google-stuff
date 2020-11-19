def foo():
    for x in range(1, 101):
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


if __name__ == '__main__':
    foo()