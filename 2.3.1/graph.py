import numpy as np
import math
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset

time = [i for i in range(1, 30)]
pres = [6.1, 6, 5.6, 5.3, 4.6, 3.9, 3.6, 3.2, 2.9, 2.7, 2.4, 2.2, 1.9, 1.7, 1.6, 1.5, 1.4, 1.4, 1.3, 1.3, 1.2, 1.1, 0.96, 0.87, 0.8, 0.74, 0.72, 0.69, 0.67]

for elem in time:
    elem = int(elem)

# for elem in pres:
#     elem = float(elem)

# x = np.array(time)
# y = np.array(pres)

# plt.errorbar(x, y, xerr=0, yerr=(y*0.1))

# plt.title("Прямая зависимость P от t")
# plt.xlabel("t (сек.)")
# plt.ylabel("P 10^-4 Па")


# plt.savefig("function_graph.png")

# plt.clf()



for i in range(len(pres)):
    pres[i] = math.log(pres[i])

print(pres)
x = np.array(time)    
y = np.array(pres)

plt.errorbar(x, y, xerr=0, yerr=(abs(y*0.05) + 0.15))

plt.title("Зависимость ln(P - P_пр) от t")
plt.xlabel("t (сек.)")
plt.ylabel("ln(P - P_пр) 10^-4 Па")

linear_model=np.polyfit(x,y,1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(0,30)
plt.plot(x_s,linear_model_fn(x_s), color="green")
plt.savefig("function_graph2.png")

