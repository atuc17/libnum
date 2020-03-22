class Caesar(object):
	"""docstring for Caesar"""
	def __init__(self, key):
		self.key = key
	def encrypt(self, plaintext, isupper=0):
		ciphertext = ''
		if isupper: root = ord('A')
		else: root = ord('a')
		for p in plaintext:
			ciphertext += chr(((ord(p)-root+self.key) % 26 + root))
		return ciphertext
	def decrypt(self, ciphertext, isupper=0):
		plaintext = ''
		if isupper: root = ord('A')
		else: root = ord('a')
		for c in ciphertext:
			plaintext += chr(((ord(c)-root-self.key) % 26 + root))
		return plaintext
	def attack(self, ciphertext, isupper=0):
		for i in range(1, 26):
			plaintext = ''
			if isupper: root = ord('A')
			else: root = ord('a')
			for c in ciphertext:
				plaintext += chr(((ord(c)-root-i) % 26 + root))
			print(plaintext)
s = Caesar(3)
s.attack('khoor')