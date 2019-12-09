import pytest
import numpy as np
import autodiff32 as ad


def test_submulti():
    x = ad.AutoDiff(3)
    func = 1 + x*5 - 2*x
    assert (func.val, func.der, func.Jacobian()) == (10, 3, 3)


def test_addnegexp():
    x = ad.AutoDiff(5)
    func = -x + 2*x**2 + 2
    assert(func.val, func.der, func.Jacobian()) == (47, 19, 19)


def test_revpower():
    x = ad.AutoDiff(2)
    func = 2 - 2**x
    assert(func.val, func.der, func.Jacobian()) == (-2, -4*np.log(2), -4*np.log(2))


def test_powers():
    x = ad.AutoDiff(2)
    func = x**x
    assert(func.val, func.der, func.Jacobian()) == (4, 4*(np.log(2) + 1), 4*(np.log(2)+1))

def test_jacobian():
    x = ad.AutoDiff(5, np.array([1, 0]))
    y = ad.AutoDiff(3, np.array([0, 1]))
    func = 5*x + 3*y
    assert np.all(func.Jacobian() == [5, 3])


def test_multivar():
    x, y = ad.Multi_AutoDiff_Creator(x=2, y=3).Vars
    func = 5*x + 3*y
    assert np.all(func.Jacobian() == [5, 3])

def test_multivar_vector():
     X = [1,2,3]
     Y = [2,3,3]
     VarValues = [X, Y]
     func = lambda Vars:np.array([1*Vars[0] + 1*Vars[1],    # first function
                                  1*Vars[0] + 1*Vars[1]])   # second function
     Values, Derivatives = ad.MultiVarVector_AutoDiff_Evaluate(VarValues,func)
     assert Values[0][0] == 3
     assert Values[0][1] == 3
     assert Values[1][0] == 5 
     assert Values[1][1] == 5
     assert Values[2][0] == 6
     assert Values[2][1] == 6
     assert Derivatives[0][0][0] == 1
     assert Derivatives[0][0][0] == 1
     assert Derivatives[0][1][0] == 1
     assert Derivatives[0][1][1] == 1
     assert Derivatives[1][0][0] == 1
     assert Derivatives[1][0][0] == 1
     assert Derivatives[1][1][0] == 1
     assert Derivatives[1][1][1] == 1
     assert Derivatives[2][0][0] == 1
     assert Derivatives[2][0][0] == 1
     assert Derivatives[2][1][0] == 1
     assert Derivatives[2][1][1] == 1


def test_str():
    x = ad.AutoDiff(5)
    func = 1/x
    assert str(func) == "f(x) = 0.20, f'(x) = -0.04"


def test_eq():
    x = ad.AutoDiff(20, 1)
    func1 = x/2 - 25
    func2 = func1
    assert (func1.val, func1.der, func1.Jacobian()) == (func2.val, func2.der, func2.Jacobian())

def test_ne():
    x = ad.AutoDiff(20, 1)
    func1 = x/2 - 25
    func2 = x/3 - 25
    assert (func1.val, func1.der, func1.Jacobian()) != (func2.val, func2.der, func2.Jacobian())


