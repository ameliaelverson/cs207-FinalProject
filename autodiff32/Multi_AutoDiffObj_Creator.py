import numpy as np
import autodiff32 as ad

class Multi_AutoDiffObj_Creator:
    
    def __init__(self,Vals): 

        """Instantiates multiple AutoDiff objects (for use in multivariate functions)
        
        INPUTS
        =======
        User defined variables and assigned values 
        (for example, you might input all of the variables in a multivariate function)

        RETURNS
        ========
        Returns len(kwargs) number of AutoDiff class objects with an associated derivative (seed) as an np.array

        NOTE:
        ========
        This class acts as a helper function to create multiple AutoDiff objects conveniently
        These multiple AutoDiff objects may be useful in the evaluation of a multivariate function

        """    
        
        deri = np.identity(len(Vals))
        self.Vars =[]
        for i in range(len(Vals)):
          self.Vars.append(ad.AutoDiff(Vals[i],deri[i]))          
         