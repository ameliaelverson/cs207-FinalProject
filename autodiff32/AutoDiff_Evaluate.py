import numpy as np
import autodiff32 as ad       

def AutoDiff_Evaluate(Vals,f):
    
    """Main function to autodifferentiate and evaluate a function at user defined values
    
    INPUTS
    =======
    User defined variable(s) and assigned value(s)

    RETURNS
    ========
    Returns len(kwargs) number of AutoDiff class objects with an associated derivative (seed) as an np.array

    NOTE:
    ========
    This is the main function that the user will interact with to 
    autodifferentiate (a) user defined function(s)
    and evaluate it at (a) user defined value(s)
        
    EXAMPLES
    =========

    # For multivariate vector inputs
    X = [1,2,3]
    Y = [2,3,3]
    Z = [3,5,3]
    W = [3,5,3]
    VarValues = [X, Y, Z, W]
    func = lambda Vars:3*Vars[0] + 4*Vars[1] + 4*Vars[2]**2 + 3*Vars[3]# Var[0] is X, Var[1] is Y
    Values, Derivatives = AutoDiff_Evaluate(VarValues,func)
    print(Values)
    print(Derivatives)
        
    # For multivariate scalar inputs
    X = [1]
    Y = [2]
    Z = [3]
    W = [3]
    VarValues = [X, Y, Z, W]
    func = lambda Vars:3*Vars[0] + 4*Vars[1] + 4*Vars[2]**2 + 3*Vars[3]# Var[0] is X, Var[1] is Y
    Values, Derivatives = AutoDiff_Evaluate(VarValues,func)
    print(Values)
    print(Derivatives)
    
    # For single variable scalar inputs
    X = [1]
    VarValues = [X]
    func = lambda Vars:3*Vars[0]
    Values, Derivatives = AutoDiff_Evaluate(VarValues,func)
    print(Values)
    print(Derivatives)
    
    # For single variable vector inputs
    X = [1,2,3]
    VarValues = [X]
    func = lambda Vars:3*Vars[0]
    Values, Derivatives = AutoDiff_Evaluate(VarValues,func)
    print(Values)
    print(Derivatives)
    
    # To find the Jacobian
    X = [1,2,3]
    VarValues = [X]
    func = lambda Vars:np.array([3*Vars[0], Vars[0]**2])
    Values, Derivatives = AutoDiff_Evaluate(VarValues,func)
    print(Values)
    print(Derivatives)
    
    """
    Values = []
    Ders = []
    for i in np.transpose(Vals):
        val = []
        der = []
        A = f(ad.Multi_AutoDiffObj_Creator(i).Vars)
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


