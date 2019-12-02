# Extension 
from __future__ import division 
import numpy as np


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





class Node:

	

	def __init__(self,value = None, Graph= None, deri = 0.0, index1 = None, index2 = None):

		if Graph== None:
			raise NotImplementError("Your Node is not Connected to any graph")

		self.value = value
		self.deri = deri
		#if the node is left multiplied by another node, then the nodeleft is just node itself
		self.nodeleft = index1
		self.noderight = index2
		self.Graph = Graph
		if self.Graph != None: self.ownindex = Graph.Nodeindex 
		#EveryTime we are creating a node, we put it into our graphs
		self.Graph.append(self)

		#Record whether it is a single node or a node which is combined by operation 
		self.operation = None

		

	@classmethod
	def CheckConstant(cls,x):
		'''
		Check if the node is a contant
		Input:
		x: A node or a constant 
		if constant

		'''
		if not isinstance(x, cls):
			ConstantNode = cls(value = x,Graph = Graph)
			ConstantNode.operation = "None"
			return ConstantNode
		else:
			return x


	def __add__(self,other):
		other = self.CheckConstant(other)
		NewNode = Node(
					value = self.value + other.value,
					Graph = self.Graph,
					index1 = self.ownindex,
					index2 = other.ownindex,
					)
		NewNode.operation = "add"
		return NewNode


	def __radd__(self,other):
		other = self.CheckConstant(other)
		NewNode = Node(
					value = self.value + other.value,
					Graph = self.Graph,
					index1 = other.ownindex,
					index2 = self.ownindex,
					)
		NewNode.operation = "add"
		return NewNode


	def __mul__(self,other):
		other = self.CheckConstant(other)
		NewNode = Node(
					value = self.value*other.value,
					Graph = self.Graph,
					#record the index of the 2 nodes which produce this combined node
					index1 = self.ownindex,
					index2 = other.ownindex
					)
		NewNode.operation = "mul"
		return NewNode


	def __rmul__(self,other):
		other = self.CheckConstant(other)
		NewNode = Node(
					value = self.value*other.value,
					Graph = self.Graph,
					#record the index of the 2 nodes which produce this combined node
					index1 = other.ownindex,
					index2 = self.ownindex
					)
		NewNode.operation = "mul"
		return NewNode




Graph = ComputationalGraph()
X = Node(value = 3, Graph = Graph)
Y = Node(value = 5, Graph = Graph)

Graph.ComputeValue()



from IPython import *
embed()

