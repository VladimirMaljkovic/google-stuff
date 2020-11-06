def find_longest_prefix_suffix_array(string, m, lps):
    length = 0  # previous best
    i = 1
    lps[0] = 0  # LPS[0] is always 0

    while i < m:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1


def does_it_repeat(string):
    n = len(string)

    lps = [0] * n  # array of n zeros

    # preprocessing the pattern
    find_longest_prefix_suffix_array(string, n, lps)

    length = lps[n-1]
    print(f'lps: {lps}')
    if n == 1:
        print('only 1 slice')
        return True
    if length > 0 and n % (n - length) == 0:
        print_my_substring(string, lps)
        return True
    else:
        return False


def print_my_substring(string, lps):
    for i in range(int(len(string)/2)-1, -1, -1):
        if lps[i] == 0:
            print(f'found last zero at index {i}')
            print(f'my string is {string[0:i+1]}')
            print(f'my substring appeared {int(len(string) / (i+1))} times')
            return


def solution_for_google(string):
    n = len(string)
    if n == 1:
        return 1
    lps = [0] * n  # array of n zeros

    # preprocessing the pattern
    find_longest_prefix_suffix_array(string, n, lps)

    length = lps[n-1]
    # print(f'lps: {lps}')
    if length > 0 and n % (n - length) == 0:
        for i in range(int(n/2) - 1, -1, -1):
            if lps[i] == 0:
                return int(n / (i+1))
    else:
        return 1


if __name__ == '__main__':
    if not does_it_repeat("abcabcabcabc"):
        print('no repeating sequence, only 1 slice')
