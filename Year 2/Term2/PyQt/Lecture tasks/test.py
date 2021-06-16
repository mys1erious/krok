def mult(n1, n2):
	l1 = len(n1)
	l2 = len(n2)

	ans = []
	add = []
	for j in range(l2-1, -1, -1):
		tmp = []
		for i in range(l1-1, -1, -1):
			tmp.append(n1[i] * n2[j])
		add.append(tmp)
	return add


def add(a, b):



def mult2(n1, n2):
	l1 = len(n1)
	l2 = len(n2)

	ans = []
	add = []

	for j in range(l2-1, -1, -1):
		if n2[j] == 1:
			add.append(n1.copy())
			n1.append(0)
		else:
			n1.append(0)

	for i in range(len(add)):
		for j in range(add[len(add)-1]):


	return add

n1 = [1, 0, 0, 1]
n2 = [0, 1, 0, 1]
s = mult2(n1, n2)

print(s)
