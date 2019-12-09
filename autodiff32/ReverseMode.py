# Extension 
from __future__ import division 
from .Graph import ComputationalGraph
import numpy as np


class Node:

    def __init__(self,value = None, Graph= None, deri = 0.0, index1 = None, index2 = None):
        
        self.value = value
        self.deri = deri
        #if the node is left multiplied by another node, then the nodeleft is just node itself
        self.nodeleft = index1
        self.noderight = index2
        self.Graph = Graph
        if Graph is None:
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
        other = self.CheckConstant(other)
        NewNode= Node(
                self.value / other.value,
                Graph = self.Graph,
                index1 = self.ownindex,
                index2 = other.ownindex
                )
        NewNode.operation = "div"
        return NewNode

    def __rtruediv__(self, other):
        other = self.CheckConstant(other)
        NewNode =  Node(
                other.value / self.value,
                Graph = self.Graph,
                index1 = other.ownindex,
                index2 = self.ownindex
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

    def __rpow__(self, other):
        other = self.CheckConstant(other)
        NewNode = Node(other.value**self.value, Graph=self.Graph, index1=other.ownindex, index2=self.ownindex)
        NewNode.operation = "rpow"
        return NewNode

    def __neg__(self):
        return self * -1

    def __eq__(self, other):
        other = self.CheckConstant(other)
        return self.Graph == other.Graph and self.value == other.value and self.ownindex == other.ownindex


