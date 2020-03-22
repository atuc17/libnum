from common import *
class RSA(object):
	"""docstring for RSA"""
	def __init__(self, p, q, e):
		self.p = p
		self.q = q
		self.e = e
		self.n = p * q
	def encrypt(self, plaintext):
		return pow(plaintext, self.e, self.n)
	def decrypt(self, ciphertext):
		phi = (self.p - 1) * (self.q - 1)
		if gcd(self.e, phi) != 1:
			print("Cannot decrypt!")
			return None
		d = inverse(self.e, phi)
		return pow(ciphertext, d, self.n)

