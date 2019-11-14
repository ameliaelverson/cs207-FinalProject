#Testing File for AutoDiff and 
import numpy as np

class AutoDiff():
    
    def __init__(self,x,der = 1):
        self.val = x
        self.der = der


    def __mul__(self,other):
        X = AutoDiff(self.val)
        try:
            value = X.val
            X.val = other.val*value
            X.der = other.val*X.der*self.der + other.der*value
        except AttributeError:
            
            X.val= other*X.val
            X.der = other*X.der*self.der

        return X

    def __rmul__(self,other):
        return self.__mul__(other)


    def __radd__(self,other):
        X = AutoDiff(self.val)
        try:
            X.val= other.val + X.val
            X.der = X.der*self.der+other.der
        except AttributeError:
            X.val= other + X.val
            X.der = X.der*self.der

        return X


    def __add__(self,other):
        return self.__radd__(other)


    def __neg__(self): #overload negative numbers
        return -1*self
    
    def __sub__(self,other): #overload subtraction
        X = AutoDiff(self.val)
        try:
            X.val=  X.val- other.val
            X.der = X.der*self.der - other.der
        except AttributeError:
            X.val= X.val - other
            X.der = X.der*self.der

        return X

    def __rsub__(self,other): #ensure commutativity of subtraction
        X = AutoDiff(self.val)
        try:
            X.val=  other.val-X.val
            X.der = other.der- X.der*self.der 
        except AttributeError:
            X.val = other -X.val
            X.der = X.der*self.der

        return X



    def __pow__(self,other): # overload power
        try:
            return AutoDiff(self.val ** other.val, other.val * (self.val ** (other.val - 1.0)) * self.der + \
                            (self.val ** other.val) * np.log(self.val) * other.der)
        except AttributeError:
            other = AutoDiff(other)
            return AutoDiff(self.val ** other.val, other.val * (self.val ** (other.val - 1.0)) * self.der)
    
    def __rpow__(self, other): # overload rpower
        return AutoDiff(other ** self.val, other ** self.val * np.log(other) * self.der)
        # return AutoDiff(other ** self.val, other ** (self.val-1) * self.val * self.der)

    
    def __truediv__(self,other): #overload true division
        return self*(other**-1)
    
    def __rtruediv__(self,other): #overload rtrue division
        return other*(self**-1)
    
    def Jacobian(self):
        """
        INPUTS
        =======
        None
        
        RETURNS
        ========
        The Jacobian of the function.
        If the function is univariate, then the Jacobian is just the derivative

        If the function is multivariate, then the Jacobian will be an array.

        """
        return self.der

   
