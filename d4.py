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