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

