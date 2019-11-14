import numpy as np
import AutoDiffObj
import math

# Implementing elemental functions
def exp(x):
    try:
        return AutoDiffObj.AutoDiff(np.exp(x.val), np.dot(np.exp(x.val),x.der))
    except Exception:
    	return np.exp(x)

def log(x):
    try:
        return AutoDiffObj.AutoDiff(np.log(x.val), (1/x.val) * x.der)
    except Exception:
    	return np.log(x)
    
def sqrt(x):
    try:
        return AutoDiffObj.AutoDiff(np.sqrt(x.val), x.der * 1/(2*np.sqrt(x.val)))
    except Exception:
    	return x**0.5
    
def sin(x):
    try:
        return AutoDiffObj.AutoDiff(np.sin(x.val), np.cos(x.val) * x.der)
    except Exception:
    	return np.sin(x)
    
def cos(x):
    try:
        return AutoDiffObj.AutoDiff(cos(x.val), -sin(x.val) * x.der)
    except Exception:
    	return np.cos(x)
       
def tan(x):
    try:
        return AutoDiff(tan(x.val), 1/(cos(x.val) ** 2) * x.der)
    except Exception:
    	return np.tan(x)
    
def asin(x):
    try:
        return AutoDiffObj.AutoDiff(asin(x.val), (1/np.sqrt(1 - x.val**2)) * x.der)
    except Exception:
    	return np.asin(x)
    
def acos(x):
    try:
        return AutoDiffObj.AutoDiff(acos(x.val), (-1/np.sqrt(1 - x.val ** 2)) * x.der)
    except Exception:
    	pass
    
def atan(x):
    try:
        return AutoDiffObj.AutoDiff(atan(x.val), (1/(1 + x.val ** 2)) * x.der)
    except Exception:
    	return np.atan(x)