# -*- coding: utf-8 -*-

import numpy as np

def fun1(x): 
    x=np.array(x)
    size=list(range(len(x)))
    F1 = sum(size  * x[:]**2 ) + sum(x[:])**2/100
    G1 =  [2*i*Xi +  sum(2*x[:]) /100 for Xi,i  in zip(x[:],size) ]   
    H1 =  [[2*i + 2/100  if(i==j) else 2/100  for i in size]  for j in size]
    return F1, G1, H1


def fun2(x):
    x=np.array(x)
    size=list(range(len(x)))
    F2 = sum((x[:size[-1]] -1) **2) + (sum(x[:]**2) -0.25)**2
    G2 = [4*Xi * (sum(x[:]**2) -0.25) +(2*Xk-2)    for Xi,Xk in zip(x,x[:size[-1]])] 
    
    if(size[-1]==1): Xk=-2 
    else: Xk=0
    
    H2 =  [[ 8*(Xi**2)+ 4* sum(x[:]**2) +1 +Xk   if(i==j) else    8*Xi*Xj   for i,Xi,Xj in zip(size,x,x)]  for j in size]
    return F2, G2, H2
    

def fun3(x): 
    x=np.array(x) 
    N = (len(x)//2)*2
    size=list(range(len(x//2)))
    F3 = sum(100*((x[1::2] - x[:N:2]**3)**2)  + (1-x[:N:2])**2)
    
    G3 =  [ 200 * (X2i - X2i1**3)  if(i%2==0)    
    else   -600 * (X2i - X2i1**3)  * (X2i1**2) + 2*(X2i1 -1)  for i,X2i, X2i1  in zip (size,x[1::2], x[:N:2] )  ] 

    H3 = [[200  if(i%2==0) else  -600* X2i * (-3*X2i**2) 
                +200* (X2i - X2i**3)*(-6*X2i)+2         if(i==j)  else
                -600* (x[2*i]**2)                       if((i-1)==j and i%2!=0)  else
                -600* X2i * (-3*X2i**2)                 if((j-1)==i and j%2==0)  else 0
                for i,X2i,X2i1 in zip(size,x[1::2], x[:N:2]) ]  for j in size]
    
    return F3, G3, H3


def fun4(x):
    x=np.array(x)
    size=list(range(len(x//2)))
    N = (len(x)//2)*2       ##OBS X2i = x[:N:2]) and X2i1 = x[1:::2]
    F4 =   sum  ((1.5  - x[:N:2] * (1-  x[1::2]       ))**2 
             +  (2.25  - x[:N:2] * (1 - x[1::2]    **2))**2
             +  (2.625 - x[:N:2] * (1 - x[1::2]    **3))**2)


    def Derivative_f4(x,i):  ##OBS x(2i) = x(2*i+1) and x(2i-1) = x(2*i)
        if (i%2==0): 
                 return  ( 2*(1.5   - x[2*i]  * (1- x[2*i+1]**1))**2 *(1-x[2*i+1])
                         + 2*(2.25  - x[2*i]  * (1- x[2*i+1]**2))**2 *(1-x[2*i+1]*2)
                         + 2*(2.625 - x[2*i]  * (1- x[2*i+1]**3))**2 *(1-x[2*i+1]*3))

        else:                                                       #they are not equal
                 return  (2*(1.5   - x[2*i]  * (1- x[2*i+1]**1))**2 *(x[2*i])
                         +2*(2.25  - x[2*i]  * (1- x[2*i+1]**2))**2 *(x[2*i])*2
                         +2*(2.625 - x[2*i]  * (1- x[2*i+1]**3))**2 *(x[2*i])*3)                       
    
                 
    G4 =  [Derivative_f4(x,i) for i in size]
    return F4, G4


def fun5(x):
   x=np.array(x) 
   def q(x,i):
       v = [len(x),(i+20)]
       return sum(x[(i-1):min(v)-1])

   def Derivative_q(x,i):
       v = [len(x),(i+20)]
       return 1*(min(v)-1)
 

   def Derivative_f5(x,i): 
       return 4* (sum([Derivative_q(x,i)**3 for i in range(1,len(x))])) -40*(sum([Derivative_q(x,i) for i in range(1,len(x))])) -0.1
   
   F5 = sum([ ((q(x,i)**4)   - (20*(q(x,i)**2)) - 0.1*q(x,i) ) for i in range(1,len(x))]) 
   G5 =  [Derivative_f5(x,i) for i in range(1,len(x)+1)]
   return F5, G5
