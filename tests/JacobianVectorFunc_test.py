
import pytest
import numpy as np
import autodiff32 as ad


def test_vectorfuncJacobian():
    x, y = ad.Multi_AutoDiff_Creator(x=2, y=3).Vars
    func = np.array([x+y, 2*x*y])
    Jacob = ad.Jacobian(func)
    assert np.all(Jacob.value() == np.array([[1.,1.],[6.,4.]]))
