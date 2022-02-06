def wagner_fischer(text, pattern):

    n, m = len(text), len(pattern)

    if n > m:
        text, pattern = pattern, text
        n, m = m, n

    current = range(n + 1)

    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous[j] + 1, current[j-1] + 1, previous[j-1]

            if text[j-1] != pattern[i-1]:
              change += 1
            current[j] = min(add, delete, change)
    print('Levenshtein distance is: ', current[n])
    return current[n]

text = input('Text = ')
pattern = input('Pattern = ')

ans = wagner_fischer(text, pattern)