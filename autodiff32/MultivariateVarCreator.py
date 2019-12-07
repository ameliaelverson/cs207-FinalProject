import numpy as np
import autodiff32 as ad

class Multi_AutoDiff_Creator:
    
    #def __init__(self, *args, **kwargs):
    def __init__(self,Vals): #Now the user need to input values as a list with the first one specifying the first val for first val and so on

        """Instantiates multiple AutoDiff objects
        
        INPUTS
        =======
        User defined variables and assigned values 
        (for example, you might input all of the variables in a multivariate function)

        RETURNS
        ========
        Returns len(kwargs) number of AutoDiff class objects with an associated derivative (seed) as an np.array

        NOTE:
        ========
        This class acts as a helper function to allow the user to create multiple 
        AutoDiff objects conveniently (instead of manually creating each AutoDiff object) 
        
        These multiple AutoDiff objects may be useful in the evaluation of a multivariate function
        
        EXAMPLES
        =========
        >>> X,Y = Multi_AutoDiff_Creator(X = 2, Y = 4).Vars
        >>> X.val
        2
        >>> X.der
        array([1., 0.])
        >>> Y.val
        4
        >>> Y.der
        array([0., 1.])
        
        #UserDEMO
        X = [1,2,3]
        Y = [2,3,3]
        Z = [3,5,3]
        W = [3,5,3]
        VarValues = [X, Y, Z, W]
        func = lambda Vars:3*Vars[0] + 4*Vars[1] + 4*Vars[2]**2 + 3*Vars[3]# Var[0] is X, Var[1] is Y
        Values ,Derivatives = AutoDiff_Evaluate(VarValues,func)
        
        AD_Obj = AutoDiff_Evaluate(VarValues,func)

        
        """    
#        deri = np.identity(len(kwargs))
#        i = 0 
#        self.Vars =[]
#        for key, value in kwargs.items():
#            self.Vars.append(ad.AutoDiff(value,deri[i]))
#            i+=1

        deri = np.identity(len(Vals))
        self.Vars =[]
        for i in range(len(Vals)):
          self.Vars.append(ad.AutoDiff(Vals[i],deri[i]))          
        


def AutoDiff_Evaluate(Vals,f):
    #val = []
    #der = []
    AutoDiff_Objects = []
    for i in np.transpose(Vals):
        A = f(Multi_AutoDiff_Creator(i).Vars)
        AutoDiff_Objects.append(A)
        #der.append(A.der)
  
    return AutoDiff_Objects#val, der