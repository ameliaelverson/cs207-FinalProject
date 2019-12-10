# from __future__ import division 

import numpy as np
import autodiff32 as ad

class Multi_AutoDiff_Creator:

    def __init__(self,*args,**kwargs):
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
        
        """    
          
        deri = np.identity(len(kwargs))
        i = 0 
        self.Vars =[]
        for key, value in kwargs.items():
            self.Vars.append(ad.AutoDiff(value,deri[i]))
            i+=1

