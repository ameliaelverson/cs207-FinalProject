import pytest
import math
import numpy as np
import Extension as ad

def test_submulti():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=3, Graph=Graph)
    y = ad.Node(value=2, Graph=Graph)
    func = 1 + x*5 - 2*y
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert(func.value, x.deri, y.deri) == (12, 5, -2)


def test_addnegexp():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=5, Graph=Graph)
    func = -x + 2*x**2 + 2
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert(func.value, x.deri) == (47, 19)


def test_revpower():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=2, Graph=Graph)
    func = 2 - 2**x
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert(func.value, x.deri) == (-2, -4*np.log(2))


def test_powers():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=2, Graph=Graph)
    func = x**x
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert(func.val, x.deri) == (4, 4*(np.log(2)+1))


#def test_series():
 #   Graph=ad.ComputationalGraph()

  #  C = [[1, 2, 3], [2, 3, 3], [3, 5, 1]]
   # D = 3
    #Vals, Ders = Graph.SeriesValues(C, D)


def test_jacobian():
    Graph = ad.ComputationGraph()
    x = ad.Node(value=3, Graph=Graph)
    y = ad.Node(value=5, Graph=Graph)
    z = ad.Node(value=1, Graph=Graph)
    f = np.array([-2*x, 2*y+z, 3*x+3*y+2*z])
    func = ad.ReverseVecFunc(f, x, y, z)
    val, jacobian = func.value(Graph)
    assert(val, jacobian) == ([-6, 11, 26], [[-2, 0, 0], [0, 2, 1], [3, 3, 2]])


def test_jacobian_series():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=3, Graph=Graph)
    y = ad.Node(value=4, Graph=Graph)
    X = [1, 3]
    Y = [2, 4]
    C = np.array([X, Y])
    D = 2  # Dimension
    f = np.array([x * 3, 5 * y ** 2])
    func = ad.ReverseVecFunc(f, x=x, y=y)
    vals, derivs = func.Seriesvalue(C, D, Graph)
    assert (vals, derivs) == ([[3, 20], [9, 80]], [[[3, 0], [3, 0]], [0, 20], [0, 40]])

def test_exp():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=3, Graph=Graph)
    func = ad.exp(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (np.exp(3), np.exp(3))

def test_logsqrt():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=2, Graph=Graph)
    func = ad.sqrt(ad.log(x))
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (np.sqrt(np.log(2)), .25 * (1 / (np.sqrt(np.log(2)))))


def test_trig1():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=math.pi, Graph=Graph)
    func = ad.cos(x) - ad.sin(2*x) + ad.tan(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (-1, -1)


def test_trig2():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=0, Graph=Graph)
    func = ad.asin(x) * ad.acos(x**2) + 2*ad.atan()
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (0, 2+2*np.arccos(0))


def test_trig3():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=0, Graph=Graph)
    func = ad.sinh(x) + ad.cosh(x) + ad.tanh(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (1, 2)


#Graph = ad.ComputationalGraph()
#x = ad.Node(value=1, Graph=Graph)
#f = x**2
#C = [4, 2, 3]
#D = 3
#Vals, Ders = Graph.SeriesValues(C=C, D=D, Graph=Graph)
#print(Vals)