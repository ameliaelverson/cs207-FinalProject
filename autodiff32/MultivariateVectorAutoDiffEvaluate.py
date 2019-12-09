import numpy as np
import autodiff32 as ad       

def MultiVarVector_AutoDiff_Evaluate(Vals,f):
    
    """Autodifferentiate and evaluate a multivariate function at user defined vector input values
    
    INPUTS
    =======
    User defined multivariate vector inputs

    RETURNS
    ========
    Returns len(kwargs) number of AutoDiff class objects with an associated derivative (seed) as an np.array

    NOTE:
    ========
    This function uses a significantly different workflow than we suggest using for 
    multivariate functions evaluated at scalar inputs and 
    univariate functions evaluated at scalar or vector inputs
    
    This is due to the complexities of allowing for vector inputs to a multivariate function
    
    MultiVarVector_AutoDiff_Evaluate CAN also be used for other types of functions (univariate) 
    and other types of inputs (scalar), but we recommend using the workflow detailed in 'documents'
    for ease of use
        
    EXAMPLES
    =========

    # For a single multivariate function evaluated at vector value inputs
    >>> X = [1,2,3]
    >>> Y = [2,3,3]
    >>> Z = [3,5,3]
    >>> W = [3,5,3]
    >>> VarValues = [X, Y, Z, W]
    >>> func = lambda Vars:3*Vars[0] + 4*Vars[1] + 4*Vars[2]**2 + 3*Vars[3]     # Var[0] is X, Var[1] is Y
    >>> Values, Derivatives = MultiVarVector_AutoDiff_Evaluate(VarValues,func)
    >>> print(Values)
    [ 56 133  66] 
    >>> print(Derivatives)
    [[ 3.  4. 24.  3.]
    [ 3.  4. 40.  3.]
    [ 3.  4. 24.  3.]]
     
    # For multiple multivariate functions evaluated at vector value inputs
    >>> X = [1,2,3]
    >>> Y = [2,3,3]
    >>> Z = [3,5,3]
    >>> W = [3,5,3]
    >>> VarValues = [X, Y, Z, W]
    >>> func = lambda Vars:np.array([3*Vars[0] + 4*Vars[1] + 4*Vars[2]**2 + 3*Vars[3],    # first function
                                     5*Vars[0] + 6*Vars[1] + 7*Vars[2]**2 + 1*Vars[3]])   # second function
    >>> Values, Derivatives = MultiVarVector_AutoDiff_Evaluate(VarValues,func)
    >>> print(Values)
    [[ 56  83]
    [133 208]
    [ 66  99]]
    >>> print(Derivatives)
    [[[ 3.  4. 24.  3.]
    [ 5.  6. 42.  1.]]

    [[ 3.  4. 40.  3.]
    [ 5.  6. 70.  1.]]

    [[ 3.  4. 24.  3.]
    [ 5.  6. 42.  1.]]]
    
    """
          

    Values = []
    Ders = []
    for i in np.transpose(Vals):
        val = []
        der = []
        A = f(ad.Multi_Vector_AutoDiff_Creator(i).Vars)
        try:
            for j in A:
                val.append(j.val)
                der.append(j.der)
            Values.append(val)
            Ders.append(der)
        except:
            Values.append(A.val)
            Ders.append(A.der)
    
    return np.array(Values), np.array(Ders)


