def trim(arr, x=0):
	a = []
	for i in xrange(len(arr)):
		if arr[i] != x:
			a = arr[i:]
			break
	return a

class poly:
	def __init__(self, coefs=[], exponent=0, char="x"):
		self.char = char
		if type(coefs) in [int, float]:
			coefs = [coefs]
		self.coefs = coefs
		self.exponent = exponent

	def __str__(self):
		string = []
		for i in xrange(len(self.coefs)):
			term = ""
			coef = self.coefs[i]
			power = len(self.coefs) - 1 - i + self.exponent

			if coef % 1 == 0:
				coef = int(coef)
			if coef == 0:
				continue
			if coef == -1:
				term += "-"
			elif coef != 1:
				term += str(coef)

			if power == 0:
				if term == "" or term == "-":
					term += "1"
			else:
				term += self.char
				if power != 1:
					term += "^%d" % power

			string.append(term)
		if len(string) == 0:
			return "0"
		return " + ".join(string).replace("+ -", "- ")

	def parse(self, x):
		total = 0
		for i in xrange(len(self.coefs)):
			power = len(self.coefs) - 1 - i + self.exponent
			total += self.coefs[i] * x**power
		return total

	def clean(self):
		self.coefs = trim(self.coefs)
		if len(self.coefs) == 0:
			return self
		while self.coefs[len(self.coefs)-1] == 0:
			self.coefs.pop()
			self.exponent += 1
			if len(self.coefs) == 0:
				return self
		return self

	def __add__(self, other):
		if type(other) in [int, float]:
			other = poly(other)
		elif type(self) in [int, float]:
			self = poly(self)
		a, b = self, other
		diff = b.exponent - a.exponent
		if diff > 0:
			b.exponent = a.exponent
			b.coefs += diff * [0]
		else:
			a.exponent = b.exponent
			a.coefs += -diff * [0]

		diff = len(b.coefs) - len(a.coefs)
		if diff > 0:
			a.coefs = diff * [0] + a.coefs
		else:
			b.coefs = -diff * [0] + b.coefs

		coefs = []
		for i in xrange(len(a.coefs)):
			coefs.append(a.coefs[i] + b.coefs[i])

		return poly(coefs, a.exponent).clean()

	def __sub__(self, other):
		if type(other) in [int, float]:
			other = poly(other)
		elif type(self) in [int, float]:
			self = poly(self)
		a, b = self, other
		diff = b.exponent - a.exponent
		if diff > 0:
			b.exponent = a.exponent
			b.coefs += diff * [0]
		else:
			a.exponent = b.exponent
			a.coefs += -diff * [0]

		diff = len(b.coefs) - len(a.coefs)
		if diff > 0:
			a.coefs = diff * [0] + a.coefs
		else:
			b.coefs = -diff * [0] + b.coefs

		coefs = []
		for i in xrange(len(a.coefs)):
			coefs.append(a.coefs[i] - b.coefs[i])

		return poly(coefs, a.exponent).clean()

	def __mul__(self, other):
		if type(other) in [int, float]:
			other = poly(other)
		elif type(self) in [int, float]:
			self = poly(self)
		coefs = []
		for i in range(len(self.coefs)):
			for j in range(len(other.coefs)):
				try:
					coefs[i + j] += self.coefs[i] * other.coefs[j]
				except:
					coefs.append(self.coefs[i] * other.coefs[j])
		expo = self.exponent + other.exponent
		return poly(coefs, expo).clean()

	def __div__(self, other):
		if type(other) in [int, float]:
			other = poly(other)
		elif type(self) in [int, float]:
			self = poly(self)
		a, b = trim(self.coefs), trim(other.coefs)

		diff = other.exponent - self.exponent
		expo = 0
		if diff > 0:
			expo = self.exponent
			b += diff * [0]
		else:
			expo = other.exponent
			diff = -diff
			a += diff * [0]

		coefs = [0] * (len(a) - len(b) + 1)

		for i in xrange(len(a)):
			n = float(a[i]) / b[0]
			coefs[i] = n
			a[i] = 0

			for j in xrange(1, len(b)):
				a[i + j] -= n * b[j]

			if len(trim(a)) < len(trim(b)):
				break
		return poly(trim(coefs), diff).clean()

	def __mod__(self, other):
		if type(other) in [int, float]:
			other = poly(other)
		elif type(self) in [int, float]:
			self = poly(self)
		a, b, coefs = trim(self.coefs), trim(other.coefs), []

		diff = other.exponent - self.exponent
		expo = 0
		if diff > 0:
			expo = self.exponent
			b += diff * [0]
		else:
			expo = other.exponent
			diff = -diff
			a += diff * [0]

		for i in xrange(len(a)):
			n = float(a[i]) / b[0]
			coefs.append(n)
			a[i] = 0

			for j in xrange(1, len(b)):
				a[i + j] -= n * b[j]

			if len(trim(a)) < len(trim(b)):
				break
		return poly(trim(a), diff).clean()

	def differentiate(self):
		coefs = self.coefs
		for i in xrange(len(coefs)):
			power = len(coefs) - 1 - i + self.exponent
			coefs[i] *= power
		return poly(coefs, self.exponent-1)

	def integrate(self, x = 0, y = 5):
		coefs = self.coefs
		for i in xrange(len(coefs)):
			power = len(coefs) - 1 - i + self.exponent
			coefs[i] /= float(power + 1)
		c = y - poly(coefs, self.exponent+1).parse(x)

		expo = self.exponent + 1
		if expo > 0:
			coefs += expo * [0]
			expo = 0

		coefs[len(coefs) + expo - 1] += c

		return poly(coefs, expo).clean()

	@staticmethod
	def interpolate(*points):
		a = poly()
		for i in range(len(points)):
			temp = poly(1)
			for j in range(len(points)):
				if j == i:
					continue

				temp *= poly([1, -points[j][0]]) / (points[i][0] - points[j][0])
			a += temp * points[i][1]
		return a.clean()

	def get_roots(self):
		return 0

	def plot(self, against="y"):
		string = str(self)
		string.


## y = 1.9e-19x^12 + 2.6e-6x^11 - 0.0002x^10
## y=1.9e{-19}x^{12}+2.6e{-6}x^{11}-0.0002x^{10}