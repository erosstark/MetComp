

import sys
from math import sin

A = float(sys.argv[1])
w = float(sys.argv[2])
t = float(sys.argv[3])
x = A*sin(w*t)

print (x)
