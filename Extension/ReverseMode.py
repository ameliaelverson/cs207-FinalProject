# Extension 

import numpy as np


class ComputationalGraph:

	def __init__(self):

		self.Nodeindex = 0 
		self.NodeList =[]

	def append(self, Node):
		self.Nodeindex +=1
		self.NodeList.append(Node)

	def ValidOp(self,i):  #Valid operation
		switcher ={
			1 :"add",
			2 : "mul",
			3 : "exp"
		}
		return  switcher.get(i," Invalid Operator")

	def ComputeValue(self):
		'''
		This function utilize forward pass to compute the value of the function


		'''
		for nodes in NodeList:
			if node.operation == ValidOp(1):
				node.value = self.NodeList[node.nodeleft].value + self.NodeList[node.noderight].value

			elif node.operation == ValidOp(2):
				node.value = self.NodeList[node.nodeleft].value*self.NodeList[node.noderight].value


	def ComputeGradient(self,lastIndex):
		'''
		This function back propagate to calculate the gradient of the variables

		'''
		#Set the seed 
		self.NodeList[lastIndex].deri = 1.0
		#Perform back prop
		for node in self.NodeList[-1::-1]:
			if node.operation == ValidOp(1):
				self.NodeList[node.nodeleft].deri += node.deri
				self.NodeList[node.nodeleft].deri += node.deri

			elif node.operation == ValidOp(2):
				self.NodeList[node.nodeleft].deri += node.deri * self.NodeList[node.noderight].value
				self.NodeList[node.noderight].deri += node.deri * self.NodeList[node.nodeleft].value





class Node:

	

	def __init__(self,value = None, deri = 0.0, index1 = None, index2 = None):
		self.value = value
		self.deri = deri
		#if the node is left multiplied by another node, then the nodeleft is just node itself
		self.nodeleft = index1
		self.noderight = index2
		self.Graph = Graph
		self.ownindex = Graph.Nodeindex if self.Graph != None
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

		'''
		if not isinstance(x, cls):
			return cls(value = x)
		else:
			return x


	def __add__(self,other):
		other = self.CheckConstant(other)
		NewNode = Node(
					value = self.value + other.value,
					index1 = self.ownindex,
					index2 = other.ownindex
					)
		NewNode.operation = "add"
		return NewNode


	def __mul__(self,other):
		other = self.CheckConstant(other)
		NewNode = Node(
					value = self.value*other.value,
					#record the index of the 2 nodes which produce this combined node
					index1 = self.ownindex,
					index2 = other.ownindex
					)
		NewNode.operation = "mul"
		return NewNode








