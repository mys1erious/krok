def lps_array(pattern):
    d = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = d[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        d[i] = j
    return d
def KMP_search(pattern, text):

    lpsPattern = lps_array(pattern)
    i = 0
    j = 0

    while i in range(len(text)):
        if pattern[j] == text[i]:
            j += 1
            i += 1
            if j == len(pattern):
                print(f'Pattern found at index: {i-j}')
                return(i-j)
        else:
            if j == 0:
                i += 1
            else:
                j = lpsPattern[j - 1]
    print('Pattern not found in text')


text = input("Text: ")
pat = input("Pattern: ")

#lpstest = lps_array(pat)
#print(lpstest)

check = KMP_search(pat, text)
print(check)

