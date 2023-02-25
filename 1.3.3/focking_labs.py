import numpy as np
import math
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset


#Трубка на 3,95

Q_395 = [25, 19, 15,12,10, 9.8, 9, 7.95, 7.58, 7.54, 7.3, 7.24, 6.81, 6.4, 6.23, 5.95]
dP_395 = [30, 40, 50, 60, 70, 80, 105, 160,170,180,190, 205,217,240,260,280]

#Трубка на 5,3

Q_53 = [12.14,10.22,9.83,9.28,9.26,8.38,7.35, 5.78,5.52,5.58,5.25,5.27]
dP_53 = [30,40,50,60,70,80,105,160,170,180,190,195]


#Строим график трубки 395

x = np.array(dP_395)
y = np.array(Q_395)

plt.plot(x, y, 'bo')

plt.title("Зависимость расхода от dP")
plt.xlabel("dP (дел.)")
plt.ylabel("Расход Q (л/с)")


linear_model=np.polyfit(x[0:7],y[0:7],1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(0,200)
plt.plot(x_s,linear_model_fn(x_s), color="green")

plt.savefig("function_graph.png")

plt.clf()




