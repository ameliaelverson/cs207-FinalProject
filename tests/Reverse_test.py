import pytest
import math
import numpy as np
import autodiff32 as ad

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


def test_div():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=5, Graph=Graph)
    func = 1 / x + x/2
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (2.7, .46)

def test_revpower():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=2, Graph=Graph)
    func = 2 - 2**x
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert(func.value, x.deri) == (-2, -4*np.log(2))


def test_series():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=5, Graph=Graph)
    f = x ** 2
    C = np.array([[4, 2, 3]])
    D = 1
    Vals, Ders = Graph.SeriesValues(C, D, Graph)
    assert np.array_equal(Vals, [16, 4, 9]) and np.array_equal(Ders, [[8], [4], [6]])


def test_jacobian():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=3, Graph=Graph)
    y = ad.Node(value=5, Graph=Graph)
    z = ad.Node(value=1, Graph=Graph)
    f = np.array([-2*x, 2*y+z, 3*x+3*y+2*z])
    func = ad.ReverseVecFunc(f, x=x, y=y, z=z)
    val, jacobian = func.value(Graph)
    assert np.array_equal(val, [-6, 11, 26]) and np.array_equal(jacobian, [[-2, 0, 0], [0, 2, 1], [3, 3, 2]])


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
    assert np.array_equal(vals, [[3, 20], [9, 80]]) and np.array_equal(derivs, [[[3, 0], [0,20]], [[3, 0], [0, 40]]])


def test_exp():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=3, Graph=Graph)
    func = ad.expr(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (np.exp(3), np.exp(3))


def test_logsqrt():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=2, Graph=Graph)
    func = ad.sqrtr(ad.logr(x))
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (np.sqrt(np.log(2)), .25 * (1 / (np.sqrt(np.log(2)))))


def test_trig1():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=math.pi, Graph=Graph)
    func = ad.cosr(x) - ad.sinr(2*x) + ad.tanr(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert abs(func.value - (-1)) < .000001 and abs(x.deri - (-1)) < .000001


def test_trig2():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=0, Graph=Graph)
    func = ad.asinr(x) * ad.acosr(x**2) + 2*ad.atanr(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (0, 2+np.arccos(0))


def test_trig3():
    Graph = ad.ComputationalGraph()
    x = ad.Node(value=0, Graph=Graph)
    func = ad.sinhr(x) + ad.coshr(x) + ad.tanhr(x)
    Graph.ComputeValue()
    Graph.ComputeGradient()
    assert (func.value, x.deri) == (1, 2)



