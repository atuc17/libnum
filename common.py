def gcd(a, b): # greatest common divisor of a and b
    while b:
        a, b = b, a % b
    return abs(a)
'''
def xgcd(a, b): # return gcd(a, b), x, y satisfy ax + by = gcd(a, b)
    a1, a2, a3 = 1, 0, a
    b1, b2, b3 = 0, 1, b
    r1, r2, r3 = 0, 0, 0
    while b3 != 0 and b3 != 1:
        q = a3 // b3
        r1 = a1 - q * b1
        r2 = a2 - q * b2
        r3 = a3 - q * b3
        a1, a2, a3 = b1, b2, b3
        b1, b2, b3 = r1, r2, r3
    if b3 == 0:
        return a3, a1, a2
    else:
        return b3, b1, b2
'''
def xgcd(a, b):
    u, g, x, y = 1, a, 0, b
    while y != 0:
        q = g // y
        t = g - q*y
        s = u - q*x
        u, g = x, y
        x, y = s, t
    v = (g - a*u) // b
    return g, u, v
    
def inverse(a, n):
    d, _, b = xgcd(a, n)
    if d == 1:
        return b % n
    return None
def nroot(a, n):
    high = 1
    while high ** n < a:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if mid ** n < a and mid > low:
            low = mid
        elif mid ** n > a and mid < high:
            high = mid
        else:
            return mid
    return mid + 1
#from http://python.6.x6.nabble.com/cube-root-tp1733498p1733529.html
def root3rd(x):
    y, y1 = None, 2
    while y != y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
        print(y, y1)
    return y
def iroot(a, n): # find integer x such that x^n <= a < (x+1)^n
    x = a
    y = (a + n - 1) // n
    # y = 2
    # Newton's method
    while y < x:
        x = y
        y = ((n-1) * x + a // (x ** (n-1))) // n
    return x

def powmod(g, A, N):
    a = g
    b = 1
    while A > 0:
        if A % 2 == 1:
            b = (b * a) % N
        a = (a * a) % N
        A = A // 2
    return b
