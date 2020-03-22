import common
def solve_crt(t, n):
    N = 1
    x = 0
    for i in n:
        N *= i
    for i in range(len(n)):
        Ni = N // n[i]
        Ni_inv = common.inverse(Ni, n[i])
        x = x + (t[i] * Ni * Ni_inv)
    return x
def legendre_symbol(a, p):
	ls = pow(a, (p-1)//2, p)
	if ls == p-1: 
		return -1
	return 1
def modular_sqrt(a, p):
	if legendre_symbol(a, p) == -1:
		return 0
	elif a == 0:
		return 0
	elif p == 2:
		return 0
	elif p % 4 == 3:
		return pow(a, (p+1)//4, p)
	u = p-1
	s = 0
	while u % 2 == 0:
		u = u // 2
		s += 1
	z = 2
	while legendre_symbol(z, p) != -1:
		z += 1
	c = pow(z, u, p)
	t = pow(a, u, p)
	r = pow(a, (u+1) // 2, p)
	while True:
		y = t
		i = 0
		for i in range(s):
			if y == 1:
				break
			y = pow(y, 2, p)
		if i == 0:
			return r
		b = pow(c, 2**(s-i-1), p)
		s = i
		c = (b*b) % p
		t = (t*b*b) % p
		r = (r*b) % p
def jacobi_symbol(n, k):
	assert (k > 0 and k % 2 == 1)
	n = n % k
	t = 1
	while n != 0:
		while n % 2 == 0:
			n = n // 2
			r = k % 8
			if r == 3 or r == 5:
				t = -t
		n, k = k, n
		if n % 4 == 3 and k % 4 == 3:
			t = -t
		n = n % k
	if k == 1:
		return t
	else:
		return 0
