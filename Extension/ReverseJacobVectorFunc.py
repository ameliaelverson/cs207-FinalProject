from __future__ import division 
import numpy as np
from Graph import ComputationalGraph
from ReverseMode import Node 

class Jacobian:
    def __init__(self,args,**kwargs):

        self.function = args
        self.Vars =[]
        for key, value in kwargs.items():
            self.Vars.append(value)
  

    def value(self):
        Val=[]
        Jacobian=[]
        i = 0
        length = 0 
        for item in self.function:
            Jac =[]
            F = item
            Graph.ComputeValue()
            Graph.ComputeGradient(F.ownindex)
            Val.append(Graph.NodeList[F.ownindex].value)
            for j in range (len(self.Vars)):
                Jac.append(Graph.NodeList[j].deri)
            Jacobian.append(Jac)



        return np.array(Val), np.array(Jacobian)




Graph = ComputationalGraph()
X = Node(value = 3, Graph = Graph)
Y = Node(value = 5, Graph = Graph)
Z = Node(value = 1, Graph = Graph)

#VectorFunction 
G = np.array([-2*X,
               2*Y + Z,
               3*X+3*Y+2*Z])
Func = Jacobian(G,X =X,Y= Y,Z= Z)
#Value
Val,Deri = Func.value()
print(Val)
print(Deri)
from IPython import *
embed()