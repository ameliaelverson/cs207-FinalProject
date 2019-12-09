from __future__ import division 
import numpy as np
from .Graph import ComputationalGraph
from .ReverseMode import Node

class ReverseVecFunc:
    def __init__(self,args,**kwargs):
        """
        INPUTS
        =======
        The vector function as an np.array and the variables in Node Form
        arg: The vector function (an array of Node classes)
        **kwargs: The related variables

        """

        self.function = args
        self.Vars =[]
        for key, value in kwargs.items():
            self.Vars.append(value)
  

    def value(self, Graph):
        '''
        This function computes the value and the Jacobian matrix for reversemode AD 


        RETURNS
        ========
        Return value and Jacobian of the vector Func

        '''
        Val = []
        Jacobian = []
        for item in self.function:
            Jac =[]
            F = item
            Graph.ComputeValue()
            Graph.ComputeGradient(F.ownindex)
            Val.append(Graph.NodeList[F.ownindex].value)
            for j in range(len(self.Vars)):
                Jac.append(Graph.NodeList[j].deri)
            Jacobian.append(Jac)



        return np.array(Val), np.array(Jacobian)


    def Seriesvalue(self,C,D, Graph):
        '''
        This function computes the series of value and the Jacobian matrix for reversemode AD 


        RETURNS
        ========
        Return value and Jacobian of the vector Func

        '''
        Val=[]
        Jacobian=[]
        for item in self.function:
            F = item
            V,De = self.Wrapper(Graph,F,C,D)
            Val.append(V)
            Jacobian.append(De)
        Jacobian = np.array(Jacobian)
        R=[]
        for i in range(len(Jacobian)):
            R.append(Jacobian[i][1])
        return np.array(Val).T, Jacobian


    def Wrapper(self,Graph,F,C,D):
        ValList=[]
        DerList =[]
        C = C.T
        for j in range(len(C)):
            Graph.WIPER(D)
            for i in range(0,D):
                Graph.NodeList[i].value = C[j][i]
            Graph.ComputeValue()
            Graph.ComputeGradient(F.ownindex)
            ValList.append(Graph.NodeList[F.ownindex].value)
            Deri =[]
            for i in range(0,D):
                 Deri.append(Graph.NodeList[i].deri)
            DerList.append(Deri)
        return ValList,DerList



# if __name__ == "main":

#Graph = ComputationalGraph()
#X = Node(value = 3, Graph = Graph)
#Y = Node(value = 5, Graph = Graph)
#Z = Node(value = 1, Graph = Graph)

#VectorFunction 
# G = np.array([-2*X,
#                2*Y + Z,
#                3*X+3*Y+2*Z])
# Func = ReverseVecFunc(G,X =X,Y= Y,Z= Z)
# #Value
# Val,Deri = Func.value()
# print(Val)
# print(Deri)


#x = [1,2,3]
#y = [6,7,4]
#z = [3,8,1]
#C = np.array([x,y,z])
#D = 3 #Dimension
#G = np.array([-2*X,
#               2*Y + Z*Y,
#               3*X+3*Y*X+2*Z])
#Func = ReverseVecFunc(G,X =X,Y= Y,Z= Z)
#Vals,Deris=Func.Seriesvalue(C,D)
#print(Vals)
#print(Deris)
#from IPython import *
#embed()