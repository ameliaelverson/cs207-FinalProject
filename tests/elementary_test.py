import pytest
import numpy as np
import autodiff32 as ad

def test_exp():
    x = ad.AutoDiff(3)
    func = ad.exp(x)
    assert(func.val, func.der, func.Jacobian()) == (np.exp(3), np.exp(3), np.exp(3))


def test_logsqrt():
    x = ad.AutoDiff(2)
    func = ad.sqrt(ad.log(x))
    assert(func.val, func.der, func.Jacobian()) == (np.sqrt(np.log(2)), .25 * (1/(np.sqrt(np.log(2)))), .25 * (1/(np.sqrt(np.log(2)))))


def test_trig1():
    x = ad.AutoDiff(4)
    func = ad.cos(x) - 1
    assert(func.val, func.der, func.Jacobian()) == (np.cos(4)-1, -np.sin(4), -np.sin(4))


def test_trig2():
    x = ad.AutoDiff(2)
    func = ad.sin(x) + 2*ad.cosh(x) + 3 * ad.atan(x**2)
    assert(func.val, func.der, func.Jacobian()) == (np.sin(2) + 2 * np.cosh(2) + 3 * np.arctan(4), np.cos(2) + 2 * np.sinh(2) + 12/17, np.cos(2) + 2 * np.sinh(2) + 12/17)


def test_npexp():
    x = ad.AutoDiff(3)
    func = ad.exp(4)*x
    assert(func.val, func.der, func.Jacobian()) == (np.exp(4)*3, np.exp(4),np.exp(4))


def test_nplog():
    x = ad.AutoDiff(3)
    func = ad.log(4)*x
    assert(func.val, func.der, func.Jacobian()) == (np.log(4)*3, np.log(4),np.log(4))

def test_npsqrt():
    x = ad.AutoDiff(3)
    func = ad.sqrt(4)*x
    assert(func.val, func.der, func.Jacobian()) == (np.sqrt(4)*3, np.sqrt(4),np.sqrt(4))


def test_npcosh():
    x = ad.AutoDiff(3)
    func = ad.cosh(4)*x
    assert(func.val, func.der, func.Jacobian()) == (np.cosh(4)*3, np.cosh(4),np.cosh(4))



def test_sinh():
	x = ad.AutoDiff(3)
	func = ad.sinh(x) + ad.sinh(4)
	assert(func.val, func.der, func.Jacobian()) == (np.sinh(3)+np.sinh(4) , np.cosh(3),np.cosh(3))



def test_tan():
	x = ad.AutoDiff(3)
	func = ad.tan(x) + ad.tan(4)
	assert(func.val, func.der, func.Jacobian()) == (np.tan(3)+np.tan(4) ,1/np.cos(3)**2,1/np.cos(3)**2)
