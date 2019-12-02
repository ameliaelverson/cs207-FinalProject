# Extension 
from __future__ import division 
from Graph import ComputationalGraph
import numpy as np


class Node:

    def __init__(self,value = None, Graph= None, deri = 0.0, index1 = None, index2 = None):

        if Graph == None:
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
            ConstantNode.operation = "Const"
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
        return self.__add__(other)


    def __sub__(self,other):
        other = self.CheckConstant(other)
        NewNode = Node(
                    value = self.value - other.value,
                    Graph = self.Graph,
                    index1 = self.ownindex,
                    index2 = other.ownindex,
                    )
        NewNode.operation = "sub"
        return NewNode

    def __rsub__(self,other):
        other = self.CheckConstant(other)
        NewNode = Node(
                    value = other.value - self.value,
                    Graph = self.Graph,
                    index1 = other.ownindex,
                    index2 = self.ownindex,
                    )
        NewNode.operation = "sub"
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
        return self.__mul__(other)


    def __truediv__(self, other):
        other = Node.CheckConstant(other)
        NewNode= Node(
                self.value / other.value,
                Graph = self.Graph,
                index1 = self.ownindex,
                index2 = other.ownindex
                )
        NewNode.operation = "div"
        return NewNode


    def __rtruediv__(self,other):
        other = Node.CheckConstant(other)
        NewNode =  Node(
                self.value / other.value,
                Graph = self.Graph,
                index1 = other.ownindex,
                index2 = own.ownindex
                )
        NewNode.operation = "div"
        return NewNode


    def __pow__(self,other):
        other = Node.CheckConstant(other)
        NewNode = Node(
                    self.value**other.value,
                    Graph = self.Graph,
                    index1 = self.ownindex,
                    index2 = other.ownindex
                    )
        NewNode.operation = "pow"
        Return NewNode





Graph = ComputationalGraph()
X = Node(value = 3, Graph = Graph)
Y = Node(value = 5, Graph = Graph)

#DEMO FOR Univariate Scalar Function
F = 2*X + 3
Graph.ComputeValue()
Graph.ComputeGradient(-1)
print("The Value of the Function is",F.value)
print("Derivative of X is:",X.deri)
print("Derivative of Y is:",Y.deri)

print("\n")
#DEMO FOR Multivariate Scalar Function
G = 2*X*Y + 3*Y
Graph.ComputeValue()
Graph.ComputeGradient(-1)
print("The Value of the Function is",G.value)
print("Derivative of X is:",X.deri)
print("Derivative of Y is:",Y.deri)




from IPython import *
embed()

