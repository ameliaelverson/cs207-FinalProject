import numpy as np
import autodiff32 as ad

class Multi_AutoDiff_Creator:

    def __init__(self,*args,**kwargs):
        """
        INPUTS
        =======
        The values of each variable in the multivariate function 
        Eg:

        Multi_AutoDiff_Creator(X = 2, Y = 4)

        RETURNS
        ========
        Return len(kwargs) number of AutoDiff class variables with derivative (seed) as an np.array


        NOTE:
        ========
        This class acts as a helper function for user to create multiple 
        AutoDiff Objects conveniently (instead of manually create many AutoDiff objects) to use in the evaluation of the multivariate function.


        """
           
        deri = np.identity(len(kwargs))
        i = 0 
        self.Vars =[]
        for key, value in kwargs.items():
            self.Vars.append(ad.AutoDiff(value,deri[i]))
            i+=1
            
        
