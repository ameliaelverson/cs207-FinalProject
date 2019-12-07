# Extension 
from __future__ import division 
from Graph import ComputationalGraph
import numpy as np


class Node:

    def __init__(self,value = None, Graph= None, deri = 0.0, index1 = None, index2 = None):
        
        self.value = value
        self.deri = deri
        #if the node is left multiplied by another node, then the nodeleft is just node itself
        self.nodeleft = index1
        self.noderight = index2
        self.Graph = Graph
        if Graph == None:
            raise NotImplementError("Your Node is not Connected to any graph")
        else:
            self.ownindex = Graph.Nodeindex 
        #EveryTime we are creating a node, we put it into our graphs
        self.Graph.append(self)

        #Record whether it is a single node or a node which is combined by operation 
        self.operation = None

    def CheckConstant(self,x):
        '''
        Check if the node is a contant
        Input:
        x: A node or a constant 
        if constant

        '''
        if not isinstance(x, Node):
            ConstantNode = Node(value = x,Graph =self.Graph)
            ConstantNode.operation = "Const"
            return ConstantNode
        else:
            return x

    def __add__(self, other):
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

    def __sub__(self, other):
        other = self.CheckConstant(other)
        NewNode = Node(
                    value = self.value - other.value,
                    Graph = self.Graph,
                    index1 = self.ownindex,
                    index2 = other.ownindex,
                    )
        NewNode.operation = "sub"
        return NewNode

    def __rsub__(self, other):
        other = self.CheckConstant(other)
        NewNode = Node(
                    value = other.value - self.value,
                    Graph = self.Graph,
                    index1 = other.ownindex,
                    index2 = self.ownindex,
                    )
        NewNode.operation = "sub"
        return NewNode

    def __mul__(self, other):
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

    def __rmul__(self, other):
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

    def __rtruediv__(self, other):
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
        other = self.CheckConstant(other)
        NewNode = Node(
                    self.value**other.value,
                    Graph = self.Graph,
                    index1 = self.ownindex,
                    index2 = other.ownindex
                    )
        NewNode.operation = "pow"
        return NewNode

    def __neg__(self):
        return self * -1

    def __eq__(self, other):
        return self.Graph == other.Graph


def exp(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.exp(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "exp"
    return NewNode


def log(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.log(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "log"
    return NewNode


def sqrt(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.sqrt(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "sqrt"
    return NewNode


def sin(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.sin(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "sin"
    return NewNode


def cos(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.cos(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "cos"
    return NewNode


def tan(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.tan(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "tan"
    return NewNode


def asin(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.arcsin(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "asin"
    return NewNode


def acos(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.arccos(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "acos"
    return NewNode


def atan(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.arctan(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "atan"
    return NewNode


def sinh(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.sinh(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "sinh"
    return NewNode


def cosh(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.cosh(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "cosh"
    return NewNode


def tanh(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.tanh(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "tanh"
    return NewNode




