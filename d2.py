<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:08:49 2022

@author: Notandi
"""
import math
import numpy as np

def NW4(x,y,z,d):
    iv=[x,y,z,d]
    c=299792.458
    dti=10**(-8)
    rho=26570
    
        #skilgreina gervitungl 1
    
    phi1=0
    theta1=0
    a1=rho*math.cos(phi1)*math.cos(theta1)
    b1=rho*math.cos(phi1)*math.sin(theta1)
    c1=rho*math.sin(phi1)
    r1=math.sqrt(a1**2+b1**2+(c1-6370)**2)
    t1=d+(r1/c)
    t1s=d+dti+(r1/c)
    
        #skilgreina gervitungl 2
    
    phi2=math.pi/3
    theta2=math.pi/3
    a2=rho*math.cos(phi2)*math.cos(theta2)
    b2=rho*math.cos(phi2)*math.sin(theta2)
    c2=rho*math.sin(phi2)
    r2=math.sqrt(a2**2+b2**2+(c2-6370)**2)
    t2=d+(r2/c)
    t2s=d+dti+(r2/c)
    
        #skilgreina gervitungl 3
    
    phi3=math.pi/4
    theta3=math.pi/4
    a3=rho*math.cos(phi3)*math.cos(theta3)
    b3=rho*math.cos(phi3)*math.sin(theta3)
    c3=rho*math.sin(phi3)
    r3=math.sqrt(a3**2+b3**2+(c3-6370)**2)
    t3=d+(r3/c)
    t3s=d+dti+(r3/c)
    
        #skilgreina gervitungl 4
    
    phi4=0
    theta4=0
    a4=rho*math.cos(phi4)*math.cos(theta4)
    b4=rho*math.cos(phi4)*math.sin(theta4)
    c4=rho*math.sin(phi4)
    r4=math.sqrt(a4**2+b4**2+(c4-6370)**2)
    t4=d+(r4/c)
    t4s=d+dti+(r4/c)
    
    #engin skekkja
    
    f1=(x-a1)**2+(y-b1)**2+(z-c1)**2-(c*(t1-d))**2
    f2=(x-a2)**2+(y-b2)**2+(z-c2)**2-(c*(t2-d))**2
    f3=(x-a3)**2+(y-b3)**2+(z-c3)**2-(c*(t3-d))**2
    f4=(x-a4)**2+(y-b4)**2+(z-c4)**2-(c*(t4-d))**2
    
    F=[f1,f2,f3,f4]
    
    J=np.matrix([[(2*x-2*a1), (2*y-2*b1), (2*z-2*c1), (-2*c**2*d+2*c**2*t1)],
           [(2*x-2*a2), (2*y-2*b2), (2*z-2*c2), (-2*c**2*d+2*c**2*t2)],
           [(2*x-2*a3), (2*y-2*b3), (2*z-2*c3), (-2*c**2*d+2*c**2*t3)],
           [(2*x-2*a4), (2*y-2*b4), (2*z-2*c4), (-2*c**2*d+2*c**2*t4)]])
    
    v=np.linalg.solve(J,F)
    xv=v+iv
    
    for i in range(10):
        x=xv[0]
        y=xv[1]
        z=xv[2]
        d=xv[3]
        print(x)


        f1=(x-a1)**2+(y-b1)**2+(z-c1)**2-(c*(t1-d))**2
        f2=(x-a2)**2+(y-b2)**2+(z-c2)**2-(c*(t2-d))**2
        f3=(x-a3)**2+(y-b3)**2+(z-c3)**2-(c*(t3-d))**2
        f4=(x-a4)**2+(y-b4)**2+(z-c4)**2-(c*(t4-d))**2

        F=[f1,f2,f3,f4]

        J=np.matrix([[(2*x-2*a1), (2*y-2*b1), (2*z-2*c1), (-2*c**2*d+2*c**2*t1)],
                     [(2*x-2*a2), (2*y-2*b2), (2*z-2*c2), (-2*c**2*d+2*c**2*t2)],
                     [(2*x-2*a3), (2*y-2*b3), (2*z-2*c3), (-2*c**2*d+2*c**2*t3)],
                     [(2*x-2*a4), (2*y-2*b4), (2*z-2*c4), (-2*c**2*d+2*c**2*t4)]])
        
        v=np.linalg.solve(J,F)
        xv = v+xv
    # Með skekkju
    
    f1=(x-a1)**2+(y-b1)**2+(z-c1)**2-(c*(t1s-d))**2
    f2=(x-a2)**2+(y-b2)**2+(z-c2)**2-(c*(t2s-d))**2
    f3=(x-a3)**2+(y-b3)**2+(z-c3)**2-(c*(t3s-d))**2
    f4=(x-a4)**2+(y-b4)**2+(z-c4)**2-(c*(t4s-d))**2
    
    F=[f1,f2,f3,f4]
    
    J=np.matrix([[(2*x-2*a1), (2*y-2*b1), (2*z-2*c1), (-2*c**2*d+2*c**2*t1s)],
           [(2*x-2*a2), (2*y-2*b2), (2*z-2*c2), (-2*c**2*d+2*c**2*t2s)],
           [(2*x-2*a3), (2*y-2*b3), (2*z-2*c3), (-2*c**2*d+2*c**2*t3s)],
           [(2*x-2*a4), (2*y-2*b4), (2*z-2*c4), (-2*c**2*d+2*c**2*t4s)]])
    
    v=np.linalg.solve(J,F)
    xv=v+iv
    
    for i in range(10):
        x=xv[0]
        y=xv[1]
        z=xv[2]
        d=xv[3]


        f1=(x-a1)**2+(y-b1)**2+(z-c1)**2-(c*(t1s-d))**2
        f2=(x-a2)**2+(y-b2)**2+(z-c2)**2-(c*(t2s-d))**2
        f3=(x-a3)**2+(y-b3)**2+(z-c3)**2-(c*(t3s-d))**2
        f4=(x-a4)**2+(y-b4)**2+(z-c4)**2-(c*(t4s-d))**2

        F=[f1,f2,f3,f4]

        J=np.matrix([[(2*x-2*a1), (2*y-2*b1), (2*z-2*c1), (-2*c**2*d+2*c**2*t1s)],
                     [(2*x-2*a2), (2*y-2*b2), (2*z-2*c2), (-2*c**2*d+2*c**2*t2s)],
                     [(2*x-2*a3), (2*y-2*b3), (2*z-2*c3), (-2*c**2*d+2*c**2*t3s)],
                     [(2*x-2*a4), (2*y-2*b4), (2*z-2*c4), (-2*c**2*d+2*c**2*t4s)]])
        
        v=np.linalg.solve(J,F)
        xv = v+xv    
NW4(4,5,6,9)   
=======
import numpy as np
from sympy import *

#fastar
c=299792.458

#Gervihnattastaðsetningar
A1=15600
B1=7540
C1=20140
t1=0.07074

A2=18760
B2=2750
C2=18610
t2=0.07220

A3=17610
B3=14630
C3=13480
t3=0.07690

A4=19170
B4=610
C4=18390
t4=0.07242

#Stuðlar fyrir framan x, y, z og d í fyrstu línulegu jöfnunni og fasti w
f1x = 2*A2-2*A1
f1y = 2*B2-2*B1
f1z = 2*C2-2*C1
f1d = 2*c**2*(t1-t2)
w1 = -(A1**2 - A2**2 + B1**2 - B2**2 + C1**2 - C2**2 + c**2*(t2**2-t1**2))

#Stuðlar fyrir framan x, y, z og d í annari línulegu jöfnunni og fasti w
f2x = 2*A3-2*A1
f2y = 2*B3-2*B1
f2z = 2*C3-2*C1
f2d = 2*c**2*(t1-t3)
w2 = -(A1**2 - A3**2 + B1**2 - B3**2 + C1**2 - C3**2 + c**2*(t3**2-t1**2))

#Stuðlar fyrir framan x, y, z og d í þriðju línulegu jöfnunni og fasti w
f3x = 2*A4-2*A1
f3y = 2*B4-2*B1
f3z = 2*C4-2*C1
f3d = 2*c**2*(t1-t4)
w3 = -(A1**2 - A4**2 + B1**2 - B4**2 + C1**2 - C4**2 + c**2*(t4**2-t1**2))

#Finnum x, y, z sem fall af d
M = Matrix([[f1x, f1y, f1z, f1d, w1], [f2x, f2y, f2z, f2d, w2], [f3x, f3y, f3z, f3d, w3]])
E = M.rref()[0]

def x(d): return E[0,4]-E[0,3]*d
def y(d): return E[1,4]-E[1,3]*d
def z(d): return E[2,4]-E[2,3]*d

#Finnum nú d með því að stinga inn x, y, z sem fall af d í fyrstu jöfnuna og leysum annars stigs jöfnuna sem fæst
a = (E[0,3]**2 + E[1,3]**2 + E[2,3]**2 - c**2);
b = (2*A1*E[0,3] - 2*E[0,3]*E[0,4] + 2*B1*E[1,3] - 2*E[1,3]*E[1,4] + 2*C1*E[2,3] - 2*E[2,3]*E[2,4] + 2*c**2*t1);
c = (E[0,4]**2 - 2*A1*E[0,4] + A1**2 + E[1,4]**2 - 2*B1*E[1,4] + B1**2 + E[2,4]**2 - 2*C1*E[2,4] + C1**2 - c**2*t1**2);

d1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x1 = x(d1)
y1 = y(d1)
z1 = z(d1)

print('x, y, z, d:')
print(x1, y1, z1, d1)

>>>>>>> d90963d6be03bd7daefc81c32242b74d473a4bda
