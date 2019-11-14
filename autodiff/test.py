import numpy as np
from Elementary import *
from AutoDiffObj import AutoDiff

# Demo  for single input function
# (checked answers using wolframalpha.com)
X = AutoDiff(3)


# # testing division
# print("\ntesting division:")
# func = 1/X**2
# print("value of function:",func.val)
# print("derivative with respect to X: ",func.der)
# print("Jacobian:", func.Jacobian())

# # testing exponents
# print("\ntesting exponents:")
# func = X**2
# print("value of function:",func.val)
# print("derivative with respect to X: ",func.der)
# print("Jacobian:", func.Jacobian())



# # testing exponents
# print("\ntesting exponents:")
# func = 2**(X**2)
# print("value of function:",func.val)
# print("derivative with respect to X: ",func.der)
# print("Jacobian:", func.Jacobian())


# testing exp
print("\ntesting exp:")
func = exp(X**2)
print("value of function:",func.val)
print("derivative with respect to X: ",func.der)
print("Jacobian:", func.Jacobian())

# testing sin
print("\ntesting sin:")
func = sin(X**2 + 1)
print("value of function:",func.val)
print("derivative with respect to X: ",func.der)
print("Jacobian:", func.Jacobian())

# testing something complicated
print("\ntesting something complicated:")
func = exp(sin(X**2 + X))
print("value of function:",func.val)
print("derivative with respect to X: ",func.der)
print("Jacobian:", func.Jacobian())