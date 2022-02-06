n1 = frozenset('ab') | set('bc') == set('bc') | frozenset('ab')
print(n1) # True.

n2 = type(frozenset('ab')|set('bc')) == type(set('bc')|frozenset('ab'))
print(n2) # False.

n3 = {5} | {6} - {5}
print(n3) # {5, 6}

n4 = {5, 6} < {5, 6, 7} == {5, 6} in {5, 6, 7}
print(n4) # False.

n5 = 16/2**+4 in {i*i for i in range(5)}
print(n5) # True.