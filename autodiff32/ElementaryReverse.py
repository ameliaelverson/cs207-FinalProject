
from ReverseMode import Node
from Graph import ComputationalGraph
import numpy as np

def expr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.exp(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "exp"
    return NewNode


def logr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.log(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "log"
    return NewNode


def sqrtr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.sqrt(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "sqrt"
    return NewNode


def sinr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.sin(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "sin"
    return NewNode


def cosr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.cos(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "cos"
    return NewNode


def tanr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.tan(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "tan"
    return NewNode


def asinr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.arcsin(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "asin"
    return NewNode


def acosr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.arccos(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "acos"
    return NewNode


def atanr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.arctan(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "atan"
    return NewNode


def sinhr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.sinh(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "sinh"
    return NewNode


def coshr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.cosh(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "cosh"
    return NewNode


def tanhr(x):
    x = Node.CheckConstant(x, x)
    NewNode = Node(np.tanh(x.value), x.Graph, index1=x.ownindex, index2=None)
    NewNode.operation = "tanh"
    return NewNode

