text= 'GCTTCTGCTACCTTTTGCGCGCGCGCGGAA'
#      0123456789?!!!!?!!!!?!!!!?!!!!?!!!!?!!!!?
pat = 'CCTTTTGC'
#      012345678

i = 0

# Only with (bad char rule) for now.

while i <= (len(text)-len(pat)):
    j = len(pat)-1
    t = ''
    while j >= 0 and pat[j] == text[i+j]:
        t+=pat[j]
        j -= 1
    if j < 0:
        print("Index found at", i)
        break
    else:
        if text[i+j] not in pat:
            i += j+1
        else:
            k = j
            while k >= 0:
                if text[i+j] != pat[k-1]:
                    k -= 1
                else:
                    i += j-k+1
                    break
print(t)

# text = 'there would have been a time for such a word'
# pat = 'word'
#
# text= 'GCTTCTGCTACCTTTTGCGCGCGCGCGGAA'
# pat = 'CCTTTTGC'
#
# text= 'CGTGCCTACTTACTTACTTACTTACGCGAA'
# pat = 'CTTACTTAC'