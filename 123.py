import math as mat
import matplotlib.pyplot as plt
#
# a = [ mat.cos(mat.radians(x)) for x in range(0,90)]
#
# print(a)

# y = x*sin(x)

y = [mat.radians(x)*mat.sin(mat.radians(x))
     for x in range(0,5000)]
print(y)
a = []

for e in range(0, 4000):
    if abs(y[e]) < abs(y[e+1]) < abs(y[e+2]):
        a.append(y[e+1])
    else:
        a.append(0)

# print(a)
plt.plot(a)
plt.show()
