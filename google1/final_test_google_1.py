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


def solution(string):
    n = len(string)
    lps = [0] * n  # array of n zeros

    # preprocessing the pattern
    find_longest_prefix_suffix_array(string, n, lps)

    length = lps[n-1]
    # print(f'lps: {lps}')
    if length > 0 and n % (n - length) == 0:
        for i in range(int(len(string)/2), 1, -1):
            if lps[i] == 0:
                return int(len(string) / (i+1))
    else:
        return -1

print(solution('aaabaacaaabaac'))