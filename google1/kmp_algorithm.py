def naive_pattern_matching(string, substring):
    patterns_found = 0
    n = len(string)
    m = len(substring)
    for i in range(n - m + 1):
        j = 0

        while j < m:
            if string[i+j] != substring[j]:
                break
            j += 1
        if j == m:
            print(f"pattern found and index {i}")
            patterns_found += 1
    return patterns_found


def nadji_tokene(word, j):
    x = word[len(word) - j - 1:len(word)]
    lista = list()
    lista = word.split(x)
    y = lista[0]
    for i in lista:
        if (i == ''):
            continue
        if (y != i):
            print("NO")
            nadji_tokene(word, j + 1)
            return
    y += x
    print(y)


def kmp_search(pattern, text):
    pass



if __name__ == '__main__':
    text = "GEEKGEEK"
    pattern = 'GEEK'
    found_patterns = naive_pattern_matching(text, pattern)

    max_patterns = len(text) / len(pattern)
    print(f'max patterns -> {max_patterns}')
    print(f'i have found {found_patterns} patterns')
    if max_patterns == found_patterns:
        print('solved')

    print()

    nadji_tokene('abababababaab', 1)
