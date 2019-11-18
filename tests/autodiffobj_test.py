import pytest
import numpy as np
import autodiff32 as ad


def test_submulti():
    x = ad.AutoDiff(3)
    func = x*5 - 2*x
    assert (func.val, func.der, func.Jacobian()) == (9, 3, 3)


def test_addnegexp():
    x = ad.AutoDiff(5)
    func = -x + 2*x**2
    assert(func.val, func.der, func.Jacobian()) == (45, 19, 19)


def test_revpower():
    x = ad.AutoDiff(2)
    func = 2**x
    assert(func.val, func.der, func.Jacobian()) == (4, 4*np.log(2), 4*np.log(2))


def test_jacobian():
    x = ad.AutoDiff(5, np.array([1, 0]))
    y = ad.AutoDiff(3, np.array([0, 1]))
    func = 5*x + 3*y
    assert np.all(func.Jacobian() == [5, 3])


def test_multivar():
    x, y = ad.Multi_AutoDiff_Creator(x=2, y=3).Vars
    func = 5*x + 3*y
    assert np.all(func.Jacobian() == [5, 3])

def test_badinput():
    with pytest.raises():
        ad.AutoDiff("abc")



