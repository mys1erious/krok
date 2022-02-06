def bad_char(text, pattern):

    n = len(text)
    m = len(pattern)
    d = [m] * (ord(max(max(text), max(pattern))) + 1)

    for i in range(m - 1):
        d[ord(pattern[i])] = m - i - 1
    return d
def BMH_search(text, pattern):

    n = len(text)
    m = len(pattern)
    badChar = bad_char(text, pattern)
    pos = -1
    i = 0

    while n - i >= m and pos == -1:
        j = m - 1
        while text[i + j] == pattern[j]:
            if j == 0:
                pos = i
                break
            j -= 1
        i += badChar[ord(text[i + m - 1])]
    if pos != -1:
        return pos
    print('Элемент не найден.')


text = input("Text: ")
pat = input("Pattern: ")
x = BMH_search(text, pat)

print('Index', x)