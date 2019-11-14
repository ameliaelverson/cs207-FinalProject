class Jacobian:
	def __init__(self,vector_func):
		self.function = vector_func
		self.l = len(self.function)

	def value(self):
		Jacob=[]
		for i in range(self.l):
			Jacob.append(self.function[i].der)
		return np.array(Jacob)