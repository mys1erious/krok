with open('f.txt', 'r') as f:
    text_f = f.read()
with open('g.txt', 'r') as g:
    text_g = g.read()
with open('h.txt', 'w') as h:
    h.write(text_f+'\n'+text_g)