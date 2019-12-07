import numpy as np

class Jacobian:
    """Computes the Jacobian matrix for vector functions
        
    INPUTS
    =======
    A user defined vector function of any length
    
    RETURNS
    ========
    Returns the full Jacobian matrix as a numpy array
    
    EXAMPLES
    =========
    >>> X,Y = Multi_AutoDiff_Creator(X = 2, Y = 4).Vars
    >>> func = np.array([X+Y, 2*X*Y])
    >>> J = Jacobian(func)
    >>> print(J.value())
    [[1. 1.]
    [8. 4.]]   
    
    X = [2]
    Y = [4]
    VarValues = [X,Y]
    func = lambda Vars:3*Vars[0] + Vars[1]**2
    AD_Obj = AutoDiff_Evaluate(VarValues,func)
    
    X_ad = AD_Obj[0]
    Y_ad = AD_Obj[1]
    func = np.array([3*X + Y**2])
    J = Jacobian(func)
    print(J.value())
    """ 
    def __init__(self,vector_func):
        self.function = vector_func
        self.l = len(self.function)

    def value(self):
        Jacob=[]
        for i in range(self.l):
            Jacob.append(self.function[i].der)
        return np.array(Jacob)