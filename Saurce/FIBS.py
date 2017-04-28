class FIBS:
	def __init__(self,max = 10):
		self.a = 0
		self.b = 1
		self.max = max

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b, self.a + self.b
		if self.a > self.max:
			raise StopIteration
		return self.a
