import math

c = 299792.458

S1=[15600,7540,20140]
S2=[18760,2750,18610]
S3=[17610,14630,13480]
S4=[19170,610,18390]

SS=[S1,S2,S3,S4]

t1=0.07074
t2=0.07220
t3=0.07690
t4=0.07242

t = 0.003
vec =(0,0,6370,0)

def r(x,y,z,s):
    return math.sqrt((x-s[0])**2+(y-s[1])**2+(z-s[2])**2)

import numpy as np

def Jacobian(x,y,z,d):
    J=np.zeros((4,4))

    for i in range(0,4):
            J[i,0] = (x+SS[i][0])/r(x,y,z,SS[i])
            J[i,1] = (y+SS[i][1])/r(x,y,z,SS[i])
            J[i,2] = (z+SS[i][2])/r(x,y,z,SS[i])
            J[i,3] = c
    return J

def F(x,y,z,d):
    f1=r(x,y,z,S1)-c*(t1-d)
    f2=r(x,y,z,S2)-c*(t2-d)
    f3=r(x,y,z,S3)-c*(t3-d)
    f4=r(x,y,z,S4)-c*(t4-d)
    return [f1,f2,f3,f4]

def newton(vec):
    x=vec[0]
    y=vec[1]
    z=vec[2]
    d=vec[3]
    res = vec - np.dot(np.linalg.inv(Jacobian(x,y,z,d)),F(x,y,z,d))
    return res


print(newton(vec))
