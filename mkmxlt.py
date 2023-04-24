import numpy as np


def read():
	S = []
	while True:
		try:
			S.append(input("> "))
		except EOFError:
			break
	print()
	return S


def parse(s: str):
	return list(map(float, s.split()))

def make_mx(S):
	a = []
	for s in S:
		a.append(parse(s))
	return np.array(a)


def calc_lambda(c):
	n = len(c)
	l = np.zeros((n, n))
	#print(l)
	for i in range(1, n):
		l[i][0] = float('inf')

	for k in range(1, n):
		for i in range(1, n):
			l[i][k] = np.min([l[j][k - 1] + c[j][i] for j in range(n)])
	return l
		

def cc(i):
	return "$\inf$" if i == float('inf') else str(i) + "\t"

def print_mx(a):
	n = len(a)
	m = max([len(a[i]) for i in range(n)])
	print("\\begin{pmatrix}")
	for i in range(n):
		print(cc(a[i][0]), end=" ")
		for j in range(1, len(a[i])):
			print("& ", cc(a[i][j]), end=" ")
		for j in range(m - len(a[i])):
			print("& 0", end=" ")
		if i < n - 1:
			print("\\\\")
		else:
			print()

	print("\\end{pmatrix}")


def print_table(r):
	n = len(r)
	for i in range(n):
		print("$V{}$".format(i + 1), end=" ")
		for j in r[i]:
			print("&", cc(j), end=" ")
		if i < n - 1:
			print("\\\\")

c = make_mx(read())
l = calc_lambda(c)

n = len(c)

r = np.zeros((n, 2*n))
for i in range(n):
	r[i] = np.concatenate((c[i], l[i]))

print_table(r)