def naive_str_search(text, pattern):

    i = -1
    j = 0
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
    if (j == len(pattern)):
        return i

text = input("Text: ")
pat = input("Pattern: ")

ans = naive_str_search(text, pat)
print('Index', ans)