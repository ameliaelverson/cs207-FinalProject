import numpy as np

class ComputationalGraph:

	def __init__(self):

		self.Nodeindex = 0 
		self.NodeList =[]

	def append(self, Node):
		'''
		This method append the node to the graph in sequence and record the index of that node

		INPUTS
		======

		Node: The Node that is to be appended on the List

		Return
		======
		None

		'''
		self.Nodeindex +=1
		self.NodeList.append(Node)



	def ValidOp(self,i):  #Valid operation
		'''

		INPUT
		=====
		i : The number corresponding to the operators 

		Return
		======
		The Value of the key in the swither


		NOTES
		======
		This method structurally defines a way to 
		store all the valid operators 
		supported by this reverse mode class 

		'''
		switcher ={
			1: "add",
			2: "mul",
			3: "neg",
			4: "div",
			5: "pow",
			6: "sub",
			7: "exp",
			8: "log",
			9: "sqrt",
			10: "sin",
			11: "cos",
			12: "tan",
			13: "asin",
			14: "acos",
			15: "atan",
			16: "sinh",
			17: "cosh",
			18: "tanh",
			19: "rpow"
		}
		return  switcher.get(i," Invalid Operator")

	def ComputeValue(self):
		'''
		This function utilize forward pass to compute the value of the function

		'''
		for node in self.NodeList:
			if node.operation == self.ValidOp(1):
				node.value = self.NodeList[node.nodeleft].value + self.NodeList[node.noderight].value

			elif node.operation == self.ValidOp(2):
				node.value = self.NodeList[node.nodeleft].value*self.NodeList[node.noderight].value

			elif node.operation == self.ValidOp(4):
				node.value = self.NodeList[node.nodeleft].value/self.NodeList[node.noderight].value

			elif node.operation == self.ValidOp(6):
				node.value = self.NodeList[node.nodeleft].value-self.NodeList[node.noderight].value

			elif node.operation == self.ValidOp(5):
				node.value = self.NodeList[node.nodeleft].value**self.NodeList[node.noderight].value

			elif node.operation == self.ValidOp(7):
				node.value = np.exp(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(8):
				node.value = np.log(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(9):
				node.value = np.sqrt(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(10):
				node.value = np.sin(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(11):
				node.value = np.cos(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(12):
				node.value = np.tan(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(13):
				node.value = np.arcsin(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(14):
				node.value = np.arccos(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(15):
				node.value = np.arctan(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(16):
				node.value = np.sinh(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(17):
				node.value = np.cosh(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(18):
				node.value = np.tanh(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(19):
				node.value = self.NodeList[node.nodeleft].value**self.NodeList[node.noderight].value




	def ComputeGradient(self,lastIndex = -1):
		'''
		This function back propagate to calculate the gradient of the variables with reverse mode

		INPUT 
		=====

		'''
		#Set the seed 
		self.clearGraph()
		self.NodeList[lastIndex].deri = 1.0
		#Perform back prop
		for node in self.NodeList[-1::-1]:
			if node.operation == self.ValidOp(1):
				self.NodeList[node.nodeleft].deri += node.deri
				self.NodeList[node.noderight].deri += node.deri

			if node.operation == self.ValidOp(6):
				self.NodeList[node.nodeleft].deri += node.deri
				self.NodeList[node.noderight].deri -= node.deri

			elif node.operation == self.ValidOp(2):
				self.NodeList[node.nodeleft].deri += node.deri * self.NodeList[node.noderight].value
				self.NodeList[node.noderight].deri += node.deri * self.NodeList[node.nodeleft].value

			elif node.operation == self.ValidOp(4):
				self.NodeList[node.nodeleft].deri += node.deri / self.NodeList[node.noderight].value
				self.NodeList[node.noderight].deri += -node.deri * self.NodeList[node.nodeleft].value/self.NodeList[node.noderight].value**2

			elif node.operation == self.ValidOp(5):
				self.NodeList[node.nodeleft].deri += node.deri*self.NodeList[node.noderight].value * self.NodeList[node.nodeleft].value **(self.NodeList[node.noderight].value-1)

			elif node.operation == self.ValidOp(7):
				self.NodeList[node.nodeleft].deri += node.deri*np.exp(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(8):
				self.NodeList[node.nodeleft].deri += node.deri / self.NodeList[node.nodeleft].value

			elif node.operation == self.ValidOp(9):
				self.NodeList[node.nodeleft].deri += node.deri/(2*np.sqrt(self.NodeList[node.nodeleft].value))

			elif node.operation == self.ValidOp(10):
				self.NodeList[node.nodeleft].deri += node.deri*np.cos(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(11):
				self.NodeList[node.nodeleft].deri += node.deri*-1*np.sin(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(12):
				self.NodeList[node.nodeleft].deri += node.deri/((np.cos(self.NodeList[node.nodeleft].value))**2)

			elif node.operation == self.ValidOp(13):
				self.NodeList[node.nodeleft].deri += node.deri/(np.sqrt(1 - self.NodeList[node.nodeleft].value ^ 2))

			elif node.operation == self.ValidOp(14):
				self.NodeList[node.nodeleft].deri += -node.deri/(np.sqrt(1 - self.NodeList[node.nodeleft].value ^ 2))

			elif node.operation == self.ValidOp(15):
				self.NodeList[node.nodeleft].deri += node.deri/(1 + self.NodeList[node.nodeleft].value ^ 2)

			elif node.operation == self.ValidOp(16):
				self.NodeList[node.nodeleft].deri += node.deri*np.cosh(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(17):
				self.NodeList[node.nodeleft].deri += node.deri*np.sinh(self.NodeList[node.nodeleft].value)

			elif node.operation == self.ValidOp(18):
				self.NodeList[node.nodeleft].deri += node.deri / ((np.cosh(self.NodeList[node.nodeleft].value)) ** 2)

			elif node.operation == self.ValidOp(19):
				self.NodeList[node.noderight].deri += node.deri * (self.NodeList[node.nodeleft].value ** self.NodeList[node.noderight].value) * np.log(self.NodeList[node.noderight].value)


	def clearGraph(self):
		'''
		In order to reuse the node for different functions, 
		we clear the graph by reassign the derivatives for all node to zero
		'''
		for i in self.NodeList:
			i.deri = 0 


	def WIPER(self,D):
		for i in self.NodeList[D:]:
			if i.operation != "Const":
				i.deri = 0
				i.value = 0

	def SeriesValues(self,C,D, Graph):
		ValList = []
		DerList = []
		C = C.T
		for j in range(len(C)):
			self.WIPER(D)
			for i in range(0, D):
				self.NodeList[i].value = C[j][i]
			Graph.ComputeValue()
			Graph.ComputeGradient()
			ValList.append(self.NodeList[-1].value)
			Deri = []
			for i in range(0, D):
				Deri.append(self.NodeList[i].deri)
			DerList.append(Deri)
		return ValList, DerList


