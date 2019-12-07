
from ReverseMode import Node
from Graph import ComputationalGraph
import numpy as np

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

