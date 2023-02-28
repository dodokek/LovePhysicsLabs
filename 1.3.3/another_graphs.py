import numpy as np
import math
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset


#Трубка на 3,95

Res1 = [52,43,64,65]
Res2 = [59,31,48,55]
Pair1 = [1, 2, 3, 4]

#Строим график трубки 395

y = np.array(Res1)
x = np.array(Pair1)

plt.plot(x, y, 'bo', color = "red")

y = np.array(Res2)
plt.plot(x, y, "v", color = "blue")


plt.title("Разность давлении в зависимости от сектора трубки")
plt.xlabel("Номер пары")
plt.ylabel("Разность давлений (дел)")

plt.savefig("function_graph.png")

plt.clf()




