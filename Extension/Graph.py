

class ComputationalGraph:

	def __init__(self):

		self.Nodeindex = 0 
		self.NodeList =[]

	def append(self, Node):
		'''This method append the node to the graph in sequence and record the index of that node'''
		self.Nodeindex +=1
		self.NodeList.append(Node)

	def ValidOp(self,i):  #Valid operation
		'''
		This method structurally defines a way to 
		store all the valid operators 
		supported by this reverse mode class 

		'''
		switcher ={
			1 : "add",
			2 : "mul",
			3 : "exp",
			4 : "truediv",
			5 : "pow"
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


	def ComputeGradient(self,lastIndex):
		'''
		This function back propagate to calculate the gradient of the variables with reverse mode

		'''
		#Set the seed 
		self.clearGraph()
		self.NodeList[lastIndex].deri = 1.0
		#Perform back prop
		for node in self.NodeList[-1::-1]:
			if node.operation == self.ValidOp(1):
				self.NodeList[node.nodeleft].deri += node.deri
				self.NodeList[node.noderight].deri += node.deri

			elif node.operation == self.ValidOp(2):
				self.NodeList[node.nodeleft].deri += node.deri * self.NodeList[node.noderight].value
				self.NodeList[node.noderight].deri += node.deri * self.NodeList[node.nodeleft].value

	def clearGraph(self):
		'''
		In order to reuse the node for different functions, 
		we clear the graph by reassign the derivatives for all node to zero
		'''
		for i in self.NodeList:
			i.deri = 0 



