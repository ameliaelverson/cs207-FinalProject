import numpy as np

class AutoDiff():
    """ Instantiates an AutoDiff object
    
    INPUTS
    =======
    A scalar value and a derivative
    The default derivative is 1
        
    RETURNS
    ========
    An AutoDiff Object
    
    NOTES
    =====
    The AutoDiff class overloads many basic operations and comparison operators
    This allows for operations and comparisons to be performed on/using the
    instantiated AutoDiff object
    
    EXAMPLES
    =========
    >>> X = AutoDiff(3)
    >>> X.val
    3
    >>> X.der
    1
    
    """    
    
    def __init__(self, val, der = 1):
        self.val = val
        self.der = der

    def __mul__(self, other): # overload multiplication
        try:
            	return AutoDiff(self.val * other.val, (self.val * other.der) + (self.der * other.val))
        except AttributeError:
        		return AutoDiff(self.val * other, self.der * other)


    def __rmul__(self, other): # overload reverse multiplication
        return self.__mul__(other)


    def __add__(self, other): # overload addition
        try:
            	return AutoDiff(self.val + other.val, self.der + other.der)
        except AttributeError:
        		return AutoDiff(self.val + other, self.der)


    def __radd__(self, other): # overload reverse addition
        return self.__add__(other)


    def __neg__(self): # overload negative numbers
        return -1 * self
    
    def __sub__(self, other): # overload subtraction
        try:
            	return AutoDiff(self.val - other.val, self.der - other.der)
        except AttributeError:
        		return AutoDiff(self.val - other, self.der)

    def __rsub__(self,other): # overload subtraction, ensures commutativity of subtraction
        try:
            	return AutoDiff(other.val - self.val, other.der - self.der)
        except AttributeError:
        		return AutoDiff(other - self.val, self.der * -1)

    def __pow__(self,other): # overload power
        try:
            return AutoDiff(self.val ** other.val, other.val * (self.val ** (other.val - 1.0)) * self.der + (self.val ** other.val) * np.log(self.val) * other.der)
        except AttributeError:
            return AutoDiff(self.val ** other, other * (self.val ** (other - 1.0)) * self.der)
    
    def __rpow__(self, other): # overload reverse power
        return AutoDiff(other ** self.val, other ** self.val * np.log(other) * self.der)
    
    def __truediv__(self,other): # overload true division
        return self * (other ** -1)
    
    def __rtruediv__(self,other): # overload reverse true division
        return other * (self ** -1)
    
    def __str__(self): # overload string
        	return "f(x) = {:.2f}, f'(x) = {:.2f}".format(self.val, self.der)

    def __eq__(self, other): # overload 'equal to' comparison operator
        try:
            return (self.val == other.val and self.der == other.der)
        except AttributeError:
            return self.val == other
            
    def __ne__(self, other): # overload 'not equal to' comparison operator
        return not self==other

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

   
